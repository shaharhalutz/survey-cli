import json,httplib
import logging

def send_notification(token,message,url):
    connection = httplib.HTTPSConnection('api.pushed.co', 443)
    connection.connect()
    connection.request('POST', '/1/push', json.dumps({
    "app_key": "VCOYAuA7JN2nZnoH179z",
    "app_secret": "sO4wHcxr7X1LL1v7c6oi5997LpAEbd00jAbuERdfUxCHBYUUQJ6U6vAjED1QymII",
    "target_type": "pushed_id",
    "pushed_id": token,
    "target_alias": "shahar.halutz@gmail.com",
    "content": message,
    "content_type": "url",
    "content_extra": url}),
    {
        "Content-Type": "application/json"
    }
    )
    result = json.loads(connection.getresponse().read())
    if result["response"]["type"] == "shipment_successfully_sent":
        logging.debug("notifications pushed successfully to: %s" % token)
        return True
    else:
        logging.error("error pushing to : %s" % token)
        return False