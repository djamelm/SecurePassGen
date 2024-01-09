import random
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class PasswordGeneratorApp:
	def __init__(self, master):
		self.master = master
		self.master.title("Password Generator")

		# Variables
		self.lettres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
				'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
				'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
				'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
				'W', 'X', 'Y', 'Z']
		self.nombres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		self.symboles = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
		self.password_length = tk.IntVar()
		self.include_letters = tk.BooleanVar()
		self.include_symbols = tk.BooleanVar()
		self.include_numbers = tk.BooleanVar()
		self.file_path = tk.StringVar()
		self.generated_password = tk.StringVar()

		# Create frames
		self.create_menu_bar()
		self.create_input_frame()
		self.create_password_frame()
		self.create_buttons_frame()

	def create_input_frame(self):
		frame = tk.LabelFrame(self.master, text="Paramètres du mot de passe", padx=10, pady=10)
		frame.grid(row=0, column=0, padx=10, pady=5, sticky="w")

		tk.Label(frame, text="Password Length:").grid(row=0, column=0, sticky="w")
		tk.Entry(frame, textvariable=self.password_length).grid(row=0, column=1, padx=10)

		tk.Checkbutton(frame, text="Include Letters", variable=self.include_letters).grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=5)
		tk.Checkbutton(frame, text="Include Symbols", variable=self.include_symbols).grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=5)
		tk.Checkbutton(frame, text="Include Numbers", variable=self.include_numbers).grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=5)

	def create_password_frame(self):
		frame = tk.LabelFrame(self.master, text="Mot de passe généré", padx=10, pady=10)
		frame.grid(row=1, column=0, padx=10, pady=5, sticky="w")

		tk.Button(frame, text="Generate Password", command=self.generate_password).grid(row=0, column=0, columnspan=3, pady=10)
		tk.Entry(frame, textvariable=self.generated_password, state='readonly', width=30).grid(row=1, column=0, columnspan=3, padx=10, pady=5)
		tk.Button(frame, text="Copy to Clipboard", command=self.copy_to_clipboard).grid(row=2, column=0, columnspan=3, pady=10)

	def create_buttons_frame(self):
		frame = tk.LabelFrame(self.master, text="Chemin de sauvegarde", padx=10, pady=10)
		frame.grid(row=2, column=0, padx=10, pady=5)

		tk.Label(frame, text="Save Password to File:").grid(row=4, column=0, sticky="w", pady=5)
		tk.Entry(frame, textvariable=self.file_path).grid(row=4, column=1, padx=10)
		tk.Button(frame, text="Browse", command=self.browse_file).grid(row=4, column=2, padx=5)

		tk.Button(frame, text="Save to File", command=self.save_to_file).grid(row=1, column=0, columnspan=3, pady=10)
	def create_menu_bar(self):
		menubar = tk.Menu(self.master)
		self.master.config(menu=menubar)

		file_menu = tk.Menu(menubar, tearoff=0)
		edit_menu = tk.Menu(menubar, tearoff=0)
		help_menu = tk.Menu(menubar, tearoff=0)

		self.create_file_menu(file_menu)
		self.create_edit_menu(edit_menu)
		self.create_help_menu(help_menu)

		menubar.add_cascade(label="Fichier", menu=file_menu)
		menubar.add_cascade(label="Editer", menu=edit_menu)
		menubar.add_cascade(label="Aide", menu=help_menu)
  
	def create_file_menu(self, file_menu):
		file_menu.add_command(label="Enregistrer", command=self.save_to_file)
		file_menu.add_separator()
		file_menu.add_command(label="Quitter", command=self.master.destroy)
	
	def create_edit_menu(self, edit_menu):
		edit_menu.add_command(label="Undo", command=self.undo_action)
		edit_menu.add_command(label="Redo", command=self.redo_action)
		edit_menu.add_separator()
		edit_menu.add_command(label="Cut", command=self.cut_action)
		edit_menu.add_command(label="Copy", command=self.copy_action)
		edit_menu.add_command(label="Paste", command=self.paste_action)

	def create_help_menu(self, help_menu):
		help_menu.add_command(label="Documentation", command=self.open_documentation)
		help_menu.add_separator()
		help_menu.add_command(label="About", command=self.show_about_info)

	def undo_action(self):
		# Implement undo functionality here
		pass

	def redo_action(self):
		# Implement redo functionality here
		pass

	def cut_action(self):
		# Implement cut functionality here
		pass

	def copy_action(self):
		# Implement copy functionality here
		pass

	def paste_action(self):
		# Implement paste functionality here
		pass

	def open_documentation(self):
		# Implement opening documentation action here
		pass

	def show_about_info(self):
		about_info = "SecurePassGen\nVersion 2.0\n© 2024 Djamel Eddine MEKKI"
		messagebox.showinfo("About", about_info)


	def generate_password(self):
		longueur_mot_de_passe = int(self.password_length.get())

		mot_de_passe = ""
		
		# Liste des caractères à inclure dans le mot de passe
		caracteres = []

		if self.include_letters.get():
			caracteres.extend(self.lettres)
		if self.include_symbols.get():
			caracteres.extend(self.symboles)
		if self.include_numbers.get():
			caracteres.extend(self.nombres)

		if not caracteres:
			messagebox.showwarning("Warning", "Please select at least one option for character inclusion.")
			return
		
		# Générer le mot de passe en choisissant aléatoirement parmi les caractères sélectionnés
		mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur_mot_de_passe))
		self.generated_password.set(mot_de_passe)

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
