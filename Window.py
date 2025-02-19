from tkinter import *


window = Tk() 
window.geometry("475x475")

window.title("Password Generator")

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

num_yes_button = Checkbutton(window, text="Yes", bg="black", fg="#2ee800", font=('Ink Free', 10))
num_yes_button.place(x=350, y= 200)
num_no_button = Checkbutton(window, text="No", bg="black", fg="#2ee800", font=('Ink Free', 10))
num_no_button.place(x=400, y= 200)

spec_char = Label(window, text="Add Special Characters? ", font=('Ink Free', 15), fg="#2ee800", bg="black")
spec_char.place(x=10, y=250)

char_yes_button = Checkbutton(window, text="Yes", bg="black", fg="#2ee800", font=('Ink Free', 10))
char_yes_button.place(x=350, y= 250)
char_no_button = Checkbutton(window, text="No", bg="black", fg="#2ee800", font=('Ink Free', 10))
char_no_button.place(x=400, y= 250)


button = Button(window, text='Submit', font=('Ink Free', 10, 'bold'), bg='#2b2b2a', fg='#2ee800', activebackground='#2ee800', activeforeground='#2b2b2a')
button.place(x=window.winfo_width() // 2 - button.winfo_reqwidth() // 2, y=300) 

pwd_output_box = Text(window, height=6, width=55, bg="#2b2b2a", fg="#2ee800")
pwd_output_box.place(x=15, y=350)

pwd_output_box.config(state=DISABLED)
 
window.mainloop()