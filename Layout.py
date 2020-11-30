import tkinter
from tkinter import *
import json

def load_json(file_name):
    """Deze functie zorgt ervoor dat het json bestand wordt geladen in Python."""
    steam_json_file = open(file_name, 'r')
    steam_json_data = steam_json_file.read()
    steam_json_load = json.loads(steam_json_data)
    return steam_json_load

steam_json = load_json('json/steam_JSON_file.json')

class MyApp:
    def __init__(self, parent):

        self.myParent = parent
        self.myParent.geometry("1280x720")

        self.myContainer1 = Frame(parent)  ###
        self.myContainer1.pack(expand=YES, fill=BOTH)

        """ Dit is ons demo frame. """
        self.demo_frame = Frame(self.myContainer1)  ###
        self.demo_frame.pack(side=RIGHT, expand=YES, fill=BOTH)

        """ Dit is ons top frame. """
        self.top_frame = Frame(self.demo_frame)
        self.top_frame.config(bg='#d8e2e9')
        self.top_frame.pack(side=TOP, expand=YES, fill=BOTH)  ###

        """ Linker kant menu. """
        self.header_frame = Frame(self.top_frame,
                                  borderwidth=0, relief=RIDGE,
                                  bg='#c7d5e0'
                                  )
        self.header_frame.pack(side=LEFT, fill=BOTH, expand=NO)

        """ Pagina afbeelding. """
        self.image = PhotoImage(file="images/steam_inverse_mid.png")
        label = Label(self.header_frame, image=self.image, bg='#c7d5e0', width=400)
        label.pack(fill=X)

        """ Dit zijn onze pagina's in het menu aan de linker kant. """
        self.headTitle = Label(self.header_frame, text="Home")
        self.headTitle.config(font=("Sans-serif", 30), bg='#c7d5e0')
        self.headTitle.pack(anchor=CENTER, padx=40, pady=20)

        self.Page1 = Label(self.header_frame, text="Pagina 1")
        self.Page1.config(font=("Sans-serif", 30), bg='#c7d5e0')
        self.Page1.pack(anchor=CENTER, padx=40, pady=20)

        self.Page2 = Label(self.header_frame, text="Pagina 2")
        self.Page2.config(font=("Sans-serif", 30), bg='#c7d5e0')
        self.Page2.pack(anchor=CENTER, padx=40, pady=20)

        self.Page3 = Label(self.header_frame, text="Pagina 3")
        self.Page3.config(font=("Sans-serif", 30), bg='#c7d5e0')
        self.Page3.pack(anchor=CENTER, padx=40, pady=20)

        self.Page4 = Label(self.header_frame, text="Pagina 4")
        self.Page4.config(font=("Sans-serif", 30), bg='#c7d5e0')
        self.Page4.pack(anchor=CENTER, padx=40, pady=20)


        """ Title en content veld voor de GUI. """
        self.Title = Label(self.top_frame, text="API")
        self.Title.config(font=("Sans-serif", 50), bg='#d8e2e9')
        self.Title.pack(anchor=NW, padx=40, pady=20)

        self.apiVeld = Label(self.top_frame, text="Eerste Game: " + steam_json[0]["name"], width=50, height=50)
        self.apiVeld.config(font=("Sans-serif", 40), bg='#b3c0ca')
        self.apiVeld.pack(anchor=NW, padx=40, pady=30)


root = Tk()
myapp = MyApp(root)
root.mainloop()