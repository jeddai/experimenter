import requests
from django.conf import settings


class CirrusMiddleware:
    """
    A middleware that calls to Cirrus to fetch the features for Experimenter
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.features = {"test-feature": {"enabled": False}}
        if settings.CIRRUS_URL:
            try:
                user = request.user

                body = {
                    "client_id": user.username,
                    "context": {"username": user.username, "email": user.email},
                }

                r = requests.post(settings.CIRRUS_URL, json=body)
                features = r.json()
                request.features = features
            except Exception as e:
                print(e)

        if self.get_response:
            return self.get_response(request)
