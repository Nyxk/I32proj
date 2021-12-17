CREATE DOMAIN d_age AS INT CHECK(VALUE BETWEEN 2 AND 100);

Create DOMAIN d_sexe AS char(1) CHECK (VALUE IN ('M','F'));

CREATE TABLE parents(
id_parents INT PRIMARY KEY NOT NULL,
nom_p VARCHAR(225),
prenom_p VARCHAR(225),
age d_age,
sexe d_sexe,
adr_p VARCHAR(225),
adr_mail VARCHAR(225),
n_tel INT
);

CREATE TABLE prof (
id_prof INT PRIMARY KEY NOT NULL,
nom_prof VARCHAR(20),
prenom_prof VARCHAR(20),
age d_age,
sexe d_sexe,
adr_prof VARCHAR(50),
adr_mail_prof VARCHAR(50),
num_tel INT
);


CREATE TABLE classe(
id_classe INT PRIMARY KEY NOT NULL,
id_prof INT,
CONSTRAINT id_prof_fk
FOREIGN KEY (id_prof)
REFERENCES prof(id_prof)
ON DELETE CASCADE
);


CREATE TABLE eleve (
id_eleve INT PRIMARY KEY NOT NULL,
nom_e VARCHAR(225),
prenom_e VARCHAR(225),
adr_e VARCHAR(225),
adr_mail_e VARCHAR(255),
age d_age,
sexe d_sexe,
id_classe INT,
CONSTRAINT id_classe_fk
FOREIGN KEY(id_classe)
REFERENCES classe(id_classe)
ON DELETE CASCADE
);


CREATE TABLE famille(
id_fam INT,
id_eleve INT,
id_parents INT,
CONSTRAINT id_eleve_fk
FOREIGN KEY(id_eleve)
REFERENCES eleve (id_eleve)
ON DELETE CASCADE,
CONSTRAINT id_parents_fk
FOREIGN KEY(id_parents)
REFERENCES parents(id_parents)
ON DELETE CASCADE
);


CREATE TABLE promo(
id_promo INT , 
id_classe INT,
CONSTRAINT id_classe_fk
FOREIGN KEY(id_classe)
REFERENCES classe (id_classe)
ON DELETE CASCADE
);


CREATE TABLE a_sport(
nom_s VARCHAR(255),
id_s INT PRIMARY KEY,
id_prof INT,
CONSTRAINT id_prof_fk
FOREIGN KEY(id_prof)
REFERENCES prof (id_prof)
ON DELETE CASCADE
);


CREATE TABLE inscription_s(id_s INT,
id_eleve INT,
CONSTRAINT id_inscription_s PRIMARY KEY (id_s, id_eleve),
CONSTRAINT id_s_fk 
FOREIGN KEY (id_s) 
REFERENCES a_sport(id_s)
ON DELETE CASCADE,
CONSTRAINT id_eleve_fk 
FOREIGN KEY (id_eleve) 
REFERENCES eleve(id_eleve)
ON DELETE CASCADE
);


CREATE TABLE a_art(
nom_a VARCHAR(255),
id_a INT PRIMARY KEY,
id_prof INT,
CONSTRAINT id_prof_fk
FOREIGN KEY(id_prof)
REFERENCES prof (id_prof)
ON DELETE CASCADE
);


CREATE TABLE inscription_a(
id_a INT,
id_eleve INT,
CONSTRAINT id_inscription_a PRIMARY KEY (id_a, id_eleve),
CONSTRAINT id_a_fk 
FOREIGN KEY (id_a) 
REFERENCES a_art(id_a)
ON DELETE CASCADE,
CONSTRAINT id_eleve_fk 
FOREIGN KEY (id_eleve) 
REFERENCES eleve(id_eleve)
ON DELETE CASCADE
);


CREATE TABLE matieres(
id_matiere INT PRIMARY KEY,
n_matiere VARCHAR(255),
id_prof INT,
CONSTRAINT id_prof_fk
FOREIGN KEY (id_prof)
REFERENCES prof(id_prof)
ON DELETE CASCADE
);


CREATE TABLE services(
id_service INT PRIMARY KEY,
n_service VARCHAR(255)
);


