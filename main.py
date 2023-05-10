import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x700")
root.title("Python Apps")

def login():
    print("Login")
    
def signup():
    print("Sign Up")
    
def slider_callback(value):
    progress.set(value)
    

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

button_signup = customtkinter.CTkButton(master=frame, text="Sign Up", command=signup)
button_signup.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

progress = customtkinter.CTkProgressBar(master=frame)
progress.pack(pady=12, padx=10)

slider = customtkinter.CTkSlider(master=frame, command=slider_callback, from_=0, to=1)
slider.pack(pady=12, padx=10)

radiobutton = tkinter.IntVar(value=1)

radio1 = customtkinter.CTkRadioButton(master=frame, variable=radiobutton, value=1, text="Pilihan Pertama")
radio1.pack(pady=12, padx=10)

radio2 = customtkinter.CTkRadioButton(master=frame, variable=radiobutton, value=2, text="Pilihan Kedua")
radio2.pack(pady=12, padx=10)

switch = customtkinter.CTkSwitch(master=frame, text="Switch")
switch.pack(pady=12, padx=10)

optionmenu = customtkinter.CTkOptionMenu(master=frame, values=["Option 1", "Option 2", "etc."])
optionmenu.pack(pady=12, padx=10)

combo = customtkinter.CTkComboBox(master=frame, values=["Option 1", "Option 2", "etc."])
combo.pack(pady=12, padx=10)

root.mainloop()