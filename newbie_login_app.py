#import module
from tkinter import *
from tkinter import messagebox
import  ast

#Create Sign in window
main = Tk()
main.title('Login')
main.geometry('700x500+410+150')
main.configure(bg='white')
main.resizable(1, 1)

#create signin read file module
def signin():
    username = user.get()
    password = code.get()
    file = open('datasheet.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()
    if username in r.keys() and password == r[username]:
        new_window = Toplevel(main)
        new_window.title('finish')
        new_window.geometry('700x500+410+150')
        new_window.config(bg='white')
        text = Label(new_window, text='finish', bg='white', font=('Angsana New',69,'bold'))
        text.pack(expand=True)
        new_window.mainloop()
    else:
        messagebox.showerror('Invalid', 'invalid username or password')


#####################################################Sign up window#####################################################
#Run Sign up window module
def signup_command():
    main2 = Toplevel(main)
    main2.title('SignUp')
    main2.geometry('700x500+410+150')
    main2.configure(bg='white')
    main2.resizable(0, 0)

    # Create signup write file module
    def signup():
        username = user.get()
        password = code.get()
        confirm_password = confirm_code.get()
        if password == confirm_password:
            try:
                file = open('datasheet.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)
                dict2 = {username: password}
                r.update(dict2)
                file.truncate()
                file.close()
                file = open('datasheet.txt', 'w')
                w = file.write(str(r))
                messagebox.showinfo('Signup', 'Sucessfully sign up')
                main2.destroy()
            except:
                file = open('datasheet.txt', 'w')
                x = str({'Username': 'password'})
                file.write(x)
                file.close()
        else:
            messagebox.showerror('Invalid', 'Something went wrong !, Please check again')
    def sign():
        main2.destroy()

    #create frame
    frame = Frame(main2, width=350, height=390, bg='white')
    frame.pack(expand=YES)

    #Create Sign up heading label
    heading = Label(frame, text='Sign up', fg='#FFCC00', bg='white', font=('Microsft YaHei UI Light',28,'bold'))
    heading.place(x=100, y=1)

    #---------------------------------------- username input ----------------------------------------#

    def on_enter(event):
        user.delete(0, 'end')


    def on_leave(event):
        if user.get() == '':
            user.insert(0, 'Username')


    user = Entry(frame, width=25, border=0, fg='black', bg='white', font=('Microsoft Yahei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)


    frame_user = Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    #---------------------------------------- password input ----------------------------------------#

    def on_enter(event):
        code.delete(0, 'end')


    def on_leave(event):
        if code.get() == '':
            code.insert(0, 'Password')


    code = Entry(frame, width=25, border=0, fg='black', bg='white', font=('Microsoft Yahei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)


    frame_password = Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    #---------------------------------------- confirm_password input ----------------------------------------#

    def on_enter(event):
        confirm_code.delete(0, 'end')

    def on_leave(event):
        if confirm_code.get() == '':
            confirm_code.insert(0, 'Password')

    confirm_code = Entry(frame, width=25, border=0, fg='black', bg='white', font=('Microsoft Yahei UI Light', 11))
    confirm_code.place(x=30, y=220)
    confirm_code.insert(0, 'Confirm Password')
    confirm_code.bind('<FocusIn>', on_enter)
    confirm_code.bind('<FocusOut>', on_leave)


    frame_confirm_password = Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)
    # ---------------------------------------------------------------------------------------------------------

    #Create Sign up button
    Button(frame, width=39, pady=7, text='Sign up', bg='#FFCC00', fg='white', border=0, command=signup).place(x=35,y=280)
    signup_button_label = Label(frame, text='Already have an account?', fg='black', bg='white', font=('Microsoft Yahei UI Light', 9))
    signup_button_label.place(x=60, y=340)

    #Create Sign in button
    signin = Button(frame, width=6, border=0, text='Sign in', bg='white', cursor='hand2', fg='#FFCC00', command=sign)
    signin.place(x=210, y=340)


    main2.mainloop()

########################################################################################################################

# create frame
frame = Frame(main, width=350, height=350, bg='white')
frame.pack(expand=YES)

# create Sign In heading
heading = Label(frame, text='Sign In', fg='#FFCC00', bg='white', font=('Microsft YaHei UI Light', 28, 'bold'))
heading.place(x=110, y=1)

#---------------------------------- username input ----------------------------------#

def on_enter(event):
    user.delete(0, 'end')

def on_leave(event):
    if user.get() == '':
        user.insert(0, 'Username')


user = Entry(frame, width=25, border=0, bg='white', font=('Microsft YaHei UI Light',11))
user.place(x=30, y=80)
user.insert(0,'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
frame_user = Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

#---------------------------------- password input ----------------------------------#

def on_enter(event):
    code.delete(0,'end')


def on_leave(event):
    if code.get() == '':
        code.insert(0,'Password')


code = Entry(frame, width=25, border=0, bg='white', font=('Microsft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)


frame_password = Frame(frame,width=295, height=2, bg='black').place(x=25, y=177)

#Sign in button
Button(frame,width=39, border=0, pady=7, text='Sign in', fg='white', bg='#FFCC00', command=signin).place(x=35, y=204)
signin_button_label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsft YaHei UI Light', 9))
signin_button_label.place(x=75, y=270)

#Sign up button
sign_up =Button(frame, width=6, border=0, text='Sign up', bg='white', cursor='hand2', fg='#FFCC00', command=signup_command)
sign_up.place(x=215, y=270)

#run program
main.mainloop()