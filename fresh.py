# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 12:27:25 2020

@author: KRUPASON
"""
import freshlib as fl
import time

fl.create_or_load_file()
            
#sample CRD operations to populate the file        
fl.create("qwerty",70,1220)
fl.create("qwertyy",70,120)
fl.read("qwerty")
fl.delete("qwertyy")



#performing CRD operations
while(1):
    flag=input("Do you want to perform CRD?(yes/no)")
    if flag=="no":
        break
    x=int(input("1.Create 2.Read 3.Delete :: Enter(1/2/3):"))
    if x==1:
        key=input("enter key")
        value=int(input("enter value"))
        timeout=int(input("enter timeout"))
        t1=Thread(target=fl.create,args=(key,value,timeout)) 
        t1.start()
        t2=Thread(target=fl.create,args=(key,value,timeout)) #Thread safety demonstration using sleep method
        t2.start()  #gives error saying that key is already present (because it is already created by t1 thread)
        time.sleep(2)
    elif x==2:
        key=input("enter key")
        t5=Thread(target=fl.read,args=(key,)) 
        t5.start()
        t3=Thread(target=fl.read,args=(key,)) #Thread safety demonstration using sleep method
        t3.start()  
        time.sleep(2)
    elif x==3:
        key=input("enter key")
        t4=Thread(target=fl.delete,args=(key,)) 
        t4.start()
        time.sleep(2)  #Thread safety demonstration using sleep method
        t7=Thread(target=fl.delete,args=(key,)) # gives error saying that no record with key is present as it is already deleted by above thread
        t7.start()  
        
    else:
        print("entered wrong no")