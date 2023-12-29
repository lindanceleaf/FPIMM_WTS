import tkinter as tk
from tkinter import messagebox
import sys

selected_options = []

def get_option():
    return selected_options

def kill_window():
    root.destroy()

def choose_mode() -> list:
    def toggle_button_color(button):
        current_bg = button.cget("background")
        new_bg = "#65e665" if current_bg == "gray" else "gray"  # 使用淺綠色代表選擇
        button.config(background=new_bg)

    def get_selected_modes():
        global selected_options
        selected_options = [options[i] for i, button in enumerate(buttons) if button.cget("background") == "#65e665"]
        if not selected_options:
            choice = messagebox.askretrycancel("No file selected", "Retry to select a file?")
            if not choice:
                # print(selected_options)
                root.destroy()
                sys.exit()
        else:
            root.quit()

    global root
    root = tk.Tk()
    root.title("Mode Select")
    selected_options = []

    options = ['piano', 'vocals', 'drums', 'bass', 'other']

    buttons = []

    for i, option in enumerate(options):
        button = tk.Button(root, text=option, width=10, height=5, background="gray", font=('Arial', 14, 'bold'), command=lambda b=i: toggle_button_color(buttons[b]))
        button.pack(padx=10, pady=5)
        buttons.append(button)

    submit_button = tk.Button(root, text="Selected", command=lambda:get_selected_modes(), font=('Arial', 14, 'bold'))
    submit_button.pack(pady=10)

    root.update_idletasks()
    width = root.winfo_width() + 80
    height = root.winfo_height()
    x_offset = (root.winfo_screenwidth() - width) // 2
    y_offset = (root.winfo_screenheight() - height) // 2
    root.geometry(f"{width}x{height}+{x_offset}+{y_offset}")
    root.resizable(False, False)
    root.mainloop()
