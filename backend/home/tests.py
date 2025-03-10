from django.test import TestCase, Client, override_settings
import logging

# Create your tests here.

class MaintenanceModeMiddlewareTest(TestCase):
    def setUp(self):
        self.client = Client()
        logging.disable(logging.CRITICAL)


    @override_settings(MAINTENANCE_MODE=True)
    def test_response_when_maintenacne_mode_is_on(self):
        resposne = self.client.get('/')
        self.assertContains(resposne, "Application is in maintenance mode, Please come back later.")

    @override_settings(MAINTENANCE_MODE=False)
    def test_response_when_maintenacne_mode_is_off(self):
        response = self.client.get('/home/')
        self.assertContains(response, "Articles")
        self.assertTemplateUsed(
            response,
            "index.html"
        )
