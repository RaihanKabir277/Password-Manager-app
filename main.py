# print("Code will starts here....")

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ----------------Random password Generator -----------
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

    # print(f"Your password is: {password}")


# ---------Save into the file -------------
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
         website: {
              "email" : email,
              "password" : password,
         }
    }

    if len(website) < 3 or len(password) < 3:
        messagebox.showinfo(title="Oops",message="Please do not Leave any fields empty or less then 3 character")

    else:    
        # is_ok = messagebox.askokcancel(title="Website", message=f"There are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")

        # if is_ok:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file) 
                # file.write(f"{website} | {email} | {password}\n")
                
                

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
                
        else:
            # updating old data from new data   
            data.update(new_data)

            with open("data.json", "w") as file:
                    # saving updating data
                    json.dump(data, file, indent=4)   #for write data in json

        finally:             
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            # email_entry.delete(0,4)
            words = email.split("@")
            if len(words) > 1:
                        new_text = " ".join(words[1:])
            else:
                        new_text = " "
            email_entry.delete(0, END)
            email_entry.insert(0, new_text)

# ---------------- Searching from the file --------------------
def searching():
    website = website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except:
        messagebox.showerror(title="Error", message="No data file added like this")
            
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPasswors: {password}")
            

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

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "name@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# ------Buttons-------
search_btn = Button(text="Search",width=13, command=searching)
search_btn.grid(row=1, column=2)
password_btn = Button(text="Generate Password", command=generate_password)
password_btn.grid(row=3, column=2)
add_btn = Button(text="ADD", width=30, command=save)
add_btn.grid(row=4, column=1,columnspan=2)


window.mainloop()
