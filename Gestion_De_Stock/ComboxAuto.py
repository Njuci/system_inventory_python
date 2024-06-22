import tkinter as tk
from tkinter import ttk

class AutoCompleteCombobox(ttk.Combobox):
	"""Combobox avec auto-complétion."""
	def __init__(self, parent, *args):
    	super().__init__(parent, *args, *combobox_kwargs)
    	self._completion_list = []
    	self._completion_index = 0
    	self.bind("<KeyRelease>", self._on_key_release)

	def set_completion_list(self, completion_list):
    	"""Définit la liste des options d'auto-complétion."""
    	self._completion_list = completion_list
    	self._completion_index = 0

	def _on_key_release(self, event):
    	"""Gère l'événement de relâchement de touche."""
    	self.current(0)
    	entry_text = self.get()

    	if entry_text:
        	matches = [x for x in self._completion_list if entry_text.lower() in x.lower()]
        	if matches:
            	self._completion_index = 0
            	self.set_completion_list(matches)
            	self.current(self._completion_index)
            	self.selection_range(0, len(entry_text))
    	else:
        	self.set_completion_list(self._completion_list)

# Créer la fenêtre principale
root = tk.Tk()
root.title("Combobox avec auto-complétion")

# Créer la combobox avec auto-complétion
data = ["Paris", "Lyon", "Marseille", "Toulouse", "Bordeaux", "Lille", "Nice", "Nantes"]
combobox = AutoCompleteCombobox(root, values=data)
combobox.pack()

root.mainloop()