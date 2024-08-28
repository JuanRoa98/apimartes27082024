#datos para la coneccion a base de datos 

dataBaseName="gestor_de_venta"
userName="root"
userPassword=""
cocentionPort=3306
server="localhost"

#Creando la conexion

dataBaseConnection=f"mysql+mysqlconnector://{userName}:{userPassword}@{server}:{cocentionPort}/{dataBaseName}"

print(dataBaseConnection)