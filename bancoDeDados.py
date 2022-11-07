import mysql.connector as mysql
from mysql.connector import Error

# Cria a conexão com o Banco de dados
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connect(
            host= host_name, 
            user = user_name, 
            password = user_password
            )
        print("MySQL Database connection successful")
    except Error as err:
        print('Erro ao conectar o MySQL', err)
    return connection

# Mostra a versão do Banco de dados
def version_database(connection):
    if connection.is_connected():
        versao = connection.get_server_info()
        print('Conectado ao MySQL Server versão ', versao)
        cursor = connection.cursor()
        cursor.execute('SELECT DATABASE();')
        resultado = cursor.fetchone()
        print('Você está conectado ao banco de dados: ', resultado)

# Destroi a conexão com o Banco de dados 
def server_connection_destroy(connection):
    if (connection.is_connected()):
        cursor = connection.cursor()
        cursor.close()
        connection.close()
        connection = None
        print('Conexão MySQL está fechado')
    return connection

# Cria o banco de dados
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

# Cria a tabela Pessoas
def create_table_Pessoas(connection):
    cursor = connection.cursor()
    cursor.execute('USE pizzariaKivy')
    cursor.execute('CREATE TABLE Pessoas'
        '(id_Pessoa INT NOT NULL AUTO_INCREMENT, '
        'nome_Pessoa VARCHAR(255) NOT NULL, '
        'sobrenome_Pessoa VARCHAR(255) NOT NULL, '
        'PRIMARY KEY (id_Pessoa))'
        )

# Cria a tabela Contas 
def create_table_Contas(connection):
    cursor = connection.cursor()
    cursor.execute('USE pizzariaKivy')
    cursor.execute('CREATE TABLE Contas'
        '(id_Conta INT NOT NULL AUTO_INCREMENT PRIMARY KEY, '
        'email_Conta VARCHAR(255) NOT NULL, '
        'senha_Conta VARCHAR(255) NOT NULL,'
        'status_Conta TINYINT(1) NOT NULL DEFAULT 0,'
        'id_Pessoa_Conta INT NOT NULL, '
        'CONSTRAINT fk_id_Pessoa_Conta FOREIGN KEY (`id_Pessoa_Conta`) REFERENCES Pessoas(`id_Pessoa`), '
        'CONSTRAINT unique_email_Conta UNIQUE (email_Conta))'
        )



# Área de execução
connection = create_server_connection('localhost', 'root', '')
create_database_query = "CREATE DATABASE pizzariaKivy;"
create_database(connection, create_database_query)
version_database(connection)
create_table_Pessoas(connection)
create_table_Contas(connection)
server_connection_destroy(connection)