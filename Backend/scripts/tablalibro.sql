-- agregamos la columna libro
USE bookmatch;
create table libro(
libro_id int primary key auto_increment,
id_compra int,
titulo varchar(120),
Autor varchar(120),
isbn int (11),
FOREIGN KEY (id_compra) REFERENCES compra(compra_id)
);
