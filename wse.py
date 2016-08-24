#!/usr/bin/env python 
from __future__ import print_function
import re
import time
import os
import sys
import json
import requests
from bs4 import BeautifulSoup

def eprint(*args, **kwargs):
	print(*args, file=sys.stderr, **kwargs)


if len(sys.argv) != 3:
	eprint("Usage:\n./wse.py [json config] [db file]")
	sys.exit()

#meh todo
url="TODO"
what="TODO"
search="TODO"

tab = []
with open("list.txt") as f:
	tab = f.read().splitlines()
tab = set(tab)

rld = open("list.txt", "w")

for item in tab:
	rld.write("%s\n" % item)
	
rld.close()

file = open("list.txt", "a")
log = open("log.txt", "w")


t0 = time.clock()
item_count = 9999999999
while len(tab)<item_count:
	page = requests.get(url)
	soup = BeautifulSoup(page.content, "html.parser")
	item_count = int(re.search(search, str(soup.title)).group(1))
	cod = re.search(what, soup.source.get('src')).group(1)
	if not (cod in tab):
		tab.add(cod)
		file.write(cod+"\n")
		print(str(len(tab))+"/"+str(item_count) + "\t" + str(time.clock() - t0))
		log.write(str(len(tab)) + "\t" + str(time.clock() - t0)+"\n")
		file.flush()
		log.flush()
		os.fsync(file.fileno())
		os.fsync(log.fileno())
		t0 = time.clock()
