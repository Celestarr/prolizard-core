from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def global_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    print(exc, context)
    response = exception_handler(exc, context)

    if response:
        # Now add the HTTP status code to the response.
        custom_error_message = None
        default_errors = response.data
        # errors_messages = []

        for field_name, field_errors in default_errors.items():
            # del field_name

            if isinstance(field_errors, list):
                for field_error in field_errors:
                    # error_message = '%s: %s' % (field_name, field_error)
                    # print(field_name, field_error)
                    error_message = field_error
                    custom_error_message = error_message
                    break

            if custom_error_message:
                break

        if not custom_error_message:
            if response.data.get("detail"):
                custom_error_message = response.data["detail"]
            else:
                custom_error_message = _("One or more fields contain invalid data.")

        response.data = {
            "message": custom_error_message,
        }
    else:
        response = Response(
            {"message": _("Something went wrong.")},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return response
