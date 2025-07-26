from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer :
    def __init__(self,root):
        self.root= root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer System")
        
        
        title_label=Label(self.root,text="DEVELOPER",font=("times new roman",30,"bold"),bg="black",fg="blue")
        title_label.place(x=0,y=0,width=1300,height=35)
        
        #image1
        img_top=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig20.jpg")
        img_top=img_top.resize((1500,650),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
    
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=35,width=1300,height=650)
        
        
        #======================Frame============================
        main_frame=Frame(f_lbl,bd=2)
        main_frame.place(x=400,y=0,width=500,height=600)
        
       
        
        developer_label=Label(main_frame,text="Hello My Name is Prajwal student at East West Institute of Technology. Over the past few years, I've developed a strong foundation in programming, particularly in Python, SQL, and web development. I've also worked on practical projects like a Smart Fire Extinguisher and facial recognition using OpenCV, which improved my hands-on and problem-solving skills.",wraplength=500,font=("times new roman",20,"bold"),bg="white")
        developer_label.place(x=0,y=100)
        
       
        
       
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()