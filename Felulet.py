from tkinter import *
import tkinter as tk
from Communication import keresFutoSzerver, kuldAkkord, kuldDal , kuldKikapcs, kuldAkkordPengetes, kuldPengetesFajtak, kuldAkkordFelbont1,kuldAkkordFelbont3
LARGE_FONT = ('Verdana', 12)

szerverek = []

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_attributes("-fullscreen", True) # set size of the main window to 300x300 pixels
 
        # this container contains all the pages
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)   # make the cell in grid cover the entire window
        container.grid_columnconfigure(0,weight=1) # make the cell in grid cover the entire window
        self.frames = {} # these are pages we want to navigate to
 
        for F in (StartPage, Page1, Page2, Page3, Page1_1,Page1_21,Page1_22, Page1_2, Page2_1, Page2_2,Page2_21, Page2_22, Page2_3, Page3_1, Page3_2): # for each page
            frame = F(container, self) # create the page
            self.frames[F] = frame  # store into frames
            frame.grid(row=0, column=0, sticky='nsew') # grid it to container
 
        self.show_frame(StartPage) # let the first page is StartPage
 
    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
 
class StartPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
 
        kezdo = tk.Button(self, text='Kezdő',  
                            command=lambda : controller.show_frame(Page1),
                            font=('lucida handwriting', 35), height=4, width=250, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        kezdo.pack() # pack it in

        kozepes = tk.Button(self, text='Közepes', 
                            command=lambda : controller.show_frame(Page2),
                            font=('lucida handwriting', 35), height=4, width=250, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        kozepes.pack()

        halado = tk.Button(self, text='Haladó', 
                            command=lambda : controller.show_frame(Page3),
                            font=('lucida handwriting', 35), height=4, width=250,bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        halado.pack()

        # bg="#FEA680", activebackground="#ffd2c4", bd=1,fg='#E24E42',activeforeground='#E24E42'
        # bg="#FEDCD2", activebackground="#ffd2c4", bd=1,fg='#DF744A',activeforeground='#DF744A'

class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        vissza = tk.Button(self, text='Vissza',font=('lucida handwriting', 12), bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A',
                            command=lambda: controller.show_frame(StartPage))
        vissza.grid(row =0,column=0,sticky=W)
        label = tk.Label(self, text='Kezdő', font=('lucida handwriting', 34),fg='#DF744A')
        label.grid(columnspan=15,ipadx=5)
        label_ures = tk.Label(self,text=" ",font=('lucida handwriting', 50))
        label_ures.grid(row=14,column=4)

        akkord_gomb = tk.Button(self, text='Akkordok', 
                            command=lambda : controller.show_frame(Page1_1),
                            font=('lucida handwriting', 34), height=9, width=25, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        akkord_gomb.grid(row=30,column=0)
        pengetes_gomb = tk.Button(self, text='Pengetések', 
                            command=lambda : controller.show_frame(Page1_2),
                            font=('lucida handwriting', 34), height=9, width=25, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        pengetes_gomb.grid(row=30,column=1)

class Page1_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        vissza = tk.Button(self, text='Vissza', bg="#bfd8d2", activebackground="#bad6d8", bd=1, font=('lucida handwriting', 12), fg='#DF744A',activeforeground='#DF744A', 
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), controller.show_frame(Page1), kuldKikapcs(szerverek[0]['ip'])])
        vissza.grid(row =0,column=0,sticky=W)
        label = tk.Label(self, text='Kezdő', font=('lucida handwriting', 34), fg='#bc5c36')
        label.grid(columnspan=15,ipadx=5)
        label = tk.Label(self, text='Akkordok', font=('lucida handwriting', 30), fg='#DF744A')
        label.grid(columnspan=15,ipadx=5)
        label_ures = tk.Label(self, font=('lucida handwriting', 25))
        label_ures.grid(row=3,column=4)


        em_gomb = tk.Button(self, text='Em',
                            command=lambda : [em_gomb.configure(bg='#93b0c9'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkord(szerverek[0]['ip'], "em")],
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        em_gomb.grid(row=15, column=0)
        am_gomb = tk.Button(self, text='Am',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#93b0c9'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkord(szerverek[0]['ip'], "am")],
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        am_gomb.grid(row=15, column=4)
        dm_gomb = tk.Button(self, text='Dm',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#93b0c9'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkord(szerverek[0]['ip'], "dm")], 
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        dm_gomb.grid(row=15, column=5)
        c_gomb = tk.Button(self, text='C',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#93b0c9'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkord(szerverek[0]['ip'], "c")],
                            font=('lucida handwriting', 34), height=4, width=13, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        c_gomb.grid(row=15, column=6)
        a_gomb = tk.Button(self, text='A',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#93b0c9'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkord(szerverek[0]['ip'], "a")],
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        a_gomb.grid(row=16, column=0)
        e_gomb = tk.Button(self, text='E',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#93b0c9'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkord(szerverek[0]['ip'], "e")],
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        e_gomb.grid(row=16, column=4)
        g_gomb = tk.Button(self, text='G',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#93b0c9'), d_gomb.configure(bg='#bfd8d2'), kuldAkkord(szerverek[0]['ip'], "g")],
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        g_gomb.grid(row=16, column=5)
        d_gomb = tk.Button(self, text='D',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#93b0c9'), kuldAkkord(szerverek[0]['ip'], "d")],
                            font=('lucida handwriting', 34), height=4, width=13, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        d_gomb.grid(row=16, column=6)
    
class Page1_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        vissza = tk.Button(self, text='Vissza', bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A', font=('lucida handwriting', 12),
                            command=lambda : controller.show_frame(Page1))
        vissza.grid(row =0,column=0,sticky=W)
        label = tk.Label(self, text='Kezdő', font=('lucida handwriting', 34), fg='#bc5c36')
        label.grid(columnspan=15,ipadx=5)
        label = tk.Label(self, text='Pengetések', font=('lucida handwriting', 30), fg="#DF744A")
        label.grid(columnspan=15,ipadx=5)
        label_ures = tk.Label(self,text=" ",font=('lucida handwriting', 25))
        label_ures.grid(row=14,column=4)

        akkordpeng_gomb = tk.Button(self, text='Akkord pengetés',
                                font=('lucida handwriting', 34),height=9, width=25, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A', 
                            command=lambda : controller.show_frame(Page1_21)
                            )
        akkordpeng_gomb.grid(row=30,column=0)
        pengfajt_gomb = tk.Button(self, text='Pengetés fajták',
                                font=('lucida handwriting', 34),height=9, width=25, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A',
                             command=lambda : controller.show_frame(Page1_22)
                            )
        pengfajt_gomb.grid(row=30,column=1)

class Page1_21(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        vissza = tk.Button(self, text='Vissza', bg="#bfd8d2", activebackground="#bad6d8", bd=1, font=('lucida handwriting', 12), fg='#DF744A',activeforeground='#DF744A', 
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), controller.show_frame(Page1_2)])
        vissza.grid(row =0,column=0,sticky=W)
        label = tk.Label(self, text='Kezdő', font=('lucida handwriting', 34), fg='#bc5c36')
        label.grid(columnspan=15,ipadx=5)
        label = tk.Label(self, text='Akkord pengetés', font=('lucida handwriting', 30), fg='#DF744A')
        label.grid(columnspan=15,ipadx=5)
        label_ures = tk.Label(self, font=('lucida handwriting', 25))
        label_ures.grid(row=3,column=4)

        em_gomb = tk.Button(self, text='Em',
                            command=lambda : [em_gomb.configure(bg='#93b0c9'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordPengetes(szerverek[0]['ip'], "em")],
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        em_gomb.grid(row=15, column=0)
        am_gomb = tk.Button(self, text='Am',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#93b0c9'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordPengetes(szerverek[0]['ip'], "am")],
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        am_gomb.grid(row=15, column=4)
        dm_gomb = tk.Button(self, text='Dm',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#93b0c9'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordPengetes(szerverek[0]['ip'], "dm")], 
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        dm_gomb.grid(row=15, column=5)
        c_gomb = tk.Button(self, text='C',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#93b0c9'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordPengetes(szerverek[0]['ip'], "c")],
                            font=('lucida handwriting', 34), height=4, width=13, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        c_gomb.grid(row=15, column=6)
        a_gomb = tk.Button(self, text='A',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#93b0c9'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordPengetes(szerverek[0]['ip'], "a")],
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        a_gomb.grid(row=16, column=0)
        e_gomb = tk.Button(self, text='E',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#93b0c9'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordPengetes(szerverek[0]['ip'], "e")],
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        e_gomb.grid(row=16, column=4)
        g_gomb = tk.Button(self, text='G',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#93b0c9'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordPengetes(szerverek[0]['ip'], "g")],
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        g_gomb.grid(row=16, column=5)
        d_gomb = tk.Button(self, text='D',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#93b0c9'), kuldAkkordPengetes(szerverek[0]['ip'], "d")],
                            font=('lucida handwriting', 34), height=4, width=13, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        d_gomb.grid(row=16, column=6)

class Page1_22(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        vissza = tk.Button(self, text='Vissza', bg="#bfd8d2", activebackground="#bad6d8", bd=1, font=('lucida handwriting', 12), fg='#DF744A',activeforeground='#DF744A', 
                            command=lambda : [egy_gomb.configure(bg='#bfd8d2'), ketto_gomb.configure(bg='#bfd8d2'), harom_gomb.configure(bg='#bfd8d2'), negy_gomb.configure(bg='#bfd8d2'), ot_gomb.configure(bg='#bfd8d2'), hat_gomb.configure(bg='#bfd8d2'), controller.show_frame(Page1_2)])
        vissza.grid(row =0,column=0,sticky=W)
        label = tk.Label(self, text='Kezdő', font=('lucida handwriting', 34), fg='#bc5c36')
        label.grid(columnspan=15,ipadx=5)
        label = tk.Label(self, text='Pengetés fajták', font=('lucida handwriting', 30), fg='#DF744A')
        label.grid(columnspan=15,ipadx=5)
        label_ures = tk.Label(self, font=('lucida handwriting', 25))
        label_ures.grid(row=3,column=4)

        egy_gomb = tk.Button(self, text='1', 
                            command=lambda : [egy_gomb.configure(bg='#93b0c9'), ketto_gomb.configure(bg='#bfd8d2'), harom_gomb.configure(bg='#bfd8d2'), negy_gomb.configure(bg='#bfd8d2'), ot_gomb.configure(bg='#bfd8d2'), hat_gomb.configure(bg='#bfd8d2'), kuldPengetesFajtak(szerverek[0]['ip'], "1")],
                            font=('lucida handwriting', 34), height=4, width=16, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        egy_gomb.grid(row=15, column=0)
        ketto_gomb = tk.Button(self, text='2', 
                            command=lambda : [egy_gomb.configure(bg='#bfd8d2'), ketto_gomb.configure(bg='#93b0c9'), harom_gomb.configure(bg='#bfd8d2'), negy_gomb.configure(bg='#bfd8d2'), ot_gomb.configure(bg='#bfd8d2'), hat_gomb.configure(bg='#bfd8d2'), kuldPengetesFajtak(szerverek[0]['ip'], "2")],
                            font=('lucida handwriting', 34), height=4, width=17, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        ketto_gomb.grid(row=15, column=1)
        harom_gomb = tk.Button(self, text='3', 
                            command=lambda : [egy_gomb.configure(bg='#bfd8d2'), ketto_gomb.configure(bg='#bfd8d2'), harom_gomb.configure(bg='#93b0c9'), negy_gomb.configure(bg='#bfd8d2'), ot_gomb.configure(bg='#bfd8d2'), hat_gomb.configure(bg='#bfd8d2'), kuldPengetesFajtak(szerverek[0]['ip'], "3")], 
                            font=('lucida handwriting', 34), height=4, width=16, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        harom_gomb.grid(row=15, column=2)
        negy_gomb = tk.Button(self, text='4', 
                            command=lambda : [egy_gomb.configure(bg='#bfd8d2'), ketto_gomb.configure(bg='#bfd8d2'), harom_gomb.configure(bg='#bfd8d2'), negy_gomb.configure(bg='#93b0c9'), ot_gomb.configure(bg='#bfd8d2'), hat_gomb.configure(bg='#bfd8d2'), kuldPengetesFajtak(szerverek[0]['ip'], "4")],
                            font=('lucida handwriting', 34), height=4, width=16, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        negy_gomb.grid(row=16, column=0)
        ot_gomb = tk.Button(self, text='5', 
                            command=lambda : [egy_gomb.configure(bg='#bfd8d2'), ketto_gomb.configure(bg='#bfd8d2'), harom_gomb.configure(bg='#bfd8d2'), negy_gomb.configure(bg='#bfd8d2'), ot_gomb.configure(bg='#93b0c9'), hat_gomb.configure(bg='#bfd8d2'), kuldPengetesFajtak(szerverek[0]['ip'], "4")],
                            font=('lucida handwriting', 34), height=4, width=17, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        ot_gomb.grid(row=16, column=1)
        hat_gomb = tk.Button(self, text='6', 
                            command=lambda : [egy_gomb.configure(bg='#bfd8d2'), ketto_gomb.configure(bg='#bfd8d2'), harom_gomb.configure(bg='#bfd8d2'), negy_gomb.configure(bg='#bfd8d2'), ot_gomb.configure(bg='#bfd8d2'), hat_gomb.configure(bg='#93b0c9'), kuldPengetesFajtak(szerverek[0]['ip'], "5")],
                            font=('lucida handwriting', 34), height=4, width=16, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        hat_gomb.grid(row=16, column=2)

class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        vissza = tk.Button(self, text='Vissza', font=('lucida handwriting', 12), bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A', 
                            command=lambda : controller.show_frame(StartPage))
        vissza.grid(row =0,column=0,sticky=W)

        label = tk.Label(self, text='Közepes', font=('lucida handwriting', 34), fg='#bc5c36')
        label.grid(columnspan=15,ipadx=5)
        label = tk.Label(self, text='Pengetések', font=('lucida handwriting', 30), fg='#DF744A')
        label.grid(columnspan=15,ipadx=5)
        label_ures = tk.Label(self,text=" ",font=('lucida handwriting', 25))
        label_ures.grid(row=14,column=4)
        

        akkord_gomb = tk.Button(self, text='Akkordok',  
                            command=lambda : controller.show_frame(Page2_1),font=('lucida handwriting', 34), height=9, width=16, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        akkord_gomb.grid(row=30,column=0)
        felbontas_gomb = tk.Button(self, text='Akkord\nfelbontások',  
                            command=lambda : controller.show_frame(Page2_2),font=('lucida handwriting', 34),height=9, width=17, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        felbontas_gomb.grid(row=30,column=1)
        dalok_gomb = tk.Button(self, text='Dalok',  
                            command=lambda : controller.show_frame(Page2_3),font=('lucida handwriting', 34),height=9, width=16, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        dalok_gomb.grid(row=30,column=2)
 
class Page2_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        vissza = tk.Button(self, text='Vissza', font=('lucida handwriting', 12), bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A',
                            command=lambda : [variable.set("Válassz!"), akk.configure(text=""), controller.show_frame(Page2), kuldKikapcs(szerverek[0]['ip'])])
        vissza.grid(row =0,column=0,sticky=W)

        label = tk.Label(self, text='Közepes', font=('lucida handwriting', 34), fg='#bc5c36')
        label.grid(column=5,row=1,sticky="e", ipadx=20)
        label.place(x=765, y=50, anchor="center")
        label = tk.Label(self, text='Akkordok', font=('lucida handwriting', 30), anchor="center", fg='#DF744A')
        label.grid(column=5,row=2,sticky="e", ipadx=20)
        label.place(x=765, y=110, anchor="center")
        label_ures = tk.Label(self,text=" ",font=('lucida handwriting', 53))
        label_ures.grid(row=14,column=4)

        lista = tk.Label(self, text='', font=('lucida handwriting', 50))
        lista.grid(row=15,column=3)

        akk = tk.Label(self, text="", font=('lucida handwriting', 100), fg='#bc5c36')

        OPTIONS = [
        "Aadd9",
        "Asus4",
        "Amaj7",
        "Eadd9",
        "E7",
        "Em7",
        "A7",
        "Am7",
        "D7",
        "Dm7",
        "G7",
        "C7",
        "Esus4",
        "Emaj7",
        "B7",
        "Fadd9",
        "Fmaj7",
        "Gadd9",
        "Gmaj7",
        "Dadd9",
        "Dsus4",
        "Dmaj7",
        "Cadd9",
        "Csus4",
        "Cmaj7",
        "Cmaj9"
        ]
        variable = StringVar()
        variable.set("Válassz!") # default value

        def callback(*args):            
            akk.configure(text=variable.get())
            akk.grid(column=5,row=1,sticky="e", ipadx=20)
            akk.place(x=765, y=400, anchor="center")
            kuldAkkord(szerverek[0]['ip'], variable.get())

        w = OptionMenu(lista, variable, *OPTIONS)
        w.pack()
        variable.trace("w", callback)
        menu = w.nametowidget(w.menuname)
        menu.configure(font=('Lucida Handwriting', 12))
        w.configure(font=('Lucida Handwriting', 12))

class Page2_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        vissza = tk.Button(self, text='Vissza', bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A', font=('lucida handwriting', 12),
                            command=lambda : controller.show_frame(Page2))
        vissza.grid(row =0,column=0,sticky=W)
        label = tk.Label(self, text='Közepes', font=('lucida handwriting', 34), fg='#bc5c36')
        label.grid(columnspan=15,ipadx=5)
        label = tk.Label(self, text='Akkordfelbontas', font=('lucida handwriting', 30), fg="#DF744A")
        label.grid(columnspan=15,ipadx=5)
        label_ures = tk.Label(self,text=" ",font=('lucida handwriting', 25))
        label_ures.grid(row=14,column=4)

        akkordpeng_gomb = tk.Button(self, text='1',
                                font=('lucida handwriting', 34),height=9, width=25, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A',  
                            command=lambda : controller.show_frame(Page2_21)
                            )
        akkordpeng_gomb.grid(row=30,column=0)
        pengfajt_gomb = tk.Button(self, text='2',
                                font=('lucida handwriting', 34),height=9, width=25, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A',  
                             command=lambda : controller.show_frame(Page2_22)
                            )
        pengfajt_gomb.grid(row=30,column=1)

class Page2_21(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        vissza = tk.Button(self, text='Vissza', font=('lucida handwriting', 12), bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A',# likewise Page2
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), controller.show_frame(Page2_2)])
        vissza.grid(row =0,column=0,sticky=W)
        label = tk.Label(self, text='Közepes', font=('lucida handwriting', 34), fg='#bc5c36')
        label.grid(columnspan=15,ipadx=5)
        label.place(x=765, y=50, anchor="center")
        label = tk.Label(self, text='Akkordfelbontások', font=('lucida handwriting', 30), fg='#DF744A')
        label.grid(columnspan=15,ipadx=5)
        label.place(x=765, y=110, anchor="center")
        label_ures = tk.Label(self,text="",font=('lucida handwriting', 90))
        label_ures.grid(row=14,column=4)

        em_gomb = tk.Button(self, text='Em',
                            command=lambda : [em_gomb.configure(bg='#93b0c9'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordFelbont1(szerverek[0]['ip'], "em")],
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        em_gomb.grid(row=15, column=0)
        am_gomb = tk.Button(self, text='Am',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#93b0c9'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordFelbont1(szerverek[0]['ip'], "am")],
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        am_gomb.grid(row=15, column=4)
        dm_gomb = tk.Button(self, text='Dm',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#93b0c9'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordFelbont1(szerverek[0]['ip'], "dm")], 
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        dm_gomb.grid(row=15, column=5)
        c_gomb = tk.Button(self, text='C',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#93b0c9'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordFelbont1(szerverek[0]['ip'], "c")],
                            font=('lucida handwriting', 34), height=4, width=13, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        c_gomb.grid(row=15, column=6)
        a_gomb = tk.Button(self, text='A',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#93b0c9'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordFelbont1(szerverek[0]['ip'], "a")],
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        a_gomb.grid(row=16, column=0)
        e_gomb = tk.Button(self, text='E',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#93b0c9'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordFelbont1(szerverek[0]['ip'], "e")],
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        e_gomb.grid(row=16, column=4)
        g_gomb = tk.Button(self, text='G',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#93b0c9'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordFelbont1(szerverek[0]['ip'], "g")],
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        g_gomb.grid(row=16, column=5)
        d_gomb = tk.Button(self, text='D',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#93b0c9'), kuldAkkordFelbont1(szerverek[0]['ip'], "d")],
                            font=('lucida handwriting', 34), height=4, width=13, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        d_gomb.grid(row=16, column=6)

class Page2_22(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        vissza = tk.Button(self, text='Vissza', font=('lucida handwriting', 12), bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A',# likewise Page2
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), controller.show_frame(Page2_2)])
        vissza.grid(row =0,column=0,sticky=W)

        label = tk.Label(self, text='Közepes', font=('lucida handwriting', 34), fg='#bc5c36')
        label.grid(columnspan=15,ipadx=5)
        label.place(x=765, y=50, anchor="center")
        label = tk.Label(self, text='Akkordfelbontások', font=('lucida handwriting', 30), fg='#DF744A')
        label.grid(columnspan=15,ipadx=5)
        label.place(x=765, y=110, anchor="center")
        label_ures = tk.Label(self,text="",font=('lucida handwriting', 90))
        label_ures.grid(row=14,column=4)

        em_gomb = tk.Button(self, text='Em',
                            command=lambda : [em_gomb.configure(bg='#93b0c9'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordFelbont3(szerverek[0]['ip'], "em")],
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        em_gomb.grid(row=15, column=0)
        am_gomb = tk.Button(self, text='Am',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#93b0c9'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordFelbont3(szerverek[0]['ip'], "am")],
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        am_gomb.grid(row=15, column=4)
        dm_gomb = tk.Button(self, text='Dm',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#93b0c9'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordFelbont3(szerverek[0]['ip'], "dm")], 
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        dm_gomb.grid(row=15, column=5)
        c_gomb = tk.Button(self, text='C',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#93b0c9'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordFelbont3(szerverek[0]['ip'], "c")],
                            font=('lucida handwriting', 34), height=4, width=13, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        c_gomb.grid(row=15, column=6)
        a_gomb = tk.Button(self, text='A',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#93b0c9'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordFelbont3(szerverek[0]['ip'], "a")],
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        a_gomb.grid(row=16, column=0)
        e_gomb = tk.Button(self, text='E',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#93b0c9'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordFelbont3(szerverek[0]['ip'], "e")],
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        e_gomb.grid(row=16, column=4)
        g_gomb = tk.Button(self, text='G',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#93b0c9'), d_gomb.configure(bg='#bfd8d2'), kuldAkkordFelbont3(szerverek[0]['ip'], "g")],
                            font=('lucida handwriting', 34), height=4, width=12, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        g_gomb.grid(row=16, column=5)
        d_gomb = tk.Button(self, text='D',
                            command=lambda : [em_gomb.configure(bg='#bfd8d2'), am_gomb.configure(bg='#bfd8d2'), dm_gomb.configure(bg='#bfd8d2'), c_gomb.configure(bg='#bfd8d2'), a_gomb.configure(bg='#bfd8d2'), e_gomb.configure(bg='#bfd8d2'), g_gomb.configure(bg='#bfd8d2'), d_gomb.configure(bg='#93b0c9'), kuldAkkordFelbont3(szerverek[0]['ip'], "d")],
                            font=('lucida handwriting', 34), height=4, width=13, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A')
        d_gomb.grid(row=16, column=6)

class Page2_3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        vissza = tk.Button(self, text='Vissza', font=('lucida handwriting', 12), bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A',# likewise Page2
                            command=lambda : [variable.set("Válassz!"), akk.configure(text=""), controller.show_frame(Page2)])
        vissza.grid(row =0,column=0,sticky=W)

        label = tk.Label(self, text='Közepes', font=('lucida handwriting', 34), fg='#bc5c36')
        label.grid(column=5,row=1,sticky="e", ipadx=20)
        label.place(x=765, y=50, anchor="center")
        label = tk.Label(self, text='Dalok', font=('lucida handwriting', 30), fg='#DF744A')
        label.grid(columnspan=15,ipadx=5)
        label.place(x=765, y=110, anchor="center")
        label_ures = tk.Label(self,text=" ",font=('lucida handwriting', 90))
        label_ures.grid(row=14,column=4)

        lista = tk.Label(self, text='', font=('lucida handwriting', 50))
        lista.grid(row=15,column=3)

        akk = tk.Label(self, text="", font=('lucida handwriting', 60), fg='#bc5c36')

        OPTIONS = [
        "Pioneer",
        "Jó nekem",
  		"Egyszerű dal",
  		"Monster",
        "Mad World",
        "Here Comes the Sun"
        ]
        variable = StringVar()
        variable.set("Válassz!") # default value

        def callback(*args):
            akk.configure(text=variable.get())
            akk.grid(column=5,row=1,sticky="e", ipadx=20)
            akk.place(x=765, y=400, anchor="center")
            kuldDal(szerverek[0]['ip'], variable.get())
            

        w = OptionMenu(lista, variable, *OPTIONS)
        w.pack()
        variable.trace("w", callback)
        menu = w.nametowidget(w.menuname)
        menu.configure(font=('Lucida Handwriting', 20))
        w.configure(font=('Lucida Handwriting', 20))

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        vissza = tk.Button(self, text='Vissza', font=('lucida handwriting', 12), bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A',
                            command=lambda : controller.show_frame(StartPage))
        vissza.grid(row =0,column=0,sticky=W)

        label = tk.Label(self, text='Haladó', font=('lucida handwriting', 34), fg='#DF744A')
        label.grid(columnspan=13,ipadx=5)
        label.place(x=765, y=50, anchor="center")

        label_ures = tk.Label(self,text=" ",font=('lucida handwriting', 50))
        label_ures.grid()

        akkord_gomb = tk.Button(self, text='Akkordok',font=('lucida handwriting', 34), height=10, width=25, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A',
                              
                            command=lambda : controller.show_frame(Page3_1))
        akkord_gomb.grid(row=30,column=0)
        dalok_gomb = tk.Button(self, text='Dalok', font=('lucida handwriting', 34), height=10, width=25, bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A', 
                            command=lambda : controller.show_frame(Page3_2))
        dalok_gomb.grid(row=30,column=1)

class Page3_1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        vissza = tk.Button(self, text='Vissza',font=('lucida handwriting', 12), bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A', # likewise Page2
                            command=lambda : [variable.set("Válassz!"), akk.configure(text=""), controller.show_frame(Page3), kuldKikapcs(szerverek[0]['ip'])])
        vissza.grid(row =0,column=0,sticky=W)

        label = tk.Label(self, text='Haladó', font=('lucida handwriting', 34), fg='#bc5c36')
        label.grid(column=5,row=1,sticky="e", ipadx=20)
        label.place(x=765, y=50, anchor="center")
        label = tk.Label(self, text='Akkordok', font=('lucida handwriting', 30), fg='#DF744A')
        label.grid(columnspan=15,ipadx=5)
        label.place(x=765, y=110, anchor="center")
        label_ures = tk.Label(self,text=" ",font=('lucida handwriting', 80))
        label_ures.grid(row=14,column=4)

        lista = tk.Label(self, text='', font=('lucida handwriting', 50))
        lista.grid(row=15,column=3)

        akk = tk.Label(self, text="", font=('lucida handwriting', 100), fg='#bc5c36')

        OPTIONS = [
        "Cm",
        "Gm",
        "Fm",
        "Bm",
        "Bbm",
        "F",
        "B",
        "Bb",
        "Cm7",
        "Gsus4",
        "Fsus4",
        "Bmaj7",
        "Bsus4",
        "Badd9"
        ]
        variable = StringVar()
        variable.set("Válassz!") # default value

        def callback(*args):
            akk.configure(text=variable.get())
            akk.grid(column=5,row=1,sticky="e", ipadx=20)
            akk.place(x=765, y=400, anchor="center")
            kuldAkkord(szerverek[0]['ip'], variable.get())

        w = OptionMenu(lista, variable, *OPTIONS)
        w.pack()
        variable.trace("w", callback)
        menu = w.nametowidget(w.menuname)
        menu.configure(font=('Lucida Handwriting', 20))
        w.configure(font=('Lucida Handwriting', 20))
       
class Page3_2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        vissza = tk.Button(self, text='Vissza', font=('lucida handwriting', 12), bg="#bfd8d2", activebackground="#bad6d8", bd=1,fg='#DF744A',activeforeground='#DF744A',# likewise Page2
                            command=lambda : [variable.set("Válassz!"), akk.configure(text=""), controller.show_frame(Page3)])
        vissza.grid(row =0,column=0,sticky=W)

        label = tk.Label(self, text='Haladó', font=('lucida handwriting', 34), fg='#bc5c36')
        label.grid(column=5,row=1,sticky="e", ipadx=20)
        label.place(x=765, y=50, anchor="center")
        label = tk.Label(self, text='Dalok', font=('lucida handwriting', 30), fg='#DF744A')
        label.grid(columnspan=15,ipadx=5)
        label.place(x=765, y=110, anchor="center")
        label_ures = tk.Label(self,text=" ",font=('lucida handwriting', 90))
        label_ures.grid(row=14,column=4)


        lista = tk.Label(self, text='', font=('lucida handwriting', 50))
        lista.grid(row=15,column=3)

        akk = tk.Label(self, text="", font=('lucida handwriting', 60), fg='#bc5c36')
        
        OPTIONS = [
        "Heavy",
        "67-es út",
  		"Believer",
  		"Boulevard of Broken Dreams",
        "Can't Help Falling in Love",
        "Let It Be"
        ]
        variable = StringVar()
        variable.set("Válassz!") # default value

        def callback(*args):
            akk.configure(text=variable.get())
            akk.grid(column=5,row=1,sticky="e", ipadx=20)
            akk.place(x=765, y=400, anchor="center")
            kuldDal(szerverek[0]['ip'], variable.get())

        w = OptionMenu(lista, variable, *OPTIONS)
        w.pack()
        variable.trace("w", callback)
        menu = w.nametowidget(w.menuname)
        menu.configure(font=('Lucida Handwriting', 20))
        w.configure(font=('Lucida Handwriting', 20))

if __name__ == '__main__':
    probalkozasok = 0
    while len(szerverek) == 0:
        szerverek = keresFutoSzerver()
        probalkozasok += 1
        if probalkozasok > 10:
            break
    print(szerverek)
    app = MainWindow()
    app.mainloop()


