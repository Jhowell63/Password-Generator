from tkinter import *
import random
import Password_Gen

window = Tk() 
window.geometry("475x475")

window.title("Password Generator")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = 475
window_height = 475
x_position = (screen_width // 2) - (window_width // 2)
y_position = (screen_height // 2) - (window_height // 2)

window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


lock_icon = PhotoImage(file= 'lock.png')
window.iconphoto(True, lock_icon)

window.config(background="black")

window.update_idletasks()

app_title = Label(window, text="Random Password Generator", font=('Ink Free', 25), fg="#2ee800", bg="black")
app_title.place(x=window.winfo_width() // 2 - app_title.winfo_reqwidth() // 2, y=20)

min_char = Label(window, text="Minimum number of characters: ", font=('Ink Free', 15), fg="#2ee800", bg="black")
min_char.place(x=10, y=100)
min_box = Entry(window, width="8", bg='#2b2b2a', fg='#2ee800', font=('Ink Free', 15))
min_box.place(x=350, y=100)

max_char = Label(window, text="Maximun number of characters: ", font=('Ink Free', 15), fg="#2ee800", bg="black")
max_char.place(x=10, y=150)
max_box = Entry(window, width="8", bg='#2b2b2a', fg='#2ee800', font=('Ink Free', 15))
max_box.place(x=350, y=150)

add_num = Label(window, text="Add numbers? ", font=('Ink Free', 15), fg="#2ee800", bg="black")
add_num.place(x=10, y=200)

num_var = IntVar()
num_yes_button = Checkbutton(window, text="Yes", bg="black", fg="#2ee800", font=('Ink Free', 10), variable=num_var, onvalue=1, offvalue=0)
num_yes_button.place(x=350, y= 200)
num_no_button = Checkbutton(window, text="No", bg="black", fg="#2ee800", font=('Ink Free', 10), variable=num_var, onvalue=0, offvalue=1)
num_no_button.place(x=400, y= 200)

spec_char = Label(window, text="Add Special Characters? ", font=('Ink Free', 15), fg="#2ee800", bg="black")
spec_char.place(x=10, y=250)

char_var = IntVar()
char_yes_button = Checkbutton(window, text="Yes", bg="black", fg="#2ee800", font=('Ink Free', 10), variable=char_var, onvalue=1, offvalue=0)
char_yes_button.place(x=350, y= 250)
char_no_button = Checkbutton(window, text="No", bg="black", fg="#2ee800", font=('Ink Free', 10), variable=char_var, onvalue=0, offvalue=1)
char_no_button.place(x=400, y= 250)
char_no_button.place(x=400, y= 250)


def generate_password_from_gui():
    try:
        min_length = int(min_box.get())  
        max_length = int(max_box.get())  
        
        if min_length > max_length:
            pwd_output_box.config(state=NORMAL)
            pwd_output_box.delete(1.0, END)
            pwd_output_box.insert(END, "Minimum can't be greater than maximum!")
            pwd_output_box.config(state=DISABLED)
            return

        include_numbers = num_var.get() == 1
        include_special_chars = char_var.get() == 1
        
        if max_length > 20:
            password_length = random.randint(min_length, 20)
        else:
            password_length = random.randint(min_length, max_length)

        pwd = Password_Gen.generate_password(password_length, include_numbers, include_special_chars)

        pwd_output_box.config(state=NORMAL)
        pwd_output_box.delete(1.0, END)
        pwd_output_box.insert(END, pwd)
        pwd_output_box.config(state=DISABLED)
        
    except ValueError:
        pwd_output_box.config(state=NORMAL)
        pwd_output_box.delete(1.0, END)
        pwd_output_box.insert(END, "Please enter valid numbers.")
        pwd_output_box.config(state=DISABLED)



button = Button(window, text='Submit', font=('Ink Free', 10, 'bold'), bg='#2b2b2a', fg='#2ee800', activebackground='#2ee800', activeforeground='#2b2b2a', command=generate_password_from_gui)
button.place(x=window.winfo_width() // 2 - button.winfo_reqwidth() // 2, y=300)


pwd_output_box = Text(window, height=2, width=25, bg="#2b2b2a", fg="#2ee800", font=("Ink Free", 12))
pwd_output_box.place(x=100, y=350)


pwd_output_box.config(state=DISABLED)

def copy_to_clipboard():
    password = pwd_output_box.get("1.0", END).strip() 
    
    if password:
        window.clipboard_clear()
        window.clipboard_append(password) 
        window.update()
        

copy_button = Button(window, text='Copy', font=('Ink Free', 10, 'bold'), bg='#2b2b2a', fg='#2ee800', activebackground='#2ee800', activeforeground='#2b2b2a', height=2, command=copy_to_clipboard)
copy_button.place(x=window.winfo_width() // 2 - copy_button.winfo_reqwidth() // 2 + 115, y=350)

 
window.mainloop()