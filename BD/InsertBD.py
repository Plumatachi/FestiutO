import mysql.connector


liste_groupe = [(1,'Les Rolling Stones', 'Un groupe de rock britannique formé à Londres en 1962.', 'twitter.com/rollingstones', "../static/Images/logo-Rolling-Stones.jpg", 4),

(2,'The Beatles', 'Un groupe de rock britannique formé à Liverpool en 1960.', 'twitter.com/thebeatles', "../static/Images/beatles.jpg", 4),


(3,'AC/DC', 'Un groupe de hard rock australien formé à Sydney en 1973.', 'twitter.com/acdc', "../static/Images/acdc.jpg", 4),


(4,'Metallica', 'Un groupe de thrash metal américain formé à Los Angeles en 1981.', 'twitter.com/metallica', "../static/Images/Logo-Metallica.jpg", 4),


(5,'Pink Floyd', 'Un groupe de rock progressif britannique formé à Londres en 1965.', 'twitter.com/pinkfloyd', "../static/Images/pinkFloyd.jpg", 4)
]

# Convert images or files data to binary format
def convert_data(file_name):
    with open(file_name, 'rb') as file:
        binary_data = file.read()
    return binary_data





try:
    connection = mysql.connector.connect(host='servinfo-maria',
                                         database='DBkaplia',
                                         user='kaplia',
                                         password='kaplia')
    cursor = connection.cursor()


    query = """ INSERT INTO GROUPE(idgroupe, nomDuGroupe, description, reseausocial, photo, nbpersonne)\
	VALUES (%s,%s,%s,%s,%s,%s)"""

    for elem in liste_groupe:
        idgroupe = elem[0]
        nomDuGroupe = elem[1]
        description = elem[2]
        reseausocial = elem[3]
        photo = convert_data(
            elem[4])
        nbpersonne = elem[5]
        # Inserting the data in database in tuple format
        result = cursor.execute(
            query,
            (idgroupe, nomDuGroupe, description,reseausocial,photo,nbpersonne))
        # Committing the data
        connection.commit()

        print("Successfully Inserted Values")

    
    # Lire le fichier SQL
    with open('insFestKaplia.sql', 'r') as file:
        sql_statements = file.read()

    # Séparer les instructions par le point-virgule
    statements = sql_statements.split(';')

    # Exécuter chaque instruction
    for statement in statements:
        try:
            cursor.execute(statement)
        except mysql.connector.Error as err:
            print(f"Erreur d'exécution : {err}")

    # Valider (commit) les modifications
    connection.commit()


# Print error if occurred
except mysql.connector.Error as error:
    print(format(error))

finally:

    # Closing all resources
    if connection.is_connected():

        cursor.close()
        connection.close()
        print("MySQL connection is closed")
        






        
