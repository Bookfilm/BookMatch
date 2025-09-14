USE bookmatch;
create table usuario(
usuario_id int primary key auto_increment,
Nombre varchar(50),
Apellido varchar(50),
Email varchar(50) unique,
Contraseña varchar(50),
fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
id_rol int,-- esto guarda el momento en que se creo el usuario
FOREIGN KEY (id_rol) REFERENCES rol(rol_id)
);