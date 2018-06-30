import pickle
from bawiBot.bawiBot import *

boardList, readPostsIdSet = "", ""

def run():
    global boardList, readPostsIdSet
    
    # Load the Memory 
    boardList = pickle.load(open("boardList.pkl", "br"))
    readPostsIdSet = pickle.load(open("readPostsIdSet.pkl", "br"))
    
    # Run the agent
    driver = getBawiDriver()
    checkNewPosts(driver, boardList, readPostsIdSet)
    driver.quit()
    
    # Read the Memory
    pickle.dump(boardList, open("boardList.pkl", "wb"))
    pickle.dump(readPostsIdSet, open("readPostsIdSet.pkl", "wb"))
    
if __name__ == "__main__":
	run()
