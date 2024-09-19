#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install psycopg2-binary


# In[6]:


import psycopg2

db_config = {
    'dbname': 'ecole',  
    'user': 'postgres', 
    'password': 'Hatsune3Miku,',
    'host': 'localhost', 
    'port': '5432'          

try:
    # Connexion
    connection = psycopg2.connect(**db_config)
    cursor = connection.cursor()
    
    # Extraction des données des tables
    query = "SELECT * FROM eleves;"
    cursor.execute(query)
    
    # Récupération des résultats
    students = cursor.fetchall()

    # Affichage des données
    print("Liste des étudiants :")
    for student in students:
        print(f"ID: {student[0]}, Prénom: {student[1]}, Nom: {student[2]}, Téléphone: {student[4]}, Email: {student[5]}")
    
    # Fermeture du curseur et de la connexion
    cursor.close()
    connection.close()

except Exception as error:
    print(f"Erreur de connexion à la base de données: {error}")


# In[8]:


eleves = [
    (1, 'Mark', 'Watney', 5),
    (2, 'John', 'Doe', 4),
    (3, 'Jane', 'Smith', 5)
]

enseignants = [
    (1, 'Jonas', 'Salk', 5),
    (2, 'Albert', 'Einstein', 4)
]

associations = []

for eleve in eleves:
    student_id, prenom_eleve, nom_eleve, classe_eleve = eleve
    for enseignant in enseignants:
        teacher_id, prenom_enseignant, nom_enseignant, classe_enseignant = enseignant
        if classe_eleve == classe_enseignant:
            associations.append({
                "eleve": f"{prenom_eleve} {nom_eleve}",
                "enseignant": f"{prenom_enseignant} {nom_enseignant}",
                "classe": classe_eleve
            })

# Afficher les associations
for association in associations:
    print(f"L'élève {association['eleve']} est assigné à l'enseignant {association['enseignant']} pour la classe {association['classe']}")


# In[9]:


eleve_count = {}

for eleve in eleves:
    student_id, prenom_eleve, nom_eleve, classe_eleve = eleve
    # Trouver l'enseignant correspondant à la classe
    for enseignant in enseignants:
        teacher_id, prenom_enseignant, nom_enseignant, classe_enseignant = enseignant
        if classe_eleve == classe_enseignant:
            # Créer une clé pour l'enseignant
            enseignant_nom = f"{prenom_enseignant} {nom_enseignant}"
            if enseignant_nom in eleve_count:
                eleve_count[enseignant_nom] += 1
            else:
                eleve_count[enseignant_nom] = 1

for enseignant, count in eleve_count.items():
    print(f"L'enseignant {enseignant} a {count} élève(s) sous sa responsabilité.")


# In[1]:


import psycopg2

# Connexion à la base de données PostgreSQL
def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="ecole", user="postgres", password="Hatsune3Miku,", host="localhost", port="5432"
        )
        print("Connexion réussie à la base de données.")
        return conn
    except Exception as e:
        print(f"Erreur lors de la connexion à la base de données : {e}")
        return None


def get_data(conn):
        cur = conn.cursor()

        # Requête pour extraire les élèves
        cur.execute("SELECT student_id, prenom, nom, numero_classe FROM eleves;")
        eleves = cur.fetchall()

        # Requête pour extraire les enseignants
        cur.execute("SELECT teacher_id, prenom, nom, numero_classe FROM enseignants;")
        enseignants = cur.fetchall()

        cur.close()
        return eleves, enseignants

# Associer chaque élève à son enseignant responsable
def associate_students_with_teachers(eleves, enseignants):
    associations = []

    for eleve in eleves:
        student_id, prenom_eleve, nom_eleve, classe_eleve = eleve
        for enseignant in enseignants:
            teacher_id, prenom_enseignant, nom_enseignant, classe_enseignant = enseignant
            if classe_eleve == classe_enseignant:
                associations.append((prenom_eleve, nom_eleve, prenom_enseignant, nom_enseignant))

    return associations

# Compter le nombre d'élèves par enseignant
def count_students_per_teacher(associations):
    eleve_count = {}

    for association in associations:
        prenom_eleve, nom_eleve, prenom_enseignant, nom_enseignant = association
        enseignant_nom = f"{prenom_enseignant} {nom_enseignant}"
        if enseignant_nom in eleve_count:
            eleve_count[enseignant_nom] += 1
        else:
            eleve_count[enseignant_nom] = 1

    return eleve_count

# Afficher les résultats
def display_results(eleve_count):
    for enseignant, count in eleve_count.items():
        print(f"L'enseignant {enseignant} a {count} élève(s) sous sa responsabilité.")

# Automatisation du pipeline
def main():
    # Connexion à la base de données
    conn = connect_to_db()
    if conn is None:
        return

    # Extraction des données
    eleves, enseignants = get_data(conn)
    if not eleves or not enseignants:
        print("Aucune donnée trouvée.")
        conn.close()
        return

    # Associer les élèves à leurs enseignants
    associations = associate_students_with_teachers(eleves, enseignants)

    # Compter le nombre d'élèves par enseignant
    eleve_count = count_students_per_teacher(associations)

    # Afficher les résultats
    display_results(eleve_count)

    # Fermeture de la connexion à la base de données
    conn.close()
    print("Connexion fermée.")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




