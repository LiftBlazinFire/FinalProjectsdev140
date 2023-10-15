# Keagan Centeno
# 
# Final Project
import tkinter as tk 
window = tk.Tk()
window.title("Welcome to Skyline")
#define a label 
title_label = tk.Label(window, text=("Getting Your Name for your Order"), font=("Arial", 20))
title_label.pack()
#define a function to keep the name 
def get_name():
    name = name_entry.get()  

#define a label 
name_entry= tk.Entry(window)
name_entry.pack()
# Button Creation 
name_button = tk.Button(window, text="Get Name", command=get_name)
name_button.pack()
#window for Combo Selections
window2=tk.Tk()
window2.title("Combo Selections")
#title for window 2 
title_label=tk.Label(window2, text=("Here are your Combo Selections"), font=("Arial", 20))
title_label.pack()
# define selections buttons 
c1 = tk.Checkbutton(window2, text ="Combo 1: 3 way regular with a cheese coney with mustard and onion" )
c1.pack()
c2 = tk.Checkbutton(window2, text= "Combo 2: Chilli cheese Fries with two cheese coney with no mustard and onion")
c2.pack()
c3 = tk.Checkbutton(window2, text= "Combo 3: 4 way with bean and a cheese coney with only onion")
c3.pack()
c4 = tk.Checkbutton(window2, text= "Combo 4: a chili bowl with chili cheese")
c4.pack()
#a function to close window 
def quit():
    window.quit()
    window2.quit()
#button to close the window
close_button=tk.Button(window2, text=("Close"), command=quit)
close_button.pack()

window.mainloop()
window2.mainloop()   
    

    
   
    

