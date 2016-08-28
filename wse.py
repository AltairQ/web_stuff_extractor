#!/usr/bin/env python 
from __future__ import print_function
import re
import time
import os
import sys
import pprint
import json
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

#setup
ua = UserAgent()

pp = pprint.PrettyPrinter(indent=4)

def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)

#end of setup


if len(sys.argv) != 2:
	eprint("Usage:\n./wse.py [json config]")
	sys.exit()


with open(sys.argv[1], "r") as config:
	tmpdec = json.loads(config.read())
	pp.pprint(tmpdec)
	url = tmpdec["url"] #page url
	domn = tmpdec["element"] #attr of a specific tag
	search = tmpdec["regex"] #extract info from attr
	dbfile = tmpdec["output"] #where to output
	unique = tmpdec["unique"] #todo
	delay = tmpdec["delay"] #delay in ms

res = open(dbfile, "a")

header = {'User-Agent': ua.random}

t0 = time.clock()
while True: #todo add goal and handler maybe
	page = requests.get(url, headers=header)
	soup = BeautifulSoup(page.content, "html.parser")
	cod = re.search(search, eval("soup."+domn)).group(1) #ugly eval ugh
	eprint(cod, end="\t")
	eprint(str(time.clock() - t0))
	res.write(cod+"\n")
	res.flush()
	os.fsync(res.fileno())
	time.sleep(delay/1000)
	t0 = time.clock()
