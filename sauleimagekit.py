import csv
import tkinter as tk
from tkinter import filedialog

from PIL import Image, ImageFont, ImageDraw

class Application(tk.Frame):
    csv_file = None
    root_dir = None
    color_select = ''

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.btn = tk.Button(self, text='Select CSV File', command=self.OpenCSV)
        self.btn_loop = tk.Button(self, text="Go", command=self.loop_over_csv)
        self.btn_dir = tk.Button(self, text="Select Directory", command=self.OpenDir)
        self.btn.pack(side="top")
        self.btn_dir.pack(side="top")
        self.btn_loop.pack(side="top")
        vals = ['white', 'black']
        etiqs = ['White', 'Black']
        self.color_select = tk.StringVar()
        self.color_select.set('white')
        for i in range(2):
            b = tk.Radiobutton(root, variable=self.color_select, text=etiqs[i], value=vals[i])
            b.pack(side='left', expand=1)


    def UpdateImage(self, filename='image1.jpg', text='text_default'):
        print('Try UpdateImage' + filename, text , 'in color', self.color_select.get())
        try:
            img = Image.open(filename)
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("./fonts/CentieSans.ttf", 50)
            draw.text((img.width - 300, img.height - 100), text, self.color_select.get(), font=font)
            img.save(filename.split('.')[0] + '_update.' + filename.split('.')[1])
        except:
            print('Can\'t find %s' % filename)
            pass

    def OpenDir(self):
        self.root_dir = filedialog.askdirectory(initialdir = ".")

    def OpenCSV(self):
        self.csv_file = filedialog.askopenfilename(initialdir = ".",title = "Select CSV file",filetypes = (("csv files","*.csv"),("all files","*.*")))

    def loop_over_csv(self):
        print('loopping over %s in dir %s' % (self.csv_file, self.root_dir))
        f = open(self.csv_file)
        csv_f = csv.reader(f)
        next(csv_f)
        for row in csv_f:
            self.UpdateImage(self.root_dir + '/' + row[0], row[1])
        return 



root = tk.Tk()
app = Application(master=root)
app.mainloop()