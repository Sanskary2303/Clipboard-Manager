import tkinter as tk
from tkinter import ttk
import pyperclip
import threading
import keyboard

class ClipboardSaverApp:
    def __init__(self):
        self.root = None
        self.copied_texts = []

    def create_widgets(self):
        self.root = tk.Tk()
        self.root.title("Clipboard Saver")
        
        self.label = tk.Label(self.root, text="Copied Text:")
        self.label.pack(pady=5)

        self.textbox_frame = tk.Frame(self.root)
        self.textbox_frame.pack(pady=5)

        self.textbox = tk.Text(self.textbox_frame, width=50, height=10)
        self.textbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.textbox_frame, orient=tk.VERTICAL, command=self.textbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.textbox.config(yscrollcommand=self.scrollbar.set)

        self.copy_button = tk.Button(self.root, text="Copy All", command=self.copy_all)
        self.copy_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.copy_selected_button = tk.Button(self.root, text="Copy Selected", command=self.copy_selected)
        self.copy_selected_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.clear_button = tk.Button(self.root, text="Clear All", command=self.clear_text)
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)

    def monitor_clipboard(self):
        # Function to monitor clipboard and update textbox
        def check_clipboard():
            current_text = pyperclip.paste().strip()
            if current_text and current_text not in self.copied_texts:
                self.copied_texts.append(current_text)
                self.update_textbox()
            threading.Timer(1, check_clipboard).start()  # Check clipboard every second

        check_clipboard()

    def update_textbox(self):
        self.textbox.delete("1.0", tk.END)
        for i, text in enumerate(self.copied_texts):
            self.textbox.insert(tk.END, f"{text}\n{'-' * 50}\n" if i < len(self.copied_texts) - 1 else text)

    def copy_all(self):
        pyperclip.copy("\n".join(self.copied_texts))

    def copy_selected(self):
        selected_text = self.textbox.get(tk.SEL_FIRST, tk.SEL_LAST)
        if selected_text:
            pyperclip.copy(selected_text)

    def clear_text(self):
        self.copied_texts.clear()
        pyperclip.copy("")  # Clear clipboard
        self.update_textbox()

def show_app():
    app = ClipboardSaverApp()
    app.create_widgets()
    app.monitor_clipboard()
    app.root.mainloop()

def monitor_ctrl_g():
    keyboard.add_hotkey('ctrl+g', lambda: show_app())
    keyboard.wait('esc')  # Wait for 'esc' key to exit

if __name__ == "__main__":
    monitor_ctrl_g()
