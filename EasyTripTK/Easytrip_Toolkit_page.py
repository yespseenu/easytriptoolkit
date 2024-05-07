import time
from datetime import date
from tkinter import *
from currency_converter import CurrencyConverter
from tkinter import ttk
import googletrans
from googletrans import Translator
from tkinter import filedialog

C=CurrencyConverter()
a=Tk()
bc=PhotoImage(file="backlo.png")
c=PhotoImage(file="trpic.png")
hm1=PhotoImage(file="clint1.png")
hm=PhotoImage(file="mot1.png")
pic = PhotoImage(file="fpcoverpic.png")
pic1 = PhotoImage(file="cur1.png")
m = PhotoImage(file="lan1.png")
m1 = PhotoImage(file="lan2.png")
bg = PhotoImage(file="BG.png")
w1 = PhotoImage(file="te1.png")
of = PhotoImage(file="us.png")
a.geometry("2000x1000")
a.config(bg="Light blue")

def datag():

      O = Toplevel()
      O.title("EasyTrip Toolkit Data page")

      def getdata():
            username = "seenu"
            password = "seenu123"
            if username == EE1.get() and password == EE2.get():
                  IN.config(text=" ")
                  f = open("user data.txt", mode="r")
                  f1 = f.read()
                  gettxt.insert(INSERT, f1)
                  f.close()

            else:
                  IN.config(text="invalid user and password")
                  gettxt.delete(1.0, END)


      Label(O, image=of).pack()

      gettxt = Text(O, bg="pink", bd=5, fg="blue",relief=SUNKEN)
      gettxt.place(x=500, y=150)
      Frame(O, bg="pink", width=650, height=80, bd=10, relief=GROOVE).place(x=500, y=590)
      UB = Button(O, text="Show User data", bg="Light pink", width=25, command=getdata).place(x=950, y=612)
      Label(O, text="User Name", bg="pink").place(x=510, y=615)
      EE1 = Entry(O, bg="Light pink")
      EE1.place(x=580, y=618)
      Label(O, text="Password", bg="pink").place(x=720, y=615)
      EE2 = Entry(O, bg="Light pink")
      IN = Label(O, text=" ", bg="pink", fg="red")
      IN.place(x=765, y=638)
      EE2.place(x=780, y=618)
      O.mainloop()
