from sympy import sympify, symbols,solve,parse_expr,Eq
import matplotlib.pyplot as plt
import numpy as np
import sys
import time
from PIL import Image
import subprocess
import string
import plotille
import numpy as np
# GRAPH = np.sort(np.random.normal(size=1000))
class logger:
    def __init__(self):
        self.terminal=sys.stdout
        self.log=open(f+".log","a")
        self.legend=True
    def write(self,message):
        #self.terminal.write(message)
        #self.terminal.flush()
        self.log.write(message)
        self.log.flush()
        
    def flush(self):
        pass
f=input("enter file name")
LETTERS = string.ascii_letters
DIGITS = '0123456789'
log_filename = f+".log"
with open(log_filename, 'w'):
    pass
sys.stdout=logger()
command = f'start "Log Viewer" cmd /c powershell -ExecutionPolicy Bypass -Command "Get-Content -Path {log_filename} -Wait"'
subprocess.Popen(command, shell=True)


class DelYa:
    store={}
    div={}
    def __init__(self,fun=0):
        if fun!=0:
            self.fun=fun
        else:
            self.fun=input()
        idx=0
        self.symbol='y'
        self.var='x'
        for i in self.fun:
            if i in LETTERS and (self.fun[self.fun.index(i)-1] not in DIGITS or self.fun[self.fun.index(i)-1]!="-"):
                idx=self.fun.index(i)
                self.symbol=i
                if idx!=0 and(self.fun[idx-1]=='-' or self.fun[idx-1] in DIGITS):
                    print("Unknown syntax",self.fun[idx-1])
                    exit()
                self.fun=self.fun.replace(i,'')
                self.fun=self.fun.replace('=','')
                DelYa.store.update({i:self.fun})
                print(DelYa.store)
                break
        for i in self.fun:
            if i in LETTERS:
                self.var=i
                break
            
        if self.var==self.symbol:
            print("Error//Unknown syntax")
        if '/'in self.fun:
            if")" not in self.fun:
                print("syntax Error/expected ')'")
                exit( )
            div=sympify(self.fun[self.fun.index('/')+2:self.fun.index(")")])
            di=Eq(div,0)
            s=solve(di,i)
            DelYa.div[self.symbol]=s[0]
            print(self.div)
    # def graph(self,*a,fun):
    #     for i in a[0]:
    #         yield self.eval(fun,i)
    def plot(self,funName,n=0):
        if funName not in DelYa.store.keys():
            print("Error//function is not defined")
            exit()
        self.symbol=funName
        self.fun=DelYa.store[self.symbol]
        for i in self.fun:
            if i in LETTERS:
                self.var=i
                break
        # if self.var==self.symbol:
        #     print("Error//Unknown syntax")
        #     exit()
        self.y = symbols(self.symbol)
        self.x=symbols(self.var)
        # دریافت ورودی به عنوان یک استرینگ
        self.expression_string =self.fun
        self.expression = parse_expr(self.expression_string)
        self.equation = Eq(self.y, self.expression)
        y_expr = solve(self.equation, self.y)[0]
        # تبدیل عبارت به یک تابع قابل اجرا
        y_func = lambda x_val: y_expr.subs(self.x, x_val)
        # تولید دامنه x
        x_vals = np.linspace(-10, 10, 100)
        # محاسبه مقادیر y متناظر با x در دامنه
        y_vals = [y_func(x_val) for x_val in x_vals]
        # رسم نمودار
        plt.plot(x_vals, y_vals, label=self.fun)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(self.fun)
        plt.legend()
        plt.grid(True)
        plt.axhline(0, color='black', linewidth=2)
        plt.axvline(0, color='black', linewidth=2)
        print("plot")  
        plt.show()
        """گراف"""
        # fig = plotille.Figure()
        # fig.width = 60
        # fig.height = 30
        # fig.set_x_limits(min_=-3, max_=3)
        # fig.set_y_limits(min_=-1, max_=1)
        # fig.color_mode = 'byte'
        # fig.legend=True
        # C=list(zip(x_vals,y_vals))
        # X,Y=zip(*C)
       
        # # s=plotille.scatter(X,self.graph(X,self.fun),width=1000,height=1000)
        # print(s)
        # fig.scatter(list(X),list(Y), lc=100, label=self.fun)
        
        # with open('graph.txt', 'w') as file:
        #     s=fig.show(legend=True)
        #     file.write(str(s))
        # # print(fig.show(legend=True))
        
        if n==1:
            plt.savefig("plotimage.jpg")
    def eval(self ,funName,value):
        if funName not in DelYa.store.keys():
            print("Error//function is not defined")
            exit()
        self.symbol=funName
        self.fun=DelYa.store[self.symbol]
        for i in self.fun:
            if i in LETTERS:
                self.var=i
                break
        self.y = symbols(self.symbol)
        self.x=symbols(self.var)
        # دریافت ورودی به عنوان یک استرینگ
        self.expression_string =self.fun
        self.expression = parse_expr(self.expression_string)
        self.value=value
        if type(self.value)!=int and type(self.value)!= float:
            print("Invalid value(",{self.value},")")
            exit()
        # self.expression = parse_expr(self.expression_string)
        result =self.expression.evalf(subs={self.x: self.value})
        if self.symbol in DelYa.div.keys():
            if DelYa.div[self.symbol]==self.value:
                print("devision by 0>>Error")
        else:
            print(result)
        
        
    def Solve1(self,*a):
       
        li=set()
        inV=set()
        outV=set()
        x=set()
        for i in a[0]:
            if i not in DelYa.store.keys():
                print("Error//not found")
                exit
            else:
                li.add(DelYa.store[i])
                x.add(DelYa.store[i]+'-'+i)
                inV.add(i)
        for j in li:
            for k in j:
                if k in LETTERS and k not in inV:
                    outV.add(k)
        if not outV:
            print("not value")
            self.solve2(*a)
        else:
            print(outV,inV,"\n enter value for",outV,":")
            val={}
            for i in outV:
                val[i]=input()
                print(i,"=",val[i])
            solution=solve(x,inV)
            print(solution)
            if not solution:
                print("The equations have no answer")
                exit(0)
            for i,j in solution.items():
            
                for k,t in val.items():
                    solution[i]=sympify(solution[i])
                    s=solution[i].subs(k,t)
                    result = s.evalf()
                    solution[i]=result
                    # print(solution[i])
            print(solution)
            
    def solve2(self,*a):
        li=set()
        x=set()
        for i in a[0]:
            if i not in DelYa.store.keys():
                print("Error//not found",i)
                exit()
            else:
                li.add(DelYa.store[i])
                x.add(DelYa.store[i]+'-'+i)
        # print(x,a[0])
        print(solve(x,a[0]))
    def load (self,name):
        f=name
        sys.stdout=logger()
        command = f'start "Log Viewer" cmd /c powershell -ExecutionPolicy Bypass -Command "Get-Content -Path {log_filename} -Wait"'
        subprocess.Popen(command, shell=True)
    def clear(self):
        DelYa.store={}
        print(DelYa.store)
        subprocess.call('cls', shell=True)
        with open(log_filename, 'w'):
            pass
        sys.stdout=logger()
        command = f'start "Log Viewer" cmd /c powershell -ExecutionPolicy Bypass -Command "Get-Content -Path {log_filename} -Wait"'
        subprocess.Popen(command, shell=True)


