import mysql.connector as mysql
from mysql.connector import Error
import bancoDeDados

def create_database():
    connection = bancoDeDados.create_server_connection('localhost', 'root', '')
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS pizzariaKivy;")
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")
    finally:
        bancoDeDados.server_connection_destroy(connection)

def create_table_Contas():
    connection = bancoDeDados.create_server_connection('localhost', 'root', '')
    cursor = connection.cursor()
    cursor.execute('USE pizzariaKivy')
    cursor.execute('CREATE TABLE IF NOT EXISTS Contas'
        '(id_Conta INT NOT NULL AUTO_INCREMENT PRIMARY KEY, '
        'nome_Conta VARCHAR(255) NOT NULL, '
        'sobrenome_Conta VARCHAR(255) NOT NULL, '
        'email_Conta VARCHAR(255) NOT NULL, '
        'senha_Conta VARCHAR(255) NOT NULL,'
        'status_Conta TINYINT(1) NOT NULL DEFAULT 0,'
        'CONSTRAINT unique_email_Conta UNIQUE (email_Conta))')
    bancoDeDados.server_connection_destroy(connection)

def version_database():
    connection = bancoDeDados.create_server_connection('localhost', 'root', '')
    if connection.is_connected():
        versao = connection.get_server_info()
        print('Conectado ao MySQL Server versão ', versao)
        cursor = connection.cursor()
        cursor.execute('SELECT DATABASE()')
        resultado = cursor.fetchone()
        print('Você está conectado ao banco de dados: ', resultado)
        bancoDeDados.server_connection_destroy(connection)

def create_table_Pedidos():
    connection = bancoDeDados.create_server_connection('localhost', 'root', '')
    cursor = connection.cursor()
    cursor.execute('USE pizzariaKivy')
    cursor.execute('CREATE TABLE  IF NOT EXISTS Pedidos '
        '(id_Pedidos INT NOT NULL AUTO_INCREMENT PRIMARY KEY, '
        'data_Pedido VARCHAR(10) NOT NULL, '
        'horario_Pedido VARCHAR(10) NOT NULL, '
        'telefone_Pedido VARCHAR(255) NOT NULL, '
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
    bancoDeDados.server_connection_destroy(connection)
