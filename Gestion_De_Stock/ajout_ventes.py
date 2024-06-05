
from produit_backend import Product_back
from client_backend import Client_back
from facture_back import Facture_back
from pv_back import Prix_vente_back
from stock_backend import Stock_back
from vente_back import Vente_back

class InventoryManagementSystem:
    def __init__(self, db,listeArtticle):
        self.db = db
        self.listeArtticle=listeArtticle

    def start_transaction(self):
        self.db.autocommit = False
        self.db.start_transaction()

    def commit_transaction(self):
        self.db.commit()
        self.db.autocommit = True

    def rollback_transaction(self):
        self.db.rollback()
        self.db.autocommit = True

    def add_invoice(self, client_id):
        print('Client:', client_id)
        invoice = Facture_back(client_id)
        self.start_transaction()
        if invoice.add_fact(self.db.cursor()):
            fact_id = self.get_last_invoice_id()
            print('Invoice:', fact_id)
            try:
                for item in self.listeArtticle:
                    self.process_item(item, fact_id)
                self.commit_transaction()
                return True
            except Exception as e:
                print("An error occurred:", e)
                self.rollback_transaction()
                return False
        else:
            self.rollback_transaction()
            return False

    def get_last_invoice_id(self):
        self.db.cursor().execute('SELECT MAX(id_facture) FROM tb_facture')
        return self.db.cursor().fetchone()[0]

    def process_item(self, item, fact_id):
        prix = Prix_vente_back("", 0).get_last_pv(self.db.cursor(), item[0])[1][0][0]
        print("Price is:", prix)
        quantite_demande = int(item[2])
        quantite_dispo, stock = self.find_stock(item[0])
        print("Available quantity is:", quantite_dispo)
        if quantite_dispo >= quantite_demande:
            self.record_sale(item, stock, fact_id, prix, quantite_demande)
        else:
            self.handle_insufficient_stock(item, fact_id, prix, quantite_demande, quantite_dispo)

    def find_stock(self, product_id):
        stock_info = Stock_back("", 0, 0).get_stock_dispo_id(self.db.cursor(), product_id)[1][0]
        quantity_info = Stock_back("", 0, 0).get_stock_ecoule(self.db.cursor(), stock_info[1])[1][0]
        quantite_dispo = quantity_info[2] - quantity_info[3]
        return quantite_dispo, stock_info[1]

    def record_sale(self, item, stock, fact_id, prix, quantite_demande):
        sale = Vente_back(item[0], stock, fact_id, prix, quantite_demande)
        print(item[0], stock, fact_id, prix, quantite_demande)
        sale.add_vente(self.db.cursor())

    def handle_insufficient_stock(self, item, fact_id, prix, quantite_demande, quantite_dispo):
        while quantite_dispo < quantite_demande:
            quantite_dispo, stock = self.find_stock(item[0])
            if quantite_dispo >= quantite_demande:
                self.record_sale(item, stock, fact_id, prix, quantite_demande)
                break
            else:
                quantite_demande -= quantite_dispo
