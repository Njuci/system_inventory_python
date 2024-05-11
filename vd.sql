drop database if exists gest_stock_invent;
create database if not exists gest_stock_invent;
use gest_stock_invent;
create table  tb_produit(
    id int auto_increment unique key,
id_produit varchar(10) primary key,
designation_produit varchar(30) unique

);
create table tb_stock(
    id int auto-increment unique key,
	id_stock varchar(10) primary key,
    id_produit varchar(10),
    date_entree datetime default current_timestamp(),
    nombre_piece integer,
    prix_unitaire float(12,2), 
    statut_stock varchar(10),
    constraint pf_st_produit foreign key (id_produit) references tb_produit(id_produit)
    );

create table tb_prix_vente(
    id int auto-increment unique key,
	id_pv varchar(10) primary key,
    id_produit varchar(10),
    date_fixation  datetime default current_timestamp(),
    montant float(12,2),
    unique key(id_produit,date_fixation),
    constraint pf_pv_produit foreign key (id_produit) references tb_produit(id_produit)
	

	);
CREATE TABLE tb_client (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_client VARCHAR(10) UNIQUE,
  nom_cli VARCHAR(30) UNIQUE,
  adresse VARCHAR(30)
);

CREATE TABLE sequence_table (
  table_name VARCHAR(20) NOT NULL,
  next_id INT NOT NULL,
  PRIMARY KEY (table_name)
);

INSERT INTO sequence_table (table_name, next_id) VALUES ('tb_client', 1);
DELIMITER //
CREATE TRIGGER avant_insertion_client
BEFORE INSERT ON tb_client
FOR EACH ROW
BEGIN
  DECLARE next_id INT;
  SELECT next_id INTO next_id FROM sequence_table WHERE table_name = 'tb_client';
  SET NEW.id_client = CONCAT('CLI', LPAD(next_id, 7, '0'));
  UPDATE sequence_table SET next_id = next_id + 1 WHERE table_name = 'tb_client';
END; //
DELIMITER ;

create table tb_facture(
    id int auto-increment unique key,
	id_facture varchar(10) primary key,
    id_client varchar(10),
    date_facturation datetime default current_timestamp(),
    constraint pf_fac_cli foreign key (id_client) references tb_client(id_client)
	);
create table tb_vente(
    id int auto-increment unique key,
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

