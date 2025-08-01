from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train :
    def __init__(self,root):
        self.root= root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Detection System")
        
       
         
        title_label=Label(self.root,text="TRAIN DATASET",font=("times new roman",30,"bold"),bg="black",fg="red")
        title_label.place(x=0,y=0,width=1300,height=35)
        
        #image1
        img_top=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig20.jpg")
        img_top=img_top.resize((1500,300),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
    
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=35,width=1300,height=300)
        
        #Button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",20,"bold"),bg="black",fg="yellow")
        b1_1.place(x=0,y=300,width=1300,height=50)
        
        
        #Image 2
        img_bottom=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig21.jpg")
        img_bottom=img_bottom.resize((1500,300),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
    
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=350,width=1500,height=300)
        
        
    #==============================Function==============================
    def train_classifier(self):
        data_dir=("data")
        path=[os.path .join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]
        
        for image in path :
            img=Image.open(image).convert('L') #Gray Scanle Image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
       
        
        #============================Train the classifier And save====================================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!!!")
       
       
            
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()