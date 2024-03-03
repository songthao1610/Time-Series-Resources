'''
This script will download all papers/books and rename to proper name
if there is no copyright issue

TODO: Download resources by item number
TODO: add exception handler for downloader

'''
import re
import pathlib 
import urllib.request

pathlib.Path('resources').mkdir(parents=True, exist_ok = True)

f = open('resor')