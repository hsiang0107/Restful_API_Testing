import jwt
import hashlib
import requests
import urllib3
import time
import codecs
from lib.ConfigHelper import ConfigHelper
from lib.ExtendSeleniumLibrary import ExtendSeleniumLibrary

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_jwt(http_method, raw_url, header, request_body, private_key=None, app_id=None, algorithm='HS256', version='V1'):
    string_for_hash = http_method.upper() + '|' + raw_url.lower() + '|' + header + '|' + request_body
    hash_obj = hashlib.sha256(string_for_hash.encode('utf-8'))
    hash_byte = hash_obj.digest()
    base64_byte = codecs.encode(hash_byte, 'base64')
    hash_string = base64_byte.decode('utf-8')
    hash_string = hash_string[:-1]

    config = ConfigHelper()
    issue_time = time.time()
    if private_key is None:
        private_key = config.get_data_from_config('CM', 'api_key')
    if app_id is None:
        app_id = config.get_data_from_config('CM', 'application_id')
    payload = {
        'appid': app_id,
        'iat': issue_time,
        'version': version,
        'checksum': hash_string
    }
    token = jwt.encode(payload, private_key, algorithm=algorithm).decode('utf-8')
    return token


def decode_jwt(jwt_token, secrete, algorithm='HS256'):
    data = jwt.decode(jwt_token, secrete, algorithm)
    return data


def get_cm_login_session(credential):
    config = ConfigHelper()
    cm_login = config.get_data_from_config('CM', 'address')
    cm_cookies = ExtendSeleniumLibrary().get_cm_cookies(cm_login, credential)
    s = requests.Session()
    for cookie in cm_cookies:
        s.cookies.set(cookie['name'], cookie['value'])
    return s


def send_request(server, api, interface, credential=None, params=None, body=None, jwt_token=None):
    session = requests.Session()
    if jwt_token:
        session.headers.update({'Authorization': 'Bearer ' + jwt_token, 'Content-Type': 'application/json'})
    if int(interface) == 1:
        session = get_cm_login_session(credential)
    url = server + api.get('path')
    print('Going to do request, url = %s.' % url)
    return {
        'GET': lambda: session.get(url, params=params, verify=False),
        'POST': lambda: session.post(url, data=body, verify=False),
        'PUT': lambda: session.put(url, data=body, verify=False),
        'DELETE': lambda: session.delete(url, params=params, verify=False),
    }.get(api.get('method'))()
