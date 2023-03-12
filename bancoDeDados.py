import mysql.connector as mysql
from mysql.connector import Error
import sys

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

def server_connection_destroy(connection):
    if (connection.is_connected()):
        cursor = connection.cursor()
        cursor.close()
        connection.close()
        connection = None
        print('Conexão MySQL está fechado')
    return connection

def insert_table_Contas(nome, sobrenome, email, senha):
    connection = create_server_connection('localhost', 'root', '')
    cursor = connection.cursor()
    cursor.execute('USE pizzariaKivy')
    teste = 1
    try:
        cursor.execute('INSERT INTO Contas'
            '(nome_Conta, sobrenome_Conta, email_Conta, senha_Conta) VALUES' 
            '(%s, %s, %s, %s);', (nome, sobrenome, email, senha)
        )

        print("Inserido",cursor.rowcount,"linha de informação.")
        connection.commit()
        cursor.close()
        connection.close()
        print("Todos os processos da inserção foram finalizados.")
        teste = 0
        return teste
    except Error as err:
        print('Erro ao conectar o MySQL', err)
        teste = 1
        return teste
    server_connection_destroy(connection)

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

    print("Inserido",cursor.rowcount,"linha de informação.")
    connection.commit()
    cursor.close()
    connection.close()
    print("Todos os processos da inserção foram finalizados.")
    server_connection_destroy(connection)

def search_account_status(email):
    connection = create_server_connection('localhost', 'root', '')
    cursor = connection.cursor()
    cursor.execute('USE pizzariaKivy')

    try:
        cursor.execute('SELECT status_Conta FROM Contas WHERE email_Conta = "{}"'.format(email))
        status_Conta = cursor.fetchall()
        status_Conta = status_Conta[0][0]
        
        if status_Conta == 0:
            return 0
        else:
            return 1
    except Error as e:
        print("Algo errado aconteceu ", e)
        return 1
    server_connection_destroy(connection)

def search_account_login(email, senha):
    retornar = 13
    retorno = 13
    connection = create_server_connection('localhost', 'root', '')
    cursor = connection.cursor()
    cursor.execute('USE pizzariaKivy')

    try:
        cursor.execute('SELECT senha_Conta FROM Contas WHERE email_Conta = "{}"'.format(email))
        senha_bd = cursor.fetchall()
        senha_bd = senha_bd[0][0]
        
        if senha == senha_bd:
            retornar = 0        
        if retornar == 0:
            return 0
        else:
            return 13
    except Error as e:
        print("Algo errado aconteceu ", e)
        return 13
    server_connection_destroy(connection)

def search_account_id(email):
    connection = create_server_connection('localhost', 'root', '')
    cursor = connection.cursor()
    cursor.execute('USE pizzariaKivy')
    
    try:
        cursor.execute('SELECT id_Conta FROM Contas WHERE email_Conta = "{}"'.format(email))
        idConta = cursor.fetchall()
        idConta = idConta[0][0]
        return idConta
    except IndexError: # esse erro é quando não encontra o email que é inserido no bando de dados
        print("OPS!!! encontramos um erro")
        return 0
    finally:
        server_connection_destroy(connection)