def np():

      Te = Toplevel()
      Te.geometry("2000x1000")
      Te.title("EasyTrip Toolkit Notepad")


      Te.config(bg="white")

      def clr():
            nott.config(fg=En1.get())
            En1.delete(0, END)

      def un():
            nott.config(font=("", 11, "underline"))

      def un1():
            nott.config(font=("", 11,))

      def fnt():
            nott.config(font=(En2.get(), 11))
            En1.delete(0,END)

      def sav():
            s = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=[("text", ".txt")])
            if s is None:
                  return
            t = str(nott.get(1.0, END))
            s.write(t)
            s.close()

      def op():
            o = filedialog.askopenfile(mode='r', filetypes=[("text file", "*.txt")])
            if o is not None:
                  c = o.read()
                  nott.insert(INSERT, c)

      def de():
            nott.delete(1.0, END)

      def df():
            nott.config(fg="black")

      def bg():
            nott.config(bg=En3.get())
            En3.delete(0,END)

      def bg1():
            nott.config(bg="white")

      Label(Te, image=w1, bg="white").pack()
      Frame(Te, width=800, height=33, bg="Light blue").place(x=0, y=0)
      Label(Te, text=" EasyTrip", fg="gray", bg="Light blue", font=("", 18)).place(x=0, y=0)
      Label(Te, text=" Toolkit", fg="orange", bg="Light blue", font=("", 18)).place(x=105, y=0)
      Label(Te, text=" Notes", fg="white", bg="Light blue", font=("", 18)).place(x=700, y=0)
      nott = Text(Te, width=80, bd=10, height=30, font=("", 11))
      nott.place(x=500, y=107)
      b1 = Button(Te, text="Save", width=15, bg="Teal", fg="white", command=sav)
      b1.place(x=1050, y=650)
      b1 = Button(Te, text="open", width=15, bg="Teal", fg="white", command=op)
      b1.place(x=500, y=650)
      b1 = Button(Te, text="Colour", width=15, bg="Teal", fg="white", command=clr)
      b1.place(x=10, y=70)
      En1 = Entry(Te, bg="Light blue", fg="black", width=18)
      En1.place(x=12, y=120)
      b2 = Button(Te, text="Font", width=15, bg="Teal", fg="white", command=fnt)
      b2.place(x=10, y=170)
      En2 = Entry(Te, bg="Light blue", fg="black", width=18)
      En2.place(x=12, y=220)
      b2 = Button(Te, text="Underline", width=15, bg="Teal", fg="white", command=un)
      b2.place(x=10, y=300)
      b1 = Button(Te, text="De-Underline", width=15, bg="Teal", fg="white", command=un1)
      b1.place(x=10, y=350)
      b1 = Button(Te, text="Default fg", width=15, bg="Teal", fg="white", command=df)
      b1.place(x=10, y=400)
      b1 = Button(Te, text="Delete all", width=15, bg="Teal", fg="white", command=de)
      b1.place(x=10, y=450)
      b1 = Button(Te, text="Default bg", width=15, bg="Teal", fg="white", command=bg1)
      b1.place(x=10, y=500)

      b1 = Button(Te, text="Background", width=15, bg="Teal", fg="white", command=bg)
      b1.place(x=10, y=600)
      En3 = Entry(Te, bg="Light blue", fg="black", width=18)
      En3.place(x=12, y=650)

      Label(Te, text="N", fg="green", bg="white", font=("", 30)).place(x=1280, y=50)
      Label(Te, text="O", fg="green", bg="white", font=("", 30)).place(x=1280, y=150)
      Label(Te, text="T", fg="green", bg="white", font=("", 30)).place(x=1280, y=250)
      Label(Te, text="E", fg="green", bg="white", font=("", 30)).place(x=1280, y=350)
      Label(Te, text="P", fg="green", bg="white", font=("", 30)).place(x=1280, y=450)
      Label(Te, text="A", fg="green", bg="white", font=("", 30)).place(x=1280, y=550)
      Label(Te, text="D", fg="green", bg="white", font=("", 30)).place(x=1280, y=650)

      Te.mainloop()

