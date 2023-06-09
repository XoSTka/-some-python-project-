from tkinter import *
from tkinter import messagebox
import ast


class Login:
    def __init__(self, main, user_sign_in, pass_sign_in, user_sign_out, pass_sign_out, confirm_pass_sign_out):
        self.username_signin = user_sign_in
        self.password_signin = pass_sign_in
        self.username_sign_out = user_sign_out
        self.password_sign_out = pass_sign_out
        self.confirm_password_sign_out = confirm_pass_sign_out
        self.root = main
        self.root.geometry("700x500+410+150")
        self.root.configure(bg='white')
        self.root.resizable(0, 0)
        self.login_form()
        file = open('member.txt', 'w')
        pp = str("{}")
        file.write(pp)
        file.close()

    def login_form(self):
        self.root.title('Login')
        login_frame = Frame(self.root, width=350, height=350, bg='white')
        login_frame.place(x=180, y=85)

        signin_heading = Label(login_frame, text='Sign In', fg='#FFCC00', bg='white', font=('Helvetica', 28, 'bold'))
        signin_heading.place(x=110, y=5)

        def on_enter(event):
            self.username_signin.delete(0, 'end')

        def on_leave(event):
            name = self.username_signin.get()
            if name == '':
                self.username_signin.insert(0, 'Username')

        self.username_signin = Entry(login_frame, width=35, border=0, fg='black', bg='white', font=('Helvetica', 11))
        self.username_signin.place(x=30, y=80)
        self.username_signin.insert(0, 'Username')
        self.username_signin.bind('<FocusIn>', on_enter)
        self.username_signin.bind('<FocusOut>', on_leave)
        username_signin_frame = Frame(login_frame, width=295, height=2, bg='black')
        username_signin_frame.place(x=25, y=107)

        def on_enter(event):
            self.password_signin.delete(0, 'end')

        def on_leave(event):
            name = self.password_signin.get()
            if name == '':
                self.password_signin.insert(0, 'Password')

        self.password_signin = Entry(login_frame, width=35, border=0, fg='black', bg='white', font=('Helvetica', 11))
        self.password_signin.place(x=30, y=150)
        self.password_signin.insert(0, 'Password')
        self.password_signin.bind('<FocusIn>', on_enter)
        self.password_signin.bind('<FocusOut>', on_leave)
        password_signin_password = Frame(login_frame, width=295, height=2, bg='black')
        password_signin_password.place(x=25, y=177)

        signin_button = Button(login_frame, width=20, pady=7, border=0, text='Sign in', fg='white', bg='#FFCC00',
                               command=self.signin)
        signin_button.place(x=100, y=210)

        label = Label(login_frame, text="Don't have an account?", fg='black', bg='white', font=('Helvetica', 9))
        label.place(x=75, y=270)

        sign_up = Button(login_frame, text='Sign up', border=0, bg='white', cursor='hand2', fg='#FFCC00',
                         font=('Helvetica', 9, 'underline'), command=self.register_form)
        sign_up.place(x=215, y=270)

    def signin(self):
        username_signin_input = self.username_signin.get()
        password_signin_input = self.password_signin.get()

        file = open('member.txt', 'r')
        x = file.read()
        y = ast.literal_eval(x)
        file.close()
        if username_signin_input in y.keys() and password_signin_input == y[username_signin_input]:
            self.finish()
        else:
            messagebox.showerror('Invalid', 'Invalid Username or Password')

    def register_form(self):
        self.root.title("Register")
        sign_out_frame = Frame(self.root, width=350, height=390, bg='white')
        sign_out_frame.place(x=185, y=70)

        sign_out_heading = Label(sign_out_frame, text='Sign up', fg='#FFCC00', bg='white',
                                 font=('Helvetica', 28, 'bold'))
        sign_out_heading.place(x=100, y=5)

        def on_enter(event):
            self.username_sign_out.delete(0, 'end')

        def on_leave(event):
            if self.username_sign_out.get() == '':
                self.username_sign_out.insert(0, 'Username')

        self.username_sign_out = Entry(sign_out_frame, width=35, border=0, fg='black', bg='white',
                                       font=('Helvetica', 11))
        self.username_sign_out.place(x=30, y=80)
        self.username_sign_out.insert(0, 'Username')
        self.username_sign_out.bind('<FocusIn>', on_enter)
        self.username_sign_out.bind('<FocusOut>', on_leave)
        username_sign_out_frame = Frame(sign_out_frame, width=295, height=2, bg='black')
        username_sign_out_frame.place(x=25, y=107)

        def on_enter(event):
            self.password_sign_out.delete(0, 'end')

        def on_leave(event):
            if self.password_sign_out.get() == '':
                self.password_sign_out.insert(0, 'Password')

        self.password_sign_out = Entry(sign_out_frame, width=35, fg='black', border=0, bg='white',
                                       font=('Helvetica', 11))
        self.password_sign_out.place(x=30, y=150)
        self.password_sign_out.insert(0, 'Password')
        self.password_sign_out.bind('<FocusIn>', on_enter)
        self.password_sign_out.bind('<FocusOut>', on_leave)
        password_sign_out_frame = Frame(sign_out_frame, width=295, height=2, bg='black')
        password_sign_out_frame.place(x=25, y=177)

        def on_enter(event):
            self.confirm_password_sign_out.delete(0, 'end')

        def on_leave(event):
            if self.confirm_password_sign_out.get() == '':
                self.confirm_password_sign_out.insert(0, 'Confirm Password')

        self.confirm_password_sign_out = Entry(sign_out_frame, width=35, fg='black', border=0, bg='white',
                                               font=('Helvetica', 11))
        self.confirm_password_sign_out.place(x=30, y=220)
        self.confirm_password_sign_out.insert(0, 'Confirm Password')
        self.confirm_password_sign_out.bind('<FocusIn>', on_enter)
        self.confirm_password_sign_out.bind('<FocusOut>', on_leave)
        confirm_code_sign_out_frame = Frame(sign_out_frame, width=295, height=2, bg='black')
        confirm_code_sign_out_frame.place(x=25, y=247)

        signin_button = Button(sign_out_frame, width=20, pady=7, text='Sign up', bg='#FFCC00', fg='white', border=0,
                               command=self.signup)
        signin_button.place(x=100, y=280)

        have_account_label = Label(sign_out_frame, text='Already have an account?', fg='black', bg='white',
                                   font=('Helvetica', 9))
        have_account_label.place(x=70, y=340)

        signin = Button(sign_out_frame, text='Sign in', border=0, bg='white', cursor='hand2', fg='#FFCC00',
                        font=('Helvetica', 9, 'underline'), command=self.login_form)
        signin.place(x=225, y=340)

    def signup(self):
        username_signin = self.username_sign_out.get()
        password = self.password_sign_out.get()
        confirm_password = self.confirm_password_sign_out.get()
        if password == confirm_password:
            file = open('member.txt', 'r+')
            x = file.read()
            y = ast.literal_eval(x)
            dict2 = {username_signin: password}
            y.update(dict2)
            file.truncate()
            file.close()
            file = open('member.txt', 'w')
            file.write(str(y))
            messagebox.showinfo('Signup', 'Successfully sign up')
            self.login_form()
        else:
            messagebox.showerror('Invalid', 'Something wrong !')

    def finish(self):
        self.root.title('finish')
        f1 = Frame(self.root, width=700, height=500, bg='white')
        f1.place(x=0, y=0)
        label = Label(f1, text='finish', fg='black', bg='white', font=('Helvetica', 40, 'bold'))
        label.place(x=270, y=200)


window = Tk()
run = Login(window, pass_sign_in=YES, user_sign_in=YES, user_sign_out=YES, pass_sign_out=YES, confirm_pass_sign_out=YES)
window.mainloop()
