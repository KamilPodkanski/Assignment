# Kamil Podkański
# Coded and tested on Windows 10 in Visual Studio Code, with Python 3.10.6 and watchdog 2.1.9 instlled
# Please install Python and watchdog(API) before using this program
# https://www.python.org/downloads/
# https://pypi.org/project/watchdog/

import time
import os
import shutil
import subprocess
import platform
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class file_validator(PatternMatchingEventHandler):
    # validate if file is in right format
    def __init__(self, source_path):
        super(file_validator, self).__init__(patterns=["*.txt"], ignore_patterns=[], ignore_directories=True)
        self.source_path = source_path
    # action for placing file in monitor folder    
    def on_created(self, event):
        # data to work on
        file_name = event.src_path
        src_file = file_name
        basename = os.path.basename(file_name)
        dst_file = os.path.join(path_two, basename)
        path = file_name
        keywords=['MOCAP']
        # check for a keyword
        with open(path) as f:
            searchInLines = f.readlines()
            f.close()
        for line in searchInLines:
            for keyword in keywords:
                if keyword in line.upper():
                    print("Match!")
                    
                    # copy file to the destination folder
                    shutil.copyfile(src_file, dst_file) 
                    print("Copied.")
                    
                    # open file
                    if platform.system() == 'Darwin':       # macOS
                        subprocess.call(('open', dst_file))
                        print("Opened.")
                    elif platform.system() == 'Windows':    # Windows
                        os.startfile(dst_file)
                        print("Opened.")
                    else:                                   # linux variants
                        subprocess.call(('xdg-open', dst_file))
                        print("Opened.")
      
if __name__ == "__main__":
    # Folder selection
        # Folder to monitor
    path_one = input("Please copy and paste path of the folder you want to monitor.\n!!!In VSC use Ctrl+Shift+V to paste!!!\nYour Path: ")
        # Folder to save txt files with MOCAP word in it
    path_two = input("Please copy and paste path of the folder you want to place MOCAP files in.\n!!!In VSC use Ctrl+Shift+V to paste!!!\nYour Destination Path: ")
        #Calling class to identify, read, select, copy and open the file.
    event_handler = file_validator(source_path = path_one)
    observer = Observer()
    observer.schedule(event_handler, path_one, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()