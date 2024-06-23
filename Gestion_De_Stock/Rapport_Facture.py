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
        top=2
        bottom=10
        nom_entreprise = "Votre Nom d'Entreprise"
        adresse_entreprise = "Votre Adresse complète"
        numero_telephone_entreprise = "+243 81 234 5678"
        email_entreprise = "contact@votredomaine.com"

        # Informations du client
        nom_client = "Jeremie ndeke "
        adresse_client = "Adresse complète du Client"

        # Informations de la facture
        numero_facture = "FACT-2024-06-01"
        date_facture = "01 Juin 2024"
        date_echeance = "30 Juin 2024"

        # Liste des produits
        produits=data[1]
        print(data[0]['num_fac'],"Data")
        ListeArticleFacture=[]
        a=0
        total_ht = 0
        if len(produits)!=0:

            # Calcul du total
            for item in (produits):
                total_ht+=item[4]
                ListeArticleFacture.append((item[1],item[3],f'{item[2]}$',item[4]))
       

        hauteurDynamique=80
        a=0
        if len(produits)!=0:
            a=7*(len(produits)+1)
            hauteurDynamique+=a

        # Calcul du total
        tva = total_ht * 0.18  # TVA à 18%
        total_ttc = total_ht + tva

        # Création d'un document PDF de format A6 (petit format)
        pagesize = (105 * mm, 99 * mm)  # Format A6
        doc = SimpleDocTemplate("facture.pdf", pagesize=pagesize, leftMargin=left,
                    rightMargin=right,
                    topMargin=top,
                    bottomMargin=bottom)

        # Éléments de la facture
        elements = []

        # En-tête de la facture


        # Informations du client
        elements.append(Paragraph(""))
        elements.append(Paragraph(""))
        elements.append(Paragraph(""))
        elements.append(Paragraph(""))

        L=[130,130]
        H=[25,40,20]
        DataHeader=[["Mson. DANIELLO","Facture"],
        ["N° d'Impôt : A1206219Z \nTéléphone : +243 997 129 073 \n Goma / R.D.C", f"N° {data[0]['num_fac']}\nGoma, le {data[0]['date_fac'].date().strftime('%d/%m/%Y')}"],
        [f"Mr,Mme {data[0]['nom_client']} "]
        ]

        HeaderFacture=Table(DataHeader,colWidths=L,rowHeights=H, style=[('GRID', (0, 0), (-1, -1), 1, colors.white)])

        style= TableStyle([('FONTSIZE', (0, 0), (-1,-1),11),
                        ('FONTSIZE', (0, 0), (0,1),8),
                        ('FONTSIZE', (0, 2), (0,2),11),
                        ('BACKGROUND', (1, 0), (1,0),'black'),
                        ('TEXTCOLOR', (1, 0), (1,0),'white'),
                        ('FONTSIZE', (1, 0), (1,0),17),
                        ('SPAN', (0, 2), (1,2)),
                        ('FONTNAME', (0, 0), (-1,-1),'Helvetica-Bold'),
                
                    ('FONTSIZE', (0, 0), (0,0),15),
                    ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
                    ('ALIGN', (0, 0), (-1,-1),'CENTER'),
                    ('VALIGN', (1, 0), (1,0),'MIDDLE'),

                    ('ALIGN', (0, 2), (0,2),'LEFT'),
                    ])
        HeaderFacture.setStyle(style)
        elements.append(HeaderFacture)


        # Liste des produits
        L=[120,40,40,50]

        table_produits = Table([
            ["Désignation", "Qnt", "Prix U.", "Prix T."], *ListeArticleFacture],colWidths=L,rowHeights=13,style=[('GRID', (0, 0), (-1, -1), 1, colors.grey)])
        elements.append(table_produits)
        style=TableStyle([('FONTSIZE', (0, 0), (-1,-1),8),
            ('BACKGROUND', (0, 0), (-1,-1),'gainsboro'),
            ('VALIGN', (0, 0), (-1,-1),'MIDDLE'),
            ('ALIGN', (0, 0), (-1,-1),'CENTER'),
        ])
        table_produits.setStyle(style)
        # Total HT, TVA, TTC
        elements.append(Table([["Total à payer:",f"{total_ht} $"],]))

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