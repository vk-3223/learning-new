from tkinter import *
import pandas
import random

background_color = "#B1DDC6"

def flip_card():
    with open("french_words.csv","r") as data:
        data_farme = pandas.read_csv(data)
        to_leran = data_farme.to_dict(orient="record")
        current_card = random.choice(to_leran)
    canvas.itemconfig(creat_title,text="English",fill="white")
    canvas.itemconfig(creat_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_image)
    
def file_reader():
    global flip_timmer
    window.after_cancel(flip_timmer)
    with open("french_words.csv","r") as data:
        data_farme = pandas.read_csv(data)
        to_leran = data_farme.to_dict(orient="record")
        current_card = random.choice(to_leran)
        #print(current_card["French"])
        canvas.itemconfig(creat_title,text="french",fill="black")
        canvas.itemconfig(creat_word,text=current_card["French"],fill="black")
        canvas.itemconfig(card_background,image=card_fornt_image)
        #canvas.itemconfig(creat_title,text="french") 
        flip_timmer = window.after(3000,func=flip_card)

def is_know():
    
    with open("french_words.csv","r") as data:
        data_farme = pandas.read_csv(data)
        to_leran = data_farme.to_dict(orient="record")
        current_card = random.choice(to_leran)
        to_leran.remove(current_card)
        print(len(to_leran))
        data_farme2 = pandas.DataFrame(to_leran)
        data_farme2.to_csv("word_to_learn.csv")
        file_reader()

window = Tk()
window.title("flashy")
window.config(padx=50,pady=50,bg=background_color)
canvas = Canvas(width=800,bg=background_color,height=526,highlightthickness=0)
canvas.grid()
flip_timmer = window.after(3000,func=flip_card)
card_fornt_image = PhotoImage(file="card_front.png")
card_back_image = PhotoImage(file="card_back.png")
canvas.create_image(400,263,image=card_back_image)
card_background = canvas.create_image(400,263,image=card_fornt_image)
canvas.grid(column=2,row=2)
creat_title = canvas.create_text(400,150,text="title",font=("Ariel",40,"bold"))
canvas.grid()
creat_word = canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))


right_image = PhotoImage(file="right.png")
right_button = Button(image=right_image,highlightthickness=0,command=file_reader)
right_button.grid(row=3,column=3)  

cancel_image = PhotoImage(file="wrong.png")
cancel_button = Button(image=cancel_image,command=file_reader)
cancel_button.grid(row=3,column=0)






window.mainloop()