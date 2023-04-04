import os
import sqlite3
import pygame
import datetime
import calendar

os.remove("events.db")

db = sqlite3.connect("events.db")
db.isolation_level = None

try:
    db.execute("CREATE TABLE Events (id INTEGER PRIMARY KEY, day INTEGER, month INTEGER, event TEXT)")
except:
    pass

def add_event(day, month, event):
    db.execute("INSERT INTO Events (day, month, event) VALUES (?, ?, ?)", [day, month, event])

def ui():
    pygame.init()
    clock = pygame.time.Clock()
    width = 1280
    height = 960
    screen = pygame.display.set_mode((width, height))
    day_height = 50
    height -= day_height
    gray = (255,255,255)
    white = (0,0,0)
    posx = 0
    posy = 0
    fontsize = width//50
    font = pygame.font.SysFont(None, fontsize)

    today = datetime.datetime.now()
    y = today.year
    m = today.month
    weekday = datetime.datetime.weekday(today)
    daynames = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    cal = calendar.Calendar()
    wds = cal.itermonthdates(y, m)
    weekdays = []
    for date in wds:
        weekdays.append(date)
    screen.fill(gray)
    d = 0
    for i in range(5):
        for j in range(7):
            date = font.render(str(weekdays[d].day), True, (0,0,0))
            dayname = font.render(daynames[j], True, (0,0,0))
            d += 1
            pygame.draw.rect(screen, white, (posx, posy+day_height, width//7, height//5), 1)
            screen.blit(date, (posx+10, posy+10+day_height))
            screen.blit(dayname, (posx, 10))
            posx += width//7
        posx = 0
        posy += height//5
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            ### LISÄÄ EVENT HANDLER JOLLA LISÄTÄÄN TEKSTIÄ KALENTERIMERKINTÄÄN
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
            pygame.display.update()
        clock.tick(600)


def main():
    ui()
    while True:
        cont = input("Continue(y/n): ")
        if cont == "n":
            break    
        day = int(input("Day: "))
        month = int(input("Month: "))
        event = input("Event: ")
        add_event(day, month, event)

def all_events():
    print(db.execute("SELECT * FROM Events").fetchall())



#ui()
#main()
#all_events()