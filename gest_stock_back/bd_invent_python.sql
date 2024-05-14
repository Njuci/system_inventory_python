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

CREATE TABLE table_name_id (
   name_table VARCHAR(255),
   ancienne_cle INT,
   nouvelle_cle INT
);
DELIMITER //
CREATE TRIGGER avant_insertion_client
BEFORE INSERT ON tb_client
FOR EACH ROW
BEGIN
    DECLARE variable_name INT DEFAULT 0;
    DECLARE max_cle INT DEFAULT 0;
    DECLARE max_nouvelle_cle INT;
    -- Récupère la plus grande valeur de nouvelle_cle et l'incrémente de 1
    -- SET @max_nouvelle_cle = (SELECT MAX(nouvelle_cle) FROM table_name_id WHERE name_table = 'tb_client');
    SET @max_nouvelle_cle = (SELECT MAX(nouvelle_cle) FROM table_name_id WHERE name_table = 'tb_client');

    
         SET @variable_name = @max_nouvelle_cle + 1;
    -- Vérifie si variable_name est NULL ou 0, et ajuste la valeur de id_client en conséquence
    IF @max_nouvelle_cle  IS NULL OR @max_nouvelle_cle  = 0 THEN
        SET NEW.id_client = CONCAT('CLI', LPAD(1, 7, '0'));
        SET @variable_name=1;
    ELSE
        SET NEW.id_client = CONCAT('CLI', LPAD(@variable_name , 7, '0'));
    END IF;
    
    
    
    
    INSERT into table_name_id VALUES ('tb_client',@max_nouvelle_cle ,@variable_name );
END;
//
DELIMITER ;
DELIMITER //
CREATE TRIGGER avant_insertion_poduit
BEFORE INSERT ON tb_produit
FOR EACH ROW
BEGIN
    DECLARE variable_name INT DEFAULT 0;
    DECLARE max_cle INT DEFAULT 0;
    DECLARE max_nouvelle_cle INT;
    -- Récupère la plus grande valeur de nouvelle_cle et l'incrémente de 1
    -- SET @max_nouvelle_cle = (SELECT MAX(nouvelle_cle) FROM table_name_id WHERE name_table = 'tb_client');
    SET @max_nouvelle_cle = (SELECT MAX(nouvelle_cle) FROM table_name_id WHERE name_table = 'tb_produit');

    
         SET @variable_name = @max_nouvelle_cle + 1;
    -- Vérifie si variable_name est NULL ou 0, et ajuste la valeur de id_client en conséquence
    IF @max_nouvelle_cle  IS NULL OR @max_nouvelle_cle  = 0 THEN
        SET NEW.id_produit = CONCAT('PRO', LPAD(1, 7, '0'));
        SET @variable_name=1;
    ELSE
        SET NEW.id_produit = CONCAT('PRO', LPAD(@variable_name , 7, '0'));
    END IF;
    
    
    
    
    INSERT into table_name_id VALUES ('tb_produit',@max_nouvelle_cle ,@variable_name );
END;
//
DELIMITER ;

DELIMITER ;
DELIMITER //
CREATE TRIGGER avant_insertion_stock
BEFORE INSERT ON tb_stock
FOR EACH ROW
BEGIN
    DECLARE variable_name INT DEFAULT 0;
    DECLARE max_cle INT DEFAULT 0;
    DECLARE max_nouvelle_cle INT;
    -- Récupère la plus grande valeur de nouvelle_cle et l'incrémente de 1
    -- SET @max_nouvelle_cle = (SELECT MAX(nouvelle_cle) FROM table_name_id WHERE name_table = 'tb_client');
    SET @max_nouvelle_cle = (SELECT MAX(nouvelle_cle) FROM table_name_id WHERE name_table = 'tb_stock');

    
         SET @variable_name = @max_nouvelle_cle + 1;
    -- Vérifie si variable_name est NULL ou 0, et ajuste la valeur de id_client en conséquence
    IF @max_nouvelle_cle  IS NULL OR @max_nouvelle_cle  = 0 THEN
        SET NEW.id_stock = CONCAT('STO', LPAD(1, 7, '0'));
        SET @variable_name=1;
    ELSE
        SET NEW.id_stock = CONCAT('STO', LPAD(@variable_name , 7, '0'));
    END IF;
    
    
    
    
    INSERT into table_name_id VALUES ('tb_stock',@max_nouvelle_cle ,@variable_name );
