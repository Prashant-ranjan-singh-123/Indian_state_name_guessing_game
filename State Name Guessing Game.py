from tkinter import *
from tkinter import messagebox as mess
from PIL import ImageTk, Image
import webbrowser
import os


class Game:
    def search_button_command(self):
        if self.right_guesses_number == 27:
            self.search_button.config(state=DISABLED)
            self.search_button_disabled = True
            self.show_all_button.config(state=DISABLED)
            mess.showinfo(title='Congrats', message='Congrats you win you answered all state name.')
        else:
            if not self.search_button_disabled:
                user_input = self.Entry_area.get().lower()
                ok_append_to_ans_list = False
                if user_input in self.state_list:
                    if user_input in self.answered_state:
                        mess.showwarning(title='Same Input', message=f'You Guessed {user_input} already :)')
                        self.Entry_area.delete(0, END)
                    else:
                        self.Entry_area.delete(0, END)
                        if user_input == 'rajasthan':
                            ok_append_to_ans_list = True
                            self.rajasthan_text = self.canvas.itemconfig(self.rajasthan_text, text='Rajasthan')

                        elif user_input == 'uttar pradesh':
                            ok_append_to_ans_list = True
                            self.uttar_pradesh_text = self.canvas.itemconfig(self.uttar_pradesh_text, text='Uttar pradesh')

                        elif user_input == 'punjab':
                            ok_append_to_ans_list = True
                            self.punjab_text = self.canvas.itemconfig(self.punjab_text, text='Punjab')

                        elif user_input == 'himachal pradesh':
                            ok_append_to_ans_list = True
                            self.himachal_pradesh_text = self.canvas.itemconfig(self.himachal_pradesh_text,
                                                                                text='Himachal Pradesh')

                        elif user_input == 'kerala':
                            ok_append_to_ans_list = True
                            self.kerala_text = self.canvas.itemconfig(self.kerala_text, text='Kerala')

                        elif user_input == 'goa':
                            ok_append_to_ans_list = True
                            self.goa_text = self.canvas.itemconfig(self.goa_text, text='Goa')

                        elif user_input == 'meghalaya':
                            ok_append_to_ans_list = True
                            self.meghalaya_text = self.canvas.itemconfig(self.meghalaya_text, text='Meghalaya')

                        elif user_input == 'manipur':
                            ok_append_to_ans_list = True
                            self.manipur_text = self.canvas.itemconfig(self.manipur_text, text='Manipur')

                        elif user_input == 'haryana':
                            ok_append_to_ans_list = True
                            self.haryana_text = self.canvas.itemconfig(self.haryana_text, text='Haryana')

                        elif user_input == 'uttarakhand':
                            ok_append_to_ans_list = True
                            self.uttara_khand_text = self.canvas.itemconfig(self.uttara_khand_text, text='Uttarakhand')

                        elif user_input == 'madhya pradesh':
                            ok_append_to_ans_list = True
                            self.madhya_pradesh_text = self.canvas.itemconfig(self.madhya_pradesh_text, text='Madhya Pradesh')

                        elif user_input == 'gujarat':
                            ok_append_to_ans_list = True
                            self.gujarat_text = self.canvas.itemconfig(self.gujarat_text, text='Gujarat')

                        elif user_input == 'maharashtra':
                            ok_append_to_ans_list = True
                            self.maharashtra_text = self.canvas.itemconfig(self.maharashtra_text, text='Maharashtra')

                        elif user_input == 'chhattisgarh':
                            ok_append_to_ans_list = True
                            self.chattishgarh_text = self.canvas.itemconfig(self.chattishgarh_text, text='Chhattisgarh')

                        elif user_input == 'bihar':
                            ok_append_to_ans_list = True
                            self.bihar_text = self.canvas.itemconfig(self.bihar_text, text='Bihar')

                        elif user_input == 'jharkhand':
                            ok_append_to_ans_list = True
                            self.jharkhand_text = self.canvas.itemconfig(self.jharkhand_text, text='Jharkhand')

                        elif user_input == 'west bengal':
                            ok_append_to_ans_list = True
                            self.west_bengal_text = self.canvas.itemconfig(self.west_bengal_text, text='West Bengal')

                        elif user_input == 'orissa' or user_input == 'odisha':
                            ok_append_to_ans_list = True
                            self.orissa_text = self.canvas.itemconfig(self.orissa_text, text='Orissa')

                        elif user_input == 'telangana' or user_input == 'andhra pradesh':
                            ok_append_to_ans_list = True
                            self.telangana_andhra_pradesh_text = self.canvas.itemconfig(self.telangana_andhra_pradesh_text,
                                                                                        text='1) Telangana\n\n\n2) Andhra Pradesh')
                            self.answered_state.append('andhra pradesh')
                            self.answered_state.append('telangana')
                            self.right_guesses_number += 1

                        elif user_input == 'karnataka':
                            ok_append_to_ans_list = True
                            self.karnataka_text = self.canvas.itemconfig(self.karnataka_text, text='Karnataka')

                        elif user_input == 'tamil nadu':
                            ok_append_to_ans_list = True
                            self.tamil_Nadu_text = self.canvas.itemconfig(self.tamil_Nadu_text, text='Tamil Nadu')

                        elif user_input == 'sikkim':
                            ok_append_to_ans_list = True
                            self.sikkim_text = self.canvas.itemconfig(self.sikkim_text, text='Sikkim')

                        elif user_input == 'assam':
                            ok_append_to_ans_list = True
                            self.assam_text = self.canvas.itemconfig(self.assam_text, text='Assam')

                        elif user_input == 'arunachal pradesh':
                            ok_append_to_ans_list = True
                            self.arunachal_pradesh_text = self.canvas.itemconfig(
                                self.arunachal_pradesh_text,
                                text='Arunachal Pradesh')

                        elif user_input == 'nagaland':
                            ok_append_to_ans_list = True
                            self.nagaland_text = self.canvas.itemconfig(self.nagaland_text, text='Nagaland')

                        elif user_input == 'mizoram':
                            ok_append_to_ans_list = True
                            self.mizoram_text = self.canvas.itemconfig(self.mizoram_text, text='Mizoram')

                        elif user_input == 'tripura':
                            ok_append_to_ans_list = True
                            self.tripura_text = self.canvas.itemconfig(self.tripura_text, text='Tripura')

                        else:
                            mess.showinfo(
                                title='Union Territory',
                                message=f'{user_input} is a Union Territory, not a state :)'
                            )

                        if ok_append_to_ans_list:
                            self.answered_state.append(user_input)
                            self.right_guesses_number += 1
                            self.canvas.itemconfig(self.score_board_label, text=f'{self.right_guesses_number}/28')
                        self.Entry_area.delete(0, END)

                    # mess.showinfo(title='Correct Input', message=f'Congrats {user_input} state exists.')
                else:
                    if user_input.startswith(' ') or len(user_input) == 0:
                        mess.showerror(title='Null Value', message='You Haven\'t type any name, please type one. :)')
                    else:
                        mess.showinfo(title='Incorrect Input', message=f'{user_input} state name does not exist.')
                        self.Entry_area.delete(0, END)

    def show_all_button_command(self):
        ask = mess.askokcancel(title='Confirmation', message='Are you sure you want to see all state names?')
        if ask:
            self.rajasthan_text = self.canvas.itemconfig(self.rajasthan_text, text='Rajasthan')
            self.uttar_pradesh_text = self.canvas.itemconfig(self.uttar_pradesh_text, text='Uttar pradesh')
            self.punjab_text = self.canvas.itemconfig(self.punjab_text, text='Punjab')

            self.himachal_pradesh_text = self.canvas.itemconfig(self.himachal_pradesh_text,
                                                                text='Himachal Pradesh')
            self.kerala_text = self.canvas.itemconfig(self.kerala_text, text='Kerala')
            self.goa_text = self.canvas.itemconfig(self.goa_text, text='Goa')
            self.meghalaya_text = self.canvas.itemconfig(self.meghalaya_text, text='Meghalaya')
            self.manipur_text = self.canvas.itemconfig(self.manipur_text, text='Manipur')
            self.haryana_text = self.canvas.itemconfig(self.haryana_text, text='Haryana')
            self.uttara_khand_text = self.canvas.itemconfig(self.uttara_khand_text, text='Uttarakhand')
            self.madhya_pradesh_text = self.canvas.itemconfig(self.madhya_pradesh_text, text='Madhya Pradesh')
            self.gujarat_text = self.canvas.itemconfig(self.gujarat_text, text='Gujarat')
            self.maharashtra_text = self.canvas.itemconfig(self.maharashtra_text, text='Maharashtra')
            self.chattishgarh_text = self.canvas.itemconfig(self.chattishgarh_text, text='Chhattisgarh')
            self.bihar_text = self.canvas.itemconfig(self.bihar_text, text='Bihar')
            self.jharkhand_text = self.canvas.itemconfig(self.jharkhand_text, text='Jharkhand')
            self.west_bengal_text = self.canvas.itemconfig(self.west_bengal_text, text='West Bengal')
            self.orissa_text = self.canvas.itemconfig(self.orissa_text, text='Orissa')
            self.telangana_andhra_pradesh_text = self.canvas.itemconfig(self.telangana_andhra_pradesh_text,
                                                                        text='1) Telangana\n\n\n2) Andhra Pradesh')
            self.karnataka_text = self.canvas.itemconfig(self.karnataka_text, text='Karnataka')
            self.tamil_Nadu_text = self.canvas.itemconfig(self.tamil_Nadu_text, text='Tamil Nadu')
            self.sikkim_text = self.canvas.itemconfig(self.sikkim_text, text='Sikkim')
            self.assam_text = self.canvas.itemconfig(self.assam_text, text='Assam')
            self.arunachal_pradesh_text = self.canvas.itemconfig(
                self.arunachal_pradesh_text,
                text='Arunachal Pradesh')
            self.nagaland_text = self.canvas.itemconfig(self.nagaland_text, text='Nagaland')
            self.mizoram_text = self.canvas.itemconfig(self.mizoram_text, text='Mizoram')
            self.tripura_text = self.canvas.itemconfig(self.tripura_text, text='Tripura')

            self.search_button.config(state=DISABLED)
            self.search_button_disabled = True
            self.show_all_button.config(state=DISABLED)
            self.Entry_area.config(state=DISABLED)

    def try_again_button_command(self):
        ask = mess.askyesno(title='Confirmation', message='Your Score will be reset.\nAre you sure?')
        if ask:
            self.window.destroy()
            Game()

    def developer_button_command(self):
        top = Toplevel()
        background = 'white'
        top.geometry('600x620')
        top.minsize(600, 620)
        top.maxsize(600, 620)
        top.title('State Name Guessing Game By Prashant Ranjan Singh')
        top.config(bg=background, padx=50, pady=50)
        top.resizable(False, False)
        self.run_next_program = False

        self.programmer_description_string = \
