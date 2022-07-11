# Python program to illustrate the usage of
# treeview scrollbars using tkinter


from tkinter import ttk
import tkinter as tk
#import mysql.connector
import pymysql

#import main.py

# Creating tkinter window
window = tk.Tk()
window.resizable(width = 50, height = 50)

con=pymysql.connect(host='localhost',user='root',password='',database='attendance')
cur=con.cursor()
cur.execute("select * from class")


# Using treeview widget
treev = ttk.Treeview(window, selectmode ='browse')

# Calling pack method w.r.to treeview
treev.pack(side ='top')

# Constructing vertical scrollbar
# with treeview
verscrlbar = ttk.Scrollbar(window,
						orient ="vertical",
						command = treev.yview)

# Calling pack method w.r.to vertical
# scrollbar
verscrlbar.pack(side ='right', fill ='x')

# Configuring treeview
treev.configure(xscrollcommand = verscrlbar.set)

# Defining number of columns
treev["columns"] = ("1", "2", "3")

# Defining heading
treev['show'] = 'headings'

# Assigning the width and anchor to the
# respective columns
treev.column("1", width = 400, anchor ='c')
treev.column("2", width = 400, anchor ='c')
treev.column("3", width = 400, anchor ='c')

# Assigning the heading names to the
# respective columns
treev.heading("1", text ="Sr.No")
treev.heading("2", text ="Class")
treev.heading("3", text ="Total Students")

# Inserting the items and their features to the
# columns built
i=0
for row in cur:
    treev.insert('',i,text=row[0],values=(row[0],row[1],row[2]))
    i=i+1

treev.pack()

def takeAttendance():
   # Get selected item to Edit
   selected_item = treev.focus()
   temp = treev.item(selected_item, 'values')
   value = temp[1]
   print(value)
   #window.destroy()
   from attendance import  find_target_face,render_image
   lis = find_target_face(value)
   render_image()
   present_name=[]

   for image in lis:
       cur.execute("select * from student where photo = %s ",(image))
       row=cur.fetchone()
       present_name.append(row[1])
    
   for name in present_name:
       print(name)
   #print(temp[0])

def viewDetails():
   # Get selected item to Edit
   selected_item = treev.focus()
   temp = treev.item(selected_item, 'values')
   value=temp[0]
   print(value)
   from view_details import show
   show(value)
  # treev.item(selected_item, text="", values=("foo", "bar"))
   
att_btn = ttk.Button(window, text="Take Attendance", command=takeAttendance)
att_btn.pack()

view_btn = ttk.Button(window, text="View Details", command=viewDetails)
view_btn.pack()
# Calling mainloop

window.mainloop()
