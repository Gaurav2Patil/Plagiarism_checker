import difflib
import tkinter as tk
from tkinter import scrolledtext, Button, Label

# Function to calculate similarity using difflib
def calculate_similarity():
    input_code = input_code_widget.get("1.0", "end-1c")
    similarity_score = check_plagiarism(input_code)
    similarity_label.config(text=f"Plagiarism Score: {similarity_score:.2%}")

def clear_input():
    input_code_widget.delete("1.0", tk.END)
    similarity_label.config(text="")

def check_plagiarism(input_code):
    similarity_scores = []

    for code in code_samples:  # Replace this with web scraping and actual code comparison
        similarity_ratio = difflib.SequenceMatcher(None, input_code, code).ratio()
        similarity_scores.append(similarity_ratio)

    return max(similarity_scores, default=0)

# Sample code snippets (replace with web-scraped content)
code_samples = [
    "for i in range(10):\n    print(i)",
    "for x in range(10):\n    print(x)",
    "while True:\n    print('Hello, World!')"
]

# Create the main window
root = tk.Tk()
root.title("Plagiarism Checker")

# Create and place widgets
input_label = Label(root, text="Enter your code:")
input_label.pack()

input_code_widget = scrolledtext.ScrolledText(root, height=10, width=50)
input_code_widget.pack()

check_button = Button(root, text="Check Plagiarism", command=calculate_similarity)
check_button.pack()

clear_button = Button(root, text="Clear Input", command=clear_input)
clear_button.pack()

similarity_label = Label(root, text="")
similarity_label.pack()

# Start the main loop
root.mainloop()
