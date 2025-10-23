import tkinter as tk
import requests
import random


root = tk.Tk();  root.geometry("800x600"); root.configure(bg="teal") #SETS UP WINDOW
msg = tk.StringVar(value="WeatherBot") #VARIABLE TO HOLD TEXT
tk.Label(root, textvariable=msg, font=("TkDefaultFont",16), fg="Orange", bg="teal").pack(pady=10) #DISPLAYS TEXT

# ...existing code...
# Live Weather data (moved before mainloop)
user_agent = "jaysonc678@gmail.com"
BASE_URL = "https://api.weather.gov"
station_and_coords = ["EPZ", 124, 104]
headers = {'User-Agent': user_agent}
endpoint = f"{BASE_URL}/gridpoints/{station_and_coords[0]}/{station_and_coords[1]},{station_and_coords[2]}/forecast"

try:
    response = requests.get(endpoint, headers=headers, timeout=5)
    response.raise_for_status()
    data = response.json()["properties"]["periods"][0]
    weather = data["shortForecast"].lower()
    msg.set(f"It is {weather} outside")   # update the UI text
except Exception:
    msg.set("Weather unavailable")



#DEFINES SETTINGS WINDOW
 
def open_settings():
    w = tk.Toplevel(root); w.title("Settings"); w.resizable(False, False)
    def add_slider(name, val=70):
        tk.Label(w, text=name).pack(anchor="w", padx=10)
        # SLIDER
        s = tk.Scale(w, from_=0, to=100, orient="horizontal"); s.set(val); s.pack(padx=10, pady=2, fill="x")
        return s
    # SLIDERS
    master = add_slider("Master")
    music  = add_slider("Music")
    sfx    = add_slider("SFX")
 
# DEFINES SEARCH BAR
def show_searchbar():
    start_btn.destroy()  # or: start_btn.pack_forget()
    topbar = tk.Frame(root, bg="teal"); topbar.pack(side="top", fill="x")
    q = tk.StringVar()
    tk.Entry(topbar, textvariable=q, font=("TkDefaultFont",12)).pack(side="left", padx=8, pady=8, fill="x", expand=True)
    tk.Button(topbar, text="Search", bg="#333", fg="white", bd=0,
              command=lambda: msg.set(f"Searching: {q.get()}")).pack(side="left", padx=6)
    #Once Search is pressed below will show weather info 
    





start_btn = tk.Button(root, text="Start", command=show_searchbar, bg="#333", fg="white", bd=0); start_btn.pack(),
 
 
# CREATES SETTINGS MENU
menu = tk.Menu(root, tearoff=0, bg="red", fg="black")
 
 
# CALLS SETTINGS WINDOW
menu.add_command(label="Settings", command=open_settings)
 
 
# ADDS EXIT OPTION
menu.add_separator(); menu.add_command(label="Exit", command=root.destroy)
 
 
# SETTINGS BUTTON
img = tk.PhotoImage(file="gear.png").subsample(3, 3)
btn = tk.Button(root, image=img, bd=0, relief="flat", highlightthickness=0,
                bg="teal", activebackground="teal",
                command=lambda: menu.tk_popup(root.winfo_pointerx(), root.winfo_pointery()))  #open menu
btn.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor="se")
 
 
def todo_list_button():
    todo_button = tk.Button(root,text='To do list',command=todo_list_window, bg="#333", fg="white", bd=1).pack()
    print(todo_button)
    
def todo_list_window():
    todo_window = tk.Toplevel()
    todo_window.title("TO DO List")
    todo_window.geometry("400x500")   
    
    
    



todo_list_button() 




root.mainloop() #RUNS PROGRAM
 


 


user_agent = "jaysonc678@gmail.com"

BASE_URL = "https://api.weather.gov"

station_and_coords = ["EPZ",124,104]


#needed to access api
headers = {'User-Agent' : f'{user_agent}'}
#link to data
endpoint = f"{BASE_URL}/gridpoints/{station_and_coords[0]}/{station_and_coords[1]},{station_and_coords[2]}/forecast"

#get info from api then get specifically the first period
response = requests.get(endpoint, headers = headers)
data = response.json()["properties"]["periods"][0]

#save the forecast in lowercase
weather = data["shortForecast"].lower()

#raise error if api failed
if response:
    print("API accessed successfully.")
else:
    raise Exception(f"Non-success status code: {response.status_code}")

print(f"It is {weather} outside")


 