from tkinter import *
from tkinter import messagebox
import random
import string

window = Tk()
window.title("Генератор на пароли")


passwords = []

def generate_password():
    chars = ""

    if lower_var.get():
        chars += string.ascii_lowercase

    if upper_var.get():
        chars += string.ascii_uppercase

    if digit_var.get():
        chars += string.digits

    if special_var.get():
        chars += string.punctuation

    if chars == "":
        messagebox.showwarning("Грешка", "Избери поне една опция!")
        return

    length = slider.get()

    password = ""
    for i in range(length):
        password += random.choice(chars)

    if len(passwords) < 10:
        passwords.append(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    if length < 12:
        strength_label.config(text="Слаба")
    elif length < 20:
        strength_label.config(text="Средна")
    else:
        strength_label.config(text="Силна")

def copy_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning("Грешка", "Няма генерирана парола!")
        return

    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()

    messagebox.showinfo("Успешно", "Паролата е копирана!")

def save_password():
    if not passwords:
        messagebox.showwarning("Грешка", "Няма генерирани пароли!")
        return

    with open("passwords.txt", "w") as file:
        for p in passwords:
            file.write(p + "\n")

    messagebox.showinfo(
        "Успешно",
        f"Запазени са {len(passwords)} пароли."
    )

Label(window, text="Дължина на паролата").pack()

slider = Scale(window, from_=8, to=32, orient= "horizontal")
slider.pack()

lower_var = IntVar(value=1)
upper_var = IntVar(value=1)
digit_var = IntVar(value=1)
special_var = IntVar(value=1)

Checkbutton(window, text="Малки букви", variable=lower_var).pack()
Checkbutton(window, text="Главни букви", variable=upper_var).pack()
Checkbutton(window, text="Цифри", variable=digit_var).pack()
Checkbutton(window, text="Специални символи", variable=special_var).pack()

Button(window, text="Генерирай", command=generate_password).pack(pady=10)

password_entry = Entry(window, width=40)
password_entry.pack()

strength_label = Label(window, text="Сила: -")
strength_label.pack(pady=10)

Button(window, text="Копирай", command=copy_password).pack()

Button(window, text="Запази списък", command=save_password).pack(pady=10)

window.mainloop()
