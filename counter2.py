from tkinter import *
import tkinter as tk
import tkinter.font as TkFont


lst_paid = []
lst_free = []

def aver_paid():

    num_paid = number_paid.get()

    if len(num_paid) == 0:
        warn_paid.config(text="Enter a value please!")
    else:
        lst_paid.append(num_paid)

        for i in range(0, len(lst_paid)):
            lst_paid[i] = int(lst_paid[i])

        average_paid = sum(lst_paid) / len(lst_paid)
        number_paid.delete(0, END)

        final_av_paid = round(average_paid, 2)
        counter_label_paid.config(text=final_av_paid)
    #print(lst_paid)
    #print(average_paid)

def aver_free():

    num_free = number_free.get()

    if len(num_free) == 0:
        warn_free.config(text="Enter a value please!")
    else:
        lst_free.append(num_free)

        for i in range(0, len(lst_free)):
            lst_free[i] = int(lst_free[i])

        average_free = sum(lst_free) / len(lst_free)
        number_free.delete(0, END)

        final_av_free = round(average_free, 2)
        counter_label_free.config(text=final_av_free)

    #print(lst_free)
    #print(average_free)

root = Tk()

root.geometry("250x480")
root.title("Candidates Per Page Counter")



count_label_paid = tk.Label(root, text='# of good candidates  - All: ', font='Helvetica 10 bold')
count_label_paid.pack(pady = 10)

number_paid = tk.Entry(width=10)
number_paid.pack(pady=5)

counter_label_paid = tk.Label(text='0.00', font=('System', 20))
counter_label_paid.pack()

average_button_paid = tk.Button(text='Average All', width=15, font=('Arial', 10), command=aver_paid, bg="#ffa981")
average_button_paid.pack(pady = 1)

warn_paid = tk.Label(text='')
warn_paid.pack(pady=20)

count_label_free = tk.Label(root, text='# of good candidates - Free: ', font='Helvetica 10 bold')
count_label_free.pack(pady = 10)

number_free = tk.Entry(width=10)
number_free.pack(pady=5)

counter_label_free = tk.Label(text='0.00', font=('System', 20))
counter_label_free.pack()

average_button_free = tk.Button(text='Average free', width=15, font=('Arial', 10), command=aver_free, bg="#72ddc3")
average_button_free.pack(pady = 1)

warn_free = tk.Label(text='')
warn_free.pack(pady=20)


exit = tk.Button(text='exit', width=15, font=('Arial', 10), command=root.destroy, bg="#ffd764")
exit.pack(pady = 10)


root.attributes('-topmost', True)

root.mainloop()