'''    (#) This Program is made on
    22, july 2022 by Prashant 
    Ranjan Singh.
    
    
    (#) It is an State name guessing 
    game (Union Territory Warning) 
    
    
    (#) Linkedin Profile of mine :-'''
        self.working_of_program_explain_str = '''Now a days we cant remember all state names and union territories, 
so by playing this game we can memorize state name as well as in
which part of india it is in.       

This game is designed in such a way that no programming skills
are required but if there is any problem contact me (Linkdin).

        \t\t\t     Shortcuts are :-

1) Enter --> For searching.                       3) Ctrl+r --> For Try Again.

2) Ctrl+Enter --> For Show All.                4) Ctrl+h --> For Developer Button.
'''

        # image
        self.password_image = ImageTk.PhotoImage(Image.open("Program Images/Mine_photo.jpg"))
        self.image = Label(top, width=250, height=250, image=self.password_image, borderwidth=0)

        # Label
        self.text = Label(top)
        self.about_programmer = Label(top, text='About Programmer', font=('LatinModernRomanDunhill', 12, 'bold'),
                                      background=background)
        self.text.configure(text=self.programmer_description_string, bg='white', justify=LEFT)
        self.link = Label(top, text="www.linkedin.com", fg="blue", cursor="hand2", bg=background)
        self.link.bind("<Button-1>", lambda a: webbrowser.open_new_tab(url="www.linkedin.com/in/prashant-ranjan-singh-b9b6b9217"))
        self.working_heading = Label(top, text='Working of Program', font=('LatinModernRomanDunhill', 12, 'bold'),
                                     bg=background)
        self.working_of_program_explain = Label(top, text=self.working_of_program_explain_str, bg='white', justify=LEFT)

        # Create a Label to display the link
        self.image.grid(column=0, row=0)
        self.about_programmer.grid(column=1, row=0, sticky=NE, padx=70)
        self.text.grid(column=1, row=0, sticky=NW, pady=50, padx=10)
        self.link.grid(column=1, row=0, sticky=SW, padx=35, pady=30)
        self.working_heading.grid(column=0, row=1, padx=50, columnspan=2, pady=5)
        self.working_of_program_explain.grid(column=0, row=2, columnspan=3, sticky=W)
        top.mainloop()

    def callback(url):
        webbrowser.open_new_tab(url)

    def __init__(self):
        self.state_list = [
            "rajasthan", "uttar pradesh", "punjab", "himachal pradesh", "kerala", "goa", "meghalaya", "manipur",
            "jammu and kashmir", "jammu", "kashmir", "haryana", "uttarakhand", "madhya pradesh", "gujarat",
            "maharashtra", "chhattisgarh", "bihar", "jharkhand", "west bengal", "orissa", "telangana", "andhra pradesh",
            "karnataka", "tamil nadu", "sikkim", "assam", "arunachal pradesh", "nagaland", "mizoram", "tripura",
            "odisha",
            # Union Territories
            "delhi", "puducherry", "ladakh", "chandigarh", "daman", "diu", "Daman and diu", "dadra", "nagar haveli",
            "dadra and nagar haveli", "lakshadweep", "andaman", "nicobar", "andaman and nicobar", "nicobar islands",
            "andaman and nicobar islands"
        ]
        self.answered_state = []
        self.right_guesses_number = 0
        self.search_button_disabled = False

        self.window = Tk()
        self.window.title('State Name Game By Prashant Singh')
        self.window.geometry("800x600")
        self.window.configure(bg="#ebebeb")

        self.canvas = Canvas(
            self.window,
            bg="#ebebeb",
            height=600,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"Program Images/background.png")
        self.canvas.create_image(
            400.5, 300.0,
            image=background_img)

        entry0_img = PhotoImage(file=f"Program Images/img_textBox0.png")
        self.canvas.create_image(
            655.0, 450.0,
            image=entry0_img)

        self.Entry_area = Entry(
            bd=0,
            bg="#ec7a00",
            disabledbackground="#ec7a00",
            font=('progenisis', 18, 'bold'),
            highlightthickness=0)
        self.Entry_area.focus()

        self.Entry_area.place(
            x=548.0, y=438,
            width=214.0,
            height=25)

        img0 = PhotoImage(file=f"Program Images/img0.png")
        self.search_button = Button(
            image=img0,
            borderwidth=0,
            background='#ebebeb',
            highlightthickness=0,
            command=lambda: self.search_button_command(),
            relief="flat")

        self.search_button.place(
            x=698, y=498,
            width=80,
            height=33)

        img1 = PhotoImage(file=f"Program Images/img1.png")
        self.show_all_button = Button(
            image=img1,
            borderwidth=0,
            background='#ebebeb',
            highlightthickness=0,
            command=lambda: self.show_all_button_command(),
            relief="flat")

        self.show_all_button.place(
            x = 537, y = 498,
            width = 80,
            height = 33)

        img3 = PhotoImage(file=f"Program Images/img3.png")
        self.developer_button = Button(
            image=img3,
            borderwidth=0,
            background='#ebebeb',
            command=lambda: self.developer_button_command(),
            highlightthickness=0,
            relief="flat")

        self.developer_button.place(
            x=537, y=552,
            width=80,
            height=33)

        img2 = PhotoImage(file=f"Program Images/img2.png")
        self.try_again_button = Button(
            image=img2,
            borderwidth=0,
            background='#ebebeb',
            command=lambda: self.try_again_button_command(),
            highlightthickness=0,
            relief="flat")

        self.try_again_button.place(
            x=698, y=552,
            width=78,
            height=33)

        self.score_board_label = self.canvas.create_text(
            392.0, 484.0,
            text="0/28",
            fill="#000000",
            font=("Arial-BoldMT", int(20.0), 'bold'))

        self.canvas.create_text(
            392.0, 448.0,
            text="Score Board",
            fill="#000000",
            font=("ArialMT", int(14.0), 'bold'))

        self.rajasthan_text = self.canvas.create_text(
            106.0, 223.0,
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.uttar_pradesh_text = self.canvas.create_text(
            225.0, 216.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.punjab_text = self.canvas.create_text(
            137.0, 157.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.himachal_pradesh_text = self.canvas.create_text(
            168.0, 133.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.kerala_text = self.canvas.create_text(
            146.0, 517.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.goa_text = self.canvas.create_text(
            94.0, 432.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.meghalaya_text = self.canvas.create_text(
            393.0, 241.0,
            text="",
            activefill='white',
            fill="#000000",
            font=("Jomhuria-Regular", int(7.0)))

        self.manipur_text = self.canvas.create_text(
            444.0, 253.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.jammu_and_kashmir_text = self.canvas.create_text(
            157.0, 85.0,
            text="Jammu \nKashmir",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.haryana_text = self.canvas.create_text(
            154.0, 181.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.uttara_khand_text = self.canvas.create_text(
            221.0, 164.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.madhya_pradesh_text = self.canvas.create_text(
            185.0, 289.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.gujarat_text = self.canvas.create_text(
            79.0, 296.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.maharashtra_text = self.canvas.create_text(
            134.0, 352.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.chattishgarh_text = self.canvas.create_text(
            250.0, 310.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(7.0)))

        self.bihar_text = self.canvas.create_text(
            308.0, 243.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.jharkhand_text = self.canvas.create_text(
            296.0, 277.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(7.0)))

        self.west_bengal_text = self.canvas.create_text(
            333.0, 286.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(7.0)))

        self.orissa_text = self.canvas.create_text(
            293.0, 324.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.telangana_andhra_pradesh_text = self.canvas.create_text(
            215.0, 417.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(7.0)))

        self.karnataka_text = self.canvas.create_text(
            137.0, 439.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.tamil_Nadu_text = self.canvas.create_text(
            188.0, 505.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(7.0)))

        self.sikkim_text = self.canvas.create_text(
            344.0, 184.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.assam_text = self.canvas.create_text(
            407.0, 221.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.arunachal_pradesh_text = self.canvas.create_text(
            444.0, 156.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.nagaland_text = self.canvas.create_text(
            477.0, 223.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.mizoram_text = self.canvas.create_text(
            444.0, 300.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.tripura_text = self.canvas.create_text(
            387.0, 280.0,
            text="",
            fill="#000000",
            font=("Jomhuria-Regular", int(9.0)))

        self.window.bind('<Return>', lambda i: self.search_button_command())
        self.window.bind('<Control-r>', lambda i: self.try_again_button_command())
        self.window.bind('<Control-h>', lambda i: self.developer_button_command())
        self.window.bind('<Control-Return>', lambda i: self.show_all_button_command())
        # self.window.bind('<Tab>', lambda i: self.Entry_area.insert(END, " "))
        self.window.resizable(False, False)
        self.window.mainloop()


class Errors:
    def __init__(self):
        self.background = None
        self.error = None
        self.what_to_do = None
        self.link = None
        self.L1 = None

    def file_missing(cls,
                     url='https://github.com/Prashant-ranjan-singh-123/Indian_state_name_guessing_game',
                     show_name_of_url='www.github.com'):
        def callback(url_is):
            webbrowser.open_new_tab(url_is)

        root = Tk()
        cls.background = 'white'
        root.geometry('500x310')
        root.resizable(False, False)
        root.title('State name guessing Game by Prashant Singh')
        root.config(background=cls.background, borderwidth=30)

        def exit_command():
            nonlocal root
            root.destroy()

        # Heading Label
        cls.L1 = Label(root, text='Prashant\'s State Guessing Game', font='LatinModernRomanDunhill 20 bold',
                       background=cls.background)
        cls.L1.pack(anchor='center')

        # Label
        cls.error = Label(root, text='Error', foreground='red', font='arial 30 bold', justify=CENTER,
                          background=cls.background)
        cls.error.pack(anchor='center', pady=20)

        cls.what_to_do = Label(root, text=f'You wont have essential component\'s for proper \n'
                                          f'execution of program please download it from \n'
                                          f'official github repository from below link :-',
                               font=('arial', 12, 'bold'), justify=CENTER, bg=cls.background)
        cls.what_to_do.pack()

        cls.link = Label(text=show_name_of_url, fg="blue", cursor="hand2", bg=cls.background,
                         font=('arial', 12, 'bold'))
        cls.link.bind("<Button-1>", lambda e: callback(url))
        cls.link.pack(anchor='center')

        # Button
        exit_button = Button(text='Previous Menu', bg='#ff4d4d', padx=40, borderwidth=2, highlightbackground='black',
                             activebackground='#ff0000', command=exit_command)
        exit_button.place(x=480, y=300)
        root.mainloop()

if __name__ == '__main__':
    if os.path.exists('Program Images') and \
            os.path.exists('Program Images/background.png') and \
            os.path.exists('Program Images/img_textBox0.png') and \
            os.path.exists('Program Images/img0.png') and \
            os.path.exists('Program Images/img1.png') and \
            os.path.exists('Program Images/img2.png') and \
            os.path.exists('Program Images/img3.png') and \
            os.path.exists('Program Images/Mine_photo.jpg'):
            Game()

    else:
        Errors().file_missing()
