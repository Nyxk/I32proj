import psycopg2
from pprint import pprint
connect=int(input("Se connecter?\n1:Oui\n2:Non\n"))
conn=psycopg2.connect(dbname="proj",user="nyx",password="Nisemono12")
cur = conn.cursor()

def eleves():
    op=int(input("Choisisez option:\n1.Ajouter eleve\n2.Supprimer eleve\n3.Chercher eleve par id\n4.Chercher eleve par son nom\n5.Nombre d'eleves\n"))
    if op == 1:
        cur.execute("select id_eleve from eleve order by id_eleve desc limit 1")
        last=cur.fetchall()
        print(last)
        id=int(input("Id\n"))
        nom=(input("Nom\n"))
        prenom=(input("Prenom\n"))
        adresse=(input("Adresse\n"))
        mail=(input("Adresse email\n"))
        age=int(input("Age\n"))
        sexe=(input("Sexe(M OU F)\n"))
        idclasse=int(input("Id classe\n"))
        cur.execute("INSERT INTO eleve(id_eleve,nom_e,prenom_e,adr_e,adr_mail_e,age,sexe,id_classe) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(id,nom,prenom,adresse,mail,age,sexe,idclasse))
        conn.commit()


    elif op ==2:
        id=int(input("Id de l'eleve que vous souhaitez supprimer\n"))
        delp="DELETE FROM eleve WHERE id_eleve = %s"
        cur.execute((delp),(id,))
        conn.commit()

    
    elif op == 3:
        id=int(input("Id de l'eleve que vous souhaitez trouver par id\n"))
        celeve="SELECT * from eleve WHERE id_eleve= %s"
        cur.execute((celeve),(id,))
        parentpr=cur.fetchall()
        for i in parentpr:
            print(i)


    elif op==4:
        nom=(input("Nom de l'eleve que vous souhaitez trouver\n"))
        celeve="SELECT * from eleve WHERE nom_e= %s"
        cur.execute((celeve),(nom,))
        parentpr=cur.fetchall()
        pprint(parentpr)
    
    elif op==5:
        cur.execute("select count(id_eleve) from eleve")
        a=cur.fetchall()
        print(a)


def parents():
    op=int(input("Choisisez option:\n1.Ajouter parent\n2.Supprimer parent\n3.chercher parent par id\n4.Chercher parent par nom\n"))
    
    if op == 1:
        cur.execute("select id_parents from parents order by id_parents desc limit 1")
        last=cur.fetchall()
        print(last)
        id=int(input("Id\n"))
        nom=(input("Mom\n"))
        prenom=(input("Prenom\n"))
        age=int(input("Age\n"))
        sexe=(input("Sexe(M OU F)\n"))
        adresse=(input("Adresse\n"))
        mail=(input("Adresse email\n"))
        tel=int(input("Telephone\n"))
        cur.execute("INSERT INTO parents(id_parents,nom_p,prenom_p,age,sexe,adr_p,adr_mail,n_tel) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(id,nom,prenom,age,sexe,adresse,mail,tel))
        conn.commit()


    elif op ==2:
        id=int(input("Id du parent que vous souhaitez supprimer\n"))
        delp="DELETE FROM parents WHERE id_parents = %s"
        cur.execute((delp),(id,))
        conn.commit()


    elif op == 3:
        id=int(input("Id du parent que vous souhaitez trouver par id\n"))
        cpar="SELECT id_parents,nom_p,prenom_p from parents WHERE id_parents= %s"
        cur.execute((cpar),(id,))
        parentpr=cur.fetchall()
        pprint(parentpr)


    elif op==4:
        nom=(input("Nom parent que vous souhaitez trouver\n"))
        cpar="SELECT * from parents WHERE nom_p= %s"
        cur.execute((cpar),(nom,))
        parentpr=cur.fetchall()
        print(parentpr)


def famille():
    op=int(input("Choisisez option:\n1.Creer id famille\n2.Voir si famille a une reduction aux frais de scolarite"))
    
    if op == 1:
        id_f=int(input("Id famille\n"))
        id_e=(input("Id eleve\n"))
        id_p=(input("Id parent\n"))
        cur.execute("INSERT INTO famille(id_fam,id_eleve,id_parents) VALUES (%s,%s,%s)",(id_f,id_e,id_p))
        conn.commit()


    
def promo():
    op=int(input("Choisisez option:\n1.Voir classes appartennants a une promo\n2.Afficher tous les promos\n"))
    if op == 1:
        id_pr=int(input("Id de promo:\n"))
        cur.execute(" SELECT id_classe from promo where id_promo= %s",(id_pr,))
        aff=cur.fetchall()
        pprint(aff)
    if op==2:
        cur.execute(" SELECT id_promo from promo")
        a=cur.fetchall()
        print(a)
        


def Classe():
    op=int(input("Choisisez option:\n1.Changer le professeur principale\n2.Voir eleves appartennant a la classe"))
    if op == 1:
        
        id_p=int(input("Id du professeur a changer:\n"))
        id_pn=int(input("id du nouveau professeur principale"))
        cur.execute("UPDATE classe SET id_prof= %s where id_prof= %s",(id_pn,id_p,))
        conn.commit()
    
    if op ==2:
        id_c=int(input("Id de la classe a afficher\n"))
        cur.execute("select e.id_eleve,e.nom_e,e.prenom_e from eleve e,classe c where e.id_classe=c.id_classe and c.id_classe= %s",(id_c,))
        aff=cur.fetchall()
        for af in aff:
            print(af)

def matieres():
    op=int(input("Choisisez option:\n1.Changer le professeur de la matiere\n2.Ajouter une matiere"))
    if op==1:
        
        id_p=int(input("Id du professeur a changer:\n"))
        id_pm=int(input("id du nouveau professeur de cette matiere"))
        cur.execute("UPDATE matieres SET id_prof= %s where id_prof= %s",(id_pm,id_p,))
        conn.commit()
    
    if op==2:
        cur.execute("select id_matiere from matieres order by id_matiere desc limit 1")
        last=cur.fetchall()
        print(last)
        idmat=int(input("Id matiere\n"))
        matiere=(input("Nom de la matiere\n"))
        prof=int(input("id de l'enseignant\n"))
        cur.execute("INSERT INTO matieres(id_matiere,n_matiere,id_prof) VALUES (%s,%s,%s)",(idmat,matiere,prof,))
        conn.commit()

        

def prof():
    op=int(input("Choisisez option:\n1.Ajouter prof\n2.Supprimer prof\n3.Afficher le professeurs\n"))
    if op == 1:
        id=int(input("Id\n"))
        nom=(input("Nom\n"))
        prenom=(input("Prenom\n"))
        age=(input("Age\n"))
        sexe=(input("Sexe(M OU F)\n"))
        adresse=int(input("Adresse\n"))
        email=(input("email\n"))
        numtel=int(input("numero de tel\n"))
        cur.execute("INSERT INTO eleve(id_eleve,nom_e,prenom_e,adr_e,adr_mail_e,age,sexe,id_classe) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",(id,nom,prenom,age,sexe,adresse,email,numtel))
        conn.commit()
    if op == 2:
        idpr=int(input("Id du professeur que vous souhaitez supprimer"))
        delpr="DELETE FROM parents WHERE id_parents = %s"
        cur.execute((delpr),(idpr,))
        conn.commit()
    if op==3:
        cur.execute("select * from prof")
        a=cur.fetchall()
        for z in a:
            print(z)

    
def asso_sport():
    op=int(input("Choisisez option:\n1.Ajouter activite\n2.Inscrire un eleve\n3.Supprimer eleve\n4.Montrer les activites disponibles"))
    if op == 1:
        cur.execute("select id_s from a_sport order by id_s desc limit 1")
        last=cur.fetchall()
        print(last)
        noms=(input("Nom de l'activite"))
        ids=int(input("Id de l'activite"))
        idp=(input("Id du professeur charge de l'activite"))
        cur.execute("INSERT INTO a_sport (nom_s, id_s, id_prof) VALUES (%s,%s,%s)",(noms,ids,idp))
        conn.commit()

    if op == 2:
        eleve=int(input("id eleve"))
        ids=int(input("Id de l'activite"))
        cur.execute("INSERT INTO inscription_s(id_s,id_eleve) VALUES (%s,%s,%s)",(ids,eleve))
        conn.commit()

    if op == 3:
        eleve=int(input("id eleve"))
        cur.execute("delete from inscription_S where id_eleve=%s )",(eleve))
    if op == 4:
        cur.execute("select * from a_sport ")
        a=cur.fetchall()
        print(a)
        


def asso_art():
    op=int(input("Choisisez option:\n1.Ajouter activite\n2.Inscrire un eleve\n3.Supprimer eleve\n4."))
    if op == 1:
        cur.execute("select id_a from a_art order by id_a desc limit 1")
        last=cur.fetchall()
        print(last)
        noma=(input("Nom de l'activite"))
        ida=int(input("Id de l'activite"))
        idp=(input("Id du professeur charge de l'activite"))
        cur.execute("INSERT INTO a_art (nom_a, id_a, id_prof) VALUES (%s,%s,%s)",(noma,ida,idp))
        conn.commit()

    if op==2:
        eleve=int(input("id eleve"))
        ids=int(input("Id de l'activite"))
        cur.execute("INSERT INTO inscription_a(id_a,id_eleve) VALUES (%s,%s,%s)",(ids,eleve))
    if op == 3:
        eleve=int(input("id eleve"))
        cur.execute("delete from inscription_a where id_eleve=%s )",(eleve))
    if op == 4:
        cur.execute("select * from a_art ")
        a=cur.fetchall()
        print(a)

def services():
    op=int(input("Choisisez option:\n1.Montrer les services disponibles"))
    if op==1:
        cur.execute("select * from services ")
        a=cur.fetchall()
        print(a)
    if op==2:
        cur.execute("select * from passageserviceh") 
        a.cur.fetchall()
        print(a)

def employe():
    op=int(input("Choisisez option:\n1.Ajouter employee\n2.Supprimer employee\n3.Afficher liste\n"))
    if op == 1:
        cur.execute("select id_emp from empl order by id_emp desc limit 1")
        last=cur.fetchall()
        print(last)
        id=int(input("Id\n"))
        nom=(input("Nom\n"))
        prenom=(input("Prenom\n"))
        age=(input("Age\n"))
        sexe=(input("Sexe\n"))
        adresse=int(input("Adresse\n"))
        email=(input("Email\n"))
        numtel=int(input("N de telephone\n"))
        numsecu=int(input("n de securite sociale\n"))
        cur.execute("INSERT INTO empl(id_emp,nom_e,prenom_e,age,sexe,adr_e,adr_mail_e,n_tel,n_secu) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id,nom,prenom,age,sexe,adresse,email,numtel,numsecu))
        conn.commit()

    if op == 2:
        ide=int(input("Id de l'employe que vous souhaitez supprimer"))
        dele="DELETE FROM parents WHERE id_emp = %s"
        cur.execute((dele),(ide,))
        conn.commit()
    if op==3:
        cur.execute("select * from empl")
        a=cur.fetchall()
        for z in a:
            print(z)


while connect == 1:
    option = int(input("Choisisez option:\n1.Eleves\n2.Parents\n3.Famille\n4.Promo\n5.Classe\n6.Matieres\n7.Professeurs\n8.Services\n9.Association Sport\n10.Association Art\n11.Employes\n")) 
    if option == 1:
        eleves()
    elif option == 2:
        parents()
    elif option == 3:
        famille()
    elif option == 4:
        promo()
    elif option == 5:
        Classe()
    elif option == 6:
        matieres()
    elif option == 7:
        prof()
    elif option == 8:
        services()
    elif option == 9:
        asso_sport()
    elif option == 10:
        asso_art()
    elif option == 11:
        employe()


    connect=int(input("Continuer?\n1.Oui\n2.Non\n"))

        








