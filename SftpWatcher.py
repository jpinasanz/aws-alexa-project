import time
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from Captioning import caption
import os
class EventHandler(FileSystemEventHandler):
    def on_created(self,event):
        #f = open("creationLog.txt", "a")
        #f.write(event.src_path+" has been created!")
        #f.write('\n')
        x = threading.Thread(target=creationProcess, args=(event.src_path,))
        x.start()
def creationProcess(path):
    time.sleep(5)
    if path.endswith(".mp4"):
        historicalSize = -1
        print("new file download started in " +os.getcwd())
        print(path)
        while (historicalSize != os.path.getsize(path)):
            historicalSize = os.path.getsize(path)
            time.sleep(1)
        print "file copy has now finished"
        caption(path)

if __name__ == "__main__":
    path = "/home/sftp_user"
    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler,path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
