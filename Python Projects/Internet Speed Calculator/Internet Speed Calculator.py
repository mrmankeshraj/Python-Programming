from tkinter import *
import speedtest

def speed_check():    # Creates a new function 
	sp = speedtest.Speedtest()
	# Creating a object "sp" of the function "speedtest" from module "Speedtest".
	sp.get_servers()
	# Connecting it with the servers.
	down = str(round(sp.download() / (10**6), 3)) + "Mbps"
	# Creating object of download fuction.
	up = str(round(sp.upload() / (10**6), 3)) + "Mbps"
	# Creating object of upload fuction.
	lab_down.config(text=down)
	# Configuring lab_down Label. 
	lab_up.config(text=up)
	# Configuring lab_up Label. 


sp = Tk()
# Creating an object of Tkinter module functions. 
sp.title("Internet Speed Calculator")
# Creates Title of the pop-up window.
sp.geometry("500x650")
# Difines the sixe of the pop-up window.
sp.config(bg="Green")
# Sets the background colour.

lab = Label(sp, text="Internet Speed Test", font=("Time New Roman", 30, "bold"), bg="yellow")
# Creates new Label called "Internet Speed Test" with specific fonts and background colour.
lab.place(x=60, y=40, height=50, width=380)
# Places the Label at specific position. 

lab = Label(sp, text="Download Speed", font=("Time New Roman", 30, "bold"), bg="yellow")
# Creates new Label called "Download Speed" with specific fonts and background colour.
lab.place(x=60, y=130, height=50, width=380)
# Places the Label at specific position. 

lab_down = Label(sp, text="00", font=("Time New Roman", 30, "bold"), bg="yellow")
# Creates new Label called "00" with specific fonts and background colour.
lab_down.place(x=60, y=200, height=50, width=380)
# Places the Label at specific position. 

lab = Label(sp, text="Upload Speed", font=("Time New Roman", 30, "bold"), bg="yellow")
# Creates new Label called "Upload Speed" with specific fonts and background colour.
lab.place(x=60, y=290, height=50, width=380)
# Places the Label at specific position. 

lab_up = Label(sp, text="00", font=("Time New Roman", 30, "bold"), bg="yellow")
# Creates new Label called "00" with specific fonts and background colour.
lab_up.place(x=60, y=360, height=50, width=380)
# Places the Label at specific position. 

button = Button(sp, text="CHECK SPEED",font=("Time New Roman", 30, "bold"), relief=RAISED, bg="red", command=speed_check)
# Creates new Label called "CHECK SPEED" with specific fonts and background colour.
button.place(x=60, y=460, height=50, width=380)
# Places the Label at specific position. 

sp.mainloop()
# Creates a new Pop-up Window.