END;
//
DELIMITER ;


DELIMITER ;
DELIMITER //
CREATE TRIGGER avant_insertion_pv
BEFORE INSERT ON tb_prix_vente
FOR EACH ROW
BEGIN
    DECLARE variable_name INT DEFAULT 0;
    DECLARE max_cle INT DEFAULT 0;
    DECLARE max_nouvelle_cle INT;
    -- Récupère la plus grande valeur de nouvelle_cle et l'incrémente de 1
    -- SET @max_nouvelle_cle = (SELECT MAX(nouvelle_cle) FROM table_name_id WHERE name_table = 'tb_client');
    SET @max_nouvelle_cle = (SELECT MAX(nouvelle_cle) FROM table_name_id WHERE name_table = 'tb_prix_vente');

    
         SET @variable_name = @max_nouvelle_cle + 1;
    -- Vérifie si variable_name est NULL ou 0, et ajuste la valeur de id_client en conséquence
    IF @max_nouvelle_cle  IS NULL OR @max_nouvelle_cle  = 0 THEN
        SET NEW.id_pv = CONCAT('PV', LPAD(1, 8, '0'));
        SET @variable_name=1;
    ELSE
        SET NEW.id_pv = CONCAT('PV', LPAD(@variable_name , 8, '0'));
    END IF;
    
    
    
    
    INSERT into table_name_id VALUES ('tb_prix_vente',@max_nouvelle_cle ,@variable_name );
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER avant_insertion_facture
BEFORE INSERT ON tb_facture
FOR EACH ROW
BEGIN
    DECLARE variable_name INT DEFAULT 0;
    DECLARE max_cle INT DEFAULT 0;
    DECLARE max_nouvelle_cle INT;
    -- Récupère la plus grande valeur de nouvelle_cle et l'incrémente de 1
    -- SET @max_nouvelle_cle = (SELECT MAX(nouvelle_cle) FROM table_name_id WHERE name_table = 'tb_client');
    SET @max_nouvelle_cle = (SELECT MAX(nouvelle_cle) FROM table_name_id WHERE name_table = 'tb_facture');

    
         SET @variable_name = @max_nouvelle_cle + 1;
    -- Vérifie si variable_name est NULL ou 0, et ajuste la valeur de id_client en conséquence
    IF @max_nouvelle_cle  IS NULL OR @max_nouvelle_cle  = 0 THEN
        SET NEW.id_facture = CONCAT('FAC', LPAD(1, 7, '0'));
        SET @variable_name=1;
    ELSE
        SET NEW.id_facture = CONCAT('FAC', LPAD(@variable_name , 7, '0'));
    END IF;
    
    
    
    
    INSERT into table_name_id VALUES ('tb_facture',@max_nouvelle_cle ,@variable_name );
END;
//
DELIMITER ;

DELIMITER ;

DELIMITER //
CREATE TRIGGER avant_insertion_vente
BEFORE INSERT ON tb_vente
FOR EACH ROW
BEGIN
    DECLARE variable_name INT DEFAULT 0;
    DECLARE max_cle INT DEFAULT 0;
    DECLARE max_nouvelle_cle INT;
    -- Récupère la plus grande valeur de nouvelle_cle et l'incrémente de 1
    -- SET @max_nouvelle_cle = (SELECT MAX(nouvelle_cle) FROM table_name_id WHERE name_table = 'tb_client');
    SET @max_nouvelle_cle = (SELECT MAX(nouvelle_cle) FROM table_name_id WHERE name_table = 'tb_vente');

    
         SET @variable_name = @max_nouvelle_cle + 1;
    -- Vérifie si variable_name est NULL ou 0, et ajuste la valeur de id_client en conséquence
    IF @max_nouvelle_cle  IS NULL OR @max_nouvelle_cle  = 0 THEN
        SET NEW.id_vente = CONCAT('TBV', LPAD(1, 7, '0'));
        SET @variable_name=1;
    ELSE
        SET NEW.id_vente = CONCAT('TBV', LPAD(@variable_name , 7, '0'));
    END IF;
    
    
    
    
    INSERT into table_name_id VALUES ('tb_vente',@max_nouvelle_cle ,@variable_name );
END;
//
DELIMITER ;