CREATE TABLE passageService(
id_eleve INT,
id_service INT,
CONSTRAINT id_passageS PRIMARY KEY (id_eleve, id_service),
CONSTRAINT id_eleve_fk 
FOREIGN KEY (id_eleve) 
REFERENCES eleve(id_eleve)
ON DELETE CASCADE,
CONSTRAINT id_service_fk 
FOREIGN KEY (id_service) 
REFERENCES services(id_service)
ON DELETE CASCADE
);

CREATE TABLE passageserviceh(
    date_p TIMESTAMP,
    id_eleve INT
);

CREATE TABLE Empl(
id_emp INT PRIMARY KEY,
nom_e VARCHAR(225),
prenom_e VARCHAR(225),
age d_age,
sexe d_sexe,
adr_e VARCHAR(225),
adr_mail_e VARCHAR(225),
n_tel INT,
n_secu INT
);


CREATE TABLE equipe(
id_service INT,
id_emp INT,
CONSTRAINT id_equipe PRIMARY KEY ( id_service,id_emp),
CONSTRAINT id_service_fk 
FOREIGN KEY (id_service) 
REFERENCES services(id_service)
ON DELETE CASCADE,
CONSTRAINT id_emp_fk 
FOREIGN KEY (id_emp) 
REFERENCES Empl(id_emp)
ON DELETE CASCADE
);

CREATE TABLE Cours(
id_classe INT,
id_mat1 INT,
id_mat2 INT,
id_mat3 INT,
id_mat4 INT,
id_mat5 INT,
id_mat6 INT,
id_mat7 INT,
id_mat8 INT,
id_mat9 INT,
id_mat10 INT,
id_mat11 INT,
id_mat12 INT,
id_mat13 INT,
CONSTRAINT id_classe_fk 
FOREIGN KEY (id_classe) 
REFERENCES classe(id_classe)
ON DELETE CASCADE,
CONSTRAINT id_mat1_fk
FOREIGN KEY (id_mat1) 
REFERENCES matieres(id_matiere)
ON DELETE CASCADE,
CONSTRAINT id_mat2_fk
FOREIGN KEY (id_mat2) 
REFERENCES matieres(id_matiere)
ON DELETE CASCADE,
CONSTRAINT id_mat3_fk
FOREIGN KEY (id_mat3) 
REFERENCES matieres(id_matiere)
ON DELETE CASCADE,
CONSTRAINT id_mat4_fk
FOREIGN KEY (id_mat4) 
REFERENCES matieres(id_matiere)
ON DELETE CASCADE,
CONSTRAINT id_mat5_fk
FOREIGN KEY (id_mat5) 
REFERENCES matieres(id_matiere)
ON DELETE CASCADE,
CONSTRAINT id_mat6_fk
FOREIGN KEY (id_mat6) 
REFERENCES matieres(id_matiere)
ON DELETE CASCADE,
CONSTRAINT id_mat7_fk
FOREIGN KEY (id_mat7) 
REFERENCES matieres(id_matiere)
ON DELETE CASCADE,
CONSTRAINT id_mat8_fk
FOREIGN KEY (id_mat8) 
REFERENCES matieres(id_matiere)
ON DELETE CASCADE,
CONSTRAINT id_mat9_fk
FOREIGN KEY (id_mat9) 
REFERENCES matieres(id_matiere)
ON DELETE CASCADE,
CONSTRAINT id_mat10_fk
FOREIGN KEY (id_mat10) 
REFERENCES matieres(id_matiere)
ON DELETE CASCADE,
CONSTRAINT id_mat11_fk
FOREIGN KEY (id_mat11) 
REFERENCES matieres(id_matiere)
ON DELETE CASCADE,
CONSTRAINT id_mat12_fk
FOREIGN KEY (id_mat12) 
REFERENCES matieres(id_matiere)
ON DELETE CASCADE,
CONSTRAINT id_mat13_fk
FOREIGN KEY (id_mat13) 
REFERENCES matieres(id_matiere)
ON DELETE CASCADE
);

CREATE FUNCTION add_dateh()
    returns trigger as $$
    BEGIN 
        INSERT INTO passageserviceh(date_p,id_eleve)
        VALUES (NOW(),OLD.id_eleve);
        RETURN NULL;
    end;
    $$
    LANGUAGE 'plpgsql';

CREATE TRIGGER hdpass
    after insert on passageService
    EXECUTE procedure add_dateh();

 
