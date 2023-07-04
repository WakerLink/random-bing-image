from random_word import RandomWords
from bing_image_downloader import downloader
import tkinter as tk
from tkinter import filedialog
r = RandomWords()
root = tk.Tk()
root.title("shitty random bing image fetcher")
root.geometry('400x100')
text = ""

def clicked():
    filePath = filedialog.askdirectory()
    theWord = str(r.get_random_word())
    res = downloader.download(theWord, limit=10, output_dir=filePath)
    lbl = tk.Label(root,text = "Download finished")
    lbl.place(relx=0.5, rely=0.7, anchor='center')
    return res


btn = tk.Button(root, text="Generate image", command=clicked)
btn.place(relx=0.5,rely=0.3,anchor='center')

root.mainloop()