def budget():

      B = Toplevel()
      B.title("EasyTrip Toolkit Calculator ")

      B.geometry("2000x1000")

      def getans():
            mm = v1.get() + v2.get() + v3.get() + v4.get() + v5.get()
            mm1 = mm / v6.get()
            tpv=round(mm1)
            LA1.config(text=mm)
            LA2.config(text=tpv)
            EN1.delete(0,END)
            EN2.delete(0,END)
            EN3.delete(0,END)
            EN4.delete(0,END)
            EN5.delete(0,END)
            EN6.delete(0,END)


      v1 = IntVar()
      v2 = IntVar()
      v3 = IntVar()
      v4 = IntVar()
      v5 = IntVar()
      v6 = IntVar()

      Label(B, image=bg, bg="Light blue").pack()
      Frame(B, width=400, height=600, bg="Light blue", bd=8, relief=GROOVE).place(x=900, y=40)
      Frame(B, width=400, height=600, bg="Light blue", bd=8, relief=GROOVE).place(x=100, y=40)
      Label(B, text="Result", bg="Light blue", fg="Teal", font=("", 30)).place(x=100, y=20)
      Label(B, text="Calculator", bg="Light blue", fg="Teal", font=("", 30)).place(x=900, y=20)
      Label(B, text="Travel Expenses", bg="Light blue", fg="black", font=("", 10)).place(x=920, y=80)
      EN1 = Entry(B, width=30, textvariable=v1)
      EN1.place(x=925, y=110)
      Label(B, text="Food Expenses", bg="Light blue", fg="black", font=("", 10)).place(x=920, y=150)
      EN2 = Entry(B, width=30, textvariable=v2)
      EN2.place(x=925, y=180)
      Label(B, text="Entry Fee", bg="Light blue", fg="black", font=("", 10)).place(x=920, y=220)
      EN3 = Entry(B, width=30, textvariable=v3)
      EN3.place(x=925, y=250)
      Label(B, text="Room Expenses", bg="Light blue", fg="black", font=("", 10)).place(x=920, y=280)
      EN4 = Entry(B, width=30, textvariable=v4)
      EN4.place(x=925, y=310)
      Label(B, text="Miscellaneous Expenses", bg="Light blue", fg="black", font=("", 10)).place(x=920, y=350)
      EN5 = Entry(B, width=30, textvariable=v5)
      EN5.place(x=925, y=380)
      Label(B, text="No of person's", bg="Light blue", fg="black", font=("", 10)).place(x=920, y=420)
      EN6 = Entry(B, width=30, textvariable=v6)
      EN6.place(x=925, y=450)
      but = Button(B, text="submit", fg="white", bg="blue", width=20, command=getans)
      but.place(x=925, y=500)
      Label(B, text="Total Amount", bg="Light blue", fg="black", font=("", 17)).place(x=150, y=100)
      Label(B, text="Amount Per Person", bg="Light blue", fg="black", font=("", 17)).place(x=150, y=200)
      Label(B,
            text="*Turning travel dreams into budget-friendly realities. Use our Trip Budget Calculator to make every adventure affordable"
            , bg="Light blue", fg="blue", font=("", 12), wraplength=300).place(x=150, y=300)
      Label(B,
            text="*Discover the joy of budget-friendly travel. Our Trip Budget Calculator takes the guesswork out of planning so you can focus on the experience"
            , bg="Light blue", fg="blue", font=("", 12), wraplength=300).place(x=150, y=400)
      Label(B,text="*Travel smart, spend wisely. Our Trip Budget Calculator is your key to unlocking affordable and unforgettable journeys"
            , bg="Light blue", fg="blue", font=("", 12), wraplength=300).place(x=150, y=500)
      Label(B,text="Wanderlust on a budget? No problem! Our Trip Budget Calculator ensures your travel dreams align with your financial reality"
            , bg="Light blue", fg="Teal", font=("", 10)).place(x=300, y=5)
      Label(B, text="< YEsp >", bg="Light blue", fg="Teal", font=("", 30)).place(x=600, y=110)
      LA1 = Label(B, text=" ", bg="Light blue", fg="Teal", font=("", 17))
      LA1.place(x=150, y=150)
      LA2 = Label(B, text=" "
                          "", bg="Light blue", fg="Teal", font=("", 17))
      LA2.place(x=150, y=250)
      B.mainloop()
def swap():
      a=C1.get()
      b=C2.get()
      C1.config(C1.set(b))
      C2.config(C2.set(a))

