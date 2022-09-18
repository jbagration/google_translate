from tkinter import *
from tkinter import ttk, END
import googletrans
from googletrans import Translator

app = Tk()
app.title('Google Переводчик')
app.geometry('1070x400')
app.resizable(False, False)
app.configure(background='white')


def label_change():
    c1 = combo1.get()
    c2 = combo2.get()
    label1.configure(text=c1)
    label2.configure(text=c2)
    app.after(1000, label_change)


def translate_now():
    text_ = text1.get(1.0, END)
    t1 = Translator(service_urls=['translate.google.com', 'translate.google.co.kr'])
    trans_text = t1.translate(text_, src=combo1.get(), dest=combo2.get())
    trans_text = trans_text.text

    text2.delete(1.0, END)
    text2.insert(END, trans_text)


# icon
image_icon = PhotoImage(file='google.png')
app.iconphoto(False, image_icon)

# arrow
arrow_image = PhotoImage(file='arrow.png')
image_label = Label(app, image=arrow_image, width=150)
image_label.place(x=460, y=50)

# languages
language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

# design first
combo1 = ttk.Combobox(app, values=languageV, font='Roboto 14', state='r')
combo1.place(x=110, y=20)
combo1.set('выбрать язык')

label1 = Label(app, text='введите текст', font='Roboto 14', bg='white', width=18,
               relief='groove', bd=5)
label1.place(x=125, y=68)

# design second
combo2 = ttk.Combobox(app, values=languageV, font='Roboto 14', state='r')
combo2.place(x=720, y=20)
combo2.set('выбрать язык')

label2 = Label(app, text='введите текст', font='Roboto 14', bg='white', width=18,
               relief='groove', bd=5)
label2.place(x=735, y=68)

# first frame
frame = Frame(app, bg='black', bd=5)
frame.place(x=10, y=118, width=440, height=210)

text1 = Text(frame, font='Robote 20', bg='white', relief='groove', wrap='word')
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(frame)
scrollbar1.pack(side='right', fill='y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# second frame
frame2 = Frame(app, bg='black', bd=5)
frame2.place(x=620, y=118, width=440, height=210)

text2 = Text(frame2, font='Robote 20', bg='white', relief='groove', wrap='word')
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(frame2)
scrollbar1.pack(side='right', fill='y')

scrollbar2.configure(command=text2.yview)
text1.configure(yscrollcommand=scrollbar2.set)

# translate button
translate = Button(app, text='перевести', font=('Roboto', 15), activebackground='white',
                   cursor='hand2', bd=1, width=10, height=2, bg='black', fg='white',
                   command=translate_now)
translate.place(x=476, y=250)

label_change()

app.configure(bg='white')
app.mainloop()
