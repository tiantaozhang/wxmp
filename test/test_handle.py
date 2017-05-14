from __future__ import absolute_import

import hashlib
from unittest import TestCase
import time


class TestHandle(TestCase):
    def test_handle(self):
        timestamp = str(time.time())
        token = "weilaidav2017"
        nonce = "123321"
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print list
        print hashcode

    def test_for(self):
        future_class_attr = {'__name__': 'name', '_name_': '_name', "name": "name", "__start__": "start"}
        attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
        for attr in attrs:
            print attr
