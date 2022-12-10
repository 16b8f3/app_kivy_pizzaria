import mysql.connector as mysql
from mysql.connector import Error
import sys

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

# Cria a tabela Contas 
def create_table_Contas(connection):
    cursor = connection.cursor()
    cursor.execute('USE pizzariaKivy')
    cursor.execute('CREATE TABLE IF NOT EXISTS Contas'
        '(id_Conta INT NOT NULL AUTO_INCREMENT PRIMARY KEY, '
        'nome_Conta VARCHAR(255) NOT NULL, '
        'sobrenome_Conta VARCHAR(255) NOT NULL, '
        'email_Conta VARCHAR(255) NOT NULL, '
        'senha_Conta VARCHAR(255) NOT NULL,'
        'status_Conta TINYINT(1) NOT NULL DEFAULT 0,'
        'CONSTRAINT unique_email_Conta UNIQUE (email_Conta))'
        )

# Inserir dado na tabela Contas
def insert_table_Contas(connection, nome, sobrenome, email, senha):
    cursor = connection.cursor()
    cursor.execute('USE pizzariaKivy')
    cursor.execute('INSERT INTO Contas'
        '(nome_Conta, sobrenome_Conta, email_Conta, senha_Conta) VALUES' 
        '(%s, %s, %s, %s);', (nome, sobrenome, email, senha)
    )

    print("Inserted",cursor.rowcount,"row(s) of data.")
    connection.commit()
    cursor.close()
    connection.close()
    print("Done.")

def procurar(connection, email, senha):
    cursor = connection.cursor()
    cursor.execute('USE pizzariaKivy')
    cursor.execute('SELECT senha_Conta FROM Contas WHERE email_Conta = "{}"'.format(email))
    senha_bd = cursor.fetchall()
    print(senha_bd[0][0])
    print(senha)
    cursor.execute('SELECT status_Conta FROM Contas WHERE email_Conta = "{}"'.format(email))
    status_Conta = cursor.fetchall()
    print(status_Conta[0][0])

    if senha_bd[0][0] == senha and status_Conta[0][0] == 0:
        print("Login realizado com sucesso!!!")
    else:
        print("Falha ao fazer o Login")
        sys.exit()
    
    # try:
    #     cursor.execute('USE pizzariaKivy')
    #     cursor.execute('SELECT senha_Conta FROM Contas WHERE email_Conta = "{}"'.format(email))
    #     senha_bd = cursor.fetchall()
    #     print(senha_bd[0][0])
    #     print(senha)
    #     cursor.execute('SELECT status_Conta FROM Contas WHERE email_Conta = "{}"'.format(email))
    #     status_Conta = cursor.fetchall()
    #     print(status_Conta[0][0])

    #     if senha_bd[0][0] == senha and status_Conta[0][0] == 0:
    #         print("Login realizado com sucesso!!!")
    #     else:
    #         print("Falha ao fazer o Login")
    #         sys.exit()

    # except:
    #     print("Erro ao validar o login")
    #     sys.exit()

def procurar_id(email):
    connection = create_server_connection('localhost', 'root', '')
    cursor = connection.cursor()
    cursor.execute('USE pizzariaKivy')
    cursor.execute('SELECT id_Conta FROM Contas WHERE email_Conta = "{}"'.format(email))
    idConta = cursor.fetchall()
    idConta = idConta[0][0]
    return idConta

# Cria a tabela Pedidos
def create_table_Pedidos(connection):
    cursor = connection.cursor()
    cursor.execute('USE pizzariaKivy')
    cursor.execute('CREATE TABLE  IF NOT EXISTS Pedidos '
        '(id_Pedidos INT NOT NULL AUTO_INCREMENT PRIMARY KEY, '
        'data_Pedido VARCHAR(10) NOT NULL, '
        'horario_Pedido VARCHAR(10) NOT NULL, '
        'telefone_Pedido INT NOT NULL, '
        'endereco_Pedido VARCHAR(255) NOT NULL, '
        'formaDePagamento_Pedido VARCHAR(255) NOT NULL, '
        'valorTotal_Pedido DOUBLE NOT NULL, '
        'status_Pedido TINYINT(1) NOT NULL DEFAULT 0, ' 
        'Contas_id_Pedido INT NOT NULL, '
        'pizza_Ads_Pedido INT NOT NULL DEFAULT 0, '
        'pizza_Baiana_Pedido INT NOT NULL DEFAULT 0, '
        'pizza_Bolonhesa_Pedido INT NOT NULL DEFAULT 0, '
        'pizza_Calabresa_Pedido INT NOT NULL DEFAULT 0, '
        'pizza_FrangoComCatupiry_Pedido INT NOT NULL DEFAULT 0, '
        'pizza_Ituiutaba_Pedido INT NOT NULL DEFAULT 0, '
        'pizza_Mucarela_Pedido INT NOT NULL DEFAULT 0, '
        'pizza_QuatroQueijos_Pedido INT NOT NULL DEFAULT 0, '
        'pizza_TresQueijos_Pedido INT NOT NULL DEFAULT 0, '
        'pizza_Brocolis_Pedido INT NOT NULL DEFAULT 0, ' 
        'pizza_Champignon_Pedido INT NOT NULL DEFAULT 0, '
        'pizza_CincoQueijos_Pedido INT NOT NULL DEFAULT 0, '
        'pizza_Salaminho_Pedido INT NOT NULL DEFAULT 0, '
        'pizza_Vegetariana_Pedido INT NOT NULL DEFAULT 0, '
        'pizza_Acai_Pedido INT NOT NULL DEFAULT 0, '
        'pizza_Banana_Pedido INT NOT NULL DEFAULT 0, '
        'pizza_Brigadeiro_Pedido INT NOT NULL DEFAULT 0, '
        'pizza_Prestigio_Pedido INT NOT NULL DEFAULT 0, '
        'pizza_RomeuAndJulieta_Pedido INT NOT NULL DEFAULT 0, '
        'CONSTRAINT fk_Contas_id_Pedido FOREIGN KEY (`Contas_id_Pedido`) REFERENCES `Contas` (`id_Conta`))'
    )

