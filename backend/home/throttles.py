from rest_framework.throttling import UserRateThrottle, ScopedRateThrottle



class BurstRateThrottle(UserRateThrottle):
    scope = "burst"


class SustainedRateThrottle(UserRateThrottle):
    scope = "sustained"


class CustomThrottleForFuncViews(UserRateThrottle):
    scope = 'my_custom_scope'
    def allow_request(self, request, view):
        return super().allow_request(request, view)