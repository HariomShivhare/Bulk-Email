# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
# Libraries imported to Tkinter
import pandas as pd
from tkinter import * 
# from time import time
import tkinter.messagebox
from tkinter import ttk 
from tkinter.filedialog import askopenfilename
import os



##Sumbited function 

def mail():
      try:
            
            # Excel With Pandas
            my_file=pd.read_excel(file_name,encoding='utf-8')
            total_row=len(my_file.email)

            # Replace funtionality
            my_file=my_file.fillna({ # replace  dicrinoary
                  'email':'hariomshivhare095@gmail.com',
                  'file':'mail or file path not faund'
                })
            
            for i in range(total_row):
                  data=my_file['email'].values[i]
                  path=my_file['file'].values[i]
                  
                  print(f'  {data}  {path}')
                  listbox.insert(END, f"{i} Email  {data}    File  {path}")
                        #Email sending Code start
      #             fromaddr= f"{from_email}"#hariomshivhare095@gmail.com" 
      #             toaddr=data
      #             print(toaddr)
      #                   #     # # instance of MIMEMultipart 
      #             msg = MIMEMultipart() 

      #                   #     # # storing the senders email address 
      #             msg['From'] = fromaddr 

      #                   #     # # storing the receivers email address 
      #             msg['To'] = toaddr  #toaddr 

      #                   #     # # storing the subject 
      #             msg['Subject'] =f"{mail_sub}"  #"text file"

      #                   #     # # string to store the body of the mail 
      #             body = f"{mail_body}"  #" send by harsh"

      #                   #     # # attach the body with the msg instance 
      #             msg.attach(MIMEText(body, 'plain')) 

      #                   #     # # open the file to be sent 
      #             file_path=path # Enter file path

      #             filename=os.path.basename(file_path) # Enter File BaseName 

      #             print(filename)
      #             attachment = open(f"{file_path}", "rb") 

      #                   # # instance of MIMEBase and named as p 
      #             p = MIMEBase('application', 'octet-stream') 

      #                   # # To change the payload into encoded form 
      #             p.set_payload((attachment).read()) 

      #                   # # encode into base64  
      #             encoders.encode_base64(p) 

      #             p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

      #                   # # attach the instance 'p' to instance 'msg' 
      #             msg.attach(p) 

      #                   # # creates SMTP session 
      #             s = smtplib.SMTP('smtp.gmail.com', 587) 

      #                   # # start TLS for security 
      #             s.starttls() 

      #                   # Authentication 
      #             s.login(fromaddr, f"{mail_paas}")#raghavdada@412" 

      #                   # # Converts the Multipart msg into a string 
      #             text = msg.as_string() 
                        
      #                   #sending the mail 
      #             s.sendmail(fromaddr, toaddr, text) 
      #             print("From Submitted ")

      #                   # terminating the session 
      #             status_bar['text']="E-mail  Sumbitting"   
      #             s.quit()
      #       status_bar['text']="E-mail is Sumbitted"
           
      except:
            tkinter.messagebox.showerror("Email Sending","Filepath not selected \n Please Select filepath")


# #Browse file and open Dailogue box
def open_file():
      global file_name
      global from_email
      global mail_body
      global mail_sub
      global mail_paas
      from_email=email.get()
      mail_body=body_text.get()
      mail_sub=subject.get()
      mail_paas=paas.get()
      print(from_email)
      
      print(mail_body)
      print(mail_sub)
      print(mail_paas)
      
      print(body_text)
      
      file_name=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
      file_path_list.insert(END,file_name)
      print(file_name)


# Creating Gui Start

root=Tk()
# root.config(background="grey") # background for Gui

 
# root.minsize(width=600,height=400)
root.title("Email sending")
root.wm_iconbitmap("email.ico")
root.minsize(557,545)
# root.maxsize(557,545)s
#Head Label of Gui
Label(root,text="Developed by Harsh Shivhare").grid(row=0,column=4,sticky=S,pady=2)
head_label2= Label(root,text="Welcome Email Sending System ",font=('helvetica',15,'bold'),fg="Black" ,bg="white")
head_label2.grid(row=0,column=4,sticky=S, pady=20)

#Labels oF Gui
subject=Label(root,text="Enter_Subejct (for all User):")
subject.grid(row=1,column=3,ipady=5,sticky=W)
body_text=Label(root,text="Enter_Body: (for all User)")
body_text.grid(row=2,column=3,ipady=5,sticky=W)

email=Label(root,text="Enter_Email_from:")
email.grid(row=3,column=3,ipady=5,sticky=W)
paas=Label(root,text="Enter_Password:")
paas.grid(row=4,column=3,ipady=5,sticky=W)
file_path=Label(root,text="Enter_Filepath:")
file_path.grid(row=5,column=3,ipady=5,sticky=W)

subject=StringVar()
body_text=StringVar()
email=StringVar()
paas=StringVar()

#Entry Box of Gui
subject_Entry=Entry(root,textvariable=subject ,width="40")
subject_Entry.grid(row=1,column=4,ipady=5,pady=6)
# body_Entry=Entry(root,textvariable=body,width="40")
# body_Entry.grid(row=2,column=4,ipady=5,pady=6)
body_text=Text(root,bd=1 ,width="40",height="10")
body_text.grid(row=2,column=4,ipady=5,sticky=S, pady=6)
email_Entry=Entry(root,textvariable=email,width="40")
email_Entry.grid(row=3,column=4,ipady=5,pady=6)
# password Entery
bullet="\u2022"
pass_Entry=Entry(root,textvariable=paas,show=bullet,width="40")
pass_Entry.grid(row=4,column=4,ipady=5,pady=6)

#ListBox of GUi
file_path_list=Listbox(root,width="40",height=2)
file_path_list.grid(row=5,column=4,ipady=5,pady=6)



scrollbar=Scrollbar(root)
scrollbar.grid(row=7,column=4)
listbox=Listbox(root,yscrollcommand=scrollbar.set,height=10,width=50)
listbox.grid(row=7,column=4,pady=6)

status_frame = Frame(root)

status =Label(status_frame, text="this is the status bar",font=('helvetica',10,''),bd=2,relief=SUNKEN,anchor=W)

status.pack(side=BOTTOM,fill=X)
status_frame.grid(columnspan=20, sticky="ew")


# Select bitton for open filedailog
add_btn=ttk.Button(root,text="Browse file ",command=open_file).grid(row=5,column=5,padx=10)

# Sumbited button  
ttk.Button(root,text="Submit",command=mail).grid(row=6,column=4,padx=30 )


        
def close():
      # msgbox=tkinter.messagebox.askquestion("Email Sending","Are You Sure You want to Exit",icon='warning')
      # if msgbox=='Yes':
      #       root.destroy()
           
      # else:
      #       tkinter.messagebox.showinfo('Return','You Will Return to the application screen')
   
   root.destroy()
root.protocol("WM_DELETE_WINDOW",close)

root.mainloop() 