def insert_table_Pedidos(
    data_Pedido, 
    horario_Pedido, 
    telefone_Pedido, 
    endereco_Pedido, 
    formaDePagamento_Pedido, 
    valorTotal_Pedido, 
    Contas_id_Pedido, 
    pizza_Ads_Pedido, 
    pizza_Baiana_Pedido, 
    pizza_Bolonhesa_Pedido, 
    pizza_Calabresa_Pedido, 
    pizza_FrangoComCatupiry_Pedido, 
    pizza_Ituiutaba_Pedido, 
    pizza_Mucarela_Pedido, 
    pizza_QuatroQueijos_Pedido, 
    pizza_TresQueijos_Pedido, 
    pizza_Brocolis_Pedido, 
    pizza_Champignon_Pedido, 
    pizza_CincoQueijos_Pedido, 
    pizza_Salaminho_Pedido, 
    pizza_Vegetariana_Pedido, 
    pizza_Acai_Pedido, 
    pizza_Banana_Pedido, 
    pizza_Brigadeiro_Pedido, 
    pizza_Prestigio_Pedido, 
    pizza_RomeuAndJulieta_Pedido):
    connection = create_server_connection('localhost', 'root', '')
    cursor = connection.cursor()
    cursor.execute('USE pizzariaKivy')
    cursor.execute('INSERT INTO Pedidos'
        '(data_Pedido, '
        'horario_Pedido, '
        'telefone_Pedido, '
        'endereco_Pedido, '
        'formaDePagamento_Pedido, '
        'valorTotal_Pedido, '
        'Contas_id_Pedido, '
        'pizza_Ads_Pedido, '
        'pizza_Baiana_Pedido, '
        'pizza_Bolonhesa_Pedido, '
        'pizza_Calabresa_Pedido, '
        'pizza_FrangoComCatupiry_Pedido, '
        'pizza_Ituiutaba_Pedido, '
        'pizza_Mucarela_Pedido, '
        'pizza_QuatroQueijos_Pedido, '
        'pizza_TresQueijos_Pedido, '
        'pizza_Brocolis_Pedido, '
        'pizza_Champignon_Pedido, '
        'pizza_CincoQueijos_Pedido, '
        'pizza_Salaminho_Pedido, '
        'pizza_Vegetariana_Pedido, '
        'pizza_Acai_Pedido, '
        'pizza_Banana_Pedido, '
        'pizza_Brigadeiro_Pedido, '
        'pizza_Prestigio_Pedido, '
        'pizza_RomeuAndJulieta_Pedido) VALUES'
        '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);', (
            data_Pedido, 
            horario_Pedido, 
            telefone_Pedido, 
            endereco_Pedido, 
            formaDePagamento_Pedido, 
            valorTotal_Pedido, 
            Contas_id_Pedido, 
            pizza_Ads_Pedido, 
            pizza_Baiana_Pedido, 
            pizza_Bolonhesa_Pedido, 
            pizza_Calabresa_Pedido, 
            pizza_FrangoComCatupiry_Pedido, 
            pizza_Ituiutaba_Pedido, 
            pizza_Mucarela_Pedido, 
            pizza_QuatroQueijos_Pedido, 
            pizza_TresQueijos_Pedido, 
            pizza_Brocolis_Pedido, 
            pizza_Champignon_Pedido, 
            pizza_CincoQueijos_Pedido, 
            pizza_Salaminho_Pedido, 
            pizza_Vegetariana_Pedido, 
            pizza_Acai_Pedido, 
            pizza_Banana_Pedido, 
            pizza_Brigadeiro_Pedido, 
            pizza_Prestigio_Pedido, 
            pizza_RomeuAndJulieta_Pedido
        )
    )

    print("Inserted",cursor.rowcount,"row(s) of data.")
    connection.commit()
    cursor.close()
    connection.close()
    print("Done.")



# connection = create_server_connection('localhost', 'root', '')
# create_database_query = "CREATE DATABASE IF NOT EXISTS pizzariaKivy;"
# create_database(connection, create_database_query)
# version_database(connection)
# create_table_Contas(connection)
# create_table_Pedidos(connection)
# server_connection_destroy(connection)
