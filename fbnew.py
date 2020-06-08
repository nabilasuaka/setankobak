#!/usr/bin/env python3
# Author : Shairul Alim
import re
import os
import sys
import shutil
import requests
from lib import Main
from getpass import getpass
from usr import login,banner,start
def menu():
    os.system("clear")
    banner.banner()
    banner.menu()
    print()
    zet = input("# Get user : ")
    if zet == '':
        menu()
    elif zet == '1':
        fr = run.parser.get("/me").find_all("a",string="Teman")
        for x in fr:
            if "friends/center" in x["href"]:
                continue
            else:
                users = run.friendlist(x["href"])
                print()
                start.sorting(users)
    elif zet == "2":
        url = input("# url post: ")
        if "https://www.facebook.com" in url:
            url = url.replace("https://www.facebook.com",'')
        elif "https://m.facebook.com" in url:
            url = url.replace("https://m.facebook.com",'')
        elif "https://mbasic.facebook.com" in url:
            url = url.replace("https://mbasic.facebook.com",'')
        else:
            exit("# url invalid")
        like = run.parser.get(url)
        try:
            react = re.findall('href="(/ufi.*?)"',str(like))[0]
        except IndexError:
            exit("# invalid")
        users = run.likes(react)
        print()
        start.sorting(users)
    elif zet =="3":
        username = run.bysearch("/search/people/?q=" + input("# query : "))
        print()
        start.sorting(username)
    elif zet == '4':
        grub = input("# ID group : ")
        users = run.fromGrub("/browse/group/members/?id=" + grub)
        print()
        if len(users) == 0:
            exit("# wrong Id")
        start.sorting(users)
    elif zet == '5':
        zet = input("# enter username/Id : ")
        if zet.isdigit():
            user = "/profile.php?id=" + zet
        else:
            user = "/" + zet
        try:
            user = run.parser.get(user).find('a',string="Teman")["href"]
            username = run.friendlist(user)
            start.sorting(username)
        except TypeError:
            exit("# user not found ")
    elif zet == '6':
        query = input("# Hashtag : ")
        username = run.hashtag("/hashtag/"+query)
        print()
        if len(username) == 0:
            exit("# no results")
        start.sorting(username)
    elif zet == '7':
        r = open("results-check.txt").read().strip()
        c = open("results-life.txt").read().strip()
        res = r + c
        final = set(res.split("\n"))
        print(f"# {str(len(final))} accounts to check")
        start.sorting(final,True)
    else:
        exit("# wrong choice")
def cek():
    os.system('clear')
    
    cookie = input("> Enter your cookie : ")
    if login.val(host, cookie):
        with open("usr/cookies","w") as f:
            f.write(cookie)
        return cookie
    else:
        getpass("# cookie wrong")
        cek()
def main():
    try:
        cookies = open("usr/cookies").read()
        if login.val(host, cookies):
            return cookies
        else:
            os.remove("usr/cookies")
            exit("# session die")
    except FileNotFoundError:
        return cek()
if "__main__" == __name__:
    try:
        os.system('clear')
        banner.banner()
        try:
            shutil.rmtree("usr/__pycache__")
            shutil.rmtree("lib/__pycache__")
            shutil.rmtree("./__pycache__")
        except FileNotFoundError:
            pass
        if len(sys.argv) == 2:
            if sys.argv[1] == 'free':
                host = "https://free.facebook.com{}"
            else:
                print("# Usage")
                exit("# Use <python3 mbf.py free> for free data")
        else:
            os.system("git pull")
            host = "https://mbasic.facebook.com{}"
        kuki = main()
        run = Main(kuki)
        menu()
    except requests.exceptions.ConnectionError:
        exit("# bad connection")
    except (KeyboardInterrupt,EOFError):
        exit("# Exit")