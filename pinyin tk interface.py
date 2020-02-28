from tkinter import Tk, Entry, Button
import pinyin


def convert():
    s = ent_hanzi.get()
    p = pinyin.get(s)
    ent_pinyin.insert('end', p)
    return


fm_main = Tk()

ent_hanzi = Entry(fm_main)
ent_pinyin = Entry(fm_main)
btn = Button(fm_main, text='显示拼音', command=convert)

ent_hanzi.pack()
btn.pack()
ent_pinyin.pack()

fm_main.mainloop()
