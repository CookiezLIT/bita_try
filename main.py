import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import ttk


def save():
    '''
    :return: nothing, it just overwrites the file
    '''
    text_text = entry.get()
    with open('output.txt', 'a') as file_object:
        file_object.write(text_text + "\n")


if __name__ == '__main__':
    # run this module in the main program
    window = tk.Tk()  # i created a window and below i gave it a name
    window.title("I made smth")
    label = tk.Label(text="Hi, please write whatever you want to tell me",
                     background="#89CFF0",
                     width=40,
                     height=5
                     )

    label.pack()
    style = ttk.Style()
    style.configure('TEntry', foreground='purple')
    entry_field_variable = tk.StringVar()
    entry = ttk.Entry(window,
                      textvariable=entry_field_variable,
                      font=('courier', 15, 'bold')
                      )  # some entry text variable
    entry.pack(ipadx=30, ipady=10)
    tk.Button(window, text="save",
              command=save).pack()  # inline command to create a button which saves my entry text to file

    window.mainloop()
