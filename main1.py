import tkinter as tk
from tkinter import messagebox
import random
import string
from tkinter import filedialog

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        # Variables
        self.password_length = tk.IntVar()
        self.include_letters = tk.BooleanVar()
        self.include_symbols = tk.BooleanVar()
        self.include_numbers = tk.BooleanVar()
        self.file_path = tk.StringVar()
        self.generated_password = tk.StringVar()

        # GUI Elements
        tk.Label(master, text="Password Length:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(master, textvariable=self.password_length).grid(row=0, column=1, padx=10, pady=5)

        tk.Checkbutton(master, text="Include Letters", variable=self.include_letters).grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=5)
        tk.Checkbutton(master, text="Include Symbols", variable=self.include_symbols).grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=5)
        tk.Checkbutton(master, text="Include Numbers", variable=self.include_numbers).grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        tk.Label(master, text="Save Password to File:").grid(row=4, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(master, textvariable=self.file_path).grid(row=4, column=1, padx=10, pady=5)
        tk.Button(master, text="Browse", command=self.browse_file).grid(row=4, column=2, padx=5, pady=5)

        tk.Button(master, text="Generate Password", command=self.generate_password).grid(row=5, column=0, columnspan=3, pady=10)
        tk.Entry(master, textvariable=self.generated_password, state='readonly', width=30).grid(row=6, column=0, columnspan=3, padx=10, pady=5)

        tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard).grid(row=7, column=0, columnspan=3, pady=10)

        tk.Button(master, text="Save to File", command=self.save_to_file).grid(row=8, column=0, columnspan=3, pady=10)

    def generate_password(self):
        length = self.password_length.get()
        include_letters = self.include_letters.get()
        include_symbols = self.include_symbols.get()
        include_numbers = self.include_numbers.get()

        characters = ""
        if include_letters:
            characters += string.ascii_letters
        if include_symbols:
            characters += string.punctuation
        if include_numbers:
            characters += string.digits

        if not characters:
            messagebox.showwarning("Warning", "Please select at least one option for character inclusion.")
            return

        generated_password = ''.join(random.choice(characters) for _ in range(length))
        self.generated_password.set(generated_password)

    def copy_to_clipboard(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.generated_password.get())
        self.master.update()

    def save_to_file(self):
        file_path = self.file_path.get()
        if not file_path:
            messagebox.showwarning("Warning", "Please enter a file path.")
            return

        try:
            with open(file_path, 'a') as file:
                file.write(self.generated_password.get() + '\n')
                messagebox.showinfo("Success", "Password saved to file.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def browse_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            self.file_path.set(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
