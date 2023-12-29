import tkinter as tk
from tkinter import filedialog, messagebox

def select_file():                                                                                                                                                                                                               
    root = tk.Tk()
    root.withdraw()

    while True:
        file_path = filedialog.askopenfilename(initialdir="audio", title="Select a file")
        if file_path:
            break
        else:
            choice = messagebox.askretrycancel("No file selected", "Retry to select a file?")
            if not choice:
                break
    return file_path[file_path.rfind('/')+1:]

# select_file()