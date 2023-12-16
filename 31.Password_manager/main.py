from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_passwd():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_1 = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_2 = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_3 = [random.choice(numbers) for _ in range(random.randint(4, 6))]

    password = password_1 + password_2 + password_3
    random.shuffle(password)
    hard_password = ''.join(password)
    password_entry.delete(0, END)
    password_entry.insert(0, hard_password)
    pyperclip.copy(hard_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website_entry.get()) < 1 or len(password_entry.get()) < 1:
        messagebox.showerror(title="oops", message="Please don't leave the box empty")

    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered: "
                                                                          f"\nEmail/Username: {email_entry.get()}"
                                                                          f"\nPassword: {password_entry.get()} "
                                                                          f"\nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"Website: {website_entry.get()}, Email/Username: {email_entry.get()}, Password: "
                                f"{password_entry.get()}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "madhu@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", width=15, command=generate_passwd)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
