create database if not exists master_python;
use master_python;

create table users(
    id int(25) not null AUTO_INCREMENT,
    fullName varchar(100),
    lastName varchar(100),
    email varchar(255) not null,
    password varchar(255) not null,
    actualDate date not null,
    CONSTRAINT pk_users PRIMARY key(id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

create table notes(
    id int(25) auto_increment not null,
    id_user int(25) not null,
    title varchar(255) not null,
    path varchar(255) not null,
    actualDate date not null,
    CONSTRAINT pk_notas PRIMARY key(id),
    CONSTRAINT fk_notes_user FOREIGN key(id_user) REFERENCES users(id)
    CONSTRAINT pk_path UNIQUE(path)
)ENGINE=InnoDb