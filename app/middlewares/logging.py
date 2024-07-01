from app.services import logger


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.debug(request.headers)

        response = self.get_response(request)

        logger.debug(response.headers)

        return response
