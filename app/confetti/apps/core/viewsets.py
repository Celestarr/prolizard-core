from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet as BaseModelViewSet

from confetti.apps.core.permissions import IsObjectOwner


class ModelViewSet(BaseModelViewSet):
    permission_classes_by_action = {
        "create": [IsAuthenticated],
        "destroy": [IsAuthenticated, IsObjectOwner],
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated, IsObjectOwner],
        "partial_update": [IsAuthenticated, IsObjectOwner],
        "update": [IsAuthenticated, IsObjectOwner],
    }
    write_only_serializer_class = None
    updated_instance = None

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

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
        if write_only and self.write_only_serializer_class is not None:
            return self.write_only_serializer_class
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
