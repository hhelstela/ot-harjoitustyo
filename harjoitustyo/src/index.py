from gui import GUI
from login import Login

#run to start the application


#need to add functionality to add tasks to other dates than the first
#need to add the functionality to change tasks to done from the UI
#need to make the code more readable, and add better comments
#...
login_screen = Login()
username = login_screen.username
password = login_screen.password
main = GUI(username, password)