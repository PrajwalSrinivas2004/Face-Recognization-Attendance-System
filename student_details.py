from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student :
    def __init__(self,root):
        self.root= root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Detection System")
        
        #===============variables===================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_photo_status=StringVar()
        

         #image1
        img1=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig1.jpg")
        img1=img1.resize((500,100),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
    
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=100)
        
        #image2
        img2=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig2.jpg")
        img2=img2.resize((500,100),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
    
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=400,height=100)

        #image3
        img3=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig3.jpeg")
        img3=img3.resize((500,100),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
    
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=900,y=0,width=500,height=100)
        
        #Background Image
        img4=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig2.jpg")
        img4=img4.resize((1530,710),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
    
        
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=100,width=1500,height=600)
        
        
        title_label=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="green")
        title_label.place(x=0,y=0,width=1350,height=35)
        
        
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=2,y=50,width=1260,height=600)
        
       
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=0,width=710,height=580)
        
        #image3
        img_left=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig3.jpeg")
        img_left=img_left.resize((700,130),Image.LANCZOS)
        self.photoimg_l=ImageTk.PhotoImage(img_left)
    
        f_lbl=Label(Left_frame,image=self.photoimg_l)
        f_lbl.place(x=5,y=0,width=650,height=80)
        
        
        #Current Course
        current_course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=10,y=100,width=660,height=110)
        
        
        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),width=20,state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","Civil","IT","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)        
        
        
        #Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=20,sticky=W)
    
    
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),width=20,state="read only")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
         
        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=30,sticky=W)
    
    
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),width=20,state="read only")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)  
        
        #Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=20,sticky=W)
    
    
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),width=20,state="read only")
        semester_combo["values"]=("Select Semester","Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6","Sem-7","Sem-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
        
         #Class Student Information
        current_course_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=10,y=210,width=660,height=280)
        
        
        
        
        #Student Id
        student_label=Label(current_course_frame,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
        student_label.grid(row=0,column=0,padx=10,sticky=W)
        
        studentID_entry=Entry(current_course_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"),bg="white")
        studentID_entry.grid(row=0,column=1,padx=5,pady=0,sticky=W)
        
        #Student Name
        student_label=Label(current_course_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        student_label.grid(row=0,column=2,padx=15,pady=2,sticky=W)
        
        studentID_entry=Entry(current_course_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"),bg="white")
        studentID_entry.grid(row=0,column=3,padx=5,pady=2,sticky=W)
        
         #Class Division
        student_label=Label(current_course_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
        student_label.grid(row=1,column=0,padx=10,pady=2,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),width=18,state="read only")
        semester_combo["values"]=("A","B","C","D")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=1,padx=5,pady=2,sticky=W)
        
        #Roll No.
        student_label=Label(current_course_frame,text="Roll No.:",font=("times new roman",13,"bold"),bg="white")
        student_label.grid(row=1,column=2,padx=15,pady=2,sticky=W)
        
        studentID_entry=Entry(current_course_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"),bg="white")
        studentID_entry.grid(row=1,column=3,padx=5,pady=2,sticky=W)
        
         #Gender
        student_label=Label(current_course_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        student_label.grid(row=2,column=0,padx=10,pady=2,sticky=W)
        
       
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),width=18,state="read only")
        semester_combo["values"]=("Male","Female","Other")
        semester_combo.current(0)
        semester_combo.grid(row=2,column=1,padx=5,pady=2,sticky=W)
        
        #DOB
        student_label=Label(current_course_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        student_label.grid(row=2,column=2,padx=15,pady=2,sticky=W)
        
        studentID_entry=Entry(current_course_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"),bg="white")
        studentID_entry.grid(row=2,column=3,padx=5,pady=2,sticky=W)
        
         #Email
        student_label=Label(current_course_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        student_label.grid(row=3,column=0,padx=10,pady=2,sticky=W)
        
        studentID_entry=Entry(current_course_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"),bg="white")
        studentID_entry.grid(row=3,column=1,padx=5,pady=2,sticky=W)
        
        #Phone No
        student_label=Label(current_course_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        student_label.grid(row=3,column=2,padx=15,pady=2,sticky=W)
        
        studentID_entry=Entry(current_course_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"),bg="white")
        studentID_entry.grid(row=3,column=3,padx=5,pady=2,sticky=W)
        
         #Address
        student_label=Label(current_course_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        student_label.grid(row=4,column=0,padx=10,pady=2,sticky=W)
        
        studentID_entry=Entry(current_course_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"),bg="white")
        studentID_entry.grid(row=4,column=1,padx=5,pady=2,sticky=W)
        
        #Teacher Name
        student_label=Label(current_course_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        student_label.grid(row=4,column=2,padx=15,pady=2,sticky=W)
        
        studentID_entry=Entry(current_course_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"),bg="white")
        studentID_entry.grid(row=4,column=3,padx=5,pady=2,sticky=W)
        
        
        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(current_course_frame,text="Take a photo Sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        radiobtn2=ttk.Radiobutton(current_course_frame,text="No Photo Sample",variable=self.var_radio1,value="No")
        radiobtn2.grid(row=6,column=1)
        
        #Button Frame
        btn_frame=Frame(current_course_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=715,height=35)
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
       
        #Photo Sample
        btn_frame1=Frame(current_course_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=210,width=715,height=35)
        
        photo_sample_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=32,font=("times new roman",13,"bold"),bg="blue",fg="white")
        photo_sample_btn.grid(row=0,column=0)
        
        reset_btn=Button(btn_frame1,text="Update Photo Sample",width=32,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=1)
        
        
    
        #right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=675,y=0,width=580,height=490)
        
        
        #image3
        img_right=Image.open(r"C:\Users\Lenovo\OneDrive\Desktop\Face detection Project\projectImages\ig3.jpeg")
        img_right=img_right.resize((700,130),Image.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_right)
    
        f_lbl1=Label(Right_frame,image=self.photoimg_2)
        f_lbl1.place(x=5,y=0,width=650,height=80)
        
        
         #======================Search System=====================================
        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        search_frame.place(x=10,y=80,width=660,height=100)
        
        search_label=Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=15,pady=2,sticky=W)
        
        
        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),width=12,state="readonly")
        search_combo["values"]=("Select" "Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry=Entry(search_frame,width=10,font=("times new roman",13,"bold"),bg="white")
        search_entry.grid(row=0,column=2,padx=5,pady=0,sticky=W)
        
        
        search_btn=Button(search_frame,text="Search",width=9,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        showAll_btn=Button(search_frame,text="Show All",width=9,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)
        
        #============table frame==========================
        table_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=190,width=560,height=270)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=130)
    
     
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
     #=====================function declaration====================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="127.0.0.1",username="root",password="1234567@eight",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                                
                                                                                                                ))
                                                                                                 
                                                                                                
                    
                                                                                           
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)      
                    
    #======================fetch data====================
    def fetch_data(self):
         conn=mysql.connector.connect(host="127.0.0.1",username="root",password="1234567@eight",database="face_recognizer")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from student")
         data=my_cursor.fetchall()
         
         if len(data)!=0:
             self.student_table.delete(*self.student_table.get_children())
             for i in data:
                 self.student_table.insert("",END,values=i)
             conn.commit()
         conn.close()
         
    #====================get cursor====================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
    #====Update dunction=============
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update the student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="127.0.0.1",username="root",password="1234567@eight",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                    
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_std_id.get()
                                                                                                            ))
                else:
                    if not update:
                        return 
                    
                messagebox.showinfo("Success","Student Details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 
                
    #================Delete function=====================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="127.0.0.1",username="root",password="1234567@eight",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)   
                
    #==========================Reset button=================================
    def  reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division ")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
                                
   
    
    #=====================================Generate data set and take samples=====================================  
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update the student details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="127.0.0.1",username="root",password="1234567@eight",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from student")
                    myreuslt=my_cursor.fetchall()
                    id=0
                    for x in myreuslt:
                        id+=1
                    my_cursor.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                                                                                    
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_std_id.get()==id+1
                                                                                                        ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()
                   
                    
                    
                    #====================Load Prdefined data on face on frantals from openCV===================
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                    
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum neightbour=5
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                        
                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data set completed!!!!") 
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)       
        
         





if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()