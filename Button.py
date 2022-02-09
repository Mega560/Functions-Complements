from tkinter import*

v=Tk()
v.geometry("500x500")
v.title("Prueba_Boton")

input_text=StringVar()
n=0
def pul(num):
    global n
    n+=1
    if n==10:
        n=1
    c =str(n)
    input_text.set(c)
     


b1=Button(v,width=30,height=10,relief="flat",textvariable=input_text,background="white",command=lambda:pul(3))
b1.place(x=40,y=30)


mainloop()
