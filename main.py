import pickle
import sys
from bawiBot.bawiBot import *

boardList, readPostsIdSet = "", ""

def run(uid, passwd, slackToken):
    global boardList, readPostsIdSet
    
    # Load the Memory 
    boardList = pickle.load(open("boardList.pkl", "br"))
    readPostsIdSet = pickle.load(open("readPostsIdSet.pkl", "br"))
    
    # Run the agent
    driver = getBawiDriver(uid, passwd)
    checkNewPosts(driver, boardList, readPostsIdSet, slackToken)
    driver.quit()
    
    # Read the Memory
    pickle.dump(boardList, open("boardList.pkl", "wb"))
    pickle.dump(readPostsIdSet, open("readPostsIdSet.pkl", "wb"))
    
if __name__ == "__main__":
	if len(sys.argv) < 4:
		print("usage : python main.py [bawiId] [bawiPasswd] [slackbotToken]")
		exit()
	
	run(sys.argv[1], sys.argv[2], sys.argv[3])
