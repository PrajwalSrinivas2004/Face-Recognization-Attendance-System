from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

myData=[]

class Attendance :
    def __init__(self,root):
        self.root= root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Attendance System")
        
        
        #===============================variables======================
        self.var_attend_id=StringVar()
        self.var_attend_roll=StringVar()
        self.var_attend_name=StringVar()
        self.var_attend_dep=StringVar()
        self.var_attend_time=StringVar()
        self.var_attend_date=StringVar()
        self.var_attend_attendance=StringVar()
        
         #image1
        img1=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig25.webp")
        img1=img1.resize((650,200),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
    
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=650,height=200)
        
        #image2
        img2=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig24.png")
        img2=img2.resize((650,200),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
    
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=650,y=0,width=650,height=200)
        
        
        #Background image
        img4=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig2.jpg")
        img4=img4.resize((1530,600),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
    
        
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=200,width=1500,height=600)
        
        title_label=Label(bg_img,text="ATTENDENCE MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="green")
        title_label.place(x=0,y=0,width=1350,height=35)
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=2,y=40,width=1260,height=600)
        
        
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=0,width=710,height=390)
        
         #image3
        img_left=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig3.jpeg")
        img_left=img_left.resize((700,130),Image.LANCZOS)
        self.photoimg_l=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_l)
        f_lbl.place(x=5,y=0,width=650,height=80)
        
        left_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_frame.place(x=1,y=90,width=660,height=250)
        
        #AttendanceID
        attendance_label=Label(left_frame,text="AttendanceID:",font=("times new roman",13,"bold"),bg="white")
        attendance_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        attendanceID_entry=Entry(left_frame,width=18,font=("times new roman",13,"bold"),textvariable=self.var_attend_id,bg="white")
        attendanceID_entry.grid(row=0,column=1,padx=5,pady=0,sticky=W)
        
        #Roll
        roll_label=Label(left_frame,text="Roll:",font=("times new roman",13,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        rollID_entry=Entry(left_frame,width=18,font=("times new roman",13,"bold"),textvariable=self.var_attend_roll,bg="white")
        rollID_entry.grid(row=0,column=3,padx=5,pady=0,sticky=W)
        
        #Name
        name_label=Label(left_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        nameID_entry=Entry(left_frame,width=18,font=("times new roman",13,"bold"),textvariable=self.var_attend_name,bg="white")
        nameID_entry.grid(row=1,column=1,padx=5,pady=0,sticky=W)
        
        #Department
        department_label=Label(left_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        departmentID_entry=Entry(left_frame,width=18,font=("times new roman",13,"bold"),textvariable=self.var_attend_dep,bg="white")
        departmentID_entry.grid(row=1,column=3,padx=5,pady=0,sticky=W)
        
        #Time
        time_label=Label(left_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        timeID_entry=Entry(left_frame,width=18,font=("times new roman",13,"bold"),textvariable=self.var_attend_time,bg="white")
        timeID_entry.grid(row=2,column=1,padx=5,pady=0,sticky=W)
        
        #Date
        date_label=Label(left_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        dateID_entry=Entry(left_frame,width=18,font=("times new roman",13,"bold"),textvariable=self.var_attend_date,bg="white")
        dateID_entry.grid(row=2,column=3,padx=5,pady=0,sticky=W)

        #Attendance Status
        attendanceStatus_label=Label(left_frame,text="Attendance Status:",font=("times new roman",13,"bold"),bg="white")
        attendanceStatus_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
    
        
        attendanceStatus_combo=ttk.Combobox(left_frame,font=("times new roman",13,"bold"),textvariable=self.var_attend_attendance,width=18,state="read only")
        attendanceStatus_combo["values"]=("Status","Present","Absent")
        attendanceStatus_combo.current(0)
        attendanceStatus_combo.grid(row=3,column=1,padx=5,pady=0,sticky=W)
        
         #Button Frame
        btn_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=715,height=35)
        
        save_btn=Button(btn_frame,text="ImportCSV",command=self.import_Csv,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="ExportCSV",command=self.exportcsv,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Update",width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        
        
         #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=675,y=0,width=580,height=390)
        
        right_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        right_frame.place(x=5,y=5,width=560,height=350)
        
        #======================scroll bar=========================
        scroll_x=ttk.Scrollbar(right_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(right_frame,orient=VERTICAL)
        
        self.AttendaceReportTable=ttk.Treeview(right_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)
        
        self.AttendaceReportTable.heading("id",text="Attendance ID")
        self.AttendaceReportTable.heading("roll",text="Roll")
        self.AttendaceReportTable.heading("name",text="Name")
        self.AttendaceReportTable.heading("department",text="Department")
        self.AttendaceReportTable.heading("time",text="Time")
        self.AttendaceReportTable.heading("date",text="Date")
        self.AttendaceReportTable.heading("attendance",text="Attendance")
        
        self.AttendaceReportTable["show"]="headings"
        
        self.AttendaceReportTable.column("id",width=100)
        self.AttendaceReportTable.column("roll",width=100)
        self.AttendaceReportTable.column("name",width=100)
        self.AttendaceReportTable.column("department",width=100)
        self.AttendaceReportTable.column("time",width=100)
        self.AttendaceReportTable.column("date",width=100)
        self.AttendaceReportTable.column("attendance",width=100)
        
        self.AttendaceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendaceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
    #=================================Fetch data========================
    
    def fetch_data(self,rows):
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
        for i in rows:
            self.AttendaceReportTable.insert("",END,values=i)
            
            
            
    #======================================Import CSV=============================================
    def import_Csv(self):
        global myData
        myData.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetch_data(myData)
            
            
            
     #=========================Export CSV==========================================
    def exportcsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No Data","No Data Found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported  "+  os.path.basename(fln)  +"  Successfully")    
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                
    #=========================Get Function==========================
    def get_cursor(self,event=""):
        cursor_row=self.AttendaceReportTable.focus()
        content=self.AttendaceReportTable.item(cursor_row)
        rows=content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])            
        self.var_attend_name.set(rows[2]) 
        self.var_attend_dep.set(rows[3]) 
        self.var_attend_time.set(rows[4]) 
        self.var_attend_date.set(rows[5]) 
        self.var_attend_attendance.set(rows[6]) 
        
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")            
        self.var_attend_name.set("") 
        self.var_attend_dep.set("") 
        self.var_attend_time.set("") 
        self.var_attend_date.set("") 
        self.var_attend_attendance.set("") 
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()