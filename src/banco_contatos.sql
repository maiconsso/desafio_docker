create database bancocontatos;

use bancocontatos;

create table contatos(
con_id int PRIMARY KEY auto_increment,
con_email varchar(255),
con_assunto varchar(255),
con_texto varchar(255)
);