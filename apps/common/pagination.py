from django.core.paginator import InvalidPage
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination as BasePageNumberPagination


class PageNumberPagination(BasePageNumberPagination):
    pass


class PageNumberPaginationFull(PageNumberPagination):
    def paginate_queryset(self, queryset, request, view=None):
        """Paginate a queryset if required, either returning a
        page object, or `None` if pagination is not configured for this view.
        """
        page_size = queryset.count()
        paginator = self.django_paginator_class(queryset, page_size)
        page_number = self.get_page_number(request, paginator)

        try:
            self.page = paginator.page(page_number)  # pylint: disable=attribute-defined-outside-init
        except InvalidPage as exc:
            msg = self.invalid_page_message.format(page_number=page_number, message=str(exc))
            raise NotFound(msg) from exc

        if paginator.num_pages > 1 and self.template is not None:
            # The browsable API should display pagination controls.
            self.display_page_controls = True

        self.request = request  # pylint: disable=attribute-defined-outside-init
        return list(self.page)
