ALTER TABLE CLIENTE
ADD COLUMN pais varchar(100) after nombre;

ALTER TABLE CLIENTE
MODIFY id int(11) PRIMARY KEY AUTO_INCREMENT;