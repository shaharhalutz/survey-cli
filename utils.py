from const import app_url as app_url
import urlparse

def create_url(config,uuid):
    
    url = config["notification"]["URL"]
    query = urlparse.urlparse(url).query
    if len(query):
        return url + '&' + 'userId=' + uuid
    else:
        return url + '?' + 'userId=' + uuid

