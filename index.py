# designing a simple project using tkinter

# Import the tkinter
from tkinter import Tk,Label,Entry,Button
# import a module that pops out a message
from tkinter.messagebox import showerror

# create the window
window = Tk()

# setting properties

# title
window.title("Simple Calculator")
# # favicon
window.iconbitmap("abc.ico")
# the size
window.geometry("350x350+100+100")
# colour
window.config(background="grey")
# making size static
window.resizable(False,False)

# the title label widget
txt_title = Label(text="Calculator",background="grey",font="aria",foreground="White")
txt_title.place(x=130,y=10)

# the first number label widget
txt_first_num= Label(text="First Number: ",background="grey")
txt_first_num.place(x=40,y=50)

# the first number entry widget
first_num_entry = Entry()
first_num_entry.place(x=150,y=50)

# the second number label widget
txt_second_num= Label(text="Second Number: ",background="grey")
txt_second_num.place(x=40,y=100)

# the second number entry widget
second_num_entry = Entry()
second_num_entry.place(x=150,y=100)

# the answer label widget
lb_answer = Label(text="Answer: ",background="grey",font=18)
lb_answer.place(x=80,y=250)

# answer space widget
answer = Label(text="0",background="white",font=18)
answer.place(x=170,y=250)



# functions to oerform operation
def plus():
    first_num = first_num_entry.get()
    second_num = second_num_entry.get()
    if not (first_num.isdigit() and second_num.isdigit() ):
        showerror("Invalid input, enter a number")
        return
    first_num = float(first_num)
    second_num = float(second_num)
    sum = first_num + second_num
    answer.config(text= sum)


def minus():
    first_num = first_num_entry.get()
    second_num = second_num_entry.get()
    if not (first_num.isdigit() and second_num.isdigit() ):
        showerror("Invalid input, enter a number")
        return
    first_num = float(first_num)
    second_num = float(second_num)
    sum = first_num - second_num
    answer.config(text= sum)
   

def times():
    first_num = first_num_entry.get()
    second_num = second_num_entry.get()
    if not (first_num.isdigit() and second_num.isdigit() ):
        showerror("Invalid input, enter a number")
        return
    first_num = float(first_num)
    second_num = float(second_num)
    sum = first_num * second_num
    answer.config(text= sum)

def divide():
    first_num = first_num_entry.get()
    second_num = second_num_entry.get()
    if not (first_num.isdigit() and second_num.isdigit() ):
        showerror("Invalid input, enter a number")
        return
    first_num = float(first_num)
    second_num = float(second_num)
    sum = first_num / second_num
    answer.config(text= sum)

def clear_inputs():
   first_num_entry.delete(0, len(first_num_entry.get()))
   second_num_entry.delete(0, len(second_num_entry.get()))
   answer.config(text= '')

# the buttons
button_add = Button(text="Add",padx=5,pady=5, command=plus, background="orange",foreground="white")
button_add.place(x=50,y=180)
button_subtract = Button(text="Minus",padx=5,pady=5,command=minus, background="orange",foreground="white")
button_subtract.place(x=100,y=180)
button_times = Button(text="times",padx=5,pady=5,command=times,  background="orange",foreground="white")
button_times.place(x=160,y=180)
button = Button(text="Divide",padx=5,pady=5, command=divide,  background="orange",foreground="white")
button.place(x=220,y=180)

# the clear button 
button_clear = Button(text="Clear",padx=5,pady=5, command=clear_inputs, background="red",foreground="white")
button_clear.place(x=150,y= 300)

window.mainloop()