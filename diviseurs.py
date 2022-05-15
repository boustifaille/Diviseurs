# boustifaille
import os
try:
    import tkinter as tk
except ImportError:
    os.system("pip3 install tkinter")


def division():
    liste = []
    try:
        a = int(text1.get())
        b = int(text2.get())
        c = int(text3.get())
    except:
        a = 1
        b = 1
        c = 1

    for i in range(2, 501):
        if a%i == 0 and b%i == 0 and c%i == 0:
            liste.append(i)
    result.config(text=f"Résultat : {liste}")
# défini root
root = tk.Tk()
root.title("Diviseurs")
root['bg'] = "#728395"
#root.iconbitmap('perso\Diviseurs\icon.ico')

# créer les boutons, les textes et les champs
button = tk.Button(root, text="Calculer", command=lambda : division(), background="#ea8d82")
text1 = tk.Entry(root, background="#728395")
text2 = tk.Entry(root, background="#728395")
text3 = tk.Entry(root, background="#728395")
tk_a = tk.Label(root, text="1er nombre : ", background="#728395")
tk_b = tk.Label(root, text="2ème nombre : ", background="#728395")
tk_c = tk.Label(root, text="3ème nombre : ", background="#728395")
result = tk.Label(root, background="#728395")
# affiche tout
tk_a.grid(column=0, row=1)
text1.grid(column=2, row=1)
tk_b.grid(column=0, row=2)
text2.grid(column=2, row=2)
tk_c.grid(column=0, row=3)
text3.grid(column=2, row=3)
button.grid(column=1, row=4)
result.grid(column=1, row=5)

root.mainloop()