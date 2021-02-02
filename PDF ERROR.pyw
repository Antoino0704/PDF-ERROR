import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
from PIL import Image, ImageTk
import os

class Danger:
    def __init__(self, win):
        #creazione menu
        menu = tk.Menu(win)
        sottomenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='options', menu=sottomenu)
        sottomenu.add_command(label='Apri', command=self.Apri)
        sottomenu.add_command(label='Danneggia', command=self.Danneggia)
        sottomenu.add_command(label='Info', command=self.Information)
        win.configure(menu=menu)

        #creazione immaggine di sfondo
        img = Image.open('image/images.png')
        self.imgtk = ImageTk.PhotoImage(img)
        label_image = tk.Label(win, image=self.imgtk)
        label_image.place(y=0, x=0, relwidth=1, relheight=1)


        #creazione label di informazione dello stato
        self.stato = tk.StringVar()
        self.stato.set('Nessun file aperto')
        confirm = tk.Label(win, textvariable=self.stato, fg='red', font=("", 35))
        confirm.grid(row=0,column=0,sticky="NW")
        confirm.grid_propagate(0)

        #apri il file
    def Apri(self):
        self.fo = tkinter.filedialog.askopenfilename(defaultextension='.pdf', filetypes=[('File PDF', '*.pdf')])
        if (os.path.exists(self.fo) == True):
            self.stato.set('File aperto')
        
    #Danneggia file
    def Danneggia(self):
        if (os.path.exists(self.fo) == True):
            fi = tkinter.filedialog.asksaveasfilename(defaultextension='.pdf', filetypes=[('File PDF', '*.pdf')])
            fp = open(fi, 'w')
            fp.close()
            self.stato.set('File Danneggiato con successo')

    #information for program
    def Information(self):
        tkinter.messagebox.showinfo('Info PDF ERROR', 'version: 1.1.4\nAuthor: Antonino Buscarino')


#parte principale
win = tk.Tk()
win.title('PDF ERROR')
win.geometry('700x600')
win.grid_columnconfigure(0, weight=1)
win.iconbitmap("image/Icon.ico")
c = Danger(win)
win.mainloop()