count=1
x=print(count,')start with function>')
c=DelYa()
while(True):
    # '-DelYa>'
        count=count+1
        print(count,"-DelYa>")
        x=input()
        if x=="HELP":
            print("this language help you to do:\n *)new function with 'Get'\n *)plot the function with 'PLOT(funName)' \n" ,
                  "*)evaluated the function with 'EVAL(funName,value)' \n *)save the plot1 with 'PLOTSAVE(fun,1)' \n *)solve equation with values 's(names)'\n *)solve equation without values 'eq(names)'\n *)clear terminal with 'clear' \n *)exit the program with 'EXIT'"
          )
        elif x=='Get':
            c=DelYa()
            continue
        elif 'PLOT(' in x:
            y=x[x.index("(")+1:-1]
            if x!='PLOT('+y+')':
                print('syntax Error')
                exit()
            c.plot(y)
            continue
        elif 'PLOTSAVE' in x:
            y=x[x.index("(")+1:-1]
            if x!='PLOTSAVE('+y+')':
                print('syntax Error')
                exit()
            c.plot(y,1)
            continue
        elif 'EVAL(' in x:
            y=x[x.index("(")+1:x.index(',')]
            z=x[x.index(",")+1:-1]
            if x!='EVAL('+y+','+z+')':
                print('syntax Error')
                exit()
            c.eval(y,int(z))
            continue
        elif 's('in x:
            x=x[1:]
            a=[]
            for i in x:
                if i in LETTERS:
                    a.append(i)
            if x[-1]!=')':
                print("syntax Error: expected ')'")
                exit()
            c.Solve1(a) 
            continue  
        elif 'eq('in x:
            x=x[2:]
            a=[]
            for i in x:
                if i in LETTERS:
                    a.append(i)
            if x[-1]!=')':
                print("syntax Error: expected ')'")
                exit()
            c.solve2(a) 
            continue      
        elif x=="clear":
            c.clear()
            count=0
            continue
        elif x=='EXIT':
            print("**goodbye DelYa**")
            exit()
        elif 'load('in x:
            x=x[5:-1]
            
            print("load page",x)
            c.load(x)
        else:
            print("invalid syntax")
            exit()
        