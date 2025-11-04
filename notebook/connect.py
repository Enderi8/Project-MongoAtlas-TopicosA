from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()


MONGO_URI = os.getenv("MONGODB_URI_ATLAS")
DB_NAME_ATLAS = os.getenv("MONGODB_DATA")

try:
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME_ATLAS]
    print("Conexión exitosa a la base de datos MongoDB Atlas")
    colecciones = db.list_collection_names()
    print("Conectando Mongo DB Atlas: Base de datos", (DB_NAME_ATLAS))
    print("Colecciones disponibles:", (colecciones))

except errors.ServerSelectionTimeoutError as e:
    print("Error al conectar con la base de datos MongoDB Atlas", e)

except errors.OperationFailure as e:
    print("Error de autenticación con la base de datos MongoDB Atlas", e)   

except Exception as e:
    print("Ocurrió un error inesperado:", e)