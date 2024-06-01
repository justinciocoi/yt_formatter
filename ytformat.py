## imports

import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
from turtle import bgcolor

root = tk.Tk()
root.geometry("600x450")
root.title("YouTube Formatter") 
root.config(bg="#451515")

### USER INPUT FIELDS
label = tk.Label(root, text="YouTube Format Converter", font=('Helvetica', 18))
label.pack(pady=20)
label.config(bg="#451515")

instr1 = tk.Label(root, text="Enter YouTube URL: ", font=('Helvetica', 14))
instr1.pack(pady=20)
instr1.config(bg="#451515")

input1 = tk.Text(root, height=2, width=70, font=('Helvetica', 12))
input1.pack()
input1.config(bg="lightgray", fg="black")

instr2 = tk.Label(root, text="Select Format: ", font=('Helvetica', 14))
instr2.pack(pady=20)
instr2.config(bg="#451515")

### DROPDOWN MENU FOR FORMAT        
options = ["mp4", "mp3", "avi"]
selected_option = tk.StringVar(root)
selected_option.set(options[0])  # Set the default option
dropdown = tk.OptionMenu(root, selected_option, *options)
dropdown.pack(pady=0)   
dropdown.config(bg="#451515")

### DIRECTORY SELECTION
selected_directory = tk.StringVar(root)
selected_directory.set(os.path.expanduser('~'))

def open_directory_dialog():
    initial_dir = os.path.expanduser('~')
    directory = filedialog.askdirectory(initialdir=initial_dir)
    if directory:
        selected_directory.set(directory)
        
instr3 = tk.Label(root, text="Selected Directory:", font=('Helvetica', 14))
instr3.pack(pady=20)
instr3.config(bg="#451515")


selected_directory_label = tk.Label(root, textvariable=selected_directory, font=('Helvetica', 12))
selected_directory_label.pack()
selected_directory_label.config(bg="#451515")
select_directory_button = tk.Button(root, text="Select Directory", command=open_directory_dialog)
select_directory_button.pack()
select_directory_button.config(bg="#451515")

### BUTTON TO RUN
def run_shell_script():
    url = input1.get("1.0", "end-1c")
    format = selected_option.get()
    directory = selected_directory.get()

    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    script_path = "yt_formatter/scripts/yt_format.sh"  # Adjust to the correct relative or absolute path
    absolute_script_path = os.path.abspath(script_path)
    command = [absolute_script_path, url, format]
    try:
        process = subprocess.run(command, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=directory)
        print("Output:", process.stdout)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred: {e.stderr}")
        return

    # Assuming script outputs the file name without extension that was downloaded
    filename = process.stdout.strip()
    source_file = f"{filename}.{format}"
    destination_file = os.path.join(directory, source_file)

    try:
        os.rename(source_file, destination_file)
        messagebox.showinfo("Success", f"File moved successfully to {directory}")
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found. Check the script output and paths.")

button = tk.Button(root, text="Download and Convert", command=run_shell_script, font=('Helvetica', 18))
button.pack(pady=20)
button.config(bg="#451515")

root.mainloop()
