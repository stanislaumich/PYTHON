import urllib
import pprint
import json
import httplib2

def google_search(query):
    url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&" + \
        urllib.urlencode({'q':query});
    referer = "http://wikipedia.org"
    h = httplib2.Http({})
    resp, content = h.request(url, "GET", headers={'Referer': referer})
    if resp.status == 200: pprint.pprint( json.loads(content) )
    else: print('Error')

google_search('bill')