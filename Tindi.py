from tkinter import *
from random import randint as ri
from tkinter import messagebox as mb
import os
import yest as y

class Contain:

    def randInt(self,temp):
        try:
            # op = open('yest.txt')
            # res = op.read()
            # res = res.split()
            # op.close()

            res = y.prt()
            rand = ""
            count = 0
            # print(res)
            while True:
                rand = ri(1,int(temp))
                count += 1
                # print(count)
                if not rand in res:
                #     continue
                # else:
                    return rand
                    # break

                if count == 20:
                    mb.showerror("Error","No Tindi left please insert more tindi")
                    break

            

        except Exception as e:
            mb.showwarning("error",e)


        
    def DisplayTindi(self):
         try:
            global lbl2
            global inst
            op = open('bin/tindi.txt')
            res = op.read()
            res = res.split("\n")
            temp = ' '.join(res)
            res = temp.split()

            i = 0
            while i < len(res):
                temp = res[i]
                i += 2

            
            ind = self.randInt(temp)
            indx = res.index(str(ind))
            
            msg = "Tindi = {}".format( res[indx + 1] )
            msg = msg.replace("-"," ")
            mb.showinfo("Tindi",msg)
            op.close()

            tempsub = int(inst.get())
            if y.retriveDays() != tempsub:
               self.sub()

            if tempsub == (y.dayCount()):
                y.reset()
                y.appi(int(ind))
                # yest.append(int(ind))
            else:
                y.appi(int(ind))

            # lbl = Label(root, text = y.dayCount() ,font = ("Times New Roman", 16))
            # lbl.place(x = 120, y = 260)

            lbl2.destroy()
            
            lbl2 = Label(root, text = y.dayCount() ,font = ("Times New Roman", 16))
            lbl2.place(x = 200, y = 10)

            # inst.delete(0,'end')
            # inst.insert(0,y.dayCount())

            # print(y.prt())
            y.update()


         except Exception as e:
             mb.showerror("error",e)

    def Ins(self):
        try:
            op = open('bin/tindi.txt')
            res = op.read()
            op.close()
            res = res.split("\n")
            rest = ' '.join(res)
            res = rest.split()

            i = 0
            while i < len(res):
                rest = res[i]
                i += 2

            insrr = str(self.ins.get()).upper()
            # print(insrr)
            self.ins.delete(0,'end')
            if not insrr in res:
                op = open('bin/tindi.txt','a+')
                op.write("\n")
                
                insrr = insrr.replace(" ","-")
                stg = "{} {}".format(str(int(rest) + 1), insrr)
                op.write(stg)
                op.close()
            else:
                error = "Tindi \'{}\' already exist".format(insrr)
                mb.showerror("Error",error)
        
        except Exception:
             mb.showerror("error",Exception)

    def buttons(self):
        self.btn = Button(root, text = "Show Tindi", bd = 3, font = ("Open Sans", 16), command = self.DisplayTindi)
        self.btn.pack()
        self.btn.place(x = 95, y = 50)

        self.ins = Entry(root, bd = 1.5, font = ("Times New Roman", 16))
        self.ins.place(x = 85, y = 150, width = 150)
        self.btn = Button(root, text = "Insert", bd = 3, font = ("Open Sans", 16), command = self.Ins)
        self.btn.pack()
        self.btn.place(x = 120, y = 200)

        btnn = Button(root, text = "Submit", bd = 3, font = ("Open Sans", 16), command = self.sub)
        btnn.pack()
        btnn.place(x = 120, y = 340)



    def sub(self): 
        global lbl2
        x = int(inst.get())
        ck = y.setDays(x)

        if ck:
            lbl2.destroy()   
            lbl2 = Label(root, text = "Reset" ,font = ("Times New Roman", 16))
            lbl2.place(x = 200, y = 10)





root = Tk()
root.resizable(0,0)

obj = Contain()
obj.buttons()

lbl = Label(root, text = "Day Count = " ,font = ("Times New Roman", 16))
lbl.place(x = 90, y = 10)
lbl2 = Label(root, text = y.dayCount() ,font = ("Times New Roman", 16))
lbl2.place(x = 200, y = 10)

lbl = Label(root, text = "Number Of Days " ,font = ("Times New Roman", 16))
lbl.place(x = 20, y = 300)
inst = Entry(root, bd = 1.5, font = ("Times New Roman", 16))
inst.place(x = 180, y = 300, width = 100)
inst.insert(0,y.retriveDays())

root.geometry("300x400")
root.title("Guess The Tindi")
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='Photos/bf.png'))



mainloop()
