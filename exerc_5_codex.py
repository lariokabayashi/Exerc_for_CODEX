from tkinter import *
from tkinter import ttk
import requests

link = "http://worldclockapi.com/api/json/utc/now"
f = requests.get(link)

# Filtering the information in the link
text = f.text.split(",")

# Separating the data
dataTime = text[1].split('T')
data = dataTime[1].split(":")[1]

#Separating the time
Time = list(dataTime[-1])
Time[1] = str(int(Time[1])-3)
Time = "".join(Time)

# Creating a widget personalized with the data and time of the day
root = Tk()
root.geometry('500x500')
img = PhotoImage(file ="codex_lembrete.png")
label = ttk.Label(root, image = img, compound = 'center', 
text = f'\n\n                    {Time[:5]} ▿ {data[1:]}',
font = ('Arial', 12))
label.pack()
root.mainloop()
