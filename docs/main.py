import os
import random
import requests
import tkinter as tk
import time
from urllib import request
from bs4 import BeautifulSoup
success = 0
failure = 0

def Main():
    def AnonPars():
        def RandomUrl():
            url = "https://anonfiles.com/"
            r = ''
            i = random.choice([7, 8, 9, 10, 11])
            for x in range(i):
                r = r + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')) 
            fullurl = url + r
            def ValidationURL():                    
                def SaveUrl():
                    named_tuple = time.localtime()
                    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
                    with open('URL.txt', 'a') as file:
                        file.write(f"{fullurl},{size}, {time_string}\n")
                    
                request = requests.get(fullurl)
                soup = BeautifulSoup(request.text, "html.parser")
                status_code = request.status_code
                if status_code == 200:
                    file = soup.find_all("div", class_="col-xs-12 col-md-4 text-center")
                    for files in file:
                        files = files.find("a", {'id':'download-url'})
                    if files is not None:
                        sublink = files.get('href')
                    size = str(files.text)
                    SaveUrl()
                    return RandomUrl()
                elif status_code == 404:
                    return RandomUrl()
                else:
                    return RandomUrl()
                
            ValidationURL()
            
        RandomUrl()
    win = tk.Tk()
    win.title("AnonPars")
    ico = tk.PhotoImage(file="docs\IMG.png")
    win.iconphoto(False, ico)
    win.geometry("100x100+600+150") 
    win.resizable(False,False)
    win.config(bg="white")
    btn_start = tk.Button(
        win,
        text="Run",
        command = AnonPars
    )
    btn_end = tk.Button(
        win,
        text="Exit",
        command = os.system("exit")
    )
    label_success = tk.Label(
        win,
        text=f"Success:{success}"
    )
    label_failure = tk.Label(
        win,
        text=f"Failure:{failure}"
    )
    btn_start.pack()
    btn_end.pack()
    label_success.pack()
    label_failure.pack()
    win.mainloop()
Main()

