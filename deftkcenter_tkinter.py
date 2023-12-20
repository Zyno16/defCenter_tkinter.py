
def tkcenter (form):
    form.update()
    fw = form.winfo_width()
    fh =form.winfo_height()
    sw =form.winfo_screenwidth()
    sh =form.winfo_screenheight()
    x =(sw-fw) / 2
    y =(sh - fh) / 2 

    form.geometry("%dx%d+%d+%d" %(fw,fh,x,y))



from tkinter import *
import tools

form =Tk()
form.geometry("600x400")
tools.tkcenter(form)
form.mainloop()

