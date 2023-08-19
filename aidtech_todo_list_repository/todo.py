import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

class ToDoListApp:
    
    def initialize_ui(self,root):
        self.root = root
        self.root.title("TO_DO_LIST")
        self.root.geometry("400x650")

        self.task_list = []


        # Top bar
        self.Image_icon=PhotoImage(file="icon.png")
        self.root.iconphoto(False,self.Image_icon)
        to_image = Image.open("topbar2.jpg")
        nsize=(400,100)
        top_image = to_image.resize(nsize)
        self.top_photo = ImageTk.PhotoImage(top_image)
        top_label = Label(self.root, image=self.top_photo)
        top_label.pack()

        # Dock icon
        dock_image = Image.open("dock2.jpeg")
        new_size = (30, 30)
        dock1_image = dock_image.resize(new_size)
        self.dock_photo = ImageTk.PhotoImage(dock1_image)
        label = Label(self.root, image=self.dock_photo)
        label.place(x=30, y=25)

        # Heading
        heading = Label(self.root, text="Organize..Your..Tasks", font=" arial 20 bold italic ",fg="white",bg="#32405b")
        heading.place(x=85, y=20)

        # Main entry and button
        frame = Frame(self.root, width=400, height=80, bg="#32405b")
        frame.place(x=0, y=180)

        self.task = StringVar()
        self.task_entry = Entry(frame, width=18, font="arial 20",bd=10)
        self.task_entry.place(x=0, y=7)
        self.task_entry.focus()

        add_icon = Image.open("add.jpeg")
        ms = (50, 50)
        add1_icon = add_icon.resize(ms)
        self.add_icon_photo = ImageTk.PhotoImage(add1_icon)

        button = Button( self.root, image=self.add_icon_photo, bd=0, command=self.add_task)
        button.place(x=310, y=190)

        # Listbox
        frame1 = Frame(self.root, bd=3, width=700, height=280, bg="#32405b")
        frame1.pack(pady=(160, 0))
        self.listbox = Listbox(frame1, font=('arial', 12), width=40, height=12,bd=20, bg="#32405b", fg="white", cursor="hand2", selectbackground="black")

        self.listbox.pack(side=LEFT, fill=BOTH, padx=2)
        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side=RIGHT, fill=BOTH)

        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        self.open_task_file()

        # Delete button
        delete_icon = Image.open("del.jpg")
        ms = (50, 50)
        delete_icon = delete_icon.resize(ms)
        self.delete_icon_photo = ImageTk.PhotoImage(delete_icon)

        Button(self.root, image=self.delete_icon_photo, bd=0, command=self.delete_task).pack(side=BOTTOM, pady=13)
        
    def add_task(self):
        i = self.task_entry.get()
        self.task_entry.delete(0, END)

        if i:
            with open("taskfile.txt", "w") as t:
                t.write(f"\n{i}")
            self.task_list.append(i)
            self.listbox.insert(END, i)

    def open_task_file(self):
        try:
            with open("taskfile.txt", "r") as t:
                tasks = t.readlines()
            for i in tasks:
                if i != '\n':
                    self.task_list.append(i)
                    self.listbox.insert(END, i)
        except:
            file = open("task_file.txt", "w")
            file.close()

    def delete_task(self):
        i = str(self.listbox.get(ANCHOR))
        if i in self.task_list:
            self.task_list.remove(i)
            with open("taskfile.txt", "w") as t1:
                for j in self.task_list:
                    t1.write(j + "\n")
            self.listbox.delete(ANCHOR)

    def run(self):
        self.root.mainloop()

root = tk.Tk()
app = ToDoListApp()
app.initialize_ui(root)
app.run()
