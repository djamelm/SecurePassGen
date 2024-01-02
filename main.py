import random
from tkinter import *
import pyperclip

lettres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
nombres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symboles = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generer_mot_de_passe():
    nb_lettres = int(lettres_spinbox.get())
    nb_symboles = int(symboles_spinbox.get())
    nb_nombres = int(nombres_spinbox.get())

    mot_de_passe = ""
    for i in range(nb_lettres):
        ran = random.randint(0, len(lettres) - 1)
        mot_de_passe += lettres[ran]
    for i in range(nb_nombres):
        ran = random.randint(0, len(nombres) - 1)
        mot_de_passe += str(nombres[ran])
    for i in range(nb_symboles):
        ran = random.randint(0, len(symboles) - 1)
        mot_de_passe += str(symboles[ran])

    result_display.config(text=mot_de_passe)
    copied_label.config(text="")  # Effacer le message copié

def copier_dans_le_presse_papiers():
    pyperclip.copy(result_display.cget("text"))
    copied_label.config(text="Copié dans le presse-papiers!")

root = Tk()
root.title("Générateur de mots de passe")
root.geometry('300x400')

input_frame = LabelFrame(root, text="Paramètres du mot de passe", padx=10, pady=10)
output_frame = LabelFrame(root, text="Mot de passe généré", padx=10, pady=10)

label_lettres = Label(input_frame, text="Nombre de lettres :")
label_symboles = Label(input_frame, text="Nombre de symboles :")
label_nombres = Label(input_frame, text="Nombre de chiffres :")
label_resultat = Label(output_frame, text="Mot de passe :")
copied_label = Label(output_frame, text="", fg="green")

lettres_spinbox = Spinbox(input_frame, from_=0, to=100)
symboles_spinbox = Spinbox(input_frame, from_=0, to=100)
nombres_spinbox = Spinbox(input_frame, from_=0, to=100)

bouton_generer = Button(input_frame, text="Générer le mot de passe", command=generer_mot_de_passe, font=('Helvetica', 10), padx=5)
bouton_copier = Button(output_frame, text="Copier dans le presse-papiers", command=copier_dans_le_presse_papiers, font=('Helvetica', 10), padx=5)

result_display = Label(output_frame, text="", font=('Helvetica', 12))

input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")
output_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

label_lettres.grid(row=0, column=0, sticky="w")
label_symboles.grid(row=1, column=0, sticky="w")
label_nombres.grid(row=2, column=0, sticky="w")
lettres_spinbox.grid(row=0, column=1, pady=5)
symboles_spinbox.grid(row=1, column=1, pady=5)
nombres_spinbox.grid(row=2, column=1, pady=5)
bouton_generer.grid(row=3, column=0, columnspan=2, pady=10)

label_resultat.grid(row=0, column=0, sticky="w")
copied_label.grid(row=3, column=0, columnspan=2)
bouton_copier.grid(row=2, column=0, columnspan=2, pady=10)

result_display.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
