import tkinter as tk
import time

sample_text = "The quick brown fox jumps over the lazy dog."

def start_typing(event):
    global start_time
    if not start_time:
        start_time = time.time()

def calculate_speed():
    end_time = time.time()
    typed = input_text.get("1.0", tk.END).strip()
    words = typed.split()
    time_taken = end_time - start_time
    if time_taken > 0:
        wpm = round(len(words) / (time_taken / 60))
        result_label.config(text=f"Typing Speed: {wpm} WPM")
    else:
        result_label.config(text="Error: Time not valid")

def reset_test():
    global start_time
    start_time = None
    input_text.delete("1.0", tk.END)
    result_label.config(text="")
    input_text.focus()

root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("600x400")
root.resizable(False, False)

start_time = None

title_label = tk.Label(root, text="Typing Speed Test", font=("Helvetica", 18, "bold"))
title_label.pack(pady=10)

text_label = tk.Label(root, text="Type the following text:", font=("Helvetica", 12))
text_label.pack()

sample_label = tk.Label(root, text=sample_text, wraplength=550, font=("Helvetica", 12), fg="blue")
sample_label.pack(pady=5)

input_text = tk.Text(root, height=7, width=70, font=("Helvetica", 12))
input_text.pack()
input_text.bind("<KeyPress>", start_typing)

submit_button = tk.Button(root, text="Done", command=calculate_speed, font=("Helvetica", 12), bg="green", fg="white")
submit_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=reset_test, font=("Helvetica", 12), bg="orange", fg="white")
reset_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

root.mainloop()
