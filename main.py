# print("Code will starts here....")

from tkinter import *


# -------UI setup------

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
# --------label-----------
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# ---------Entries--------------

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# ------Buttons-------

password_btn = Button(text="Generate Password")
password_btn.grid(row=3, column=2)
add_btn = Button(text="ADD", width=30)
add_btn.grid(row=4, column=1,columnspan=2)


window.mainloop()
