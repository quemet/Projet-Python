from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Fenêtre principale
fenetre = Tk()
fenetre.geometry("700x700")
fenetre.title("To-Do List")

tasks = [
    { 
        "title": "Sample1", 
        "description": "Sample1"
    },
    {
        "title": "Sample2",
        "description": "Sample2"
    }
]

def ajouter_tache(title, description):
    global tasks
    tasks.append({"title": title, "description": description})
    afficher_ui()
    messagebox.showinfo("Information", "Tâche ajoutée avec succès!")

def modifier_tache(old_title, old_description, new_title, new_description):
    global tasks
    for task in tasks:
        if task['title'] == old_title and task['description'] == old_description:
            task['title'] = new_title
            task['description'] = new_description
            break
    afficher_ui()
    messagebox.showinfo("Information", "Tâche modifiée avec succès!")

def supprimmer_tache(title, description):
    global tasks
    tasks = [task for task in tasks if not (task['title'] == title and task['description'] == description)]
    afficher_ui()
    messagebox.showinfo("Information", "Tâche supprimée avec succès!")

def ui_modifier_tache(title, description):
    fenetre_modify_task = Toplevel(fenetre)
    fenetre_modify_task.geometry("400x300")
    fenetre_modify_task.title("Modifier une tâche")

    label_title = Label(fenetre_modify_task, text="Entrer le titre de votre tâche :")
    label_title.pack(pady=10)

    entry_title = Entry(fenetre_modify_task)
    entry_title.insert(0, title)
    entry_title.pack(pady=5)

    label_description = Label(fenetre_modify_task, text="Entrer la description de la tâche :")
    label_description.pack(pady=10)

    entry_description = Entry(fenetre_modify_task)
    entry_description.insert(0, description)
    entry_description.pack(pady=5)

    def submit_task():
        new_title = entry_title.get()
        new_description = entry_description.get()
        if new_title and new_description:
            modifier_tache(title, description, new_title, new_description)
            fenetre_modify_task.destroy()
        else:
            messagebox.showwarning("Attention", "Veuillez remplir tous les champs.")

    button_submit = Button(fenetre_modify_task, text="Modifier la tâche", command=submit_task)
    button_submit.pack(pady=20)

def ui_ajouter_tache():
    fenetre_add_task = Toplevel(fenetre)
    fenetre_add_task.geometry("400x300")
    fenetre_add_task.title("Ajouter une tâche")

    label_title = Label(fenetre_add_task, text="Entrer le titre de votre tâche :")
    label_title.pack(pady=10)

    entry_title = Entry(fenetre_add_task)
    entry_title.pack(pady=5)

    label_description = Label(fenetre_add_task, text="Entrer la description de la tâche :")
    label_description.pack(pady=10)

    entry_description = Entry(fenetre_add_task)
    entry_description.pack(pady=5)

    def submit_task():
        title = entry_title.get()
        description = entry_description.get()
        if title and description:
            ajouter_tache(title, description)
            fenetre_add_task.destroy()
        else:
            messagebox.showwarning("Attention", "Veuillez remplir tous les champs.")

    button_submit = Button(fenetre_add_task, text="Ajouter la tâche", command=submit_task)
    button_submit.pack(pady=20)

def afficher_ui():
    for widget in fenetre.winfo_children():
        widget.destroy()
    
    label_title = Label(fenetre, text="Voici votre liste des tâches :")
    label_title.pack(pady=10)
    
    for task in tasks:
        frame_task = Frame(fenetre, relief="groove", bd=2, padx=10, pady=5)
        frame_task.pack(pady=5, fill="x")

        label_task = Label(frame_task, text=f"Titre : {task['title']}\nDescription : {task['description']}")
        label_task.pack(side="left", padx=10)

        delete_icon = ImageTk.PhotoImage(Image.open("delete_icon.png").resize((20, 20)))
        button_delete = Button(frame_task, image=delete_icon, command=lambda t=task: supprimmer_tache(t['title'], t['description']))
        button_delete.image = delete_icon
        button_delete.pack(side="right", padx=5)

        modify_icon = ImageTk.PhotoImage(Image.open("edit_icon.png").resize((20, 20)))
        button_modify = Button(frame_task, image=modify_icon, command=lambda t=task: ui_modifier_tache(t['title'], t['description']))
        button_modify.image = modify_icon
        button_modify.pack(side="right", padx=5)
    
    button_add_task = Button(fenetre, text="Ajouter une tâche", command=ui_ajouter_tache)
    button_add_task.pack(pady=20)

afficher_ui()

fenetre.mainloop()
