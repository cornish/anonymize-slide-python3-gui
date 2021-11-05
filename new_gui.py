from tkinter import *
import tkinter.messagebox as box

class App(Tk):
    def __init__(self):
        super().__init__()

        self.title('Remove label from WSIs')

        #frame = Frame(root)

        self.listbox = Listbox(self,width=50,height=20,selectmode=EXTENDED)
        self.listbox2 = Listbox(self,width=50,height=20,selectmode=EXTENDED)
        #scrollbar = Scrollbar(listbox)
        #listbox.config(yscrollcommand = scrollbar.set)
        #scrollbar.config(command = listbox.yview)

        self.listbox.insert( 1, '<filename>' )
        self.listbox.insert( 2, '<filename>' )
        self.listbox.insert( 3, '<filename>' )

        self.btn_add = Button(self, text = 'Add file', command=self.add_files)
        self.btn_add.grid(row=0,column=1,sticky=NW)
        self.btn_delete = Button(self, text = 'Delete file', command=self.delete_selected_files)
        self.btn_delete_all = Button(self, text = 'Delete all files', command=self.delete_all_files)

        self.btn_add_selection = Button(self, text = '-->', command=self.add_selected_files)
        self.btn_remove_selection = Button(self, text = '<--', command=self.remove_selected_files)

        self.listbox.grid(row=0,column=0,sticky=NW,padx=5,pady=5)
        self.listbox2.grid(row=0,column=3,sticky=NW,padx=5,pady=5)
        self.btn_add.grid(row=1,column=0,sticky=NW,padx=5,pady=5)
        self.btn_delete.grid(row=1,column=1,sticky=NW,padx=5,pady=5)
        self.btn_delete_all.grid(row=1,column=2,sticky=NW,padx=5,pady=5)
        self.btn_add_selection.grid(row=0,column=1,sticky=NW,padx=5,pady=5)
        self.btn_remove_selection.grid(row=0,column=2,sticky=NW,padx=5,pady=5)

        #btn_add.pack(side = RIGHT, padx = 5)
        #btn_delete.pack(side = RIGHT, padx = 5)
        #btn_delete_all.pack(side = RIGHT, padx = 5)

        #frame.pack(padx = 30, pady = 30)

    def add_selected_files(self):
        for i in self.listbox.curselection():
            self.listbox2.insert(END,self.listbox.get(i))

    def remove_selected_files(self):
        for i in self.listbox2.curselection():
            self.listbox2.delete(i)

    def add_files(self):
        self.listbox.insert(END,'myfile.svs')

    def delete_selected_files(self):
        for i in self.listbox.curselection():
            self.listbox.delete(i)

    def delete_all_files(self):
        self.listbox.delete(0,END)

def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()
