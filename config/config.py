import os

from raven.contrib.django.templatetags import raven

CSRF_ENABLED = False
SECRET_KEY = 'tatumn2017'
# SENTRY_SECRECT = 'http://d2a4f32451d4486499a49178acf6ccea:fba3e4f6894d49278b7182a04667baa2@127.0.0.1:9000/2'
SENTRY_SECRECT = 'http://d2a4f32451d4486499a49178acf6ccea:fba3e4f6894d49278b7182a04667baa2@127.0.0.1:9000/2'

class MyConfig(object):
    SENTRY_CONFIG = {
        'dsn': 'http://d2a4f32451d4486499a49178acf6ccea:fba3e4f6894d49278b7182a04667baa2@127.0.0.1:9000/2',
        'include_paths': ['/Users/tatumn/home/workspace/python/github.com/tiantaozhang/wxmp'],
        # 'release': raven.fetch_git_sha(os.path.dirname(__file__)),
    }
    SENTRY_USER_ATTRS = ['username', 'first_name', 'last_name', 'email']