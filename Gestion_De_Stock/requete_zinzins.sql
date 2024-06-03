SET @designation_produit = 'Bonbon';

SELECT 
    tb_produit.designation_produit,
    tb_produit.id_produit,
    tb_stock.date_entree AS 'Date d entrée',
    tb_stock.nombre_piece AS 'Nombre de pièce en stock',
    COALESCE(MAX(tb_facture.date_facturation), 'Pas encore vendu') AS 'Date de sortie',
    COALESCE(SUM(tb_vente.quantite), 0) AS 'Quantité sortie',
    COALESCE(SUM(tb_vente.quantite), 0) AS 'Nombre d\'articles déjà vendus'
FROM 
    tb_produit
LEFT JOIN 
    tb_stock ON tb_produit.id_produit = tb_stock.id_produit
LEFT JOIN 
    tb_vente ON tb_produit.id_produit = tb_vente.id_produit
LEFT JOIN 
    tb_facture ON tb_vente.id_facture = tb_facture.id_facture
WHERE 
    tb_produit.designation_produit = @designation_produit
GROUP BY 
    tb_produit.designation_produit, tb_stock.date_entree, tb_stock.nombre_piece
HAVING 
    tb_stock.nombre_piece > COALESCE(SUM(tb_vente.quantite), 0)
ORDER BY 
    tb_stock.date_entree ASC;
SET @designation_produit = 'Bonbon';

SELECT 
    p.designation_produit,
    p.id_produit,
    s.date_entree AS 'Date d entrée',
    s.nombre_piece AS 'Nombre de pièce en stock',
    COALESCE(MAX(f.date_facturation), 'Pas encore vendu') AS 'Date de sortie',
    (
        SELECT COALESCE(SUM(v.quantite), 0)
        FROM tb_vente v
        JOIN tb_facture f ON v.id_facture = f.id_facture join tb_stock s on s.id_stock=v.id_stock
        WHERE v.id_produit = p.id_produit AND v.id_stock = s.id_stock
    ) AS 'Quantité sortie sur ce stock'
FROM 
    tb_produit p
LEFT JOIN 
    tb_stock s ON p.id_produit = s.id_produit
LEFT JOIN 
    tb_vente v ON p.id_produit = v.id_produit
LEFT JOIN 
    tb_facture f ON v.id_facture = f.id_facture
WHERE 
    p.designation_produit = @designation_produit
GROUP BY 
    p.designation_produit, p.id_produit, s.date_entree, s.nombre_piece
HAVING 
    s.nombre_piece > (
        SELECT COALESCE(SUM(v.quantite), 0)
        FROM tb_vente v
        WHERE v.id_produit = p.id_produit AND v.id_stock = s.id_stock
    )
ORDER BY 
    s.date_entree ASC;
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

                    SET @designation_produit = 'Bonbon';

SELECT 
    p.designation_produit,
    p.id_produit,
    s.id_stock as stock,
    s.date_entree AS 'Date d entrée',
    s.nombre_piece AS 'Nombre de pièce en stock',
    COALESCE(MAX(f.date_facturation), 'Pas encore vendu') AS 'Date de sortie',
    (
        SELECT COALESCE(SUM(v.quantite), 0)
        FROM tb_vente v
        JOIN tb_facture f ON v.id_facture = f.id_facture join tb_stock s on v.id_stock=s.id_stock join tb_produit p on p.id_produit=v.id_produit
        WHERE v.id_produit = p.id_produit AND v.id_stock = s.id_stock 
    ) AS 'Quantité sortie sur ce stock'
FROM 
    tb_produit p
 JOIN 
    tb_stock s ON p.id_produit = s.id_produit
 JOIN 
    tb_vente v ON p.id_produit = v.id_produit
 JOIN 
    tb_facture f ON v.id_facture = f.id_facture

WHERE 
    p.designation_produit = @designation_produit and s.id_stock=v.id_stock
GROUP BY 
    p.designation_produit, p.id_produit, s.date_entree, s.nombre_piece
HAVING 
    s.nombre_piece > (
        SELECT COALESCE(SUM(v.quantite), 0)
        FROM tb_vente v,tb_stock s
        WHERE v.id_produit = p.id_produit AND v.id_stock = s.id_stock
    )
ORDER BY 
    s.date_entree ASC;

        
    
    
    
