import mysql.connector
from PIL import Image
from io import BytesIO

connection = mysql.connector.connect(host='servinfo-maria',
                                        database='DBkaplia',
                                        user='kaplia',
                                        password='kaplia')
cursor = connection.cursor()

cursor.execute("SELECT photo FROM GROUPE WHERE idgroupe = 1")

# Récupérer les données de l'image
image_data = cursor.fetchone()[0]

# Fermer le curseur
cursor.close()

# Fermer la connexion à la base de données
connection.close()

# Afficher l'image à l'aide de Pillow
image = Image.open(BytesIO(image_data))
image.show()