CREATE DATABASE desafio1;

USE desafio1;

CREATE TABLE TB_Clientes (
    id INT IDENTITY(1,1) PRIMARY KEY,
    NomeCliente NVARCHAR(150),
    CEP NVARCHAR(50),
    DataNascimento DATE
);

CREATE TABLE TB_Faixa_Etaria (
    id INT IDENTITY(1,1) PRIMARY KEY,
    uf NVARCHAR(20),
	twenty_to_thirty INT,
    thirty_one_to_sixty INT,
    more_than_sixty INT
);


SELECT * FROM TB_Clientes;
SELECT * FROM TB_Faixa_Etaria;
