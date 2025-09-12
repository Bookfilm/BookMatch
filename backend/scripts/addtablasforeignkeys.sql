-- Agregamos la columna rol a la tabla usuario 
ALTER TABLE usuario
ADD COLUMN rol INT;

-- Agregamos la clave foránea
ALTER TABLE usuario
ADD CONSTRAINT fk_id_rol
FOREIGN KEY (id_rol) REFERENCES rol(rol_id);

-- Agregamos la columna usuario a la tabla sesion 
ALTER TABLE sesion
ADD COLUMN usuario INT;

-- Agregamos la clave foránea
ALTER TABLE sesion
ADD CONSTRAINT fk_id_usuario
FOREIGN KEY (id_usuario) REFERENCES usuario(usuario_id);

-- Agregamos la columna compra a la tabla libro
ALTER TABLE libro
ADD COLUMN compra INT;

-- Agregamos la clave foránea
ALTER TABLE libro
ADD CONSTRAINT fk_id_compra
FOREIGN KEY (id_compra) REFERENCES compra(compra_id);