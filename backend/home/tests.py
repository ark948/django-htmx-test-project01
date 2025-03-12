from django.test import TestCase, Client, override_settings
from http import HTTPStatus
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



class IPBlacklistMiddlewareTest(TestCase):
    def setUp(self):
        self.client = Client()

    @override_settings(BANNED_IPS=None)
    def test_request_successful_without_blacklist_setting(self):
        resposne = self.client.get('/home/')
        self.assertEqual(resposne.status_code, HTTPStatus.OK)
        

    @override_settings(BANNED_IPS=['192.168.1.2'])
    def test_request_successful_with_non_blacklisted_ip(self):
        resposne = self.client.get('/home/', REMOTE_ADDR="192.100.1.3")
        self.assertEqual(resposne.status_code, HTTPStatus.OK)


    @override_settings(BANNED_IPS=['192.168.1.1'])
    def test_request_fails_with_blacklisted_ip(self):
        resposne = self.client.get('/home/', REMOTE_ADDR="192.168.1.1")
        self.assertEqual(resposne.status_code, HTTPStatus.FORBIDDEN)