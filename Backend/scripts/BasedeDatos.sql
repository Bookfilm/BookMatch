CREATE DATABASE IF NOT EXISTS bookmatch;
USE bookmatch;

CREATE TABLE rol (
    rol_id INT PRIMARY KEY AUTO_INCREMENT,
    rol VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE usuario (
    usuario_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    email VARCHAR(50) UNIQUE,
    contraseña VARCHAR(255),          
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_rol INT NOT NULL,
    CONSTRAINT fk_usuario_rol
        FOREIGN KEY (id_rol) REFERENCES rol(rol_id)
);

CREATE TABLE libro (
    libro_id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(120),
    autor VARCHAR(120),
    isbn VARCHAR(13) UNIQUE
);

CREATE TABLE compra (
    compra_id INT PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                              ON UPDATE CURRENT_TIMESTAMP,
    precio_total DOUBLE,
    CONSTRAINT fk_compra_usuario
        FOREIGN KEY (id_usuario) REFERENCES usuario(usuario_id)
);

CREATE TABLE detalle_compra (
    detalle_id INT PRIMARY KEY AUTO_INCREMENT,
    id_compra INT NOT NULL,
    id_libro  INT NOT NULL,
    cantidad  INT NOT NULL DEFAULT 1,
    precio_unitario DOUBLE NOT NULL,
    CONSTRAINT fk_detalle_compra
        FOREIGN KEY (id_compra) REFERENCES compra(compra_id),
    CONSTRAINT fk_detalle_libro
        FOREIGN KEY (id_libro)  REFERENCES libro(libro_id)
);

CREATE TABLE sesion (
    sesion_id INT PRIMARY KEY AUTO_INCREMENT,
    fecha_inicio DATETIME,
    fecha_fin DATETIME,
    id_usuario INT NOT NULL,
    CONSTRAINT fk_sesion_usuario
        FOREIGN KEY (id_usuario) REFERENCES usuario(usuario_id)
);