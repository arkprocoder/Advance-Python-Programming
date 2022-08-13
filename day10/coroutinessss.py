import time


def youtubeSearch():
    import time
    channel="WELCOME TO MY ARKPROCODER CHANNEL"
    print(channel)
    time.sleep(5)
    
    while True:
        text=(yield)
        if text in channel:
            print("Text is Present")
        else:
            print("Text is Absent")

search=youtubeSearch()
print("my search is getting started")
next(search)
print("Next method running")
time.sleep(9)
search.send("ARKPROCODER")
time.sleep(2)
search.send("ANEES")
time.sleep(2)
search.send("CHANNEL")
time.sleep(2)
search.close()
search.send("CHANNEL")