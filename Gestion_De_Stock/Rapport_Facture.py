import reportlab
from reportlab.lib import colors

from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.platypus.tables import Table, TableStyle
import webbrowser
class FacturePDF :
    def __init__(self):
        self.data=[]
    
    def genererFacture(self,data):
        # Initialisation des styles
        stylesheet = getSampleStyleSheet()

        # Informations de l'entreprise
        left=10
        right=10
        top=5
        bottom=10
        nom_entreprise = "Votre Nom d'Entreprise"
        adresse_entreprise = "Votre Adresse complète"
        numero_telephone_entreprise = "+243 81 234 5678"
        email_entreprise = "contact@votredomaine.com"

        # Informations du client
        nom_client = data[0][ 'nom_client']
        adresse_client = "Adresse complète du Client"

        # Informations de la facture
        numero_facture = data[0]['num_fac']
        date_facture = data[0]['date_fac']
        date_echeance = "30 Juin 2024"

        # Liste des produits
        produits = [
            ("Produit 1", 10, 5.00, 50.00),
            ("Produit 2", 8, 7.50, 60.00),
            ("Produit 3", 15, 4.20, 63.00),
            ("Produit 4", 6, 12.00, 72.00),
            ("Produit 5", 3, 9.50, 28.50),
            ("Produit 6", 12, 6.80, 81.60),
            ("Produit 7", 4, 15.20, 60.80),
            ("Produit 8", 9, 8.50, 76.50),
            ("Produit 9", 11, 11.30, 123.30),
            ("Produit 10", 5, 13.90, 69.50),
        ]
        produits=data[1]
        ListeArticleFacture=[]

        hauteurDynamique=80
        a=0
        total_ht = 0
        if len(produits)!=0:
            a=7*(len(produits)+1)
            hauteurDynamique+=a
            # Calcul du total
            for item in (produits):
                total_ht+=item[4]
                ListeArticleFacture.append((item[1],item[3],item[2],item[4]))

        tva = total_ht * 0.16  # TVA à 18%
        total_ttc = total_ht + tva

        # Création d'un document PDF de format A6 (petit format)
        pagesize = (80 * mm, hauteurDynamique * mm)  # Format A6
        doc = SimpleDocTemplate("facture.pdf", pagesize=pagesize, leftMargin=left,
                    rightMargin=right,
                    topMargin=top,
                    bottomMargin=bottom)

        # Éléments de la facture
        elements = []

        # En-tête de la facture
        logo = Image("logo.png", 1 * inch, 0.2 * inch)  # Remplacer "logo.png" par votre logo
        elements.append(logo)

        elements.append(Paragraph(nom_entreprise))
        elements.append(Paragraph(adresse_entreprise))
        elements.append(Paragraph(f"Téléphone: {numero_telephone_entreprise}"))
        elements.append(Paragraph(f"Email: {email_entreprise}"))


        # Informations du client
        elements.append(Paragraph("Facture à:"))
        elements.append(Paragraph(nom_client))
        elements.append(Paragraph(adresse_client))

        # Informations de la facture
        elements.append(Table([["N° Facture:", numero_facture],
                            ["Date Facture:", date_facture]]))

        # Liste des produits
        L=[90,40,40,40]
        table_produits = Table([
            ["Désignation", "Qnt", "Prix U.", "Prix T."], *ListeArticleFacture],colWidths=L,style=[('GRID', (0, 0), (-1, -1), 1, colors.black)])
        elements.append(table_produits)

        # Total HT, TVA, TTC
        elements.append(Table([["Total HT:",total_ht],
                            ["TVA 18%:",tva],
                                ["Total TTC::",total_ttc]]))

        """
        elements.append(Paragraph("Total HT: "+f"{:.2f} €"))
        elements.append(Paragraph("TVA 18%: "+f"{tva:.2f} €"))
        elements.append(Paragraph("Total TTC: "+f"{total_ttc:.2f} €"))
        """

        # Build the PDF
        doc.build(elements)
        webbrowser.open_new_tab("facture.pdf")
        print("Facture générée: facture.pdf")

            
    def genererRapportJournalier(self,data):
        pass