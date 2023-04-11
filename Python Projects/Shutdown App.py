"""
This programe gives you an GUI interface for Restating, Restarting with Time,
Logout and Shuting Down this system.

I uses Tkinter Module for its look and feel i.e GUI

It uses the Button function of the tkinter module.
"""

from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def logout():
    os.system("shutdown -1")

def shutdown():
    os.system("shutdown /s /t 1")

st = Tk()    # Tkinter Object creation. which is st here.
st.title("Shutdown App")    # Title of the pop up Window.
st.geometry("500x500")    # Height and Width Of the pop up window.
st.config(bg="Green")    # Background colour of the pop up window

r_button = Button(st,text="Restart", font=("Time New Roman",20,"bold"),   
                   relief=RAISED, cursor="Plus", command= restart)
                     # Functions for Restart button.
r_button.place(x=150, y=60, height=50, width=200)   
 # Co-ordinates of the Restart button.

rt_button = Button(st,text="Restart Time", font=("Time New Roman",20,"bold"),      
                    relief=RAISED, cursor="Plus", command= restart_time)
                     # Functions for Restart-Time button.
rt_button.place(x=150, y=170, height=50, width=200)   
 # Co-ordinates of the Restart-Time button.

lg_button = Button(st,text="Log-Out", font=("Time New Roman",20,"bold"),    
                    relief=RAISED, cursor="Plus", command= logout)
                    # Functions for Logout button.
lg_button.place(x=150, y=270, height=50, width=200)   
 # Co-ordinates of the Logout button.

st_button = Button(st,text="ShutDown", font=("Time New Roman",20,"bold"),   
                    relief=RAISED, cursor="Plus", command= shutdown)
                     # Functions for ShutDown button.
st_button.place(x=150, y=370, height=50, width=200)    
# Co-ordinates of the ShutDown button.

st.mainloop()