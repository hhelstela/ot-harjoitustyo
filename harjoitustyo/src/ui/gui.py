import tkinter as tk
import calendar
import datetime
from task_service import TaskService
from tkinter import ttk

class GUI:
    def __init__(self, user, password):
        self.root = tk.Tk()
        self.root.title("TaskApp")
        self.root.geometry("400x600")
        self.cont = False

        self.calendar = calendar.Calendar()
        self.today = datetime.datetime.now()
        self.weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        wd = calendar.weekday(self.today.year, self.today.month, self.today.day)
        self.weekdays = self.weekdays[wd:] + self.weekdays[:wd]

        self.user = user
        self.password = password

        self.task_service = TaskService()
        self.task_service.login(self.user, self.password)



        self.task_service.return_user_tasks_by_date(self.today)
        
        #Menubar
        self.menubar = tk.Menu(self.root)
        self.usermenu = tk.Menu(self.menubar, tearoff=0)
        self.usermenu.add_command(label='Change User', command=lambda : self.change_user())
        self.usermenu.add_command(label='Log Out')
        self.menubar.add_cascade(menu=self.usermenu, label=self.user)

        #title
        self.title = tk.Label(self.root, text='Your Tasks', font=('Arial', 20))
        self.title.pack(pady=10)
        #task adding fields, texts and grid
        self.tasklabel = tk.Label(self.root, text="Task Title", font=('Arial', 16))
        self.tasklabel.pack()
        self.tasktitlegrid = tk.Frame(self.root)
        self.tasktitlegrid.columnconfigure(0, weight=1)
        self.tasktitle = tk.Entry(self.tasktitlegrid, font=('Arial', 14))
        self.tasktitle.grid(row=0, column=0, sticky="we")
        self.tasktitlegrid.pack(fill="x")
        self.detaillabel = tk.Label(self.root, text='Details', font=('Arial', 16))
        self.detaillabel.pack()
        self.detailtext = tk.Text(self.root, height=3, font=('Arial', 12))        
        self.detailtext.pack()
        self.dropdown = ttk.Combobox(self.root, values=self.weekdays)
        self.dropdown.pack()
        #add task button
        self.addbutton = tk.Button(self.root, text='Add Task', command=lambda : self.add_task())
        self.addbutton.pack()
        #calendar and task fields
        self.calendarframe = tk.Frame(self.root)
        self.calendarframe.columnconfigure(0, weight=0)
        self.calendarframe.columnconfigure(1, weight=1)
        self.calendarframe.columnconfigure(2, weight=0)
        for i in range(7):
            self.calendarframe.rowconfigure(i, weight=1)
        
        self.tasklist0 = tk.Listbox(self.calendarframe, height=7)
        self.tasklist0.grid(row=0, column=1, sticky='news')
        self.deletebutton0 = tk.Button(self.calendarframe, text='Done', command=lambda : self.delete(self.tasklist0))
        self.deletebutton0.grid(row=0, column=2, sticky='news')

        for item in self.task_service.return_user_tasks_by_date(self.today):
            self.tasklist0.insert(tk.END, item[2])
        
        self.tasklist1 = tk.Listbox(self.calendarframe, height=7)
        self.tasklist1.grid(row=1, column=1, sticky='news')
        self.deletebutton1 = tk.Button(self.calendarframe, text='Done', command=lambda : self.delete(self.tasklist1))
        self.deletebutton1.grid(row=1, column=2, sticky='news')
        for item in self.task_service.return_user_tasks_by_date(self.today + datetime.timedelta(days=1)):
            self.tasklist1.insert(tk.END, item[2])
   
        self.tasklist2 = tk.Listbox(self.calendarframe, height=7)
        self.tasklist2.grid(row=2, column=1, sticky='news')
        self.deletebutton2 = tk.Button(self.calendarframe, text='Done', command=lambda : self.delete(self.tasklist2))
        self.deletebutton2.grid(row=2, column=2, sticky='news')
        for item in self.task_service.return_user_tasks_by_date(self.today + datetime.timedelta(days=2)):
            self.tasklist2.insert(tk.END, item[2])
   
        self.tasklist3 = tk.Listbox(self.calendarframe, height=7)
        self.tasklist3.grid(row=3, column=1, sticky='news')
        self.deletebutton3 = tk.Button(self.calendarframe, text='Done', command=lambda : self.delete(self.tasklist3))
        self.deletebutton3.grid(row=3, column=2, sticky='news')
        for item in self.task_service.return_user_tasks_by_date(self.today + datetime.timedelta(days=3)):
            self.tasklist3.insert(tk.END, item[2])

        self.tasklist4 = tk.Listbox(self.calendarframe, height=7)
        self.tasklist4.grid(row=4, column=1, sticky='news')
        self.deletebutton4 = tk.Button(self.calendarframe, text='Done', command=lambda : self.delete(self.tasklist4))
        self.deletebutton4.grid(row=4, column=2, sticky='news')
        for item in self.task_service.return_user_tasks_by_date(self.today + datetime.timedelta(days=4)):
            self.tasklist4.insert(tk.END, item[2])

        self.tasklist5 = tk.Listbox(self.calendarframe, height=7)
        self.tasklist5.grid(row=5, column=1, sticky='news')
        self.deletebutton5 = tk.Button(self.calendarframe, text='Done', command=lambda : self.delete(self.tasklist5))
        self.deletebutton5.grid(row=5, column=2, sticky='news')
        for item in self.task_service.return_user_tasks_by_date(self.today + datetime.timedelta(days=5)):
            self.tasklist5.insert(tk.END, item[2])

        self.tasklist6 = tk.Listbox(self.calendarframe, height=7)
        self.tasklist6.grid(row=6, column=1, sticky='news')
        self.deletebutton6 = tk.Button(self.calendarframe, text='Done', command=lambda : self.delete(self.tasklist6))
        self.deletebutton6.grid(row=6, column=2, sticky='news')
        for item in self.task_service.return_user_tasks_by_date(self.today + datetime.timedelta(days=6)):
            self.tasklist6.insert(tk.END, item[2])

        
        for i in range(7):
            dayentry = tk.Label(self.calendarframe, text=f"{self.weekdays[i]}")
            dayentry.grid(row=i, column=0, sticky='news')
        
        self.calendarframe.pack(fill=tk.BOTH)




        self.root.config(menu=self.menubar)
        self.root.mainloop()
    def add_task(self):
        tasklists = [self.tasklist0, self.tasklist1, self.tasklist2, self.tasklist3, self.tasklist4, self.tasklist5, self.tasklist6]
        weekday = self.dropdown.get()
        distance = self.weekdays.index(weekday)
        date = self.today + datetime.timedelta(distance)
        title = self.tasktitle.get()
        self.tasktitle.delete(0, tk.END)
        detail = self.detailtext.get('1.0', tk.END)
        self.detailtext.delete('1.0', tk.END)
        tasklists[distance].insert(tk.END, title)
        self.task_service.add_task_to_repository(title, detail, date)
        self.task_service.get_tasks_from_repository()

    def delete(self, tasklist):
        tasklists = [self.tasklist0, self.tasklist1, self.tasklist2, self.tasklist3, self.tasklist4, self.tasklist5, self.tasklist6]
        delta = tasklists.index(tasklist)
        date = self.today + datetime.timedelta(delta)
        title = tasklist.get(tk.ANCHOR)
        for task in self.task_service.retrieved_tasks:
            if task[4] == f"{date.year}-{date.month}-{date.day}" and task[2] == title:
                self.task_service.remove_task_from_db(task[0])
                break
        tasklist.delete(tk.ANCHOR)

    def change_user(self):
        print('hello')
        self.cont = True
        self.root.destroy()
        
