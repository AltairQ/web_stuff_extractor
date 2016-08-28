#!/usr/bin/env python 
from __future__ import print_function
import re
import time
import os
import sys
import json
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)


if len(sys.argv) != 2:
	eprint("Usage:\n./wse.py [json config]")
	sys.exit()


with open(sys.argv[1], "r") as config
	tmpdec = json.loads(config.read())
	pprint(tmpdec)
	url = tmpdec["url"] #page url
	domn = tmpdec["element"] #attr of a specific tag
	search = tmpdec["regex"] #extract info from attr
	dbfile = tmpdec["output"] #where to output
	unique = tmpdec["unique"] #todo
	delay = tmpdec["delay"] #delay in ms

res = open(dbfile, "a")

t0 = time.clock()
while len(tab)<item_count:
	page = requests.get(url)
	soup = BeautifulSoup(page.content, "html.parser")
	cod = re.search(regex, eval("soup."+domn)) #ugly eval
	res.write(cod+"\n")
	eprint(str(time.clock() - t0)+"\n")
	res.flush()
	os.fsync(file.fileno())
	time.sleep(delay/1000)
	t0 = time.clock()
