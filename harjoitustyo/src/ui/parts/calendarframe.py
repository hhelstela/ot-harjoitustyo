import tkinter as tk
import datetime
class CalendarFrame():
        def __init__(self, root):
            self.calendarframe = tk.Frame(root)
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