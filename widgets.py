from tkinter import *
root=Tk()
root.title("GETTING STARTED WITH WIDGETS")
root.geometry("400x300")
root.configure(bg="skyblue")
demo=Label(text="getting started with widgets",fg="black",bg="white",height=1,width=300)
name=Label(text="ENTER FIRST NUMBER",bg="lavender")
second=Label(text="ENTER SECOND NUMBER",bg="lavender")
name_entry=Entry()
second_entry=Entry()
text_box=Text(height=3)
def display():
    name1=name_entry.get()
    name2=second_entry.get()
    Message=int(name1)*int(name2)
    

    text_box.insert(END,str(Message))
BTN=Button(text="Begin",command=display,height=1, bg="black",fg="white")
demo.pack()
name.pack()
name_entry.pack()
second.pack()
second_entry.pack()
BTN.pack()
text_box.pack()
root.mainloop()
    
    
    
    
    