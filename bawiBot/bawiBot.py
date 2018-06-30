import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

def getBawiDriver():
    driver = webdriver.Chrome("/Users/huklee/Work/crawling/chromedriver")
    driver.get("http://www.bawi.org")

    wait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login_id"))).send_keys("yourID")
    wait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login_passwd"))).send_keys("yourPasswd")
    wait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login_submit"))).click()
    return driver

# For Making Test

import re
from bs4 import BeautifulSoup 


# Return new Posts from the boardTail
def getNewPosts(driver, boardTail, readPostsIdSet):
    boardHead = "https://www.bawi.org/board/"

    newPosts = {}
    readPostsId = readPostsIdSet[boardTail]

    driver.get(boardHead + boardTail)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # Every Title of the posts
    #   exmple of the title tag
    #   content > div.article-list.wrapper > ul:nth-child(3) > li.title > a
    posts = soup.select("div.article-list.wrapper > ul")

    
    # Post Check
    for p in posts:
        global pp
        tag = p.find("li", {"class":"title"}).find("a")
        pp = tag
        if tag is None: 
            continue

        title = tag.text
            
        for i in p.findAll("a", {"href":re.compile("tno")}):
    #         print(i)
    #         print(p.findAll("li", {"class":"read"}))
            if i.text not in readPostsId:
                readPostsId.add(i.text)
                urlTail = i["href"]
                newPosts[i.text] = (title, urlTail)
                print("[New Post]", i.text, urlTail)
    
    return newPosts

def init():
    boardHead = "https://www.bawi.org/board/"
    # boardList = {"구인/구직":"read.cgi?bid=8", "결혼":"read.cgi?bid=638"}
    boardTail = "read.cgi?bid=588"
    readPostsId = set()

# Test
# pp = ""

# getNewPosts(boardTail, readPostsId)

from bs4 import BeautifulSoup 

# boardList = {"#jobs":"read.cgi?bid=8", "#wedding_funeral":"read.cgi?bid=638"}
# readPostsIdSet = {"read.cgi?bid=8" : set(),
#                  "read.cgi?bid=638": set()}

def checkNewPosts(driver, boardList, readPostsIdSet):
    assert set(boardList.values()) == set(readPostsIdSet.keys())

    boardHead = "https://www.bawi.org/board/"
        
    for key in boardList.keys():
        urlTail = boardList[key]
    
        newPosts = getNewPosts(driver, urlTail, readPostsIdSet)
        print(newPosts)
        notifySlack(driver, key, newPosts)

from slacker import Slacker

def sendSlackMsg(channel, pretext, title, text, color="good"):
    token = 'your-token'
    slack = Slacker(token)
    nowTime = time.time()  # unix_time_stamp
    
    att = [{
            "pretext": pretext,
            "title": title,
            "text": text,
            "color": color, # good(green)
            "mrkdwn_in": [
                "text",
                "pretext"
            ],

            "ts":nowTime
    }]
    
    slack.chat.post_message(channel, attachments=att)    
    
# Example Case    
# sendSlackMsg("#test", "hello", "Title", "Content", "good")

newPosts = {'517': ('test4', 'read.cgi?bid=588;tno=482;p=34'),
             '518': ('test5', 'read.cgi?bid=588;tno=483;p=34')}
newPosts

def notifySlack(driver, channel, posts):
    boardHead = "https://www.bawi.org/board/"

    for title, urlTail in posts.values():
        # 01. goto the post with the driver        
        print("[NEW POST]", urlTail)
        driver.get(boardHead + urlTail)

        html = driver.page_source

        soup = BeautifulSoup(html, "html.parser")
        content = soup.select("li.body.text > table > tbody > tr > td")
        
        for i in content[0].findAll("br"):
            i.replaceWith("\n")

        text = content[0].text

        # 02. send the msg through slack
        sendSlackMsg(channel, boardHead + urlTail, title, text)
            
# Test for notify via Slack
# notifySlack(newPosts)
