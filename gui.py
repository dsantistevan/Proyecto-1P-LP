#!/usr/bin/env python3
from tkinter import *
  
root = Tk() 
root.geometry("1024x768") 
root.title("Kotlin Awesome Code Editor") 
# root.minsize(height=250, width=350) 
root.maxsize(height=768, width=1024) 
  
  
# adding scrollbar 
scrollbar = Scrollbar(root) 
  
# packing scrollbar 
scrollbar.pack(side=RIGHT, 
               fill=Y) 
  
  
text_info = Text(root, 
                 yscrollcommand=scrollbar.set) 
text_info.pack(fill=BOTH) 
  
# configuring the scrollbar 
scrollbar.config(command=text_info.yview) 
  
root.mainloop() 
