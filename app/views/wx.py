# -*- coding: utf-8 -*-

import hashlib
from flask import request
from flask import Blueprint

wx = Blueprint('wx', __name__)


@wx.route('/wx', methods=['GET', 'POST'])
def handle_wx_token():
    try:
        data = request.args
        if len(data) == 0:
            return "hello, this is handle view"
        print data
        signature = data["signature"]
        timestamp = data["timestamp"]
        nonce = data["nonce"]
        echostr = data["echostr"]
        token = "weilaidav2017"

        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print "handle/GET func: hashcode, signature: ", hashcode, signature
        if hashcode == signature:
            return echostr
        else:
            return "<p>notice: hashcode:%s, signature:%s</p>" % (hashcode, signature)
    except Exception as e:
        return '<h4>"error:" + %s </h4>' % e.message




