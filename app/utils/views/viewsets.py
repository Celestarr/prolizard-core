from typing import Optional

from django.db.models import Q, QuerySet
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin as BaseCreateModelMixin
from rest_framework.mixins import DestroyModelMixin as BaseDestroyModelMixin
from rest_framework.mixins import ListModelMixin as BaseListModelMixin
from rest_framework.mixins import RetrieveModelMixin as BaseRetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin as BaseUpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet as BaseGenericViewSet


class CreateModelMixin(BaseCreateModelMixin):
    """
    Create a model instance.
    """

    def create(self, request, *args, **kwargs):
        if hasattr(self, "_extra_create_kwargs"):
            data = dict(**request.data, **self._extra_create_kwargs)
        else:
            data = request.data

        serializer = self.get_serializer(data=data, write_only=True)
        serializer.is_valid(raise_exception=True)
        model_instance = self.perform_create(serializer)
        read_only_serializer = self.get_serializer(model_instance)
        headers = self.get_success_headers(read_only_serializer.data)
        return Response(read_only_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()


class RetrieveModelMixin(BaseRetrieveModelMixin):
    pass


class UpdateModelMixin(BaseUpdateModelMixin):
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial, write_only=True)
        serializer.is_valid(raise_exception=True)
        model_instance = self.perform_update(serializer)
        self.updated_instance = model_instance
        read_only_serializer = self.get_serializer(model_instance)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(read_only_serializer.data)

    def perform_update(self, serializer):
        return serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)


class DestroyModelMixin(BaseDestroyModelMixin):
    pass


class ListModelMixin(BaseListModelMixin):
    pass


class GenericViewSet(BaseGenericViewSet):
    # permission_classes_by_action = {
    #     "create": [IsAuthenticated],
    #     "destroy": [IsAuthenticated, IsObjectOwner],
    #     "list": [IsAuthenticated],
    #     "retrieve": [IsAuthenticated, IsObjectOwner],
    #     "partial_update": [IsAuthenticated, IsObjectOwner],
    #     "update": [IsAuthenticated, IsObjectOwner],
    # }
    permission_classes_by_action = None

    # Serializer to be used when performing creation/update.
    # A value of none indicates that default `serializer_class` will be used
    #   for everything (retrieval, creation and updates).
    serializer_class_write_only = None

    # List of lookup fields, e.g. ["pk", "username", "email"]
    # If default `lookup_field` is not enough and it is required to
    #   match object against multiple fields, use this.
    # A value of None indicates that default `lookup_field` will be used.
    lookup_fields: Optional[list] = None

    # List of allowed actions, e.g. ["list", "retrieve"]
    # A value of None indicates that all actions are allowed.
    allowed_actions: Optional[list] = None

    def check_permissions(self, request):
        # pylint: disable=unsupported-membership-test
        if self.allowed_actions and self.action not in self.allowed_actions:
            raise Http404

        return super().check_permissions(request)

    def get_permissions(self):
        if self.permission_classes_by_action is not None:
            return [permission() for permission in self.permission_classes_by_action.get(self.action, [])]

        return super().get_permissions()

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            f"Expected view {self.__class__.__name__} to be called with a URL keyword argument "
            f'named "{lookup_url_kwarg}". Fix your URL conf, or set the `.lookup_field` '
            "attribute on the view correctly."
        )

        if self.lookup_fields:
            filters = None

            for item in self.lookup_fields:  # pylint: disable=not-an-iterable
                if not filters:
                    filters = Q(**{item: self.kwargs[lookup_url_kwarg]})
                else:
                    filters |= Q(**{item: self.kwargs[lookup_url_kwarg]})

            obj = queryset.filter(filters).first()
        else:
            filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
            obj = queryset.filter(**filter_kwargs).first()

        if not obj:
            raise Http404

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj

    def get_serializer(self, *args, **kwargs):
        write_only = kwargs.get("write_only")

        if write_only and self.serializer_class_write_only:
            serializer_class = self.serializer_class_write_only
        else:
            serializer_class = self.serializer_class

        assert serializer_class is not None, (
            f"'{self.__class__.__name__}' should either include a `serializer_class` attribute, "
            "or override the `get_serializer_class()` method."
        )  # nosec

        kwargs.setdefault("context", self.get_serializer_context())
        return serializer_class(*args, **kwargs)  # pylint: disable=not-callable


class ModelViewSet(  # pylint: disable=too-many-ancestors
    CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin, GenericViewSet
):
    @action(detail=False, methods=["get"])
    def get_model_config(self, _):
        model_instance = self.get_queryset().model()
        field_config = model_instance.get_form_field_config()
        layout_config = model_instance.get_form_layout_config()

        config = {
            "fields": field_config,
            "layout": layout_config,
        }

        return Response(config)


class ListOnlyModelViewSet(ListModelMixin, GenericViewSet):
    pass


class RetrieveOnlyModelViewSet(RetrieveModelMixin, GenericViewSet):
    pass


class RetrieveUpdateModelViewSet(RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    pass


class ReadOnlyModelViewSet(RetrieveModelMixin, ListOnlyModelViewSet):  # pylint: disable=too-many-ancestors
    pass


class UserModelViewSet(ModelViewSet):  # pylint: disable=too-many-ancestors
    @property
    def _extra_create_kwargs(self):
        return {"user": self.request.user.pk}

    def get_queryset(self):
        assert self.queryset is not None, (
            f"'{self.__class__.__name__}' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
        )

        queryset = self.queryset

        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()

        queryset = queryset.filter(user=self.request.user)

        return queryset
