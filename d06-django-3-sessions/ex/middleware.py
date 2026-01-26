import random

from d06.settings import RANDOM_USERNAME


class AnonymousUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        session = request.session

        if 'anon_username' not in session:
            session['anon_username'] = random.choice(RANDOM_USERNAME)

        if not request.user.is_authenticated:
            session.set_expiry(40)
        else:
            session.set_expiry(None)
        
        request.anon_username = session['anon_username']

        return self.get_response(request)
