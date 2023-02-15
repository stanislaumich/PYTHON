from tkinter import *  
  
  
def clicked():  
    lbl.configure(text="Я же просил...")  
  
  
window = Tk()  
window.title("Добро пожаловать в приложение PythonRu")  
window.geometry('400x250')  
lbl = Label(window, text="Привет")  
lbl.grid(column=0, row=0)  
txt = Entry(window,width=10)  
txt.grid(column=1, row=0)  
btn = Button(window, text="Не нажимать!", command=clicked)  
btn.grid(column=2, row=0)  
window.mainloop()