SELECT tb_produit.designation_produit,
                            tb_stock.date_entree AS 'Date d entrée',
                            tb_stock.nombre_piece AS 'Nombre de pièce en stock',
                            COALESCE(MAX(tb_facture.date_facturation), 'Pas encore vendu') AS 'Date de sortie',
                            COALESCE(SUM(tb_vente.quantite), 0) AS 'Quantité sortie' 
                            FROM tb_stock
                            LEFT JOIN tb_vente ON tb_stock.id_stock = tb_vente.id_stock
                            JOIN tb_produit ON tb_produit.id_produit = tb_stock.id_produit
                            LEFT JOIN tb_facture ON tb_vente.id_facture = tb_facture.id_facture
                            WHERE tb_produit.designation_produit = 'Raisins'
                            GROUP BY tb_stock.id_stock
                            ORDER BY COALESCE(MAX(tb_facture.date_facturation), '0000-00-00 00:00:00') DESC;


SELECT 
    tb_produit.designation_produit,
    tb_stock.date_entree AS 'Date d entrée',
    tb_stock.nombre_piece AS 'Nombre de pièce en stock',
    COALESCE(MAX(tb_facture.date_facturation), 'Pas encore vendu') AS 'Date de sortie',
    COALESCE(SUM(tb_vente.quantite), 0) AS 'Quantité sortie'
FROM 
    tb_stock
LEFT JOIN 
    tb_vente ON tb_stock.id_stock = tb_vente.id_stock
JOIN 
    tb_produit ON tb_produit.id_produit = tb_stock.id_produit
LEFT JOIN 
    tb_facture ON tb_vente.id_facture = tb_facture.id_facture
WHERE 
    tb_produit.designation_produit = 'Bonbon'
GROUP BY 
    tb_stock.id_stock
HAVING 
    tb_stock.nombre_piece > COALESCE(SUM(tb_vente.quantite), 0)
ORDER BY 
    tb_stock.date_entree ASC
LIMIT 1;


SELECT tb_produit.designation_produit, 
                            (IFNULL(SUM(tb_stock.nombre_piece),0) - IFNULL(SUM(tb_vente.quantite), 0)) AS somme_restante
                            FROM tb_produit
                         LEFT JOIN tb_stock ON tb_produit.id_produit = tb_stock.id_produit
                         LEFT JOIN tb_vente ON tb_produit.id_produit = tb_vente.id_produit
                        GROUP BY tb_produit.designation_produit
                            HAVING somme_restante > 0;
                            
                            
SELECT 
    p.id_produit,
    p.designation_produit,
    IFNULL(s.total_entree, 0) - IFNULL(v.total_vente, 0) AS stock_restant
FROM 
    tb_produit p
LEFT JOIN (
    SELECT 
        id_produit,
        SUM(nombre_piece) AS total_entree
    FROM 
        tb_stock
    GROUP BY 
        id_produit
) s ON p.id_produit = s.id_produit
LEFT JOIN (
    SELECT 
        id_produit,
        SUM(quantite) AS total_vente
    FROM 
        tb_vente
    GROUP BY 
        id_produit
) v ON p.id_produit = v.id_produit;


                            
                            


WITH VentesCumulees AS (
    SELECT 
        id_produit,
        id_stock,
        SUM(quantite) AS quantite_vendue
    FROM 
        tb_vente
    GROUP BY 
        id_produit, id_stock
),
Stocks AS (
    SELECT 
        id_stock,
        id_produit,
        nombre_piece,
        ROW_NUMBER() OVER (PARTITION BY id_produit ORDER BY date_entree ASC) AS rang_fifo
    FROM 
        tb_stock
),
StocksDisponibles AS (
    SELECT 
        s.id_stock,
        s.id_produit,
        s.nombre_piece - COALESCE(v.quantite_vendue, 0) AS stock_restant
    FROM 
        Stocks s
    LEFT JOIN 
        VentesCumulees v ON s.id_stock = v.id_stock AND s.id_produit = v.id_produit
    WHERE 
        s.nombre_piece - COALESCE(v.quantite_vendue, 0) > 0
)
SELECT 
    sd.id_produit,
    MIN(sd.id_stock) AS id_stock_utiliser
FROM 
    StocksDisponibles sd
GROUP BY 
    sd.id_produit;
