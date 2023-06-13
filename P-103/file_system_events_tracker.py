import time 
import os
import shutil

import random 
import sys
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# add the path of downloadc folder
from_dir="C:/Users/HP/Downloads"

# Event Handler Classes

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"hey,{event.src_path}has been created")

    def on_deleted(self, event): 
        print(f"oops someone has deleted{event.src_path}!") 

    def on_modified(self, event): 
        print(f"hey there!,{event.src_path}has been modified")

    def on_moved(self, event):  
        print(f"someone moved{event.src_path}to{event.dest_path}") 

# Initialize Event Handler Class
event_handler = FileMovementHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()