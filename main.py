import random
from tkinter import *
import pyperclip
from tkinter import filedialog

# Listes des caractères disponibles
lettres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
           'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']
nombres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symboles = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Fonction pour générer un mot de passe
def generer_mot_de_passe():
    longueur_mot_de_passe = int(longueur_spinbox.get())

    mot_de_passe = ""
    
    # Liste des caractères à inclure dans le mot de passe
    caracteres = []

    if lettres_check.get():
        caracteres.extend(lettres)
    if symboles_check.get():
        caracteres.extend(symboles)
    if nombres_check.get():
        caracteres.extend(nombres)

    if not caracteres:
        result_display.config(text="Veuillez sélectionner au moins un type de caractère.")
        return
    
    # Générer le mot de passe en choisissant aléatoirement parmi les caractères sélectionnés
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur_mot_de_passe))

    result_display.config(text=mot_de_passe)
    copied_label.config(text="")  # Effacer le message copié

# Fonction pour sauvegarder le mot de passe dans un fichier
def sauvegarder_mot_de_passe():
    mot_de_passe = result_display.cget("text")
    if mot_de_passe:
        fichier = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
        if fichier:
            with open(fichier, 'w') as file:
                file.write(mot_de_passe)
                copied_label.config(text="Mot de passe sauvegardé dans {}".format(fichier))
                entry_chemin.config(state='normal')  # Activer l'entrée
                entry_chemin.delete(0, END)
                entry_chemin.insert(0, fichier)
                entry_chemin.config(state='readonly')  # Désactiver l'entrée après mise à jour

# Fonction pour copier le mot de passe dans le presse-papiers
def copier_dans_le_presse_papiers():
    pyperclip.copy(result_display.cget("text"))
    copied_label.config(text="Copié dans le presse-papiers!")

# Interface graphique
root = Tk()
root.title("Générateur de mots de passe")
root.geometry('400x450')

# Barre de menu
barre_menu = Menu(root)
root.config(menu=barre_menu)

menu_fichier = Menu(barre_menu, tearoff=0)
barre_menu.add_cascade(label="Fichier", menu=menu_fichier)
menu_fichier.add_command(label="Sauvegarder mot de passe", command=sauvegarder_mot_de_passe)

# Cadres pour organiser l'interface graphique
input_frame = LabelFrame(root, text="Paramètres du mot de passe", padx=10, pady=10)
output_frame = LabelFrame(root, text="Mot de passe généré", padx=10, pady=10)
chemin_frame = LabelFrame(root, text="Chemin de sauvegarde", padx=10, pady=10)

# Widgets pour l'entrée de l'utilisateur
label_longueur = Label(input_frame, text="Longueur du mot de passe :")
longueur_spinbox = Spinbox(input_frame, from_=1, to=100)

lettres_check = IntVar()
symboles_check = IntVar()
nombres_check = IntVar()

label_longueur.grid(row=3, column=0, sticky="w")
longueur_spinbox.grid(row=3, column=1, pady=5)

label_lettres = Checkbutton(input_frame, text="Inclure les lettres", variable=lettres_check)
label_symboles = Checkbutton(input_frame, text="Inclure les symboles", variable=symboles_check)
label_nombres = Checkbutton(input_frame, text="Inclure les chiffres", variable=nombres_check)
label_resultat = Label(output_frame, text="Mot de passe :")
copied_label = Label(output_frame, text="", fg="green")

# Boutons pour générer, copier et sauvegarder le mot de passe
bouton_generer = Button(input_frame, text="Générer le mot de passe", command=generer_mot_de_passe, font=('Helvetica', 10), padx=5)
bouton_copier = Button(output_frame, text="Copier dans le presse-papiers", command=copier_dans_le_presse_papiers, font=('Helvetica', 10), padx=5)
bouton_sauvegarder = Button(output_frame, text="Sauvegarder", command=sauvegarder_mot_de_passe, font=('Helvetica', 10), padx=5)

# Affichage du mot de passe généré
result_display = Label(output_frame, text="", font=('Helvetica', 12))
entry_chemin = Entry(chemin_frame, width=30, textvariable=StringVar(), state='readonly', relief='flat')

# Organisation des widgets dans les cadres
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")
output_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")
chemin_frame.grid(row=2, column=0, padx=10, pady=10, sticky="w")

label_lettres.grid(row=0, column=0, sticky="w")
label_symboles.grid(row=1, column=0, sticky="w")
label_nombres.grid(row=2, column=0, sticky="w")
bouton_generer.grid(row=4, column=0, columnspan=2, pady=10)

label_resultat.grid(row=0, column=0, sticky="w")
result_display.grid(row=1, column=0, columnspan=2, pady=10)
bouton_copier.grid(row=2, column=0, columnspan=2, pady=10)
copied_label.grid(row=3, column=0, columnspan=2)
bouton_sauvegarder.grid(row=5, column=0, columnspan=2, pady=10)
entry_chemin.grid(row=1, column=0, pady=5)


# Boucle principale de la fenêtre Tkinter
root.mainloop()
