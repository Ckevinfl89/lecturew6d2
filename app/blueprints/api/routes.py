from . import api


@api.route('/')
def hello():
    return 'Hello'
