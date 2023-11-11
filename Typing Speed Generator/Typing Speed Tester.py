import tkinter as tk
from tkinter import ttk
import random
import time
import difflib

class TypingSpeedTester:


    def __init__(self, master):
        self.master = master
        master.title("Typing Speed Tester")
        master.geometry("600x400")  # Set the window size
        self.create_widgets()
        self.setup_text()
        self.start_time = None
        self.total_words = 0
        self.correct_words = 0

    def create_widgets(self):
        self.text_label = ttk.Label(self.master, text="Type the text below:" , font=("Arial", 12))
        self.text_label.pack(pady=10)

        self.reference_label = ttk.Label(self.master, text="", font=("Arial", 12))
        self.reference_label.pack()

        self.text_display = ttk.Entry(self.master, font=("Arial", 12), width=50)
        self.text_display.pack()

        self.result_label = ttk.Label(self.master, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.start_button = ttk.Button(self.master, text="Start Typing Test", command=self.start_test)
        self.start_button.pack()

        # List of reference sentences
        self.reference_sentences = [
            "Practice makes man perfect",
            "The quick brown fox jumps over the lazy dog.",
            "A watched pot never boils.",
            "All that glitters is not gold.",
            "Action speak louder than words.",
            "You can't judge a book by its cover.",
            "The sun also rises, and the wind goes round and round.",
            "An apple,a day,keeps the doctor away."
        ]
    def setup_text(self):
        self.text = random.choice(self.reference_sentences)  # Randomly select a reference sentence
        self.reference_label.config(text=self.text)
        self.text_display.delete(0, tk.END)
        self.result_label.config(text="")

    def start_test(self):
        self.setup_text()
        self.start_button.config(state="disabled")
        self.text_display.config(state="normal")
        self.text_display.bind('<Return>', self.check_typing)
        self.start_time = time.time()
        self.total_words = 0
        self.correct_words = 0

    def check_typing(self, event):
        typed_text = self.text_display.get()
        typed_words = typed_text.split()
        original_words = self.text.split()
        self.total_words = len(original_words)
        self.correct_words = sum(1 for typed, original in zip(typed_words, original_words) if typed == original)
        if typed_words == original_words:
            elapsed_time = time.time() - self.start_time
            minutes = elapsed_time / 60
            wpm = int(self.total_words / minutes)
            accuracy = int((self.correct_words / self.total_words) * 100)
            self.result_label.config(text=f"Your typing speed: {wpm} WPM | Accuracy: {accuracy}%")
        else:
            self.result_label.config(text="Typing does not match. please try again.")
        self.start_button.config(state="Active")
        self.text_display.config(state="disabled")
        self.text_display.delete(0, tk.END)      # Clear the entry box

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTester(root)
    root.mainloop()












