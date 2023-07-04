from bing_image_downloader import downloader
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.title("shitty random bing image fetcher")
root.geometry('400x150')

def clicked():
    filePath = filedialog.askdirectory()
    word = wordEntry.get()
    amount = int(amountEntry.get())
    res = downloader.download(word, limit=amount, output_dir=filePath)
    lbl = tk.Label(root,text = "Download finished")
    lbl.place(relx=0.5, rely=0.7, anchor='center')
    return res

wordEntry= tk.Entry(root)
wordLabel = tk.Label(root, text="Word:")
wordEntry.place(relx=0.5,rely=0.1,anchor='center')
wordLabel.place(relx=0.29,rely=0.1,anchor='center')

amountEntry = tk.Entry(root)
amountLabel = tk.Label(root, text="Amount:")
amountEntry.place(relx=0.5,rely=0.3,anchor='center')
amountLabel.place(relx=0.27,rely=0.3,anchor='center')

btn = tk.Button(root, text="Generate image", command=clicked)
btn.place(relx=0.5,rely=0.5,anchor='center')

root.mainloop()