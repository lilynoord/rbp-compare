from tkinter import filedialog as fd


def select_file(title):
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title=title,
        initialdir='./',
        filetypes=filetypes)
   
    return str(filename)


def save_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.asksaveasfile(
        title="Save File As",
        initialdir='./files',
        filetypes=filetypes
    )

    return filename

