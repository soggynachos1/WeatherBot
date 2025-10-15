import tkinter as tk
root = tk.Tk();  root.geometry("1920x1080"); root.configure(bg="teal") #SETS UP WINDOW
msg = tk.StringVar(value="WeatherBot") #VARIABLE TO HOLD TEXT
tk.Label(root, textvariable=msg, font=("TkDefaultFont",16), fg="Orange", bg="teal").pack(pady=10) #DISPLAYS TEXT
 
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
 
 
root.mainloop() #RUNS PROGRAM
 
 