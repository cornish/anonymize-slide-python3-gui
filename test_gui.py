import sys,os
from tkinter import Tk
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from tkinter import Button

def main():
    root = Tk()
    root.withdraw()

    response = mb.askokcancel('Warning', " ".join('This program \
        permanently removes the label image from the selected \
        WSIs. It is recommended that you do not do this on \
        original or sole copy files.'.split()),icon='warning')

    if not response:
        sys.exit()

    script_path = (os.path.dirname(os.path.realpath(__file__)))
    dir = fd.askdirectory(initialdir=script_path,title='Select directory')

    #fn = fd.askopenfilename(filetypes = (("WSI", "*.tplate")
    #    ,("HTML files", "*.html;*.htm")
    #    ,("All files", "*.*") ))

    root.destroy()

    input("Press Enter to close...")

if __name__ == '__main__':
    main()
