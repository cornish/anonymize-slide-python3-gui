from tkinter import *
import tkinter.messagebox as box

def main():
    root = Tk()
    root.title('')

    #frame = Frame(root)

    listbox = Listbox(root,width=50,height=20)
    #scrollbar = Scrollbar(listbox)
    #listbox.config(yscrollcommand = scrollbar.set)
    #scrollbar.config(command = listbox.yview)

    listbox.insert( 1, '<filename>' )
    listbox.insert( 2, '<filename>' )
    listbox.insert( 3, '<filename>' )

    btn_add = Button(root, text = 'Add file', command=add_files)
    btn_add.grid(row=0,column=1,sticky=NW)
    btn_delete = Button(root, text = 'Delete file', command=delete_selected_files)
    btn_delete_all = Button(root, text = 'Delete all files', command=delete_all_files)

    listbox.grid(row=0,column=0,sticky=NW,padx=5,pady=5)
    btn_add.grid(row=1,column=0,sticky=NW,padx=5,pady=5)
    btn_delete.grid(row=1,column=1,sticky=NW,padx=5,pady=5)
    btn_delete_all.grid(row=1,column=2,sticky=NW,padx=5,pady=5)

    #btn_add.pack(side = RIGHT, padx = 5)
    #btn_delete.pack(side = RIGHT, padx = 5)
    #btn_delete_all.pack(side = RIGHT, padx = 5)

    #frame.pack(padx = 30, pady = 30)

    root.mainloop()

def add_files():
    listbox.insert(END,'myfile.svs')

def delete_selected_files():
    for i in listbox.curselection():
        listbox.delete(i)

def delete_all_files():
    listbox.delete(0,END)

if __name__ == '__main__':
    main()
