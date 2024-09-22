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
VALUES (1, 'Mark', 'Watney', 101, '777-555-1234', 2035, 5),
        (2, 'Alice', 'Dupont', '101', '777-555-1235', 'alice@example.com', 2034, 5),
        (3, 'Bob', 'Martin', '102', '777-555-1236', 'bob@example.com', 2033, 5),
        (4, 'Claire', 'Dujardin', '103', '777-555-1237', 'claire@example.com', 2034, 6),
        (5, 'David', 'Leroy', '104', '777-555-1238', 'david@example.com', 2035, 6),
        (6, 'Eve', 'Bernard', '105', '777-555-1239', 'eve@example.com', 2033, 7),
        (7, 'Franck', 'Rousseau', '106', '777-555-1240', 'franck@example.com', 2034, 7),
        (8, 'Georges', 'Morel', '107', '777-555-1241', 'georges@example.com', 2035, 8),
        (9, 'Hélène', 'Petit', '108', '777-555-1242', 'helene@example.com', 2034, 8),
        (10, 'Isabelle', 'Giraud', '109', '777-555-1243', 'isabelle@example.com', 2035, 9),
        (11, 'Jean', 'Durand', '110', '777-555-1244', 'jean@example.com', 2035, 9);

INSERT INTO enseignants (teacher_id, prenom, nom, numero_salle, departement, annee_obtention, email, telephone, numero_classe)
VALUES (1, 'Jonas', 'Salk', 102, 'Biologie', 1947, 'jsalk@school.org', '777-555-4321', 5);
