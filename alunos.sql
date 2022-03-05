CREATE TABLE Aluno
(
Nr_Rgm number(8) not null,
Nm_Nome varchar2(40) not null,
Nm_Pai varchar2(40),
Nm_Mãe varchar2(40),
Dt_Nascimento date not null,
Id_Sexo char(1) not null,
primary Key (Nr_Rgm)
);

CREATE TABLE  Classe
(
Cd_Classe number(8) not null,
Nr_AnoLetivo number(4),
Nr_Serie number(2),
Sg_Turma varchar(2),
Cd_Escola number(6),
Cd_Grau number(2),
Cd_Periodo number(2),
primary Key (Cd_Classe)
);

CREATE TABLE Matricula
(
Nr_Rgm number(8) not null,
Cd_Classe number(8) not null,
Dt_Matricula date not null,
primary Key (Nr_Rgm, Cd_Classe),
foreign Key (Nr_Rgm) references Aluno(Nr_Rgm),
foreign Key (Cd_Classe) references Classe(Cd_Classe)
);

select * from aluno

insert into Aluno 
(Nr_Rgm, Nm_Nome, Nm_Pai, Nm_Mae, Dt_Nascimento, Id_sexo)
values 
(26543,'lucas','asteu','roberta',DATE'2002-02-27','m');

select * from matricula

insert into Matricula
(Nr_rgm, Cd_classe, Dt_matricula)
values
(26543,'lucas','02',DATE'2020-01-29');

select * from Classe

insert into 
(Cd_Classe, Nr_AnoLetivo, Nr_Serie, Sg_Turma, Cd_Escola, Cd_Grau, Cd_Periodo)
values
(02,2020,'1º',01,'Humberto Paschoal','9º ano','manhã')
