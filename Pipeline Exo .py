#!/usr/bin/env python
# coding: utf-8

# In[15]:


pip install psycopg2-binary


# In[16]:


import psycopg2

def connect_db():
    return psycopg2.connect(
        dbname="ecole",
        user="postgres",
        password="Hatsune3Miku,",
        host="localhost",
        port="5432"
    )

def fetch_data(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM eleves;")
    etudiants = cur.fetchall()

    cur.execute("SELECT * FROM enseignants;")
    enseignants = cur.fetchall()

    cur.close()
    return etudiants, enseignants

def associate_students_teachers(etudiants, enseignants):
    associations = {}
    enseignants_par_classe = {enseignant[-1]: enseignant for enseignant in enseignants}

    # Associer chaque élève à son enseignant
    for etudiant in etudiants:
        classe = etudiant[-1]
        enseignant_responsable = enseignants_par_classe.get(classe)
        associations[etudiant] = enseignant_responsable

    return associations

def count_students_per_teacher(etudiants, enseignants):
    enseignants_par_classe = {enseignant[-1]: enseignant for enseignant in enseignants}
    compteur_eleves = {}

    for etudiant in etudiants:
        classe = etudiant[-1]
        enseignant_responsable = enseignants_par_classe.get(classe)

        if enseignant_responsable:
            enseignant_id = enseignant_responsable[0]
            if enseignant_id not in compteur_eleves:
                compteur_eleves[enseignant_id] = 0
            compteur_eleves[enseignant_id] += 1

    return compteur_eleves

if __name__ == "__main__":
    conn = connect_db()
    etudiants, enseignants = fetch_data(conn)

    associations = associate_students_teachers(etudiants, enseignants)
    for etudiant, enseignant in associations.items():
        if enseignant: 
            print(f"{etudiant[1]} {etudiant[2]} est associé à l'enseignant {enseignant[1]} {enseignant[2]}")
        else:
            print(f"{etudiant[1]} {etudiant[2]} n'a pas d'enseignant associé.")

    compteur_eleves = count_students_per_teacher(etudiants, enseignants)
    for enseignant_id, nombre_eleves in compteur_eleves.items():
        enseignant = next(e for e in enseignants if e[0] == enseignant_id)
        print(f"L'enseignant {enseignant[1]} {enseignant[2]} a {nombre_eleves} élève(s).")

    conn.close()

