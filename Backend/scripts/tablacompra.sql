USE bookmatch;
Create table compra(
compra_id int primary key auto_increment,
id_usuario int,
FOREIGN KEY (id_usuario) REFERENCES usuario(usuario_id),
fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- esto guarda el momento en que se creo el usuario
fecha_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
precio_total DOUBLE -- esto guarda el momento en que se modifico el usuario
);
