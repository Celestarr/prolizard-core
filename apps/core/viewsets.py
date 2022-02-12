from django.db.models import Q
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet as BaseModelViewSet


class ModelViewSet(BaseModelViewSet):
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

    # Holds the updated object after `perform_update` is called.
    updated_instance = None

    # List of lookup fields, e.g. ["pk", "username", "email"]
    # If default `lookup_field` is not enough and it is required to
    #   match object against multiple fields, use this.
    # A value of None indicates that default `lookup_field` will be used.
    lookup_fields = None

    # List of allowed actions, e.g. ["list", "retrieve"]
    # A value of None indicates that all actions are allowed.
    allowed_actions = None

    def check_permissions(self, request):
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
            "Expected view %s to be called with a URL keyword argument "
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            "attribute on the view correctly." % (self.__class__.__name__, lookup_url_kwarg)
        )

        if self.lookup_fields:
            filters = None

            for item in self.lookup_fields:
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

    def get_write_only_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class(True)
        kwargs.setdefault("context", self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def get_serializer_class(self, write_only=False):
        """
        Return the class to use for the serializer.
        """
        if write_only and self.serializer_class_write_only is not None:
            return self.serializer_class_write_only
        else:
            assert self.serializer_class is not None, (  # nosec
                "'%s' should either include a `serializer_class` attribute, "
                "or override the `get_serializer_class()` method." % self.__class__.__name__
            )
            return self.serializer_class

    def perform_create(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        if hasattr(self, "_extra_create_kwargs"):
            data = dict(**request.data, **self._extra_create_kwargs)
        else:
            data = request.data

        write_only_serializer = self.get_write_only_serializer(data=data)
        write_only_serializer.is_valid(raise_exception=True)
        model_instance = self.perform_create(write_only_serializer)
        read_only_serializer = self.get_serializer(model_instance)
        headers = self.get_success_headers(read_only_serializer.data)
        return Response(read_only_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_write_only_serializer(instance, data=request.data, partial=partial)
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


__all__ = ["ModelViewSet"]
