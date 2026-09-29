"""Application Ticker : bouge la souris et clique toutes les 5 secondes entre Start et Stop."""

import tkinter as tk

import pyautogui

INTERVALLE_MS = 5000  # 5 secondes
DEPLACEMENT = 50  # pixels


class MouseMoveApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ticker")
        self.root.geometry("260x150")
        self.root.resizable(False, False)

        self.actif = False
        self.job = None
        self.sens = 1

        self.label = tk.Label(root, text="Arrêté", font=("Arial", 14), fg="red")
        self.label.pack(pady=15)

        boutons = tk.Frame(root)
        boutons.pack()
        self.btn_start = tk.Button(boutons, text="Start", width=10, bg="#4CAF50",
                                   fg="white", command=self.start)
        self.btn_start.pack(side=tk.LEFT, padx=5)
        self.btn_stop = tk.Button(boutons, text="Stop", width=10, bg="#f44336",
                                  fg="white", command=self.stop, state=tk.DISABLED)
        self.btn_stop.pack(side=tk.LEFT, padx=5)

        self.compteur = tk.Label(root, text="Mouvements : 0")
        self.compteur.pack(pady=10)
        self.nb_mouvements = 0

        self.root.protocol("WM_DELETE_WINDOW", self.quitter)

    def start(self):
        if self.actif:
            return
        self.actif = True
        self.label.config(text="En cours...", fg="green")
        self.btn_start.config(state=tk.DISABLED)
        self.btn_stop.config(state=tk.NORMAL)
        self.job = self.root.after(INTERVALLE_MS, self.bouger)

    def stop(self):
        self.actif = False
        if self.job is not None:
            self.root.after_cancel(self.job)
            self.job = None
        self.label.config(text="Arrêté", fg="red")
        self.btn_start.config(state=tk.NORMAL)
        self.btn_stop.config(state=tk.DISABLED)

    def bouger(self):
        if not self.actif:
            return
        # Aller-retour pour que la souris ne dérive pas vers le bord de l'écran
        pyautogui.moveRel(DEPLACEMENT * self.sens, 0, duration=0.25)
        pyautogui.click()  # clic gauche à la nouvelle position
        self.sens *= -1
        self.nb_mouvements += 1
        self.compteur.config(text=f"Mouvements : {self.nb_mouvements}")
        self.job = self.root.after(INTERVALLE_MS, self.bouger)

    def quitter(self):
        self.stop()
        self.root.destroy()


if __name__ == "__main__":
    pyautogui.FAILSAFE = True  # souris dans un coin de l'écran = arrêt d'urgence
    root = tk.Tk()
    MouseMoveApp(root)
    root.mainloop()
