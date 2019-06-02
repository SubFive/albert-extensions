# -*- coding: utf-8 -*-

"""
Autocompletes Google searches
"""

import os
import subprocess
from collections import namedtuple
import requests

try:
    from albertv0 import *
except:
    pass


__iid__ = "PythonInterface/v0.1"
__prettyname__ = "Google autocomplete search"
__version__ = "1.0"
__author__ = "Jairo 'jairovsky'"
__trigger__= 'g'

def handleQuery(query):

    if not query.isTriggered:
        return

    stripped = query.string.strip().lower()
    if stripped:
        results = []

        for line in qGoogle(stripped):

                results.append(Item(id="%s%s" % (__prettyname__, line),
                                    icon=os.path.dirname(__file__)+"/google.png",
                                    text="%s" % (line),
                                    subtext="Open suggestion",
                                    actions=[ ProcAction("Open suggestion",
                                                 ["xdg-open", "https://google.com/search?q=%s" % line])]))
        return results

def qGoogle(q):

    gquery = 'https://www.google.com/complete/search?q=%s&client=firefox' % q

    suggs = requests.get(url = gquery).json()[1]

    return suggs


# for tests
try:
    from sys import argv

    if __name__ == '__main__':

        print(qGoogle(argv[1]))
except:
    pass
