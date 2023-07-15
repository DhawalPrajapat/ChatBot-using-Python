from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow


class ChatBots:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        #window size - (widthxheigth)
        self.root.geometry("740x620+0+0")
        #for click send button by keyboard enter
        self.root.bind('<Return>',self.enter_fun)

    
        main_frame = Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()

        #logo image
        img_chat=Image.open('logo.png')
        img_chat=img_chat.resize((100,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        #heading
        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text="CHAT WITH ME",font=('arial',30,'bold'),fg='lightblue',bg='white')
        Title_label.pack(side=TOP)

        #scroll bar
        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.scroll_y.pack(side=RIGHT,fill=Y)

        #Text box
        self.text=Text(main_frame,width=65,height=20,bd=4,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.text.pack()


        #button frame
        btn_frame = Frame(self.root,bd=4,bg="white",width=730)
        btn_frame.pack()

        #label
        lbl = Label(btn_frame,text="Type Something",font=('arial',14,'bold'),fg='lightblue',bg='white')
        lbl.grid(row=0,column=0,padx=5,sticky=W)

        #entry box
        self.entry= StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        #send button
        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('arial',14,'bold'),width=8,bg='lightblue')
        self.send.grid(row=0,column=2,padx=5,sticky=W)


        #Clear button
        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',14,'bold'),width=8,bg='red',fg='white')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        #label2
        self.msg=''
        self.lbl2 = Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
        self.lbl2.grid(row=1,column=1,padx=5,sticky=W)

   
    # \\\\\\\\\\\\\\\\\\\\\\\\\\\Function Declaration//////////////////////////////

    #function create for click send button by keyboard enter
    def enter_fun(self,event):
        self.send.invoke() #invoke function is use for enter
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')

    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,"\n"+send)
        self.text.yview(END)

        if(self.entry.get()==''):
            self.msg="Please enter something"
            self.lbl2.config(text=self.msg,fg='red')

        else:
            self.msg=''
            self.lbl2.config(text=self.msg,fg='red')

        if(self.entry.get()=='hello' or self.entry.get()=='Hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')
        
        elif(self.entry.get()=='hi' or self.entry.get()=='Hi'):
            self.text.insert(END,'\n\n'+'Bot: Hello')
        
        elif(self.entry.get()=='How are you?'):
            self.text.insert(END,'\n\n'+'Bot: Fine and You')

        elif(self.entry.get()=='Fantastic'):
            self.text.insert(END,'\n\n'+'Bot: Nice to hear you')

        elif(self.entry.get()=='Who created you?'):
            self.text.insert(END,'\n\n'+'Bot: Dhawal did using python')

        elif(self.entry.get()=='What is your name?'):
            self.text.insert(END,'\n\n'+'Bot: My name is era')

        elif(self.entry.get()=='bye' or self.entry.get()=='Bye'):
            self.text.insert(END,'\n\n'+'Bot: Thank you for chatting')

        elif(self.entry.get()=='Can you speak Gujarati'):
            self.text.insert(END,'\n\n'+'Bot: I am sill learning it...s')

        elif(self.entry.get()=='What is machine learning?'):
            self.text.insert(END,'\n\n'+'Bot: Machine learning is a branch of artificial intelligence (AI) \nand computer science which focuses on the use of data and \nalgorithms to imitate the way that humans learn, gradually \nimproving its accuracy.')

        elif(self.entry.get()=='How does face recognition work?'):
            self.text.insert(END,'\n\n'+'Bot: Face detection software detects faces by identifying facial \nfeatures in a photo or video using machine learning algorithms. It first \nlooks for an eye, and from there it identifies other facial features. It then \ncompares these features to training data to confirm it has detected a face.')

        elif(self.entry.get()=='How many countries use facial recognition?'):
            self.text.insert(END,'\n\n'+'Bot: Around 1 in 5 of the countries we looked at have FRT on some of \ntheir buses,with five of these countries already having widespread \nuse of the technology on this form of public transport. These countries are \nBrazil, China, Kazakhstan, Spain, and the United Arab Emirates.')

        elif(self.entry.get()=='How does facial recognition work step by step?'):
            self.text.insert(END,'\n\n'+'Bot: \nstep 1 - Detection. Detection is the process of finding a face in an image.\nstep 2 - Analysis.The facial recognition system then analyzes the \nimage of the face.\nstep 3 - Recognition.')

        elif(self.entry.get()=='What is python programming?'):
            self.text.insert(END,'\n\n'+"Bot: Python's simple, easy to learn syntax emphasizes readability and \ntherefore reduces the cost of program maintenance. Python supports \nmodules and packages, which encourages program modularity and \ncode reuse.The Python interpreter and the extensive standard library are \navailable in source or binary form without charge for all major platforms, \nand can be freely distributed.")
        elif(self.entry.get()=='What is chat bot?'):
            self.text.insert(END,'\n\n'+"Bot: A chatbot is a computer program that uses artificial intelligence \n(AI) and natural language processing (NLP) to understand customer \nquestions and automate responses to them, simulating human \nconversation.")
        else:
            self.text.insert(END,'\n\n'+"Bot: Sorry I didn't get it")



if __name__ == '__main__':
    #create tkinte window
    root= Tk()
    obj=ChatBots(root)
    #Execute Tkinter
    root.mainloop()