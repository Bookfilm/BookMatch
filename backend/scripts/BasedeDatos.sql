create database bookmatch;

-- creamos la tabla usuario/comprador (paso 2)
USE bookmatch;
create table usuario(
usuario_id int primary key auto_increment,
nombre varchar(50),
apellido varchar(50),
email varchar(50) unique,
contraseña varchar(50),
fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- esto guarda el momento en que se creo el usuario
id_rol int,
FOREIGN KEY (id_rol) REFERENCES rol(rol_id)
);

-- creamos la tabla rol (paso 3)
USE bookmatch;
create table rol(
rol_id int primary key auto_increment,
rol varchar(50)
);

-- Agregamos la columna rol a la tabla usuario (paso 4)
ALTER TABLE usuario
ADD COLUMN rol INT;

-- Agregamos la clave foránea
ALTER TABLE usuario
ADD CONSTRAINT fk_id_rol
FOREIGN KEY (id_rol) REFERENCES rol(rol_id);

-- creamos la tabla sesion (paso 5)
USE bookmatch;
create table sesion(
sesion_id int primary key auto_increment,
fecha_inicio datetime,
fecha_fin datetime,
id_usuario int,
FOREIGN KEY (id_usuario) REFERENCES usuario(usuario_id)
);

-- Agregamos la columna usuario a la tabla sesion
ALTER TABLE sesion
ADD COLUMN usuario INT;

-- Agregamos la clave foránea
ALTER TABLE sesion
ADD CONSTRAINT fk_id_usuario
FOREIGN KEY (id_usuario) REFERENCES usuario(usuario_id);

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

USE bookmatch;
Create table compra(
compra_id int primary key auto_increment,
id_usuario int,
FOREIGN KEY (id_usuario) REFERENCES usuario(usuario_id),
fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- esto guarda el momento en que se creo el usuario
fecha_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
precio_total DOUBLE -- esto guarda el momento en que se modifico el usuario
);

-- Agregamos la columna compra a la tabla libro
ALTER TABLE libro
ADD COLUMN compra INT;

-- Agregamos la clave foránea
ALTER TABLE libro
ADD CONSTRAINT fk_id_compra
FOREIGN KEY (id_compra) REFERENCES compra(compra_id);

