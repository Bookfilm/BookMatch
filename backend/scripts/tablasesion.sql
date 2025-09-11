-- creamos la tabla sesion (paso 5)
USE bookmatch;
create table sesion(
sesion_id int primary key auto_increment,
fecha_inicio datetime,
fecha_fin datetime,
id_usuario int,
FOREIGN KEY (id_usuario) REFERENCES usuario(usuario_id)
);