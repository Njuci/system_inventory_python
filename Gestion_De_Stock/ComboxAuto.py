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




        tva = total_ht * 0.16  # TVA à 16%
        total_ttc = total_ht + tva

        # Création d'un document PDF de format A6 (petit format)
        pagesize = (80 * mm, hauteurDynamique * mm)  # Format A6
        doc = SimpleDocTemplate("facture.pdf", pagesize=pagesize, leftMargin=left,
                    rightMargin=right,
                    topMargin=top,
                    bottomMargin=bottom)

        # Éléments de la facture
        elements = []
        
        chemin_absolu = os.getcwd()
        d=chemin_absolu.split("\\")
        chemin_absolu=""
        for i in range(len(d)):
            if i==0:
                chemin_absolu=d[i]
            else:
                chemin_absolu=chemin_absolu+"/"+d[i]
        print(chemin_absolu)
        # En-tête de la facture
        
        logo_path = chemin_absolu+"/logo.png"
        logo = Image(logo_path, 1 * inch, 0.2 * inch)
        elements.append(logo)

        elements.append(Paragraph(nom_entreprise,custom_style))
        elements.append(Paragraph(adresse_entreprise,custom_style))
        elements.append(Paragraph(f"Téléphone: {numero_telephone_entreprise}",custom_style))
        elements.append(Paragraph(f"Email: {email_entreprise}",custom_style))


        # Informations du client
        elements.append(Paragraph("Facture à:",custom_style))
        elements.append(Paragraph(nom_client,custom_style))
        elements.append(Paragraph(adresse_client,custom_style))

        # Informations de la facture
        elements.append(Table([["N° Facture:", numero_facture],
                            ["Date Facture:", date_facture]]).setStyle(custom_style_table))

        # Liste des produits
        L=[90,40,40,40]
        table_produits = Table([
            ["Désignation", "Qnt", "Prix U.", "Prix T."], 
            *ListeArticleFacture],colWidths=L,style=[('GRID', (0, 0), (-1, -1), 1, colors.black) , 
                                                     ('FONTNAME', (0, 0), (-1, -1), 'AgencyFB-Bold'), 
    ('FONTSIZE', (0, 0), (-1, -1), 9) ])
        elements.append(table_produits)
        elements.append(Spacer(1, 12))

        # Total HT, TVA, TTC
        elements.append(Table([["Total HT:",total_ht],
                            ["TVA 16%:",tva],
                                ["Total TTC::",total_ttc]],style=[#('GRID', (0, 0), (-1, -1), 1, colors.black) , 
                                                     ('FONTNAME', (0, 0), (-1, -1), 'AgencyFB-Bold'), 
                                                     #mettre le tableau à l'extrémité droite
                                                        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
    ('FONTSIZE', (0, 0), (-1, -1), 9) ]))

        """
        elements.append(Paragraph("Total HT: "+f"{:.2f} €"))
        elements.append(Paragraph("TVA 18%: "+f"{tva:.2f} €"))
        elements.append(Paragraph("Total TTC: "+f"{total_ttc:.2f} €"))
        """

        # Build the PDF
        doc.build(elements)
        webbrowser.open_new_tab("facture.pdf")
        print("Facture générée: facture.pdf")

            