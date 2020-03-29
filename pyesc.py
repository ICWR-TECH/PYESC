#!/usr/bin/python
# Python Email Scrapper
# Copyright (c)2020 - RND ICWR

red="\033[1;31m"
green="\033[0;32m"
blue="\033[1;34m"
normal_color="\033[0;0m"

print(red+"""
 /$$$$$$$  /$$     /$$ /$$$$$$$$  /$$$$$$   /$$$$$$ 
| $$__  $$|  $$   /$$/| $$_____/ /$$__  $$ /$$__  $$
| $$  \ $$ \  $$ /$$/ | $$      | $$  \__/| $$  \__/
| $$$$$$$/  \  $$$$/  | $$$$$   |  $$$$$$ | $$      
| $$____/    \  $$/   | $$__/    \____  $$| $$      
| $$          | $$    | $$       /$$  \ $$| $$    $$
| $$          | $$    | $$$$$$$$|  $$$$$$/|  $$$$$$/
|__/          |__/    |________/ \______/  \______/ 
                                                    
                                                    
                                                    """+normal_color+blue+"""
====================================================
"""+normal_color+green+"""[*] Python Email Scraper - RND ICWR"""+normal_color+blue+"""
====================================================
"""+normal_color)

from os.path import isfile
from re import findall
from random import randint
from requests import get
from sys import argv
from time import sleep
from threading import Thread
from datetime import datetime

class scraper():

    def __init__(self):

        self.runner()

    def save_email(self,email):

        f=open("result-email-"+str(datetime.now().strftime("%Y-%m-%d"))+".txt","a")
        f.write(email+"\n")
        f.close()

    def user_agent(self):

        arr=["Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3","Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16","Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.427.0 Safari/534.1"]
        return arr[randint(0,len(arr)-1)]

    def get_email(self,url_site):

        try:

            response=get(url=url_site,allow_redirects=True,verify=True,headers={"User-Agent":self.user_agent(),"Accept":"*/*"})
            email=findall("[\w\.-]+@[\w\.-]+",response.content)
            print("["+green+"+"+normal_color+"] "+blue+"Content is obtained from URL"+normal_color+" : "+green+url_site+normal_color)

            for x in email:

                self.save_email(x)

        except:

            print("["+red+"-"+normal_color+"] "+blue+"Error from URL"+normal_color+" : "+red+url_site+normal_color)

    def runner(self):

        if len(argv)>1:

            if isfile(argv[1]):

                for x in open(argv[1],"r").read().split("\n"):

                    if x.split("/")[0] == "http:" or x.split("/")[0] == "https:":

                        Thread(target=self.get_email,args=(x,)).start()
                        sleep(0.3)

            elif argv[1].split("/")[0] == "http:" or argv[1].split("/")[0] == "https:":

                self.get_email(argv[1])

            else:

                print("["+red+"-"+normal_color+"] Not Valid input")

        else:

            print("["+red+"-"+normal_color+"] No URL or List URL input")

if __name__ == '__main__':

    scraper()
