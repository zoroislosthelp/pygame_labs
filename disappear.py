import tkinter as tk

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Most Dangerous Writing App")
        self.root.geometry("700x500")
        self.root.configure(bg="white")

        self.text_area = tk.Text(root, font=("Helvetica", 14), wrap="word", undo=False)
        self.text_area.pack(padx=20, pady=20, expand=True, fill="both")
        self.text_area.focus_set()

        self.text_area.bind("<Key>", self.reset_timer)

        self.timer_id = None
        self.inactivity_limit = 5000  # 5 seconds

    def reset_timer(self, event=None):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.timer_id = self.root.after(self.inactivity_limit, self.clear_text)

    def clear_text(self):
        self.text_area.delete("1.0", tk.END)
        self.timer_id = None

if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()
