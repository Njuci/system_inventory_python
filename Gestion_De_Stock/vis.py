import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import PyPDF2
window = tk.Tk()
window.title("Visualiseur PDF")
window.geometry("500x600")
def open_pdf():
    try:
        file_path = filedialog.askopenfilename(title="Sélectionner un fichier PDF", filetypes=[("Fichiers PDF", "*.pdf")])
        if file_path:
            with open(file_path, 'rb') as f:
                pdf_reader = PyPDF2.PdfReader(f)
                page = pdf_reader.getPage(0)
                page_content = page.extractText()
                text_box.delete(1.0, tk.END)
                text_box.insert(tk.END, page_content)
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de l'ouverture du fichier PDF : {e}")
text_box = tk.Text(window, width=60, height=30)
text_box.pack()
open_button = tk.Button(window, text="Ouvrir un fichier PDF", command=open_pdf)
open_button.pack()

window.mainloop()