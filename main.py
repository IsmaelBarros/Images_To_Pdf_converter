from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

from converter import converter_images


class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Conversor de images em PDF")
        self.master.config(bg='white')

        self.frame = Frame(self.master, bg='white')
        self.frame.pack()

        self.master.resizable(0, 0)

        # dimensão da janela
        self.largura = 600
        self.altura = 300

        # resolução do sistema
        self.largura_screen = self.master.winfo_screenwidth()
        self.altura_screen = self.master.winfo_screenheight()

        # posição da janela
        self.posx = self.largura_screen/2 - self.largura/2
        self.posy = self.altura_screen/2 - self.altura/2

        # definir geometria
        self.master.geometry("%dx%d+%d+%d" %
                             (self.largura, self.altura, self.posx, self.posy))

        # ============================VARIAVEIS=====================================================
        self.pdf_name = StringVar()
        self.directory_path = StringVar()
        self.image_files = StringVar()

        # ==============================FRAMES======================================================
        self.frame1 = LabelFrame(self.frame, width=100, height=200, font=('arial', 20, 'bold'),
                                 relief='ridge', bg='light cyan', bd=5)
        self.frame1.pack(fill='both', side='left', expand='True')

        self.frame2 = LabelFrame(self.frame, width=100, height=200, font=('arial', 10, 'bold'),
                                 relief='ridge', bg='white smoke', bd=5)
        self.frame2.pack(fill='both', side='right', expand='True')

        # =========================WIDGETS FRAME1===================================================
        self.lblImagemName = Label(
            self.frame1, text='Escolha as imagens', font=('arial', 10, 'bold'), bg='light cyan')
        self.lblImagemName.grid(column=0, row=0, padx=10, pady=10)
        self.btnOpen = Button(
            self.frame1, text="Procurar imagens", command=self.open)
        self.btnOpen.grid(column=0, row=1, padx=5, pady=5)

        self.listbox = Listbox(self.frame1, height=10,
                               width=20,
                               bg="grey",
                               activestyle='dotbox',
                               font="Helvetica",
                               fg="yellow")

        # =========================WIDGETS FRAME 2==================================================

        self.lblPdfName = Label(
            self.frame2, text='Digite um nome para o arquivo pdf', font=('arial', 10, 'bold'), bg='white smoke')
        self.lblPdfName.grid(column=0, row=0)

        self.txtPdfName = Entry(
            self.frame2, font=('arial', 15, 'bold'), width=30, textvariable=self.pdf_name)
        self.txtPdfName.grid(column=0, row=1, padx=10, pady=10)

        self.btnConverter = Button(
            self.frame2, text="Converter em PDF", command=self.convert)
        self.btnConverter.grid(column=0, row=2, padx=10, pady=10)

    # ================================FUNCTIONS======================================================

    def open(self):
        self.master.filename = filedialog.askopenfilenames(
            initialdir='/Users/ismas/OneDrive/Imagens',
            title="Selecione uma ou mais imagens",
            filetypes=(("jpg files", "*.jpg"), ("jpeg files", "*.jpeg"), ("png files", "*.png")))
        list_full_paths = self.master.splitlist(self.master.filename)

        list_path = list_full_paths[0].split('/')
        directory_path_list = list_path[:-1]
        self.directory_path = '/'.join(directory_path_list)

        files = []

        # print files list on the screen
        for i, path in enumerate(list_full_paths):
            # files path
            list_dirs = path.split('/')
            files.append(list_dirs[-1])
            self.listbox.insert(i+1, files[i])

        self.image_files = files

        self.listbox.grid(column=0, row=1)

    def convert(self):
        pdf_name = self.pdf_name.get()
        directory_path = self.directory_path
        list_image_files = self.image_files

        converter_images(directory_path, list_image_files, pdf_name)


# RUN MAIN PROGRAM
if __name__ == '__main__':
    root = Tk()
    application = Window1(root)
    root.mainloop()
