import tkinter as tk
from tkinter import messagebox
from task_service import TaskService


class Login:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TaskApp Login")
        self.root.geometry("400x300")
        self.task_service = TaskService()
        self.username = None
        self.password = None

        self.login_label = tk.Label(
            self.root, text="TaskApp Login", font=('Arial', 20))
        self.login_label.pack(padx=10, pady=10)
        # creating frame
        self.login_frame = tk.Frame(self.root)
        self.login_frame.columnconfigure(0, weight=1)
        for i in range(6):
            self.login_frame.rowconfigure(i, weight=1)

        # creating widgets in frame
        self.password_label = tk.Label(
            self.login_frame, text='Username', font=('Arial', 12))
        self.password_label.grid(row=0, sticky="news")
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=1, sticky="news")
        self.password_label = tk.Label(
            self.login_frame, text='Password', font=('Arial', 12))
        self.password_label.grid(row=2, sticky="news")
        self.password_entry = tk.Entry(self.login_frame)
        self.password_entry.grid(row=3, sticky="news")
        self.login_button = tk.Button(
            self.login_frame, text='Login', command=lambda: self.login())
        self.login_button.grid(row=4)
        self.create_button = tk.Button(
            self.login_frame, text='Create Account', command=lambda: self.create_account())
        self.create_button.grid(row=5)

        self.login_frame.pack()
        self.root.mainloop()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(username)
        if self.task_service.login(username, password):
            self.username = username
            self.password = password
            self.root.destroy()
        else:
            messagebox.showerror('Error', 'Incorrect login credentials')

    def create_account(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.task_service.create_user(username, password):
            messagebox.showinfo('Info', 'Account created succesfully')
        else:
            messagebox.showerror('Error', 'Username is taken')
