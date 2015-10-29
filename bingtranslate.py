#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2

BING_APPID = "0FFF5300CD157A2E748DFCCF6D67F8028E5B578D"
URI = "http://api.microsofttranslator.com/V2/Ajax.svc/Translate"

def translate(text, from_language, to_language):
    params = { "appId" : BING_APPID,
        "text" : "%s"%text.encode("utf8"),
        "from" : from_language,
        "to" : to_language}

    parameters = urllib.urlencode(params)
 
    request = urllib2.Request("%s?%s"%(URI, parameters))
    results = urllib2.urlopen(request).read()

    results = results[4:-1]
    return results
