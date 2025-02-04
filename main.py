from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters


    shuffle(password_list)

    password = "".join(password_list)
    password_box.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_box.get()
    email = email_box.get()
    password = password_box.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Empty tab", message="Website or Password cannot be empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            data = {}
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_box.delete(0, END)
            password_box.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_box.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

pass_pic = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height= 200, bg="white", highlightthickness=0)
canvas.create_image(100,100, image=pass_pic)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:",bg="white", highlightthickness=0)
website_label.grid(column=0, row= 1)

email_label = Label(text="Email/Username:", bg="white", highlightthickness=0)
email_label.grid(column= 0, row=2)

password_label = Label(text="Password:", bg="white", highlightthickness=0)
password_label.grid(column= 0, row=3)

website_box = Entry(width=20)
website_box.grid(column=1, row=1)
website_box.focus()

search_button = Button(text="Search", width= 11, command= find_password)
search_button.grid(column= 2, row =1)

email_box = Entry(width=35)
email_box.grid(column=1, row=2, columnspan=2)
email_box.insert(0,"yeboah@example.com")

password_box = Entry(width=20)
password_box.grid(column=1, row=3)


gen_password = Button(text="Generate Password", width=11, command= generate_password)
gen_password.grid(column=2, row=3)

add_button = Button(text="Add", width=33, command= save)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()