import mysql.connector
#import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

#Connection Later
def connection() :
    conn = mysql.connector.connect(host='localhost',user='root',passwd='root',database='student_marks')
    return conn

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    '''for array in read():
        my_tree.insert(parent='',index='end',iid=array,text='',values=(array),tag='orow')'''

    my_tree.tag_configure('orow',background='#EEEEEE',font=('Arial',12))
    my_tree.grid(row=8,column=0,columnspan=5,rowspan=11,padx=10,pady=20)


#GUI Window-PART
root = Tk()      #Tk class object
root.title('Student Marks Database')     #Gives Title to our Window
root.geometry('1080x720')
my_tree = ttk.Treeview(root)             #Treeview has rows , columns and headings

#Functions later

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM STUDENT_MARKS")    #table connection
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return result


#GUI PART
label = Label(root,text='STUDENT MARKS DATABASE (CRUD OPERATION)',font=('Arial Bold',30))
label.grid(row=0,column=0,columnspan=8,rowspan=2,padx=50,pady=40)            #Labeling the text on window with grid method

#Labels
studnameLabel = Label(root,text='Student Id',font=('Arial',15))
physicsLabel = Label(root,text='Physics',font=('Arial',15))
chemistryLabel = Label(root,text='Chemistry',font=('Arial',15))
mathsLabel = Label(root,text='Maths',font=('Arial',15))
totalLabel = Label(root,text='Total Marks',font=('Arial',15))

#Assembling Labels on window
studnameLabel.grid(row=3,column=0,columnspan=1,padx=50,pady=5)
physicsLabel.grid(row=4,column=0,columnspan=1,padx=50,pady=5)
chemistryLabel.grid(row=5,column=0,columnspan=1,padx=50,pady=5)
mathsLabel.grid(row=6,column=0,columnspan=1,padx=50,pady=5)
totalLabel.grid(row=7,column=0,columnspan=1,padx=50,pady=5)

#Entry for Labels
#textvariable later
studnameEntry = Entry(root,width=55,bd=5,font=('Arial',15))
physicsEntry = Entry(root,width=55,bd=5,font=('Arial',15))
chemistryEntry = Entry(root,width=55,bd=5,font=('Arial',15))
mathsEntry = Entry(root,width=55,bd=5,font=('Arial',15))
totalEntry = Entry(root,width=55,bd=5,font=('Arial',15))

#Assembling Entries on Window
studnameEntry.grid(row=3,column=1,columnspan=4,padx=5,pady=0)
physicsEntry.grid(row=4,column=1,columnspan=4,padx=5,pady=0)
chemistryEntry.grid(row=5,column=1,columnspan=4,padx=5,pady=0)
mathsEntry.grid(row=6,column=1,columnspan=4,padx=5,pady=0)
totalEntry.grid(row=7,column=1,columnspan=4,padx=5,pady=0)


#Buttons
#Command Later
addBtn = Button(root,text='ADD',padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg='#84F894')
updateBtn = Button(root,text='UPDATE',padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg='#84F894')
deleteBtn = Button(root,text='DELETE',padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg='#84F894')
searchBtn = Button(root,text='SEARCH',padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg='#84F894')
resetBtn = Button(root,text='RESET',padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg='#84F894')
selectBtn = Button(root,text='SELECT',padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg='#84F894')

#Assembling the buttons on window
addBtn.grid(row=3,column=5,columnspan=1,rowspan=2)
updateBtn.grid(row=5,column=5,columnspan=1,rowspan=2)
deleteBtn.grid(row=7,column=5,columnspan=1,rowspan=2)
searchBtn.grid(row=9,column=5,columnspan=1,rowspan=2)
resetBtn.grid(row=11,column=5,columnspan=1,rowspan=2)
selectBtn.grid(row=13,column=5,columnspan=1,rowspan=2)

style = ttk.Style()         #TTK Objext
style.configure('TreeView.Heading',font=('Arial Bold',15))
my_tree['columns']=('Stud Id','Physics','Chemistry','Maths','Total')

my_tree.column('#0',width=0,stretch = NO)
my_tree.column('Stud Id',anchor=W,width=170)
my_tree.column('Physics',anchor=W,width=170)
my_tree.column('Chemistry',anchor=W,width=170)
my_tree.column('Maths',anchor=W,width=170)
my_tree.column('Total',anchor=W,width=170)

my_tree.heading('Stud Id',text='Student Name',anchor=W)
my_tree.heading('Physics',text='Student Name',anchor=W)
my_tree.heading('Chemistry',text='Student Name',anchor=W)
my_tree.heading('Maths',text='Student Name',anchor=W)
my_tree.heading('Total',text='Total Marks',anchor=W)


refreshTable()



root.mainloop()
