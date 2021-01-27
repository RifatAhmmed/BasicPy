from tkinter import Tk, Radiobutton, Button, StringVar, IntVar, Entry, Label

class TipCalculator():
        
    def __init__(self):
        window = Tk()
        window.title("Tip Calculator")
        window.configure(bg = 'sky blue')
        window.geometry('400x250')
        window.resizable(width=False, height=False)

        self.meal_cost = StringVar()
        self.tip_percent = IntVar()
        self.tip = StringVar()
        self.total_cost = StringVar()

        tip_percent = Label(window, text="Tip Percentages", bg='purple', fg='white', width=14)
        tip_percent.grid(column=0, row=0, padx=15, pady=15)
        
        bill_ammount = Label(window, text="Bill Ammount", bg='black', fg='white', width=14)
        bill_ammount.grid(column=1, row=0, padx=15)

        bill_ammount_entry = Entry(window, textvariable = self.meal_cost, width=14)
        bill_ammount_entry.grid(column=2, row=0, padx=15)

        five_percent_tip = Radiobutton(window, text="5%", value= 5, variable=self.tip_percent, width=4)
        five_percent_tip.grid(column=0, row=1, pady=1)
        ten_percent_tip = Radiobutton(window, text="10%", value= 10, variable=self.tip_percent, width=4)
        ten_percent_tip.grid(column=0, row=2,pady=1)
        fifteen_percent_tip = Radiobutton(window, text="15%", value=15, variable=self.tip_percent, width=4)
        fifteen_percent_tip.grid(column=0, row=3,pady=1)
        twenty_percent_tip = Radiobutton(window, text="20%", value=20, variable=self.tip_percent, width=4)
        twenty_percent_tip.grid(column=0, row=4, pady=1)
        thirty_percent_tip = Radiobutton(window, text="30%", value=30, variable=self.tip_percent, width=4)
        thirty_percent_tip.grid(column=0, row=5, pady=1)
        
        tip_ammount_lbl = Label(window, text="Tip Ammount", bg="brown", fg="white", width=14)
        tip_ammount_lbl.grid(column=1, row=2)
        tip_ammount_entry = Entry(window,textvariable=self.tip,width=14)
        tip_ammount_entry.grid(column=2, row=2)

        bill_ammount_lbl = Label(window, text="Total Bill", bg="blue", fg="white", width=14)
        bill_ammount_lbl.grid(column=1, row=4, padx=15)
        bill_ammount_entry = Entry(window, textvariable=self.total_cost, width=14)
        bill_ammount_entry.grid(column=2, row=4)
        
        calculate_btn = Button(window, text="Calculate", bg='green', fg='white', command=self.calculate)
        calculate_btn.grid(column=1,row=6)
        clear_btn = Button(window, text="Clear", bg='red', fg='white', command=self.clear)
        clear_btn.grid(column=2, row=6)


        window.mainloop()


    def calculate(self):
        pre_tip = float(self.meal_cost.get())
        percentage = self.tip_percent.get() / 100
        tip_ammount_entry = pre_tip * percentage
        self.tip.set(tip_ammount_entry)

        final_bill = pre_tip + tip_ammount_entry
        self.total_cost.set(final_bill)

    def clear(self):
        self.total_cost.set("")
        self.meal_cost.set("")
        self.tip.set("")

TipCalculator()

