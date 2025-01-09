import tkinter as tk
from tkinter import messagebox


class MyApp:

    def write(self,data):
        self.ekran_text = self.ekran_text + data
        self.ekran.delete(0, tk.END)
        self.ekran.insert(0, self.ekran_text)

    def button_click(self, data):
        if data == "%":
            try:
                self.ekran_text = str(int(eval(self.ekran_text))/100)
                self.ekran.delete(0, tk.END)
                self.ekran.insert(0, self.ekran_text)
            except:
                messagebox.showwarning("Diqqat","Noto'g'ri format !")
            pass
            pass
        elif data == "C":
            self.ekran_text = ""
            self.write("0")
            pass
        elif data == "<":
            if len(self.ekran_text) != 1:
                self.ekran_text = self.ekran_text[:-1]
                self.write("")
            else:
                self.ekran_text = ""
                self.write("0")
            pass
        elif data == "=":
            try:
                self.ekran_text = str(eval(self.ekran_text))
                self.ekran.delete(0, tk.END)
                self.ekran.insert(0, self.ekran_text)
            except:
                messagebox.showwarning("Diqqat","Noto'g'ri format !")
            pass
        elif data == "+/-":
            if self.ekran_text[0] != "-":
                self.ekran_text = "-" + self.ekran_text
                self.ekran.delete(0, tk.END)
                self.ekran.insert(0, self.ekran_text)
            else:
                self.ekran_text = self.ekran_text[1:]
                self.ekran.delete(0, tk.END)
                self.ekran.insert(0, self.ekran_text)
        else:
            if self.ekran_text[0] == "0":
                if data != "/" and data != "*" and  data != "+":
                    if data == ".":
                        if self.ekran_text[-1] != ".":
                            self.write(data)
                    else:
                        if self.ekran_text[-1] == ".":
                            self.write(data)
                        else:
                            self.ekran_text = ""
                            self.write(data)
                
            else:
                if data == "/":
                    if self.ekran_text[-1] != "/" and self.ekran_text[-1] != "*" and self.ekran_text[-1] != "-" and self.ekran_text[-1] != "+"and self.ekran_text[-1] != ".":
                        self.write(data)
                elif data == "-":
                    if self.ekran_text[-1] != "/" and self.ekran_text[-1] != "*" and self.ekran_text[-1] != "-" and self.ekran_text[-1] != "+"and self.ekran_text[-1] != ".":
                        self.write(data)  
                elif data == "+":
                    if self.ekran_text[-1] != "/" and self.ekran_text[-1] != "*" and self.ekran_text[-1] != "-" and self.ekran_text[-1] != "+"and self.ekran_text[-1] != ".":
                        self.write(data)
                elif data == "*":
                    if self.ekran_text[-1] != "/" and self.ekran_text[-1] != "*" and self.ekran_text[-1] != "-" and self.ekran_text[-1] != "+"and self.ekran_text[-1] != ".":
                        self.write(data)
                elif data == ".":
                    if self.ekran_text[-1] != "/" and self.ekran_text[-1] != "*" and self.ekran_text[-1] != "-" and self.ekran_text[-1] != "+"and self.ekran_text[-1] != ".":
                        self.write(data)
                else:
                    self.write(data)

    def __init__(self):
    
        self.ekran_text = "0"

        self.oyna = tk.Tk()
        self.oyna.geometry("350x410")
        self.oyna.title("Kalkulator")
        self.oyna.configure(bg = "#cccccc")
        self.oyna.resizable(False, False)

        self.ekran = tk.Entry(master = self.oyna,font = ("arial",20,"bold"),justify = "right",bg = "#eeeeee",width = 20,bd = 2)
        self.ekran.place(x = 20,y = 20)
        self.ekran.delete(0, tk.END)
        self.ekran.insert(0, self.ekran_text)
        
        self.button_1 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "%", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2,command = lambda: self.button_click("%"))
        self.button_1.place(x = 20,y = 75)
        self.button_2 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "C", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2,command = lambda: self.button_click("C"))
        self.button_2.place(x = 99,y = 75)
        self.button_3 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "<", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2,command = lambda: self.button_click("<"))
        self.button_3.place(x = 178,y = 75)
        self.button_4 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "/", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2,command = lambda: self.button_click("/"))
        self.button_4.place(x = 257,y = 75)
        
        self.button_5 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "7", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2,command = lambda: self.button_click("7"))
        self.button_5.place(x = 20,y = 140)
        self.button_6 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "8", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2,command = lambda: self.button_click("8"))
        self.button_6.place(x = 99,y = 140)
        self.button_7 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "9", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2,command = lambda: self.button_click("9"))
        self.button_7.place(x = 178,y = 140)
        self.button_8 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "*", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2,command = lambda: self.button_click("*"))
        self.button_8.place(x = 257,y = 140)
        
        self.button_9 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "4", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2,command = lambda: self.button_click("4"))
        self.button_9.place(x = 20,y = 205)
        self.button_10 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "5", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2,command = lambda: self.button_click("5"))
        self.button_10.place(x = 99,y = 205)
        self.button_11 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "6", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2,command = lambda: self.button_click("6"))
        self.button_11.place(x = 178,y = 205)
        self.button_12 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "-", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2,command = lambda: self.button_click("-"))
        self.button_12.place(x = 257,y = 205)
        
        self.button_13 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "1", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2,command = lambda: self.button_click("1"))
        self.button_13.place(x = 20,y = 270)
        self.button_14 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "2", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2,command = lambda: self.button_click("2"))
        self.button_14.place(x = 99,y = 270)
        self.button_15 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "3", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2,command = lambda: self.button_click("3"))
        self.button_15.place(x = 178,y = 270)
        self.button_16 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "+", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2,command = lambda: self.button_click("+"))
        self.button_16.place(x = 257,y = 270)
        
        self.button_17 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "+/-", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2,command = lambda: self.button_click("+/-"))
        self.button_17.place(x = 20,y = 335)
        self.button_18 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "0", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2,command = lambda: self.button_click("0"))
        self.button_18.place(x = 99,y = 335)
        self.button_19 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = ".", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2,command = lambda: self.button_click("."))
        self.button_19.place(x = 178,y = 335)
        self.button_20 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "=", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2,command = lambda: self.button_click("="))
        self.button_20.place(x = 257,y = 335)


        self.oyna.mainloop()

if __name__ == "__main__":
    MyApp()
