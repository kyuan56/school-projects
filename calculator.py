from tkinter import *
from tkinter import ttk
digitB=[]
ope=[]
equ=[]
che=[]
class Number:
    def __init__(self,numStr,base):
        self.de=""
        self.bi=""
        if numStr=="":
            numStr="0"
        if base==2:
            self.bi=numStr
            b=0
            c=0
            a=int(numStr)
            while a>0:
                b=b+(a%10)*(2**c)
                a=a//10
                c=c+1
            self.de=str(b)
        elif base==10:
            self.de=numStr
            a=int(numStr)
            d=""
            while(a>0):
                d=d+str(a%2)
                a=a//2
            e=""
            for i in range(len(d)-1,-1,-1):
                e=e+d[i]
            self.bi=e
    def GetBinary(self):
        return self.bi
    def GerDecimal(self):
        return self.de
    def BinaryToDecimal(self):
        b=0
        c=0
        a=int(self.bi)
        while a>0:
            b=b+(a%10)*(2**c)
            a=a//10
            c=c+1
        self.de=str(b)
    def DecimalToBinary(self):
        
        a=int(self.de)
        d=""
        while(a>0):
            d=d+str(a%2)
            a=a//2
        e=""
        for i in range(len(d)-1,-1,-1):
            e=e+d[i]
        self.bi=e
    
