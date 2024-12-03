'''
    Application File - To generate UI to intercat with users. It is integrated with the Bert model.

    Creating the UI for the DBS chatbot using the Tkinter (Tk interface). 
    It is a standard Python GUI (Graphical User Interface) library that provides a set of tools and widgets 
    to create desktop applications with graphical interfaces. 
    
    
    Created by: Sandeep Kumar
    Student ID: 20049275
    University: DBS
    Module Title: Programming for Data Analysis Project
    Lecturer: Alexander Victor

'''
from tkinter import *
from Research_chatbot_6 import provide_res_to_ui


# Declaring the font color and font of the text
FONT_COL = "#4E342E"
FONT = "Poppins 14"
FONT_BOLD = "Poppins 13 bold"

# Declaring the Footer background color and the main chat window color giving it a warm look
FOOTER_BG_COL = "#ABB2B9"
BODY_BG_COL = "#F7F1E3"

# Calling the bot as DBS Bot
DBS_BOT_NAME = "DBS Bot"

'''
 Defining a class DBS application. 
 It has a constructor which is called whenever a new instance of the class is instantiated. 
 Constructor creates main application window using TK. In this window widgets or other components can be added.
 Thus it will act as a container for other objects. 
 
 function run(self) executes the main functionality of the class. In this case it is main event loopof GUI app. 
 It listens for user actions, events like clicks, text inputs etc. 

    _setup_main_window function is called from constructor. It performs following execution
    setting up of the title. 
    configuring the parameters like making it non resizable so that user cannot change its size.
    configuring its height and width. 
    creation of label widget for welocome message for DBS chatbot. 
    creation of a horizontal line with the help of label widget by limiting its width to 1
    creation of a text widget, configuring its parameters like color and font, width and height. 
    Width paremeter represents the lenght of the sentence before it can be wrapped. 
    cursor="arrow" means how the cursor will look on the chat main window.
    creation of a scrollbar widget. It is placed in the text widget. 
    footer label for grey area of the chat window.
    creation of text entry field. entry widget is binded 
    with _on_enter_pressed event so that if user provides any input text and enter is pressed
    _on_enter_pressed will fire and exetutes its code. 
    creation of send button widget. 
    Its command parameter can be used to specify function (here it is _on_enter_pressed) to be attached to when it is clicked. 

'''
class DBSChatApplication:    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("DBS Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=450, height=500, bg=BODY_BG_COL)

        label_welcome = Label(self.window, bg=BODY_BG_COL, fg = FONT_COL, text="Hi there! Welcome to DBS’s virtual assistant.", font=FONT_BOLD, pady=10)
        label_welcome.place(relwidth=1)

        label_line = Label(self.window, width=430, bg = FOOTER_BG_COL)
        label_line.place(width=2, rely=0.08, relheight=0.014)

        self.text_dbs_widget = Text(self.window, width=18, height=2, bg = BODY_BG_COL, fg=FONT_COL, font=FONT, padx=5, pady=5)
        self.text_dbs_widget.place(relheight=0.746, relwidth=1, rely=0.07)
        self.text_dbs_widget.configure(cursor="arrow", state=DISABLED)

        scrollbar =Scrollbar(self.text_dbs_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_dbs_widget.yview)

        label_footer = Label(self.window, bg=FOOTER_BG_COL, height=80)
        label_footer.place(relwidth=1,rely=0.825)

        self.entry_text = Entry(label_footer, bg=BODY_BG_COL, fg=FONT_COL, font=FONT)
        self.entry_text.place(relwidth=0.72, relheight=0.05, rely=0.007, relx=0.010)
        self.entry_text.focus()
        self.entry_text.bind("<Return>",self._on_enter_pressed)

        button_send = Button(label_footer, text="Send", font=FONT_BOLD, width=20, bg=FOOTER_BG_COL, 
                             command=lambda:self._on_enter_pressed(None))
        button_send.place(relx=0.76, rely=0.007, relheight=0.05, relwidth=0.22)


    '''
        method _on_enter_pressed is defined to get the input text (from entry_text) 
        and passes on to another method _insert_message
    '''
    def _on_enter_pressed(self, event):
        msg = self.entry_text.get()
        self._insert_message(msg,"You")
    '''
        method _insert_message takes the message as an input parameter and insert it into the text_dbs_widget
        for that it has to first enable it and then disable it back. 
        
        it also calls the provide_res_to_ui function of the Research_chatbot_6.py file to fetch the response from the 
        pretrained model. The returned message is appended with bot name and inserted into the text_dbs_widget. 
        see(END) function makes sure that we are always at the end of conversation. 
    '''
    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.entry_text.delete(0,END)
        msg1 = f"{sender}:{msg}\n\n"
        self.text_dbs_widget.configure(state=NORMAL)
        self.text_dbs_widget.insert(END,msg1)
        self.text_dbs_widget.configure(state=DISABLED)

        msg2 = f"{DBS_BOT_NAME}:{provide_res_to_ui(msg)}\n\n"
        self.text_dbs_widget.configure(state=NORMAL)
        self.text_dbs_widget.insert(END,msg2)
        self.text_dbs_widget.configure(state=DISABLED)        

        self.text_dbs_widget.see(END)

#app execution code. 
if __name__ == "__main__":
    app = DBSChatApplication()
    app.run()
