import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo

window = Tk()
window.title('Hello Wikipedia!')
window.geometry('250x70')

def search_info():
	query = entry.get()
	language = wikipedia.set_lang('id') 
	answer = wikipedia.summary(query)
	showinfo("Wikipedia", answer)

label = Label(window, text="Masukkan Topik: ")
label.grid(row=0, column=0)

entry = Entry(window)
entry.grid(row=1, column=0, padx=10)

button = Button(window, text="Cari", command=search_info)
button.grid(row=1, column=1, padx=10)

window.mainloop()