class Cal:
    def __init__(self,master):
        self.binaryButtons=[]
        self.decimalButtons=[]
        self.num10bj=None
        self.num20bj=None
        self.numberSystem=10
        self.num1=""
        self.num2=""
        self.operation=""
        self.isNum1=True
        mainframe=ttk.Frame(master,relief=SUNKEN,padding="3 3 12 12")
        mainframe.grid(column=0,row=0,columnspan=7,rowspan=6,sticky="NWES")
        mainframe.grid_rowconfigure(0,weight=1)
        mainframe.grid_columnconfigure(0,weight=1)

        viewLabel=ttk.Label(mainframe,text="0")
        viewLabel.grid(column=0,row=0,columnspan=3,sticky="WE")
        
        one=ttk.Button(mainframe,text="1",command=lambda:self.AppendDigit(1,viewLabel))
        one.grid(column=0,row=1,pady=5)
        two=ttk.Button(mainframe,text="2",command=lambda:self.AppendDigit(2,viewLabel))
        two.grid(column=1,row=1,pady=5)
        three=ttk.Button(mainframe,text="3",command=lambda:self.AppendDigit(3,viewLabel))
        three.grid(column=2,row=1,pady=5)
        four=ttk.Button(mainframe,text="4",command=lambda:self.AppendDigit(4,viewLabel))
        four.grid(column=0,row=2,pady=5)
        five=ttk.Button(mainframe,text="5",command=lambda:self.AppendDigit(5,viewLabel))
        five.grid(column=1,row=2,pady=5)
        six=ttk.Button(mainframe,text="6",command=lambda:self.AppendDigit(6,viewLabel))
        six.grid(column=2,row=2,pady=5)
        seven=ttk.Button(mainframe,text="7",command=lambda:self.AppendDigit(7,viewLabel))
        seven.grid(column=0,row=3,pady=5)
        eight=ttk.Button(mainframe,text="8",command=lambda:self.AppendDigit(8,viewLabel))
        eight.grid(column=1,row=3,pady=5)
        nine=ttk.Button(mainframe,text="9",command=lambda:self.AppendDigit(9,viewLabel))
        nine.grid(column=2,row=3,pady=5)
        zero=ttk.Button(mainframe,text="0",command=lambda:self.AppendDigit(0,viewLabel))
        zero.grid(column=1,row=4,pady=5)
        
        plus=ttk.Button(mainframe,text="+",command=lambda:self.RecordOperator("+"))
        plus.grid(column=5,row=1,pady=5)
        minus=ttk.Button(mainframe,text="-",command=lambda:self.RecordOperator("-"))
        minus.grid(column=5,row=2,pady=5)
        cheng=ttk.Button(mainframe,text="*",command=lambda:self.RecordOperator("*"))
        cheng.grid(column=5,row=3,pady=5)
        chu=ttk.Button(mainframe,text="//",command=lambda:self.RecordOperator("//"))
        chu.grid(column=5,row=4,pady=5)
        eq=ttk.Button(mainframe,text="=",command=lambda:self.ComputR(viewLabel))
        eq.grid(column=6,row=3,pady=5)
        cleared=ttk.Button(mainframe,text="clear",command=lambda:self.Clearall(viewLabel))
        cleared.grid(column=6,row=4,pady=3)
        self.v=IntVar()
        bina=ttk.Radiobutton(mainframe,text="Binary",variable=self.v,value=1,command=lambda:self.AssignSystem(2,viewLabel))
        bina.grid(column=8,row=2)
        deci=ttk.Radiobutton(mainframe,text="Decimal",variable=self.v,value=2,command=lambda:self.AssignSystem(10,viewLabel))
        deci.grid(column=7,row=2)
        digitB.append(nine)
        digitB.append(eight)
        digitB.append(seven)
        digitB.append(six)
        digitB.append(five)
        digitB.append(four)
        digitB.append(three)
        digitB.append(two)
        digitB.append(one)
        digitB.append(zero)
        ope.append(plus)
        ope.append(minus)
        ope.append(cheng)
        ope.append(chu)
        equ.append(eq)
        self.binaryButtons.append(one)
        self.binaryButtons.append(zero)
        
        self.decimalButtons.append(two)
        self.decimalButtons.append(three)
        self.decimalButtons.append(four)
        self.decimalButtons.append(five)
        self.decimalButtons.append(six)
        self.decimalButtons.append(seven)
        self.decimalButtons.append(eight)
        self.decimalButtons.append(nine)
        che.append(cleared)
        self.disable(che+ope+equ)
        return
    def enable(self,Blist):
        for i in Blist:
            i.config(state=NORMAL)
    def disable(self,Blist):
        for i in Blist:
            i.config(state=DISABLED)
    def AssignSystem(self,base,view):
        k1=Number(self.num1,self.numberSystem)
        k2=Number(self.num2,self.numberSystem)
        if(base==10):
            self.num1=k1.de
            self.num2=k2.de
            if(self.isNum1==True):
                view.config(text=self.num1)
                self.num2=""
            else:
                view.config(text=self.num2)
            self.numberSystem=10
            self.enable(self.decimalButtons)
        elif(base==2):
            self.num1=k1.bi
            self.num2=k2.bi
            
            if(self.isNum1==True):
                view.config(text=self.num1)
                self.num2=""
            else:
                view.config(text=self.num2)
            self.disable(self.decimalButtons)
            self.numberSystem=2
    def AppendDigit(self,digit,viewLabel):
        if(self.isNum1):
            self.num1=self.num1+str(digit)
            viewLabel.config(text=self.num1)
            self.enable(ope+che)
        else:
            self.num2=self.num2+str(digit)
            viewLabel.config(text=self.num2)
            self.enable(equ)
        return
    def RecordOperator(self,op):
        self.num10bj=None
        self.num10bj=Number(self.num1,self.numberSystem)
        self.operation=op
        self.isNum1=False
        self.disable(ope)
        self.enable(digitB)
        if self.numberSystem==2:
            self.disable(self.decimalButtons)
        return
    def ComputR(self,viewLable):
        self.num20bj=None
        self.num20bj=Number(self.num2,self.numberSystem)
        if self.operation=="+":
            r=str(int(self.num10bj.de)+int(self.num20bj.de))
            q=""
        elif self.operation=="-":
            r=str(int(self.num10bj.de)-int(self.num20bj.de))
            q=""
        elif self.operation=="*":
            r=str(int(self.num10bj.de)*int(self.num20bj.de))
            q=""
        elif self.operation=="//":
            r=str(int(self.num10bj.de)//int(self.num20bj.de))
            q='R'+str(int(self.num10bj.de)%int(self.num20bj.de))
        rnum=Number(r,10)
        if self.numberSystem==10:
            r=rnum.de
        elif self.numberSystem==2:
            r=rnum.bi
            
        viewLable.config(text=(r+q))
        self.num1=r
        self.num2=""
        self.isNum1=True
        self.disable(digitB+equ)
        self.enable(ope)
        self.num20bj=None
        
        return
    def Clearall(self,view):
        self.num1=""
        self.num2=""
        self.isNum1=True
        view.config(text="")
        self.operation=""
        self.enable(digitB)
        self.disable(che+ope+equ)
        self.num10bj=None
        self.num20bj=None
        if self.numberSystem==2:
            self.disable(self.decimalButtons)
def main():
    master=Tk()
    
    master.title("Calculator")
    Cal(master)
    master.mainloop()

if __name__==main():
    main()

