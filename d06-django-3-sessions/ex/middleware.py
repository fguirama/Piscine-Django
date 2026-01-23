import random

from d06.settings import RANDOM_USERNAME


class AnonymousUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        session = request.session

        if 'anon_username' not in session:
            session['anon_username'] = random.choice(RANDOM_USERNAME)
            session.set_expiry(42)

        request.anon_username = session['anon_username']

        return self.get_response(request)
