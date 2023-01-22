from tkinter import *
from tkinter import filedialog
import threading
import client2

root = Tk()
# Definiowanie rozmiaru okna aplikacji
root.geometry("610x700")



def myClick2():
    event.set()
    myButton.configure(text="Connect", bg="#2587a7", command=myClick)
    myLabel.configure(text="")
    myLabel2.configure(text="")
    myLabel.grid_forget()
    myLabel2.grid_forget()
    myFillHole.grid_forget()
    myFillHole3.grid_forget()

# Działania po naciśnięciu przycisku
def myClick():
    global x
    event.clear()
    # Wyświetlenie okna do wyboru pliku
    root.filename = filedialog.askopenfilename(title="Select a file", filetypes=(("pem files", "*.pem"),("all files", "*.*")))
    # Zdefiniowanie tekstu do wyświetlenia z wpisanego tekstu
    enteredText = "Entered text: " + myEntryText.get()
    # Zdefiniowanie tekstu do wyświetlenia
    myLabel.configure(text=enteredText)
    # Wyświetlenie odstępu
    myFillHole.grid()
    # Wyświetlenie wpisanego tekstu
    myLabel.grid()
    # Zdefiniowanie tekstu do wyświetlenia z wybranego tekstu
    enteredText2 = "File path: " + root.filename
    # Wyświetlenie odstępu
    myFillHole3.grid()
    # Zdefiniowanie teskstu z nazwą ścieżki wybranego pliku
    myLabel2.configure(text=enteredText2)
    # Wyświetlenie ścieżki wybranego pliku
    myLabel2.grid()
    x = threading.Thread(target=client2.connect_to_server, args=(root.filename, event, myEntryText.get()))
    x.start()
    myButton.configure(text="Disconnect", bg="#FF0000", command=myClick2)

event = threading.Event()
# Definiowanie komponentów
myLabel1 = Label(root, text="BEST VPN EVER !!!", width=38, bg="#2587a7", height=2, fg="white", font=("Arial", 20))
myEntryText = Entry(root, width=30, font=("Arial", 15))
myButton = Button(root, text="Connect", padx=35, pady=20, bg="#2587a7", fg="white", font=("Arial", 15), command=myClick)
myFillHole = Label(root, text="                 ", width=26, height=1)
myFillHole1 = Label(root, text="                 ", width=26, height=2)
myFillHole2 = Label(root, text="                 ", width=26, height=2)
myFillHole3 = Label(root, text="                 ", width=26, height=1)
myLabel = Label(root, text="", padx=30, height=2, bg="#57badb", fg="white", font=("Arial", 15),)
myLabel2 = Label(root, text="", padx=30, height=2, bg="#57badb", fg="white", font=("Arial", 15),)

# Wypisanie zdefiniowanych komponentów
myLabel1.grid(row=0, column=0)
myFillHole1.grid(row=1, column=0)
myEntryText.grid(row=2, column=0)
myFillHole2.grid(row=3, column=0)
myButton.grid(row=4, column=0)


root.mainloop()