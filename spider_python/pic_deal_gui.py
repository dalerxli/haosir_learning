import tkinter as tk
from tkinter import messagebox
from PIL import Image
import matplotlib.pyplot as plt
window = tk.Tk()
window.title('let start myself')
window.geometry('450x220')

# welcome image
canvas = tk.Canvas(window, height=200, width=500)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(0,0, anchor='nw', image=image_file)
canvas.pack(side='top')

# user information
tk.Label(window, text='Password: ').place(x=50, y= 150)


var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=150)

def usr_login():
    usr_pwd = var_usr_pwd.get()

    if usr_pwd == "hxl":
        isok=tk.messagebox.askyesno(title='Welcome', message='let us start know?' )
        if isok:
            deal_pic()
    else:
        tk.messagebox.showerror(message='Error, your password is wrong, try again.')

# login and sign up button
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=200, y=180)

def deal_pic():
    def show():
        temp=pic_pos.get()
        img = plt.imread(temp)
        plt.figure('show')
        plt.imshow(img)
        plt.show()
    window_deal_pic = tk.Toplevel(window)
    window_deal_pic.geometry('400x230')
    window_deal_pic.title('deal your picture')

    pic_pos = tk.StringVar()
    pic_pos.set('test.jpg')
    tk.Label(window_deal_pic, text='pic_position: ').place(x=10, y=10)
    entry_pic_pos = tk.Entry(window_deal_pic, textvariable=pic_pos)
    entry_pic_pos.place(x=110, y=10)

    showbutton = tk.Button(window_deal_pic, text='show', command=show)
    showbutton.place(x=170, y=40)

    w= tk.StringVar()
    tk.Label(window_deal_pic, text='w: ').place(x=10, y= 70)
    entry_h = tk.Entry(window_deal_pic, textvariable=w)
    entry_h.place(x=110, y=70)

    h= tk.StringVar()
    tk.Label(window_deal_pic, text='h: ').place(x=10, y=100)
    entry_w = tk.Entry(window_deal_pic, textvariable=h)
    entry_w.place(x=110, y=100)

    jiaodu= tk.StringVar()
    tk.Label(window_deal_pic, text='jiaodu: ').place(x=10, y= 130)
    entry_jiaodu = tk.Entry(window_deal_pic, textvariable=jiaodu)
    entry_jiaodu.place(x=110, y=130)
    def pic_change():
        temp = pic_pos.get()
        temph=int(h.get())
        tempw=int(w.get())
        tempj=int(jiaodu.get())
        img = Image.open(temp)
        new_img = img.resize((tempw,temph), Image.ANTIALIAS)
        new_img = new_img.rotate(tempj)
        global mat
        mat = new_img
        plt.figure('new')

        plt.subplot(121)
        plt.title('before')
        plt.imshow(img)

        plt.subplot(122)
        plt.title('after')
        plt.imshow(new_img)
        plt.show()


    show_button = tk.Button(window_deal_pic, text='show', command=pic_change)
    show_button.place(x=170, y=160)
    def pic_save():
        mat.save('new.jpg')

    save_button = tk.Button(window_deal_pic, text='save', command=pic_save)
    save_button.place(x=170, y=190)




window.mainloop()
