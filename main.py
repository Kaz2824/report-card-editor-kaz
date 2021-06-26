import tkinter
from tkinter import *
from tkinter import ttk, font
import tkinter.messagebox
import mysql.connector

def new_window(Win_class):
    global win2
    try:
        if win2.state() == "normal": win2.focus()
    except NameError as e:
        print(e)
        win2 = tkinter.Toplevel(window)
        Win_class(win2)

class Win2:
    def __init__(self,root):
        self.root = root
        self.root.geometry("300x300+500+200")
        self.root["bg"] = "navy"


class GUI(Tk):

    def __init__(self):
        super().__init__()

        # Window configuration
        defaultFont = font.nametofont("TkDefaultFont")
        defaultFont.configure(family="Tw Cen MT", size=12)
        self.geometry("1280x720")
        self.title('Editor')
        self.tk_setPalette(background="#282828", foreground="#ebdbb2")
        # ==========================================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Editor", "Confirm if you want to exit")
            if iExit > 0:
                self.destroy()

        def reset():
            self.var.set(' ')
            self.var1.set(' ')
            self.var2.set(' ')
            self.FirstNam_txt.delete(0, END)
            self.LastNam_txt.delete(0, END)
            self.Adm_txt.delete(0, END)
            self.Roll_txt.delete(0, END)
            self.clicked1.set('')
            self.clicked2.set('')

            for self.Widget in self.Academic_Frame.winfo_children():
                self.Widget.destroy()

            self.Cmd_Btn.configure(state=NORMAL)
            for self.Widget in self.Optional_Frame.winfo_children():
                self.Widget.destroy()

        def add_data():
            if self.FirstNam_txt.get() == "" or self.LastNam_txt.get() == "" or self.Adm_txt.get() == "":
            # if Firstname.get() == "" or Lastname.get() == "" or AdmissionNo.get() == "":
                tkinter.messagebox.showerror("Editor", "Enter Correct Details")
            else:
                conn = mysql.connector.connect(host='localhost', user='root', password='xxxx',
                                               database='report_card_db')
                cur = conn.cursor()
                cur.execute("INSERT INTO student (AdmissionNo, Name, RollNo, Gender, Class, Section, Subject_1, Subject_1_marks, Subject_2, Subject_2_marks, Subject_3,Subject_3_marks, Subject_4, Subject_4_marks, Subject_5, Subject_5_marks) VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s, %s, %s, %s, %s, %s)", (
                    self.Adm_txt.get(),
                    self.FirstNam_txt.get() + ' ' + self.LastNam_txt.get(),
                    self.Roll_txt.get(),
                    self.var.get(),
                    self.clicked1.get(),
                    self.clicked2.get(),
                    self.lbl1.cget("text"),
                    self.txt1.get(),
                    self.lbl2.cget("text"),
                    self.txt2.get(),
                    self.lbl3.cget("text"),
                    self.txt3.get(),
                    self.lbl5.cget("text"),
                    self.txt4.get(),
                    self.lbl4.cget("text"),
                    self.txt5.get()
                ))
                conn.commit()
                conn.close()
                tkinter.messagebox.showinfo("Editor", "Data entered")

        # def display_data():




        # ==========================================================================

        # Window title
        self.Topic = Label(self, text="Student Marksheet", fg="#b8bb26", font=("Bahnschrift", 30))
        self.Topic.place(x=475, y=29)

        # Student Info
        self.Data_lbl = Label(self, text="Student Data:", font=("Bahnschrift", 20))
        self.Data_lbl.place(x=60, y=125)

        self.FirstNam_lbl = Label(self, text="First Name")
        self.FirstNam_lbl.place(x=30, y=200)
        self.FirstNam_txt = Entry(self, bd=2)
        self.FirstNam_txt.place(x=136, y=200)

        self.LastNam_lbl = Label(self, text="Last Name")
        self.LastNam_lbl.place(x=30, y=250)
        self.LastNam_txt = Entry(self, bd=2)
        self.LastNam_txt.place(x=136, y=250)

        self.Roll_lbl = Label(self, text="Roll No.")
        self.Roll_lbl.place(x=30, y=300)
        self.Roll_txt = Entry(self, bd=2)
        self.Roll_txt.place(x=136, y=300)

        self.Adm_lbl = Label(self, text="Admission No.")
        self.Adm_lbl.place(x=30, y=350)
        self.Adm_txt = Entry(self, bd=2)
        self.Adm_txt.place(x=136, y=350)

        # RadioButton
        self.var = StringVar()
        self.var.set(' ')

        self.Gender_lbl = Label(self, text="Gender")
        self.Gender_lbl.place(x=30, y=510)
        self.Male = Radiobutton(self, text="Male", variable=self.var, value=1, selectcolor="#282828")
        self.Male.place(x=136, y=500)

        self.Female = Radiobutton(self, text="Female", variable=self.var, value=2, selectcolor="#282828")
        self.Female.place(x=136, y=520)

        # Drop-Down Menu
        self.Standard = Label(self, text="Standard")
        self.Standard.place(x=30, y=420)
        self.Section = Label(self, text="Section")
        self.Section.place(x=195, y=420)

        self.options1 = ["XI", "XII"]
        self.options2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

        self.clicked1 = StringVar()
        self.clicked1.set("")

        self.clicked2 = StringVar()
        self.clicked2.set("")

        self.drop1 = OptionMenu(self, self.clicked1, *self.options1)
        self.drop1.place(x=136, y=420)

        self.drop2 = OptionMenu(self, self.clicked2, *self.options2)
        self.drop2.place(x=246, y=420)

        # Academic section

        # Header
        self.marks_lbl = Label(self, text="Academic Data:", font=("Bahnschrift", 20))
        self.marks_lbl.place(x=380, y=125)
        self.Input_Marks_lbl = Label(self, text="Enter Marks:", font=("Bahnschrift", 20))
        self.Input_Marks_lbl.place(x=960, y=125)

        # Streams and Optionals
        self.var1 = IntVar()
        self.var1.set(' ')

        # Subject-wise CheckButons
        self.Selectedsub_frame = LabelFrame(self, text="Subjects studying", font=("Bahnschrift", 16))
        self.Selectedsub_frame.place(x=350, y=200, width=190, height=250)

        self.Science_Math = Radiobutton(self.Selectedsub_frame, text="PCM", variable=self.var1, value=1,
                                        selectcolor="#282828")
        self.Science_Math.place(x=2, y=0)
        self.Science_Bio = Radiobutton(self.Selectedsub_frame, text="PCB", variable=self.var1, value=2,
                                       selectcolor="#282828")
        self.Science_Bio.place(x=2, y=40)
        self.Science_Math_Bio = Radiobutton(self.Selectedsub_frame, text="PCMB", variable=self.var1, value=3,
                                            selectcolor="#282828")
        self.Science_Math_Bio.place(x=2, y=80)
        self.Humanity = Radiobutton(self.Selectedsub_frame, text="Humanities", variable=self.var1, value=4,
                                    selectcolor="#282828")
        self.Humanity.place(x=2, y=120)
        self.Comm = Radiobutton(self.Selectedsub_frame, text="Commerce", variable=self.var1, value=5,
                                selectcolor="#282828")
        self.Comm.place(x=2, y=160)

        # Optional Subject Chosen
        self.Optional_Frame = LabelFrame(self, text="Optional Subject", font=("Bahnschrift", 16))
        self.Optional_Frame.place(x=600, y=200, width=200, height=220)

        self.var2 = IntVar()
        self.var2.set(' ')

        self.Comp_Radiobutton = Radiobutton(text="Computer Science", variable=self.var2, selectcolor="#282828")
        self.Sports_Radiobutton = Radiobutton(text="Physical Education", variable=self.var2, selectcolor="#282828")
        self.Psy_Radiobutton = Radiobutton(text="Psychology", variable=self.var2, selectcolor="#282828")
        self.Eco_Radiobutton = Radiobutton(text="Economics", variable=self.var2, selectcolor="#282828")
        self.Mat_Radiobutton = Radiobutton(text="Maths", variable=self.var2, selectcolor="#282828")
        self.Commercial_Radiobutton = Radiobutton(text="Commercial Arts", variable=self.var2, selectcolor="#282828")
        self.Informatics_Radiobutton = Radiobutton(text="Informatics Practices", variable=self.var2,
                                                   selectcolor='#282828')

        # Cmd_Function
        self.Cmd_Btn = Button(text="Select Optional Subjects", command=self.Optional_Selection)
        self.Cmd_Btn.place(x=350, y=500)

        # Marks Attained
        self.Academic_Frame = LabelFrame(self, text="Marks Attained", font=("Bahnschrift", 16))
        self.Academic_Frame.place(x=970, y=200, width=270, height=365)

        self.Marks_Btn = Button(self, text="Click to Input Marks", command=lambda: self.Marksheet())
        self.Marks_Btn.place(x=970, y=600)

        # Reset Button
        self.reset_btn = Button(self, text='Reset Entries', command=reset).place(x=655, y=500)

        # Exit Button
        self.exit_btn = Button(self, text='Exit', command=iExit).place(x=136, y=600)

        # Add Data Button
        self.submit_btn = Button(self, text='Submit', command=add_data).place(x=1185, y=600)

        # Generate Marksheet Button
        self.generate_btn = Button(self, text='Generate Marksheet', command=lambda: new_window(Win2)).place(x=500, y=600)

        # Selected subjects
        self.lbl4 = Label(self.Academic_Frame, text="English")
        self.lbl4.place(x=20, y=250)
        self.txt1 = Entry(self.Academic_Frame, bd=2)
        self.txt1.place(x=150, y=50, height=20, width=80)
        self.txt2 = Entry(self.Academic_Frame, bd=2)
        self.txt2.place(x=150, y=100, height=20, width=80)
        self.txt3 = Entry(self.Academic_Frame, bd=2)
        self.txt3.place(x=150, y=150, height=20, width=80)
        self.txt4 = Entry(self.Academic_Frame, bd=2)
        self.txt4.place(x=150, y=200, height=20, width=80)
        self.txt5 = Entry(self.Academic_Frame, bd=2)
        self.txt5.place(x=150, y=250, height=20, width=80)

    def Optional_Selection(self):
        if self.var1.get() == 1:
            self.Comp_Radiobutton = Radiobutton(self.Optional_Frame, text="Computer Science", variable=self.var2,
                                                value=1,
                                                selectcolor="#282828")
            self.Comp_Radiobutton.pack()
            self.Sports_Radiobutton = Radiobutton(self.Optional_Frame, text="Physical Education", variable=self.var2,
                                                  value=2,
                                                  selectcolor="#282828")
            self.Sports_Radiobutton.pack()
            self.Psy_Radiobutton = Radiobutton(self.Optional_Frame, text="Psychology", variable=self.var2, value=3,
                                               selectcolor="#282828")
            self.Psy_Radiobutton.pack()
            self.Eco_Radiobutton = Radiobutton(self.Optional_Frame, text="Economics", variable=self.var2, value=4,
                                               selectcolor="#282828")
            self.Eco_Radiobutton.pack()
            self.Commercial_Radiobutton = Radiobutton(self.Optional_Frame, text="Commercial Arts", variable=self.var2,
                                                      value=5,
                                                      selectcolor="#282828")
            self.Commercial_Radiobutton.pack()
        elif self.var1.get() == 2:
            self.Sports_Radiobutton = Radiobutton(self.Optional_Frame, text="Physical Education", variable=self.var2,
                                                  value=1,
                                                  selectcolor="#282828")
            self.Sports_Radiobutton.pack()
            self.Psy_Radiobutton = Radiobutton(self.Optional_Frame, text="Psychology", variable=self.var2, value=2,
                                               selectcolor="#282828")
            self.Psy_Radiobutton.pack()
            self.Eco_Radiobutton = Radiobutton(self.Optional_Frame, text="Economics", variable=self.var2, value=3,
                                               selectcolor="#282828")
            self.Eco_Radiobutton.pack()
            self.Commercial_Radiobutton = Radiobutton(self.Optional_Frame, text="Commercial Arts", variable=self.var2,
                                                      value=4,
                                                      selectcolor="#282828")
            self.Commercial_Radiobutton.pack()
        elif self.var1.get() == 3:
            self.No_Optional_lbl = Label(self.Optional_Frame, text="No Optional Subjects")
            self.No_Optional_lbl.place(x=5, y=10)
            self.No_Optional_Radiobutton = Radiobutton(self.Optional_Frame, text="Please Select the Button",
                                                       variable=self.var2,
                                                       value=1,
                                                       selectcolor="#282828")
            self.No_Optional_Radiobutton.place(x=1, y=50)
        elif self.var1.get() == 4:
            self.Mat_Radiobutton = Radiobutton(self.Optional_Frame, text="Economics", variable=self.var2, value=1,
                                               selectcolor="#282828")
            self.Mat_Radiobutton.pack()
            self.Sports_Radiobutton = Radiobutton(self.Optional_Frame, text="Physical Education", variable=self.var2,
                                                  value=2,
                                                  selectcolor="#282828")
            self.Sports_Radiobutton.pack()
            self.Commercial_Radiobutton = Radiobutton(self.Optional_Frame, text="Commercial Arts", variable=self.var2,
                                                      value=3,
                                                      selectcolor="#282828")
            self.Commercial_Radiobutton.pack()
        elif self.var1.get() == 5:
            self.Sports_Radiobutton = Radiobutton(self.Optional_Frame, text="Physical Education", variable=self.var2,
                                                  value=1,
                                                  selectcolor="#282828")
            self.Sports_Radiobutton.pack()
            self.Psy_Radiobutton = Radiobutton(self.Optional_Frame, text="Psychology", variable=self.var2, value=2,
                                               selectcolor="#282828")
            self.Psy_Radiobutton.pack()
            self.Mat_Radiobutton = Radiobutton(self.Optional_Frame, text="Maths", variable=self.var2, value=3,
                                               selectcolor="#282828")
            self.Mat_Radiobutton.pack()
            self.Commercial_Radiobutton = Radiobutton(self.Optional_Frame, text="Commercial Arts", variable=self.var2,
                                                      value=4,
                                                      selectcolor="#282828")
            self.Commercial_Radiobutton.pack()
            self.Informatics_Radiobutton = Radiobutton(self.Optional_Frame, text="Informatics Practices",
                                                       variable=self.var2, value=5,
                                                       selectcolor='black')
            self.Informatics_Radiobutton.pack()

        self.Cmd_Btn.configure(state=DISABLED)

    def Marksheet(self):
        if self.var1.get() == 1 and self.var2.get() == 1:
            self.lbl1 = Label(self.Academic_Frame, text="Physics")
            self.lbl1.place(x=20, y=50)
            self.lbl2 = Label(self.Academic_Frame, text="Chemistry")
            self.lbl2.place(x=20, y=100)
            self.lbl3 = Label(self.Academic_Frame, text="Maths")
            self.lbl3.place(x=20, y=150)
            self.lbl5 = Label(self.Academic_Frame, text="Computer Science")
            self.lbl5.place(x=20, y=200)

        elif self.var1.get() == 1 and self.var2.get() == 2:
            self.lbl1 = Label(self.Academic_Frame, text="Physics")
            self.lbl1.place(x=20, y=50)
            self.lbl2 = Label(self.Academic_Frame, text="Chemistry")
            self.lbl2.place(x=20, y=100)
            self.lbl3 = Label(self.Academic_Frame, text="Maths")
            self.lbl3.place(x=20, y=150)
            self.lbl5 = Label(self.Academic_Frame, text="Physical Education")
            self.lbl5.place(x=20, y=200)

        elif self.var1.get() == 1 and self.var2.get() == 3:
            self.lbl1 = Label(self.Academic_Frame, text="Physics")
            self.lbl1.place(x=20, y=50)
            self.lbl2 = Label(self.Academic_Frame, text="Chemistry")
            self.lbl2.place(x=20, y=100)
            self.lbl3 = Label(self.Academic_Frame, text="Maths")
            self.lbl3.place(x=20, y=150)
            self.lbl5 = Label(self.Academic_Frame, text="Psychology")
            self.lbl5.place(x=20, y=200)

        elif self.var1.get() == 1 and self.var2.get() == 4:
            self.lbl1 = Label(self.Academic_Frame, text="Physics")
            self.lbl1.place(x=20, y=50)
            self.lbl2 = Label(self.Academic_Frame, text="Chemistry")
            self.lbl2.place(x=20, y=100)
            self.lbl3 = Label(self.Academic_Frame, text="Maths")
            self.lbl3.place(x=20, y=150)
            self.lbl5 = Label(self.Academic_Frame, text="Economics")
            self.lbl5.place(x=20, y=200)

        elif self.var1.get() == 1 and self.var2.get() == 5:
            self.lbl1 = Label(self.Academic_Frame, text="Physics")
            self.lbl1.place(x=20, y=50)
            self.lbl2 = Label(self.Academic_Frame, text="Chemistry")
            self.lbl2.place(x=20, y=100)
            self.lbl3 = Label(self.Academic_Frame, text="Maths")
            self.lbl3.place(x=20, y=150)
            self.lbl5 = Label(self.Academic_Frame, text="Commercial Arts")
            self.lbl5.place(x=20, y=200)

        elif self.var1.get() == 2 and self.var2.get() == 1:
            self.lbl1 = Label(self.Academic_Frame, text="Physics")
            self.lbl1.place(x=20, y=50)
            self.lbl2 = Label(self.Academic_Frame, text="Chemistry")
            self.lbl2.place(x=20, y=100)
            self.lbl3 = Label(self.Academic_Frame, text="Biology")
            self.lbl3.place(x=20, y=150)
            self.lbl5 = Label(self.Academic_Frame, text="Physical Education")
            self.lbl5.place(x=20, y=200)

        elif self.var1.get() == 2 and self.var2.get() == 2:
            self.lbl1 = Label(self.Academic_Frame, text="Physics")
            self.lbl1.place(x=20, y=50)
            self.lbl2 = Label(self.Academic_Frame, text="Chemistry")
            self.lbl2.place(x=20, y=100)
            self.lbl3 = Label(self.Academic_Frame, text="Biology")
            self.lbl3.place(x=20, y=150)
            self.lbl5 = Label(self.Academic_Frame, text="Psychology")
            self.lbl5.place(x=20, y=200)

        elif self.var1.get() == 2 and self.var2.get() == 3:
            self.lbl1 = Label(self.Academic_Frame, text="Physics")
            self.lbl1.place(x=20, y=50)
            self.lbl2 = Label(self.Academic_Frame, text="Chemistry")
            self.lbl2.place(x=20, y=100)
            self.lbl3 = Label(self.Academic_Frame, text="Biology")
            self.lbl3.place(x=20, y=150)
            self.lbl5 = Label(self.Academic_Frame, text="Economics")
            self.lbl5.place(x=20, y=200)

        elif self.var1.get() == 2 and self.var2.get() == 4:
            self.lbl1 = Label(self.Academic_Frame, text="Physics")
            self.lbl1.place(x=20, y=50)
            self.lbl2 = Label(self.Academic_Frame, text="Chemistry")
            self.lbl2.place(x=20, y=100)
            self.lbl3 = Label(self.Academic_Frame, text="Biology")
            self.lbl3.place(x=20, y=150)
            self.lbl5 = Label(self.Academic_Frame, text="Commercial Arts")
            self.lbl5.place(x=20, y=200)

        elif self.var1.get() == 3 and self.var2.get() == 1:
            self.lbl1 = Label(self.Academic_Frame, text="Physics")
            self.lbl1.place(x=20, y=50)
            self.lbl2 = Label(self.Academic_Frame, text="Chemistry")
            self.lbl2.place(x=20, y=100)
            self.lbl3 = Label(self.Academic_Frame, text="Maths")
            self.lbl3.place(x=20, y=150)
            self.lbl5 = Label(self.Academic_Frame, text="Biology")
            self.lbl5.place(x=20, y=200)

        elif self.var1.get() == 4 and self.var2.get() == 1:
            self.lbl1 = Label(self.Academic_Frame, text="History")
            self.lbl1.place(x=20, y=50)
            self.lbl2 = Label(self.Academic_Frame, text="Political Science")
            self.lbl2.place(x=20, y=100)
            self.lbl3 = Label(self.Academic_Frame, text="Geography")
            self.lbl3.place(x=20, y=150)
            self.lbl5 = Label(self.Academic_Frame, text="Economics")
            self.lbl5.place(x=20, y=200)

        elif self.var1.get() == 4 and self.var2.get() == 2:
            self.lbl1 = Label(self.Academic_Frame, text="History")
            self.lbl1.place(x=20, y=50)
            self.lbl2 = Label(self.Academic_Frame, text="Political Science")
            self.lbl2.place(x=20, y=100)
            self.lbl3 = Label(self.Academic_Frame, text="Geography")
            self.lbl3.place(x=20, y=150)
            self.lbl5 = Label(self.Academic_Frame, text="Physical Education")
            self.lbl5.place(x=20, y=200)

        elif self.var1.get() == 4 and self.var2.get() == 3:
            self.lbl1 = Label(self.Academic_Frame, text="History")
            self.lbl1.place(x=20, y=50)
            self.lbl2 = Label(self.Academic_Frame, text="Political Science")
            self.lbl2.place(x=20, y=100)
            self.lbl3 = Label(self.Academic_Frame, text="Geography")
            self.lbl3.place(x=20, y=150)
            self.lbl5 = Label(self.Academic_Frame, text="Commercial Arts")
            self.lbl5.place(x=20, y=200)

        elif self.var1.get() == 5 and self.var2.get() == 1:
            self.lbl1 = Label(self.Academic_Frame, text="Accountancy")
            self.lbl1.place(x=20, y=50)
            self.lbl2 = Label(self.Academic_Frame, text="Business Studies")
            self.lbl2.place(x=20, y=100)
            self.lbl3 = Label(self.Academic_Frame, text="Economics")
            self.lbl3.place(x=20, y=150)
            self.lbl5 = Label(self.Academic_Frame, text="Physical Education")
            self.lbl5.place(x=20, y=200)

        elif self.var1.get() == 5 and self.var2.get() == 2:
            self.lbl1 = Label(self.Academic_Frame, text="Accountancy")
            self.lbl1.place(x=20, y=50)
            self.lbl2 = Label(self.Academic_Frame, text="Business Studies")
            self.lbl2.place(x=20, y=100)
            self.lbl3 = Label(self.Academic_Frame, text="Economics")
            self.lbl3.place(x=20, y=150)
            self.lbl5 = Label(self.Academic_Frame, text="Psychology")
            self.lbl5.place(x=20, y=200)

        elif self.var1.get() == 5 and self.var2.get() == 3:
            self.lbl1 = Label(self.Academic_Frame, text="Accountancy")
            self.lbl1.place(x=20, y=50)
            self.lbl2 = Label(self.Academic_Frame, text="Business Studies")
            self.lbl2.place(x=20, y=100)
            self.lbl3 = Label(self.Academic_Frame, text="Economics")
            self.lbl3.place(x=20, y=150)
            self.lbl5 = Label(self.Academic_Frame, text="Maths")
            self.lbl5.place(x=20, y=200)

        elif self.var1.get() == 5 and self.var2.get() == 4:
            self.lbl1 = Label(self.Academic_Frame, text="Accountancy")
            self.lbl1.place(x=20, y=50)
            self.lbl2 = Label(self.Academic_Frame, text="Business Studies")
            self.lbl2.place(x=20, y=100)
            self.lbl3 = Label(self.Academic_Frame, text="Economics")
            self.lbl3.place(x=20, y=150)
            self.lbl5 = Label(self.Academic_Frame, text="Commercial Arts")
            self.lbl5.place(x=20, y=200)

        elif self.var1.get() == 5 and self.var2.get() == 5:
            self.lbl1 = Label(self.Academic_Frame, text="Accountancy")
            self.lbl1.place(x=20, y=50)
            self.lbl2 = Label(self.Academic_Frame, text="Business Studies")
            self.lbl2.place(x=20, y=100)
            self.lbl3 = Label(self.Academic_Frame, text="Economics")
            self.lbl3.place(x=20, y=150)
            self.lbl5 = Label(self.Academic_Frame, text="Informatics Practices")
            self.lbl5.place(x=20, y=200)


if __name__ == '__main__':
    window = GUI()
    window.mainloop()
