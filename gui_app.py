import re
import tkinter as tk
from tkinter import messagebox

TOKENS = {
    "for": ("ID", "for"),
    "(": ("(", "_"),
    ")": (")", "_"),
    "int": ("data_type", "int"),
    ";": (";", "_"),
    ",": (",", "_"),
    "{": ("{", "_"),
    "}": ("}", "_"),
    "++": ("inc_opt", "++"),
    "--": ("dec_opt", "--"),
    "<=": ("rel_opt", "<="),
    ">=": ("rel_opt", ">="),
    "==": ("rel_opt", "=="),
    "!=": ("rel_opt", "!="),
    "<": ("rel_opt", "<"),
    ">": ("rel_opt", ">"),
    "+=": ("rel_opt", "+="),
    "-=": ("rel_opt", "-="),
    "*=": ("rel_opt", "*="),
    "/=": ("rel_opt", "/="),
    "=": ("assign_opt", "="),
    "+": ("arith_opt", "+"),
    "-": ("arith_opt", "-"),
    "*": ("arith_opt", "*"),
    "/": ("arith_opt", "/"),
    "[": ("[", "_"),
    "]": ("]", "_"),
    "print": ("program_output", "print"),
    "range": ("range", "_"),
    "in": ("in", "_"),
    "anynumber": ("int_const", "givennumber"),
}

def tokenize_program():
    user_input = text_input.get("1.0", "end-1c")
    lines = user_input.split('\n')

    tokens_listbox.delete(0, tk.END)

    for line_no, line in enumerate(lines, start=1):
        line_tokens = []
        words = re.findall(r"[\w']+|[(),;=+\-*/<>]+", line)

        for word in words:
            if word in TOKENS:
                token_class, token_value = TOKENS[word]
                line_tokens.append((word, token_class, token_value))
            else:
                if re.match(r"^\d+$", word):
                    line_tokens.append((word, "int_const", word))
                else:
                    line_tokens.append((word, "variable_name", word))

        tokens_listbox.insert(tk.END, f"Line {line_no}:")
        for token, token_class, token_value in line_tokens:
            tokens_listbox.insert(tk.END, f"  {token}\n    Class Part: {token_class}\n    Value Part: {token_value}")
        tokens_listbox.insert(tk.END, "")

app = tk.Tk()
app.title("For Loop Tokenizer")

app.configure(bg="#f0f0f0")
app.geometry("600x400")

title_label = tk.Label(app, text="For Loop Tokenizer", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

text_input = tk.Text(app, height=8, width=60, font=("Courier New", 12))
text_input.pack(padx=20, pady=(0, 10))

tokenize_button = tk.Button(app, text="Tokenize", command=tokenize_program, bg="#4caf50", fg="white",
                            font=("Helvetica", 12, "bold"), padx=20, pady=10)
tokenize_button.pack()

tokens_listbox = tk.Listbox(app, font=("Courier New", 10))
tokens_listbox.pack(fill=tk.BOTH, expand=True)

app.mainloop()
