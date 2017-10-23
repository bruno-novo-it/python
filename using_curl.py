#!/usr/bin/python

# To install: pip install requests

from util import bcolors

#import os

#os.system("curl -v www.google.com.br")

import requests

url = "http://www.google.com.br"

resp = requests.get(url)

print ("{}Encoding:{} {}".format(bcolors.Blue,bcolors.Final,resp.encoding),
        "\n{}URL:{} {}".format(bcolors.Blue,bcolors.Final,resp.url),
        "\n{}Status Code:{} {}".format(bcolors.Blue,bcolors.Final,resp.status_code),
        "\n{}Headers:{} {}".format(bcolors.Blue,bcolors.Final,resp.headers['Content-Type']),
        "\n{}Well Formed:{} {}".format(bcolors.Blue,bcolors.Final,resp.is_redirect),
        "\n{}Elapsed Time:{} {}".format(bcolors.Blue,bcolors.Final,resp.elapsed),
        "\n{}Cookies:{} {}".format(bcolors.Blue,bcolors.Final,resp.cookies)) #,
        #"\n{}Content:{} {}".format(bcolors.Blue,bcolors.Final,resp.content))
