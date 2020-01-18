import os #Module to use OS dependent functionality and interface with the OS Py is running on
from tkinter import *
from tkinter import filedialog #Module to access open and save dialog functions for files
import urllib.request #Module to fetch URLs
from tkinter.filedialog import askdirectory

#To check Internet Connection
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False
print("Connected" if connect() else "No Internet!")