def traslate():
      global C1,C2

      t = Toplevel()
      t.title("EasyTrip Toolkit Translator")
      t.geometry("2000x1000")
      t.config(bg="white")
      Frame(t, width=650, height=900, bg="Light blue").place(x=20, y=0)
      Label(t, image=m, bg="white").place(x=700, y=40)
      Label(t, image=m1, bg="Light blue").place(x=210, y=0)
      L=Label(t, text="FROM", bg="Light blue",fg="red",font=("",20)).place(x=100, y=200)
      L1=Label(t,  text="TO", bg="Light blue",fg="red",font=("",20)).place(x=500, y=200)

      def trans():
            s = C1.get()
            s1 = C2.get()
            s2 = T1.get(1.0, END)
            TT = Translator()
            ttt = TT.translate(text=s2, src=s, dest=s1)
            ttt = ttt.text

            T2.delete(1.0, END)
            T2.insert(END, ttt)

      # tran
      L = googletrans.LANGUAGES
      L1 = list(L.values())


      # cm
      C1 = ttk.Combobox(t, values=L1, width=40)
      C1.place(x=70, y=300)
      C1.set("english")
      C2 = ttk.Combobox(t, values=L1, width=40)
      C2.place(x=350, y=300)
      C2.set("tamil")

      # text

      T1 = Text(t, width=30, height=15, bd=5, relief=GROOVE)
      T1.place(x=70, y=350)
      T2 = Text(t, width=30, height=15, bd=5, relief=GROOVE)
      T2.place(x=360, y=350)

      # button
      B1 = Button(t, text="<->", width=30, bd=5, relief=GROOVE, bg="blue", fg="white", command=trans)
      B1.place(x=240, y=650)
      B2 = Button(t, text="Swap", width=10, relief=FLAT, bg="Light blue", fg="white",activebackground="Light blue",activeforeground="white",font=("",15),command=swap)
      B2.place(x=275, y=250)
      Label(t, text="Whether you're a traveler, business professional, or language enthusiast, our platform caters to a diverse range of needs.",
            bg="white",fg="blue",font=("",12),wraplength=750).place(x=690, y=0)

      t.mainloop()

def currency():
      a1 = Toplevel()
      a1.title("EasyTrip Toolkit CURRENCY CONVERTER")

      a.geometry("2000x1000")

      def getcy():
            aa = E1.get().upper()
            aa1 = E2.get().upper()
            aa2 = var.get()

            aa1.upper()
            cf = C.convert(aa2, aa, aa1)
            m=round(cf)
            result = (m, aa1)
            Label(a1, text = result , fg="white", bg="Teal", font=("", 15)).place(x=1000, y=30)

            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)


      Label(a1, image=pic1, bg="white").place(x=2, y=5)

      Frame(a1, width=2000, height=1000, bg="white").pack()
      Frame(a1, width=2000, height=50, bg="Teal").place(x=0, y=20)
      Label(a1, text="CURRENCY CONVERTER", fg="yellow", bg="Teal", font=("", 25)).place(x=450, y=20)
      Label(a1, text="From Currency", fg="Teal", bg="white", font=("", 15)).place(x=40, y=100)
      Label(a1, text="To Currency", fg="Teal", bg="white", font=("", 15)).place(x=40, y=150)
      Label(a1, text="Enter Amount", fg="Teal", bg="white", font=("", 15)).place(x=40, y=200)
      Label(a1, text="Result :", fg="white", bg="Teal", font=("", 20)).place(x=900, y=24)
      var = IntVar()
      E1 = Entry(a1, width=40, bd=5)
      E2 = Entry(a1, width=40, bd=5)
      E3 = Entry(a1, width=40, bd=5, textvariable=var)

      E1.place(x=200, y=105)
      E2.place(x=200, y=155)
      E3.place(x=200, y=205)

      Label(a1, image=pic, bg="white").place(x=35, y=250)

      B5 = Button(a1, text="Get", width=20, bg="Orange", fg="white", bd=10, relief=RAISED, command=getcy)

      B5.place(x=200, y=255)
      Label(a1, text="The web page lists 195 countries in the world today, with population, share of world population, and land area data for each country. It also shows the flags, dependencies, and areas of special sovereignty of the countries, as well as the list of countries ranked by the most populous and showing current …",
            bg="white", fg="Orange", font=("", 10),wraplength=500).place(x=800, y=100)
      Label(a1,
            text="What money do you use depends on where are you living or planning to travel. Totally, there are 164 official national currencies circulating around the world. Although the number of the independent countries is 197 plus about five dozen of dependent territories. The matter is, that some of them don't have their own money and officially use the foreign currency.Thus the European euro is used in 35 independent states and overseas territories, the United States dollar is used in 10 foreign countries and in the USA, the West African CFA franc - in 8 and the Central African CFA franc - in 6 African states, the East Caribbean dollar - in 6 Caribbean nations.The world's most-traded currency is the US dollar with about 47% share of global payments and 87% of the forex market's daily turnover. On the second place is the Euro, having about 33% of the daily forex transactions and 28% share of the international bank payments.",
            bg="white", fg="Orange", font=("", 10), wraplength=500).place(x=800, y=200)
      Label(a1, text="About Countries:",bg="white",fg="Teal", font=("", 18)).place(x=590, y=100)
      Label(a1, text="About Currencies:",bg="white", fg="Teal", font=("", 18)).place(x=590, y=200)

      a1.mainloop()


