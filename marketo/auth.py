from rfc3339 import rfc3339
import hmac
import hashlib
import datetime


def sign(message, encryption_key):
    digest = hmac.new(encryption_key, message, hashlib.sha1)
    return digest.hexdigest().lower()


def header(user_id, encryption_key):
    timestamp = rfc3339(datetime.datetime.now())
    signature = sign(timestamp + user_id, encryption_key)
    return (
        '<env:Header><ns1:AuthenticationHeader>' +
              '<mktowsUserId>' + user_id + '</mktowsUserId>' +
              '<requestSignature>' + signature + '</requestSignature>' +
              '<requestTimestamp>' + timestamp + '</requestTimestamp>' +
        '</ns1:AuthenticationHeader></env:Header>')
