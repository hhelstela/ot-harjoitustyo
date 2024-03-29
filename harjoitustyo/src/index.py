import tkinter as tk
import calendar
import datetime

now = datetime.datetime.now()
cal = calendar.Calendar()

def main():
    window = tk.Tk()
    window.title('TaskApp')
    window.geometry("500x500")

    label = tk.Label(window, text='TaskApp', font=('Arial', 20))
    label.pack()

    textbox = tk.Text(window, height=5, width=30, font=('Arial', 12))
    textbox.pack()

    button = tk.Button(window, height=2, width=20, text='Add Task')
    button.pack()

    frame = tk.Frame(window)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=5)
    i = 0
    for date in cal.itermonthdays(now.year, now.month):
        if date == 0:
            continue
        daydate = tk.Label(frame, text=date)
        daydate.grid(row=i, column=0, sticky=tk.W+tk.E)
        i += 1
    
    
    frame.pack(fill="x")

    window.mainloop()


main()