def cur():
      if E1.get()==" " and E2.get()==" ":
            inval.config(text="*Invalid place Enter your Name and Phone no")
      else:
            inval.config(text=" ")

            h = Toplevel()
            h.geometry("2000x1000")
            h.title("EasyTrip Toolkit home page")
            na = E1.get()
            pn = E2.get()
            t = time.localtime()
            today = date.today()
            ctime = (time.strftime("%H:%M:%S", t))
            cdate = today.strftime("%B %d %Y")

            E1.delete(0, END)
            E2.delete(0, END)

            f = open("user data.txt", mode="a")
            f.write(
                  "--------------------------------------------------------------------------------------------------------\n")
            f.write("name :")
            f.write(na)
            f.write("\n")
            f.write("phone no :")
            f.write(pn)
            f.write("\nTime :")
            f.write(ctime)
            f.write("\nDate:")
            f.write(cdate)
            f.write(
                  "\n---------------------------------------------------------------------------------------------------------")
            f.close()
            h.config(bg="Light gray")
            Label(h, image=hm, bg="gray", width=2000, height=600).place(x=0, y=65)
            Frame(h, bg="Light gray", width=500, height=500).place(x=30, y=100)
            # Label(h, image=hm1, bg="white",width=500,height=240).place(x=800, y=80)
            # Frame(h,width=850,height=50,bg="brown").place(x=390, y=60)
            Label(h, text="EasyTrip",
                  bg="Light gray", fg="gray", font=("", 30, "bold")).place(x=0, y=2)
            Label(h, text="Toolkit", bg="Light gray", fg="orange", font=("", 20, "bold")).place(x=170, y=10)
            #Label(h, text="Step into the future of productivity and exploration. Welcome to our digital hub!",
                  #bg="Light gray", fg="orange", font=("", 10)).place(x=120, y=43)
            HB1 = Button(h, width=15, text="CurrencyConverter", bg="Light gray", fg="black", font=("", 15, "underline"),
                         activebackground="Light gray", relief=FLAT, command=currency)
            HB1.place(x=600, y=10)
            HB2 = Button(h, width=15, text="Translator", bg="Light gray", fg="black", activebackground="Light gray",
                         font=("", 15, "underline"), command=traslate, relief=FLAT)
            HB2.place(x=800, y=10)
            HB3 = Button(h, width=15, text="Notes", bg="Light gray", fg="black", font=("", 15, "underline"),
                         relief=FLAT,
                         activebackground="Light gray", command=np)
            HB3.place(x=950, y=10)

            HB4 = Button(h, width=11, text="Budget", bg="Light gray", fg="black", font=("", 15, "underline"),
                         relief=FLAT,
                         activebackground="Light gray", command=budget)
            HB4.place(x=1100, y=10)
            HB5 = Button(h, width=15, text="Quit Page", bg="Light gray", fg="black", bd=5, relief=FLAT,
                         font=("", 15, "underline"), activebackground="Light gray", command=quit)
            HB5.place(x=1200, y=8)
            Label(h, text="Currency Converter", bg="Light gray", fg="gray", font=("", 15, "bold")).place(x=30, y=100)
            Label(h,
                  text="Turning currencies into conversations, one exchange at a time. Your passport to seamless international transactions. Your passport to seamless international transactions.",
                  bg="Light gray", fg="black", font=("", 11), wraplength=450).place(x=40, y=145)
            Label(h, text="Translator", bg="Light gray", fg="gray", font=("", 15, "bold")).place(x=30, y=200)
            Label(h,
                  text="Breaking language barriers, building bridges.Transcend borders with our powerful Translator. Words connect worlds – let our Translator be your guide.",
                  bg="Light gray", fg="black", font=("", 11), wraplength=450).place(x=40, y=245)
            Label(h, text="Notepad", bg="Light gray", fg="gray", font=("", 15, "bold")).place(x=30, y=300)
            Label(h,
                  text="Capturing thoughts in the digital age, one note at a time.Empower your creativity with our digital Notepad.Where ideas meet pixels, and inspiration is always just a click away",
                  bg="Light gray", fg="black", font=("", 11), wraplength=450).place(x=40, y=345)
            Label(h, text="Trip Budget Calculator", bg="Light gray", fg="gray", font=("", 15, "bold")).place(x=30,
                                                                                                             y=420)
            Label(h,
                  text="Travel smart, spend wisely – our Trip Budget Calculator at your service.Turning dream vacations into financial plans, effortlessly.Explore more, worry less – let our Trip Budget Calculator be your travel companion.",
                  bg="Light gray", fg="black", font=("", 11), wraplength=450).place(x=40, y=465)
            h.mainloop()


