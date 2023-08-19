import tkinter as tk
import random
import string
def generate_password():
    username=username_entry.get()
    password_length=int(length_entry.get())
    characters=string.ascii_letters+string.digits+string.punctuation
    generated_password=''.join(random.choice(characters) for _ in range(password_length))
    generated_password_entry.delete(0,tk.end)
    generated_password_entry.insert(0,generated_password)
def reset_password():
    generated_password_entry.delete(0,tk.END)
def accept_password():
    accepted_password=generated_password_entry.get()
    print("Accepted Password:",accepted_password)

root=tk.Tk()
root.title("password Generator")
root.geometry("300x300")
title_label=tk.Label(root,text="password generator",font=("consolas",16,"bold"),fg="black")
title_label.pack(pady=10)
username_label=tk.Label(root,text="username:")
username_label.pack()
username_entry=tk.Entry(root)
username_entry.pack()
length_label=tk.Label(root,text="password length:")
length_label.pack()
length_entry=tk.Entry(root)
length_entry.pack()
generated_button=tk.Button(root,text="generate password",bg="light blue",command=generate_password)
generated_button.pack()
button_frame=tk.Frame(root)
reset_button=tk.Button(button_frame,text="reset",command=reset_password)
accept_button=tk.Button(button_frame,text="accept",command=accept_password)
reset_button.pack(side=tk.LEFT,padx=10)
accept_button.pack(side=tk.LEFT)
button_frame.pack()
root.mainloop()
