from tkinter import *
from tkinter import filedialog
from tkinter import font, ttk
import os, subprocess

#root
root = Tk()
root.title("Pykachu")
root.iconbitmap("icon.ico")
root.geometry("980x490")

global open_status_name
open_status_name = False

#functions
def new():
    my_text.delete("1.0", END)
    root.title("New File ~ @ Pykachu")
    status_bar.config(text="New File    ")

def open_file():
    text_file = filedialog.askopenfilename(initialdir="C:/", title="Open File", filetypes=(("Python Files", "*.py"), ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("CSS Files", "*.css"), ("Javascript Files", "*.js")))
    if text_file:
        global open_status_name
        open_status_name = text_file
        name = text_file
        name_str = os.path.basename(name)
        my_text.delete("1.0", END)
        root.title(f'{name_str} ~ @ Pykachu')
        status_bar.config(text=f'Saved: {name}       ')
        text_file = open(text_file, 'r')
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()


def save_as():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="C:/", title="Save As", filetypes=(("Python Files", "*.py"), ("Text Files", "*.txt"), ("HTML Files", "*.html"), ("CSS Files", "*.css"), ("Javascript Files", "*.js")))

    if text_file:
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        name = text_file.name
        name_str = os.path.basename(name)
        root.title(f'{name_str} ~ @ Pykachu')
        status_bar.config(text=f'Saved: {name}       ')

def save_file():
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        _open_status_name = text_file.name
        print(open_status_name)
        print(_open_status_name)
        status_bar.config(text=f'Saved: {_open_status_name}        ')
    else:
        save_as()

def run():
    if open_status_name:
        text_file = open(open_status_name)
        name = text_file.name
        process = subprocess.Popen(["python", "-u", f"{name}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        code_output.insert('1.0', output)
        code_output.insert('1.0',  error)

#UI


#bottom
status_bar = Label(root, text="Ready        ", anchor=E)
status_bar.configure(fg="white")
status_bar.pack(fill=X, side=BOTTOM)

top_label = Label(root, bg="blue")
run_btn = Button(root, text ="Run", bd=0, fg="white", font=("Helvetica", 10), command = run)
run_btn.configure(bg="#33cc33")
top_label.place(x=0, y=0, relwidth=1, relheight=0.5)
run_btn.pack(side=TOP, anchor=NE, pady=5, padx=5)

code_output = Text(height=10, padx=5, pady=5)
code_output.configure(bg="#001433", fg="white")
code_output.pack(side=BOTTOM, fill=X)

#main
my_frame = Frame(root)
my_frame.pack()

#text-scroll
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#text-window
my_text = Text(my_frame, fg="white", bd=0, padx=5, pady=5, width=150, height=35, font=("Cambria", 16), selectbackground="orange", selectforeground="white", undo=True, yscrollcommand=text_scroll.set)
my_text.configure(bg="#001f4d")
my_text.pack()

# text_scroll.config(command=my_text.yview)

#menu bar
my_menu = Menu(root)
root.config(menu=my_menu)

#file menu
file_menu = Menu(my_menu, tearoff=False)
file_menu.add_command(label="New", command=new)
file_menu.add_command(label="Save as", command=save_as)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

#run menu
# run_menu = Menu(my_menu, tearoff=False)

# add all menus
my_menu.add_cascade(label="File", menu=file_menu)
status_bar.configure(bg="#0000cc")


root.mainloop()
