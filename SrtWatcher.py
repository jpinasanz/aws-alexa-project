import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PushToMediasite import send
import os
class EventHandler(FileSystemEventHandler):
    def on_created(self,event):
        f = open("srtLog.txt", "a")
        f.write(event.src_path+" has been created!"+'\n')
        f.close()
        head, tail = os.path.split(event.src_path)
        tail=tail.replace('.srt','.manifest')
        manifestPath="/home/sftp_user/"+tail
        send(manifestPath,event.src_path)
if __name__ == "__main__":
    path = "./srtOutput"
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







