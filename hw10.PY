'''
Keagan Anderson
11/27/2023

This program offers an interactive way to determine an employees gross and net pay

'''

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
root = tk.Tk()
root.withdraw()
answer = True
while (answer):
    name = simpledialog.askstring("Type your full name", "Enter your name")

    hoursWorked = simpledialog.askinteger("Enter how many hours you worked", "Enter Hours")

    hourlyRate = simpledialog.askfloat("Enter your hourly rate", "Enter rate")

    grossPay = 0

    if hoursWorked > 40:
        timeHalf = hourlyRate*1.5
        grossPay += (40 * hourlyRate) 
        grossPay += ((hoursWorked-40)*(timeHalf))
    else:
        grossPay = (hoursWorked * hourlyRate)

    netPay = grossPay - (grossPay*.07)

    dialog = f"Hello {name}!\nYou worked {hoursWorked} hours this week at a rate of {hourlyRate} per hour\nYour gross pay is {grossPay:.2f}\nYour net pay is {netPay:.2f}\nHave a great day!"

    messagebox.showinfo("Results", dialog)
    answer = messagebox.askyesno("Ask Again", "Do you want to calculate another pay stub?")