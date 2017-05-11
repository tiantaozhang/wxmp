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


