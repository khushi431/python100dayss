from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "new text"
my_label.config(text="new text") 


# button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    # my_label.config(text="Button Got Clicked")
    my_label.config(text=new_text)


button = Button(text="click me", command=button_clicked)
button.pack()

#entry

input = Entry(width=20)
input.pack()
print(input.get())

window.mainloop()

# import turtle
#
# tim = turtle.Turtle
# tim.write("Some text", font=("Times new roman", 80, "bold"))