a.title("EasyTrip Toolkit Login page")
Label(a,image=bc,bg="Light blue").place(x=390,y=80)
Label(a,image=bc,bg="Light blue").place(x=0,y=80)
Frame(a,bg="white",width=400,height=700,bd=10,relief=GROOVE).place(x=900,y=80)



Label(a,image=c,bg="white",width=370).place(x=910,y=200)

Label(a,text="Welcome to EasyTrip Toolkit",font=("",18,"bold"),bg="white",fg="Teal").place(x=925,y=100)
Label(a,text="Login to continue",bg="white").place(x=925,y=130)
Label(a,text="Name",bg="white",font=("",12)).place(x=955,y=200)
inval=Label(a,text=" ",bg="white",font=("",10),fg="red")
inval.place(x=955,y=170)
Label(a,text="Phone number",bg="white",font=("",12)).place(x=955,y=300)



#entry
E1=Entry(a,width=40,bd=5)
E2=Entry(a,width=40,bd=5)
E1.insert(0," ")
E2.insert(0," ")
E1.place(x=960,y=240)
E2.place(x=960,y=340)

#button
LB1=Button(a,width=20,text="Login",bg="blue",fg="white",bd=5,relief=SUNKEN,command=cur)
LB1.place(x=960,y=420)

Label(a,text=" *Embark on a journey of a lifetime — where each click opens a door to a new adventure.",
      bg="Light blue",fg="gray",font=("",10)).place(x=0,y=640)
Label(a,text=" *Adventure is calling, and our website is the answer. Let the exploration begin!",
      bg="Light blue",fg="gray",font=("",10)).place(x=0,y=660)
Label(a,text="EasyTrip",
      bg="Light blue",fg="gray",font=("",30,"bold")).place(x=10,y=5)
Label(a,text="Toolkit",
      bg="Light blue",fg="orange",font=("",20,"bold")).place(x=180,y=15)
Label(a,text="Travel far, dream wide. Welcome to a digital space that fuels your wanderlust.",
      bg="Light blue",fg="Teal",font=("",13)).place(x=10,y=55)



Frame(a,bg="white",width=500,height=40,).place(x=900,y=25)
LB1=Button(a,text="Get Data",bg="white",fg="Teal",relief=FLAT,command=datag,font=("",9,"underline")
           ,activebackground="white")
LB1.place(x=1280,y=30)
Label(a,text="Please log in using your personal information to stay connected with us ",
      bg="white",fg="blue",font=("",10),wraplength=350).place(x=950,y=25)



a.mainloop()
