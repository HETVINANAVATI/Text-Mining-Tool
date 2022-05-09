from tkinter import *
from timeit import default_timer as timer
from nltk.tokenize import word_tokenize
import nltk
import string
i=0
stopwords = nltk.corpus.stopwords.words('english')
def removep(txt):
    text="".join([c for c in txt if c not in string.punctuation])
    return text
def clean(txt):
    word=[i for i in txt if i not in stopwords]
    return word
def stopwfree(input):
    word=clean(word_tokenize(removep(input).lower()))
    w=' '.join([str(elem) for elem in word])
    return w
def printInput():
    end1()
    inp=T.get(1.0, "end-1c")
    lbl.config(text ="Your word count is:"+str(detectw(inp)),font=("Arial", 15))
    lbl2.config(text ="Your line count is:"+str(detectl(inp)),font=("Arial", 15))
    lbl3.config(text ="Your count for alpha-numeric character is:"+str(detectalnum(inp)),font=("Arial", 15))
    lbl4.config(text ="Your count for numeric value is:"+str(detectnum(inp)),font=("Arial", 15))
    lbl5.config(text ="Your count for uppercase character is:"+str(detectupper(inp)),font=("Arial", 15))
    lbl6.config(text ="Your count for lowercase character is:"+str(detectlower(inp)),font=("Arial", 15))
    lbl7.config(text="Time taken : " +str(check())+" seconds",font=("Arial", 15))
    lbl8.config(text="Typing speed : " +str(speed(inp))+" words per minute",font=("Arial", 15))
    global i
    i=0
    lbl10.config(text="Your message after removing stop words and punctuations : "+str(stopwfree(inp)),font=("Arial", 15))
def typingSpeed():
     global start
     start = timer()
     global i
     i=1
def end1():
    global end
    end=timer()
def check():
    if i==0:
        return "Not Applicable"
    return end-start
def speed(string):
     if i==0:
         return "Not Applicable"
     return ((detectw(string)*60)/(end-start))
def detectw(string):
    count=0;
    p=word_tokenize(removep(string))
    l=len(p)
    return l
def detectl(string):
    count=0;
    l=len(string);
    for i in range (0,l):
        if(string[i]=="\n"or i==l-1):
            count+=1
    return(count)
def detectalnum(string):
    count=0;
    l=len(string);
    for i in range (0,l):
        if(string[i].isalnum()==True):
            count+=1
    return(count)   
def detectnum(string):
    count=0;
    l=len(string);
    for i in range (0,l):
        if(string[i].isnumeric()==True):
            count+=1;
    return(count)  
def detectupper(string):
    count=0;
    l=len(string);
    for i in range (0,l):
        if(string[i].isupper()==True):
            count+=1
    return(count)  
def detectlower(string):
    count=0;
    l=len(string);
    for i in range (0,l):
        if(string[i].islower()==True):
            count+=1
    return(count)  

m=Tk()
m.geometry('1500x900')
m.minsize(1500,900)
m.maxsize(1500,900)
m.title('Text Mining Tool')
m.config(bg="#ADD8E6")
lbl11 = Label(m, text = "Write your text here for mining!", font=("Arial", 25))
lbl11.config(bg="#ADD8E6")
lbl11.pack(pady=10)
lbl12 = Label(m, text = "If you want to calculate your typing speed:", font=("Arial", 25))
lbl12.config(bg="#ADD8E6")
lbl12.pack()
button1 = Button(m, text='Calculate typing speed', width=25,font=("Arial", 15),command=typingSpeed)
button1.config(bg="#FFB6C1")
button1.place(x=1060,y=80)
T = Text(m, height=15, width=110,font=("Arial", 15))
T.pack(pady=21)   
button = Button(m, text='Ask', width=25,font=("Arial", 15), command=printInput)
button.config(bg="#FFB6C1")
button.pack(pady=16)
lbl = Label(m, text = "")
lbl.config(bg="#ADD8E6")
lbl.pack()
lbl2 = Label(m, text = "")
lbl2.config(bg="#ADD8E6")
lbl2.pack()
lbl3 = Label(m, text = "")
lbl3.config(bg="#ADD8E6")
lbl3.pack()
lbl4 = Label(m, text = "")
lbl4.config(bg="#ADD8E6")
lbl4.pack()
lbl5 = Label(m, text = "")
lbl5.config(bg="#ADD8E6")
lbl5.pack()
lbl6 = Label(m, text = "")
lbl6.config(bg="#ADD8E6")
lbl6.pack()
lbl7 = Label(m, text = "")
lbl7.config(bg="#ADD8E6")
lbl7.pack()
lbl8 = Label(m, text = "")
lbl8.config(bg="#ADD8E6")
lbl8.pack()
lbl10 = Label(m, text = "")
lbl10.config(bg="#ADD8E6")
lbl10.pack()

m.mainloop()
