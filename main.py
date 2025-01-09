import tkinter as tk
from tkinter import messagebox


class MyApp:
    def __init__(self):

        self.oyna = tk.Tk()
        self.oyna.geometry("350x410")
        self.oyna.title("Kalkulator")
        self.oyna.configure(bg = "#cccccc")
        self.oyna.resizable(False, False)

        self.ekran = tk.Entry(master = self.oyna,font = ("arial",20,"bold"),text = "0",justify = "right",bg = "#eeeeee",width = 20,bd = 2)
        self.ekran.place(x = 20,y = 20)
        
        self.button_1 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "%", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2)
        self.button_1.place(x = 20,y = 75)
        self.button_2 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "C", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2)
        self.button_2.place(x = 99,y = 75)
        self.button_3 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "<", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2)
        self.button_3.place(x = 178,y = 75)
        self.button_4 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "/", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2)
        self.button_4.place(x = 257,y = 75)
        
        self.button_5 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "7", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2)
        self.button_5.place(x = 20,y = 140)
        self.button_6 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "8", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2)
        self.button_6.place(x = 99,y = 140)
        self.button_7 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "9", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2)
        self.button_7.place(x = 178,y = 140)
        self.button_8 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "*", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2)
        self.button_8.place(x = 257,y = 140)
        
        self.button_9 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "4", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2)
        self.button_9.place(x = 20,y = 205)
        self.button_10 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "5", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2)
        self.button_10.place(x = 99,y = 205)
        self.button_11 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "6", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2)
        self.button_11.place(x = 178,y = 205)
        self.button_12 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "-", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2)
        self.button_12.place(x = 257,y = 205)
        
        self.button_13 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "1", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2)
        self.button_13.place(x = 20,y = 270)
        self.button_14 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "2", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2)
        self.button_14.place(x = 99,y = 270)
        self.button_15 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "3", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2)
        self.button_15.place(x = 178,y = 270)
        self.button_16 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "+", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2)
        self.button_16.place(x = 257,y = 270)
        
        self.button_17 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "00", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2)
        self.button_17.place(x = 20,y = 335)
        self.button_18 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "0", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2)
        self.button_18.place(x = 99,y = 335)
        self.button_19 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = ".", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2)
        self.button_19.place(x = 178,y = 335)
        self.button_20 = tk.Button(master = self.oyna,font = ("arial",14,"bold"), text = "=", justify = "center", bg = "#808080",width = 4,pady = 10,bd = 2)
        self.button_20.place(x = 257,y = 335)


        self.oyna.mainloop()

if __name__ == "__main__":
    MyApp()
