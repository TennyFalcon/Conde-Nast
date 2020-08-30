from tkinter import *
from tkinter import filedialog

def CenterWindow(w,h):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    return w,h,x,y

def Output_browse_button():
    dirname = filedialog.askdirectory()
    entry_2.delete(0, END)
    entry_2.insert(0, dirname)

def Input_browse_button():
    input_file_name = filedialog.askopenfilename(initialdir="/", title="Select file")
    entry_1.delete(0, END)
    entry_1.insert(0, input_file_name)

def Run():
    val_completed_label = Label(root,text="%VALIDATION COMPLETED%",fg='lawn green',font=("Times New Roman",50))
    val_completed_label.place(x=30,y=475)
    input_file = entry_1.get()
    print(input_file)


root = Tk()
root.geometry('%dx%d+%d+%d' % (CenterWindow(800,650)))
root.title("Conde Nast")

etl_label = Label(root, text="~~~~~ETL VALIDATIONS~~~~~",font=("Times New Roman", 50))
etl_label.place(x=40,y=50)

label_1 = Label(root, text="SQL Query File",font=("bold", 20))
label_1.place(x=140,y=180)

label_2 = Label(root, text="Output Filepath",font=("bold", 20))
label_2.place(x=140,y=230)

entry_1 = Entry(root,width=21,font=("bold",18))
entry_1.place(x=300,y=180)

entry_2 = Entry(root,width=21,font=("bold",18))
entry_2.place(x=300,y=230)

i_browse_button = Button(root,text='Browse',font=("bold"),command=Input_browse_button,state=ACTIVE)
i_browse_button.place(x=570,y=190)

o_browse_button = Button(root,text='Browse',font=("bold"),command=Output_browse_button,state=ACTIVE)
o_browse_button.place(x=570,y=238)

validate_button = Button(root,text= 'Run',width=15,height=5,font=("bold", 15),command=Run)
validate_button.place(x=400,y=300)

quit_button = Button(root,text= 'Exit',width=15,height=5,font=("bold", 15),command=root.quit)
quit_button.place(x=200,y=300)

root.mainloop()