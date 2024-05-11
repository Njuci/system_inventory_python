drop database if exists gest_stock_invent;
create database if not exists gest_stock_invent;
use gest_stock_invent;
create table  tb_produit(
    id int auto_increment unique key,
id_produit varchar(10) primary key,
designation_produit varchar(30) unique

);
create table tb_stock(
    id int auto_increment unique key,
	id_stock varchar(10) primary key,
    id_produit varchar(10),
    date_entree datetime default current_timestamp(),
    nombre_piece integer,
    prix_unitaire float(12,2), 
    statut_stock varchar(10),
    constraint pf_st_produit foreign key (id_produit) references tb_produit(id_produit)
    );

create table tb_prix_vente(
    id int auto_increment unique key,
	id_pv varchar(10) primary key,
    id_produit varchar(10),
    date_fixation  datetime default current_timestamp(),
    montant float(12,2),
    unique key(id_produit,date_fixation),
    constraint pf_pv_produit foreign key (id_produit) references tb_produit(id_produit)
	

	);
create table tb_client(
    id int auto_increment primary key,
	id_client varchar(10) unique key ,
    nom_cli varchar(30) unique,
    adresse varchar(30)
    );
create table tb_facture(
    id int auto_increment unique key,
	id_facture varchar(10) primary key,
    id_client varchar(10),
    date_facturation datetime default current_timestamp(),
    constraint pf_fac_cli foreign key (id_client) references tb_client(id_client)
	);
create table tb_vente(
    id int auto_increment unique key,
	id_vente varchar(10),
    id_produit varchar(10),
    id_pv varchar(10),
    quantite integer,
    id_facture varchar(10),
    id_stock varchar(10),
    constraint pf_fac_vente foreign key (id_facture) references tb_facture (id_facture),
    constraint pf_vente_produit foreign key(id_produit) references tb_produit(id_produit),
    constraint pf_vente_id_stock foreign key (id_stock) references tb_stock(id_stock),
    constraint pf_pv_vente foreign key(id_pv) references tb_prix_vente (id_pv),
    constraint pk_vente primary key(id_stock,id_facture,id_produit)
    );

CREATE TABLE table_name_client (
   name_table VARCHAR(255),
   ancienne_cle INT,
   nouvelle_cle INT
);

--create TRIGGER
--

DELIMITER //
CREATE TRIGGER avant_insertion_client
AFTER INSERT ON tb_client
FOR EACH ROW
BEGIN
    IF NEW.id IS NULL THEN
        SET NEW.id_client = CONCAT('CLI', LPAD(LAST_INSERT_ID(), 7, '0'));
    ELSE
        SET NEW.id_client = CONCAT('CLI', LPAD(LAST_INSERT_ID() + 1, 7, '0'));
    END IF;
END;
//
DELIMITER ;

