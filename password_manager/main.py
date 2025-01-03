from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT_NAME = "Poppins"
background_clr = "#d6ccb1"
text = "#173B45"
# ...............................Password ...
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]

    password_list = password_letters + password_symbols +password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)


#......................................... Save password ...


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)

    if not website or not email or not password:
        messagebox.showinfo(title="Are you Stupid?",message="You Left Some of The Boxes Empty. Fill Them Now")
    else:
        ok = messagebox.askokcancel(title="website",message=f"Is This Correct:\n Email:{email} \n Password:{password}")
        # the ok variable stores the boolean output from messagebox.askokcancel() which is used below with an if statement, if value is true(when user clicks ok) then executes rest of the function
        if ok:
            f = open("data.txt", "a")
            f.write(f"{website} | {email} | {password}\n")
            f.close()


# ................................................. UI ...

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
lock = PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(row=0, column=1)

#................... Labels ...
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#........................ Entries ...
website_entry = Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "sangeet.himire@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#............................ Buttons ...
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)





window.mainloop()