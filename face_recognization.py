from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

class Face_Recognization :
    def __init__(self,root):
        self.root= root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")
        
        title_label=Label(self.root,text="FACE RECOGNIZATION",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_label.place(x=0,y=0,width=1300,height=35)
        
        #image1
        img_top=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig25.jpg")
        img_top=img_top.resize((650,620),Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)
    
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=35,width=650,height=620)
        
        #image2
        img_left=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig22.webp")
        img_left=img_left.resize((650,620),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
    
        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=650,y=35,width=650,height=620)
        
        #Button
        b1_1=Button(f_lbl,text="Face Recognization",cursor="hand2",command=self.face_recog,font=("times new roman",15,"bold"),bg="white",fg="black")
        b1_1.place(x=222,y=550,width=200,height=40)
        
    #===========================attendance System======================================
    def mark_attendance(self,i,r,n,d):
        with open("attendanceSheet.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not  in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                
        
        
        
    #=========================face Recognization===========================
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)
                
            coord=[]
                
            for(x,y,w,h) in features:
                cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                    
                conn=mysql.connector.connect(host="127.0.0.1",username="root",password="1234567@eight",database="face_recognizer")
                my_cursor=conn.cursor()
                    
                my_cursor.execute("SELECT Name FROM student WHERE Student_id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n) 

                    
                my_cursor.execute("SELECT Roll FROM student WHERE Student_id="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r) 

                my_cursor.execute("SELECT Dep FROM student WHERE Student_id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)
                
                my_cursor.execute("SELECT Student_id FROM student WHERE Student_id="+str(id))
                i= my_cursor.fetchone()
                i= "+".join(i) 

                    
                    
                if confidence>60:
                    cv2.putText(img,f"ID:{r}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                
                else:
                    cv2.rectangle(img(x,y),(x+w,w+h),(0,0,255),3)
                    cv2.putText(img,f"Unknown Face:{r}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        
                coord=[x,y,w,h]
                    
                    
            return coord
            
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
            
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
            
        video_cap=cv2.VideoCapture(0)
            
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognization Camera",img)
                
            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()                    
            
        
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognization(root)
    root.mainloop()