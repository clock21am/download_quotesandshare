#!usr/bin/python

import tweepy
from bs4 import BeautifulSoup
from urllib2 import urlopen
import urllib
import os
import cv2
import signal

#key delecrations 
consumer_key = 'ZLVrCPU8If3vdWxJL1GxMuPnG'
consumer_secret_key = 'dWtnkhkjO2JyoGFDmxLPFhi7GFFfhoyjnTJ4ebhif6h9RKZxIZ'
access_key = '3317497801-iNe205MSOO7kcwLZTaaMk5SjDolbeR3T8EKiNmP'
access_key_secret = 'sNuDvxBcp9kAqvxE1N3nYRxldo3gdt59Rp6Otyg2fD0qs'
url = 'http://www.wookmark.com'
path = '/home/bugeater/Documents/Jugnoo/download_quotesandshare'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret_key);
auth.set_access_token(access_key,access_key_secret);

try:
    redirect_url = auth.get_authorization_url()
except:
    print "failed"

api = tweepy.API(auth)

def make_soup(url):
	html = urlopen(url).read()
	return BeautifulSoup(html)


def downloading():
    soup = make_soup(url)
    images = [img for img in soup.findAll('img')]
    print(str(len(images)) + "images found.")
    print 'Downloading images to current working directory.'
    image_links = [each.get('src') for each in images]
    count = 0
    for each in image_links:
    	if count == 10:
        	break
        else:
        	count = count + 1
        filename=each.split('/')[-1]
    	print filename
        urllib.urlretrieve(each, filename)
        
    

def uploadinganddelteting():
	images = os.listdir(path)
	count = 0
	for f in images[:]:
	   if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".gif"):
	      print f;
	      count = count + 1
	      break
	
	if count == 0:
		downloading()
		images = os.listdir(path)
		for f in images[:]:
			if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".gif"):
				api.update_with_media(f);
				os.remove(path+'/'+f)
				print "done"
				break
	else:
		for f in  images[:]:
			if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".gif"):
				api.update_with_media(f);
				os.remove(path+'/'+f)
				print "done"
				break




uploadinganddelteting()

	
