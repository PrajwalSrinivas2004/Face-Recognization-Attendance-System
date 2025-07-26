from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from student_details import Student
import os
from train import Train
from face_recognization import Face_Recognization
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime

class Face_Recognition_System :
    def __init__(self,root):
        self.root= root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Detection System")

        #image1
        img1=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig1.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
    
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=433,height=130)
        
        #image2
        img2=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig2.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
    
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=400,height=130)

        #image3
        img3=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig3.jpeg")
        img3=img3.resize((500,130),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
    
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=300,height=130)
        
        #Background Image
        img4=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig2.jpg")
        img4=img4.resize((1530,710),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
    
        
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1500,height=600)
        
        
        title_label=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWARE",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_label.place(x=0,y=0,width=1300,height=45)
        
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        
        lbl=LabelFrame(title_label,font=('times new roman',14,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()
        
         
        #Student Details
        img6=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig9.jpg")
        img6=img6.resize((200,150),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg6,command=self.Student_details,cursor="hand2")
        b1.place(x=100,y=100,width=200,height=150)
        
        b1_1=Button(bg_img,text="Student Details",command=self.Student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=250,width=200,height=30)
        
       
        # Detect Face Button
        img7=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig10.jpeg")
        img7=img7.resize((200,150),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=100,width=200,height=150)
        
        b1_1=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=250,width=200,height=30) 
        
        
        # Detect Face Attendence
        img8=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig11.jpg")
        img8=img8.resize((200,150),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.attendance_data)
        b1.place(x=700,y=100,width=200,height=150)
        
        b1_1=Button(bg_img,text="Attendence",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=700,y=250,width=200,height=30) 
        
        
        # Help Desk
        img9=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig12.jpg")
        img9=img9.resize((200,150),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.help_data)
        b1.place(x=1000,y=100,width=200,height=150)
        
        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white",command=self.help_data)
        b1_1.place(x=1000,y=250,width=200,height=30) 
        
        
         # Train Face Button
        img10=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig13.jpeg")
        img10=img10.resize((200,150),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.Train_data)
        b1.place(x=100,y=300,width=200,height=150)
        
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.Train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=100,y=450,width=200,height=30) 
        
        
         # Train Face Button
        img11=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig14.jpeg")
        img11=img11.resize((200,150),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=300,width=200,height=150)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=400,y=450,width=200,height=30) 
        
        
         # Train Face Button
        img12=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig15.jpg")
        img12=img12.resize((200,150),Image.LANCZOS)
        self.photoimg12=ImageTk.PhotoImage(img12)
        
        b1=Button(bg_img,image=self.photoimg12,cursor="hand2",command=self.developer_data)
        b1.place(x=700,y=300,width=200,height=150)
        
        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white",command=self.developer_data)
        b1_1.place(x=700,y=450,width=200,height=30) 
        
         #Exit Button
        img13=Image.open(r"projectImages\ig16.webp")
        img13=img13.resize((200,150),Image.LANCZOS)
        self.photoimg13=ImageTk.PhotoImage(img13)
        
        b1=Button(bg_img,image=self.photoimg13,cursor="hand2",command=self.i_exit)
        b1.place(x=1000,y=300,width=200,height=150)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white",command=self.i_exit)
        b1_1.place(x=1000,y=450,width=200,height=30) 
        
    def open_img(self):
        os.startfile("data")
        
    def i_exit(self):
        self.i_exit=tkinter.messagebox.askyesno("Face Recognization","Are you sure you want to exit this project",parent=self.root)
        if self.i_exit>0:
            self.root.destroy()
        else:
            return
        
        
        #=====================Function Button=======================
    def Student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def Train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
            
            
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognization(self.new_window)
        
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
        
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
        
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        
       
        
        
        
        
        
       
        
    
    
    
    
    
    
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()