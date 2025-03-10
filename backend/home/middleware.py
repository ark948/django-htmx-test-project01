import logging
from django.http import HttpResponse
from django.conf import settings

logger = logging.Logger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
logger.addHandler(handler)
logger.setLevel(logging.INFO)



class MaintenanceModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called.
        logger.info("------------> [Request IN]")
        if settings.MAINTENANCE_MODE:
            logger.warning("Application is in maintenance mode!")
            return HttpResponse("Application is in maintenance mode, Please come back later.")

        response = self.get_response(request)
        logger.info("------------> [Request OUT]")
        # Code to be executed for each request/response after the view is called.

        return response