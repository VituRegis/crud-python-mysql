CREATE DATABASE CampeonatoDeCaraOuCoroa;
USE CampeonatoDeCaraOuCoroa;

CREATE TABLE usuario(
	idusu INT NOT NULL AUTO_INCREMENT,
	tipousu INT NOT NULL DEFAULT '1', 	
    nomeusu VARCHAR(30),
    emailusu VARCHAR(50),
    nascimento DATE,
    nacionalidade VARCHAR(20) DEFAULT 'Brasil',
	PRIMARY KEY(idusu) 
)DEFAULT CHARSET = utf8;

CREATE TABLE tipo_usuario(
	tipousu INT NOT NULL AUTO_INCREMENT,
    desctipo VARCHAR(30),
	PRIMARY KEY(tipousu),
    FOREIGN KEY(tipousu) REFERENCES usuario(tipousu)
)DEFAULT CHARSET = utf8;

CREATE TABLE campeonato(
	idcamp INT NOT NULL AUTO_INCREMENT,
	inscritos INT NOT NULL DEFAULT '0', 	
    maxinscritos INT NOT NULL DEFAULT '100',
    mininscritos INT NOT NULL DEFAULT '1',
    tipocamp INT NOT NULL DEFAULT '1',
	PRIMARY KEY(idcamp) 
)DEFAULT CHARSET = utf8;

CREATE TABLE inscricao_campeonato(
	idinscrito INT NOT NULL AUTO_INCREMENT,
    idcamp INT NOT NULL,
    idusu INT NOT NULL,
    PRIMARY KEY(idinscrito),
	FOREIGN KEY(idcamp) REFERENCES campeonato(idcamp),
    FOREIGN KEY(idusu) REFERENCES usuario(idusu)
)DEFAULT CHARSET = utf8;

INSERT INTO usuario VALUES
(DEFAULT,DEFAULT,'Vitor Regis','vitorregis27@gmail.com','2003-02-27',DEFAULT),
(DEFAULT,99,'Gio Tesser','gigitesser@gmail.com','2001-08-01',DEFAULT);

INSERT INTO tipo_usuario VALUES
(1,'Jogador'),
(99,'Administrador');

INSERT INTO campeonato VALUES
(DEFAULT,DEFAULT,DEFAULT,DEFAULT,DEFAULT);

INSERT INTO inscricao_campeonato VALUES
(DEFAULT,1,1);

SELECT * FROM usuario;
SELECT * FROM tipo_usuario;
SELECT * FROM campeonato;
SELECT * FROM inscricao_campeonato;

SELECT ins.idinscrito, usu.nomeusu, camp.tipocamp 
FROM inscricao_campeonato ins 
JOIN usuario    usu  ON ins.idusu  = usu.idusu 
JOIN campeonato camp ON ins.idcamp = camp.idcamp;

ALTER TABLE tipo_usuario
ADD FOREIGN KEY(tipousu)
REFERENCES usuario(tipousu);

SELECT tip.tipousu, usu.nomeusu
FROM tipo_usuario tip 
JOIN usuario usu  ON tip.tipousu  = usu.tipousu 
AND usu.tipousu = 99;




