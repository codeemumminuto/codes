#pip install mysql-connector-python
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="meubanco"
)

cursor = conexao.cursor()
#Criando uma tabela
cursor.execute("CREATE TABLE minhatabela (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), idade INT)")

#Inserindo registros
#Registro 1
sql = "INSERT INTO minhatabela (nome, idade) VALUES (%s, %s)"
cursor.execute(sql, ("João", 22))
conexao.commit()
#Registro 2
sql = "INSERT INTO minhatabela (nome, idade) VALUES (%s, %s)"
cursor.execute(sql, ("Maria", 19))
conexao.commit()

#Lendo os registros existentes na tabela
sql = "SELECT * FROM minhatabela"
cursor.execute(sql)
pessoas = cursor.fetchall()
for pessoa in pessoas:
    print(f"Aluno: {pessoa[1]}, Idade: {pessoa[2]}")