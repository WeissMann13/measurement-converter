import tkinter as tk

root = tk.Tk()

hello = tk.Label(root,text='Hello World')
name = tk.Label(root,text='x')

hello.pack()
name.pack()

root.mainloop()