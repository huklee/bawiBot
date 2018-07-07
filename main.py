import pickle
import sys
from bawiBot.bawiBot import *
import time

boardList, readPostsIdSet = "", ""

def run(uid, passwd, slackToken):
    global boardList, readPostsIdSet
    
    # Load the Read List 
    boardList = pickle.load(open("boardList.pkl", "br"))
    readPostsIdSet = pickle.load(open("readPostsIdSet.pkl", "br"))
    
    # Run the agent
    driver = getBawiDriver(uid, passwd)
    checkNewPosts(driver, boardList, readPostsIdSet, slackToken)
    driver.quit()
    
    # Write the Read List
    pickle.dump(boardList, open("boardList.pkl", "wb"))
    pickle.dump(readPostsIdSet, open("readPostsIdSet.pkl", "wb"))
    
if __name__ == "__main__":
	if len(sys.argv) < 4:
		print("usage : python main.py [bawiId] [bawiPasswd] [slackbotToken]")
		exit()
	
	run(sys.argv[1], sys.argv[2], sys.argv[3])
	sendSlackMsgSimple(sys.argv[3], "#test", "CHECKED "+time.strftime("%Y-%m-%d %l:%M%p %Z"))                                                                                                                   
