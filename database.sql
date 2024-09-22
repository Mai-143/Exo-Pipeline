CREATE DATABASE ecole;

CREATE TABLE eleves (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    prenom VARCHAR(50) NOT NULL,
    nom VARCHAR(50) NOT NULL,
    numero_salle INT NOT NULL,
    telephone VARCHAR(20) NOT NULL UNIQUE, 
    email VARCHAR(100) UNIQUE,             
    annee_obtention INT NOT NULL,
    numero_classe INT NOT NULL
);

CREATE TABLE enseignants (
    teacher_id INT PRIMARY KEY AUTO_INCREMENT,
    prenom VARCHAR(50) NOT NULL,
    nom VARCHAR(50) NOT NULL,
    numero_salle INT NOT NULL,
    departement VARCHAR(100) NOT NULL,
    annee_obtention INT NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,    
    telephone VARCHAR(20) NOT NULL UNIQUE,
    numero_classe INT NOT NULL
);

INSERT INTO eleves (student_id, prenom, nom, numero_salle, telephone, annee_obtention, numero_classe)
VALUES (1, 'Mark', 'Watney', 101, '777-555-1234', 2035, 5);

INSERT INTO enseignants (teacher_id, prenom, nom, numero_salle, departement, annee_obtention, email, telephone, numero_classe)
VALUES (1, 'Jonas', 'Salk', 102, 'Biologie', 1947, 'jsalk@school.org', '777-555-4321', 5);
