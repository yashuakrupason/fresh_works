# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 12:27:25 2020

@author: KRUPASON
"""

import json
import time
import os
from threading import *
fname=""
d={}
def create_or_load_file():
    global fname
    global d
    flag=input("Do you want to enter file path(or use default file path)?(yes/no)")
    if flag=="yes":
        fname=input("Enter path along with file name(json file) without syntax error")
    else:
        fname="D:\datastore.json"
    with open(fname,'w') as ds:
        if os.stat(fname).st_size == 0:
            st='{}'
            ds.write(st)
            print("file created")
    with open(fname,'r') as ds:
        data_load = json.load(ds)            
        temp=data_load
        print("loaded db")
        print(temp)
        d=temp


#create method
def create(key,value,timeout=0):
    global fname
    global d
    if key in d:
        print("error: this key already exists") #error message
    else:
        if(key.isalpha()):
            if len(d)<(1024*1024*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                print("created");
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    d[key]=l
                    with open(fname,'w') as ds:
                        json.dump(d,ds)
            else:
                print("error: Memory limit exceeded!! ")#error message for memory limit exceeded
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message3


# read method            
def read(key):
    global fname
    global d
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message
    else:
        b=d[key]
        if b[1]!=0:
                stri=str(key)+":"+str(b[0]) 
                print(stri)
                return stri
        else:
            stri=str(key)+":"+str(b[0])
            print(stri)
            return stri

#delete method
def delete(key):
    global fname
    global d
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del d[key]
                with open(fname,"r") as mo:#reading from the master.json file
                    data_load = json.load(mo)
                    if key in data_load:
                        del data_load[key]
                res = not data_load
                
                if res==True:
                    with open(fname,"w") as ds: #for underflow
                        st='{}'
                        ds.write(st)
                else:
                    with open(fname,"w") as ds:
                        json.dump(d,ds)
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message
        else:
            del d[key]
            print("key is successfully deleted")


       