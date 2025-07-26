from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help :
    def __init__(self,root):
        self.root= root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help Desk")
        
        
        title_label=Label(self.root,text="HELP DESK",font=("times new roman",30,"bold"),bg="black",fg="blue")
        title_label.place(x=0,y=0,width=1300,height=35)
        
        #image1
        img_top=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig27.jpg")
        img_top=img_top.resize((1500,650),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
    
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=35,width=1300,height=650)
        
        developer_label=Label(f_lbl,text="prajwalsrinivas04@gmail.com",font=("times new roman",20,"bold"),bg="white")
        developer_label.place(x=500,y=100)
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()