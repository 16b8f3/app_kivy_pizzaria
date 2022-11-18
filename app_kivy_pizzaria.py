# Importações

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

import bancoDeDados
# import funcoes

global quantidadeMaximaDePizzaDeUmSabor # Pode ser acessada por qualquer função 
quantidadeMaximaDePizzaDeUmSabor = 10 # Defini a quantidade maxima de cada pizza

class Gerente_das_telas(ScreenManager):
    pass



class Login(Screen):
    def teste_integrarLogin(self):
        connection = bancoDeDados.create_server_connection('localhost', 'root', '')
        email = self.ids.log.text
        senha = self.ids.sen.text
        bancoDeDados.procurar(connection, email, senha)



class Cadastrar(Screen):
    def teste_integrarCadastro(self):
        connection = bancoDeDados.create_server_connection('localhost', 'root', '')
        nome = self.ids.nome.text
        sobrenome = self.ids.sobrenome.text
        email = self.ids.email.text
        senha = self.ids.senha.text
        bancoDeDados.insert_table_Contas(connection, nome, sobrenome, email, senha)
        # self.ids.nome.text = ''
        # self.ids.sobrenome.text = ''
        # self.ids.email.text = ''
        # self.ids.senha.text = ''



class Menu(Screen):
    pass



class Pedido(Screen):
# PIZZAS TRADICIONAIS

## Funções da Pizza Ads
    def pizza_Ads(self): # Ela será chamada pelas funções incrementar e decrementar
        valorUnitarioDaPizza_Ads = (float(self.ids.valor_Ads.text)) # Pega o valor da pizza e passe ele de str para float
        quantidadeDePizza_Ads = (float(self.ids.quantidade_Ads.text)) # Pega o valor do contador da pizza
        valorTotalDaPizza_Ads = quantidadeDePizza_Ads * valorUnitarioDaPizza_Ads # Faz o calculo do total da pizza multiplicando o valor e a quantidade
        return valorTotalDaPizza_Ads # Retorna o valor total da pizza

    def incrementar_Ads(self): # Será chamada sempre que for apertado o botão de + da pizza
        if (int(self.ids.quantidade_Ads.text)) < quantidadeMaximaDePizzaDeUmSabor: # Enquanto a quantidade for menor que 10 vai acontecer...
            self.ids.quantidade_Ads.text = str(int(self.ids.quantidade_Ads.text) + 1) # transforma em int soma 1 e transforma o novo valor em str
            self.pizza_Ads() # Chama a função para atualizar o valor total do pedido

            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Baiana = self.pizza_Baiana() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Bolonhesa = self.pizza_Bolonhesa() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Calabresa = self.pizza_Calabresa() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Ituiutaba = self.pizza_Ituiutaba() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Mucarela = self.pizza_Mucarela() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_QuatroQueijos = self.pizza_QuatroQueijos() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_TresQueijos = self.pizza_TresQueijos() # Atribui a variavel a função que retorna o valor total da pizza

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Champignon = self.pizza_Champignon() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_CincoQueijos = self.pizza_CincoQueijos() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Salaminho = self.pizza_Salaminho() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Vegetariana = self.pizza_Vegetariana() # Atribui a variavel a função que retorna o valor total da pizza

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Banana = self.pizza_Banana() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Brigadeiro = self.pizza_Brigadeiro() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Prestigio = self.pizza_Prestigio() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta() # Atribui a variavel a função que retorna o valor total da pizza
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta) # Chama a função responsavel para somar o valor total e mostrar ele

    def decrementar_Ads(self):
        if (int(self.ids.quantidade_Ads.text)) > 0:
            self.ids.quantidade_Ads.text = str(int(self.ids.quantidade_Ads.text) - 1) 
                
            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Baiana = self.pizza_Baiana() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Bolonhesa = self.pizza_Bolonhesa() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Calabresa = self.pizza_Calabresa() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Ituiutaba = self.pizza_Ituiutaba() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Mucarela = self.pizza_Mucarela() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_QuatroQueijos = self.pizza_QuatroQueijos() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_TresQueijos = self.pizza_TresQueijos() # Atribui a variavel a função que retorna o valor total da pizza

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Champignon = self.pizza_Champignon() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_CincoQueijos = self.pizza_CincoQueijos() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Salaminho = self.pizza_Salaminho() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Vegetariana = self.pizza_Vegetariana() # Atribui a variavel a função que retorna o valor total da pizza

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Banana = self.pizza_Banana() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Brigadeiro = self.pizza_Brigadeiro() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_Prestigio = self.pizza_Prestigio() # Atribui a variavel a função que retorna o valor total da pizza
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta() # Atribui a variavel a função que retorna o valor total da pizza
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta) # Chama a função responsavel para somar o valor total e mostrar ele



    ## Funções da Pizza Baiana
    def pizza_Baiana(self):
        valorUnitarioDaPizza_Baiana = (float(self.ids.valor_Baiana.text))
        quantidadeDePizza_Baiana = (float(self.ids.quantidade_Baiana.text))
        valorTotalDaPizza_Baiana = quantidadeDePizza_Baiana * valorUnitarioDaPizza_Baiana
        return valorTotalDaPizza_Baiana 

    def incrementar_Baiana(self): 
        if (int(self.ids.quantidade_Baiana.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Baiana.text = str(int(self.ids.quantidade_Baiana.text) + 1) 
            self.pizza_Baiana()
                
            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)

    def decrementar_Baiana(self):
        if (int(self.ids.quantidade_.text)) > 0:
            self.ids.quantidade_Baiana.text = str(int(self.ids.quantidade_Baiana.text) - 1) 
            self.pizza_Baiana()

            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)



    ## Funções da Pizza Bolonhesa
    def pizza_Bolonhesa(self):
        valorUnitarioDaPizza_Bolonhesa = (float(self.ids.valor_Bolonhesa.text))
        quantidadeDePizza_Bolonhesa = (float(self.ids.quantidade_Bolonhesa.text))
        valorTotalDaPizza_Bolonhesa = quantidadeDePizza_Bolonhesa * valorUnitarioDaPizza_Bolonhesa
        return valorTotalDaPizza_Bolonhesa

    def incrementar_Bolonhesa(self): 
        if (int(self.ids.quantidade_Bolonhesa.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Bolonhesa.text = str(int(self.ids.quantidade_Bolonhesa.text) + 1) 
            self.pizza_Bolonhesa()
              
            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)

    def decrementar_Bolonhesa(self):
        if (int(self.ids.quantidade_Bolonhesa.text)) > 0:
            self.ids.quantidade_Bolonhesa.text = str(int(self.ids.quantidade_Bolonhesa.text) - 1) 
            self.pizza_Bolonhesa()

            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)



    ## Funções da Pizza Calabresa
    def pizza_Calabresa(self):
        valorUnitarioDaPizza_Calabresa = (float(self.ids.valor_Calabresa.text))
        quantidadeDePizza_Calabresa = (float(self.ids.quantidade_Calabresa.text))
        valorTotalDaPizza_Calabresa = quantidadeDePizza_Calabresa * valorUnitarioDaPizza_Calabresa
        return valorTotalDaPizza_Calabresa 

    def incrementar_Calabresa(self): 
        if (int(self.ids.quantidade_Calabresa.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Calabresa.text = str(int(self.ids.quantidade_Calabresa.text) + 1) 
            self.pizza_Calabresa()
                
            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)

    def decrementar_Calabresa(self):
        if (int(self.ids.quantidade_Calabresa.text)) > 0:
            self.ids.quantidade_Calabresa.text = str(int(self.ids.quantidade_Calabresa.text) - 1) 
            self.pizza_Calabresa()

            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)



    ## Funções da Pizza Frango com Catupiry
    def pizza_FrangoComCatupiry(self):
        valorUnitarioDaPizza_FrangoComCatupiry = (float(self.ids.valor_FrangoComCatupiry.text))
        quantidadeDePizza_FrangoComCatupiry = (float(self.ids.quantidade_FrangoComCatupiry.text))
        valorTotalDaPizza_FrangoComCatupiry = quantidadeDePizza_FrangoComCatupiry * valorUnitarioDaPizza_FrangoComCatupiry
        return valorTotalDaPizza_FrangoComCatupiry

    def incrementar_FrangoComCatupiry(self): 
        if (int(self.ids.quantidade_FrangoComCatupiry.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_FrangoComCatupiry.text = str(int(self.ids.quantidade_FrangoComCatupiry.text) + 1) 
            self.pizza_FrangoComCatupiry()
              
            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)

    def decrementar_FrangoComCatupiry(self):
        if (int(self.ids.quantidade_.text)) > 0:
            self.ids.quantidade_FrangoComCatupiry.text = str(int(self.ids.quantidade_FrangoComCatupiry.text) - 1) 
            self.pizza_FrangoComCatupiry()

            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
               
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)



    ## Funções da Pizza Ituiutaba
    def pizza_Ituiutaba(self):
        valorUnitarioDaPizza_Ituiutaba = (float(self.ids.valor_Ituiutaba.text))
        quantidadeDePizza_Ituiutaba = (float(self.ids.quantidade_Ituiutaba.text))
        valorTotalDaPizza_Ituiutaba = quantidadeDePizza_Ituiutaba * valorUnitarioDaPizza_Ituiutaba
        return valorTotalDaPizza_Ituiutaba 

    def incrementar_Ituiutaba(self): 
        if (int(self.ids.quantidade_Ituiutaba.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Ituiutaba.text = str(int(self.ids.quantidade_Ituiutaba.text) + 1) 
            self.pizza_Ituiutaba()
                
            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
              
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)

    def decrementar_Ituiutaba(self):
        if (int(self.ids.quantidade_Ituiutaba.text)) > 0:
            self.ids.quantidade_Ituiutaba.text = str(int(self.ids.quantidade_Ituiutaba.text) - 1) 
            self.pizza_Ituiutaba()

            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)



    ## Funções da Pizza Mucarela
    def pizza_Mucarela(self):
        valorUnitarioDaPizza_Mucarela = (float(self.ids.valor_Mucarela.text))
        quantidadeDePizza_Mucarela = (float(self.ids.quantidade_Mucarela.text))
        valorTotalDaPizza_Mucarela = quantidadeDePizza_Mucarela * valorUnitarioDaPizza_Mucarela
        return valorTotalDaPizza_Mucarela 

    def incrementar_Mucarela(self): 
        if (int(self.ids.quantidade_Mucarela.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Mucarela.text = str(int(self.ids.quantidade_Mucarela.text) + 1) 
            self.pizza_Mucarela()
                
            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)

    def decrementar_Mucarela(self):
        if (int(self.ids.quantidade_Mucarela.text)) > 0:
            self.ids.quantidade_Mucarela.text = str(int(self.ids.quantidade_Mucarela.text) - 1) 
            self.pizza_Mucarela()

            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
              
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)



    ## Funções da Pizza Quatro Queijos
    def pizza_QuatroQueijos(self):
        valorUnitarioDaPizza_QuatroQueijos = (float(self.ids.valor_QuatroQueijos.text))
        quantidadeDePizza_QuatroQueijos = (float(self.ids.quantidade_QuatroQueijos.text))
        valorTotalDaPizza_QuatroQueijos = quantidadeDePizza_QuatroQueijos * valorUnitarioDaPizza_QuatroQueijos
        return valorTotalDaPizza_QuatroQueijos 

    def incrementar_QuatroQueijos(self): 
        if (int(self.ids.quantidade_QuatroQueijos.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_QuatroQueijos.text = str(int(self.ids.quantidade_QuatroQueijos.text) + 1) 
            self.pizza_QuatroQueijos()
                
            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)

    def decrementar_QuatroQueijos(self):
        if (int(self.ids.quantidade_QuatroQueijos.text)) > 0:
            self.ids.quantidade_QuatroQueijos.text = str(int(self.ids.quantidade_QuatroQueijos.text) - 1) 
            self.pizza_QuatroQueijos()

            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)



    ## Funções da Pizza Tres Queijos
    def pizza_TresQueijos(self):
        valorUnitarioDaPizza_TresQueijos = (float(self.ids.valor_TresQueijos.text))
        quantidadeDePizza_TresQueijos = (float(self.ids.quantidade_TresQueijos.text))
        valorTotalDaPizza_TresQueijos = quantidadeDePizza_TresQueijos * valorUnitarioDaPizza_TresQueijos
        return valorTotalDaPizza_TresQueijos 

    def incrementar_TresQueijos(self): 
        if (int(self.ids.quantidade_TresQueijos.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_TresQueijos.text = str(int(self.ids.quantidade_TresQueijos.text) + 1) 
            self.pizza_TresQueijos()
                
            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)

    def decrementar_TresQueijos(self):
        if (int(self.ids.quantidade_TresQueijos.text)) > 0:
            self.ids.quantidade_TresQueijos.text = str(int(self.ids.quantidade_TresQueijos.text) - 1) 
            self.pizza_TresQueijos()

            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
               
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)



    # PIZZAS ESPECIAIS

    ## Funções da Pizza Brocolis
    def pizza_Brocolis(self):
        valorUnitarioDaPizza_Brocolis = (float(self.ids.valor_Brocolis.text))
        quantidadeDePizza_Brocolis = (float(self.ids.quantidade_Brocolis.text))
        valorTotalDaPizza_Brocolis = quantidadeDePizza_Brocolis * valorUnitarioDaPizza_Brocolis
        return valorTotalDaPizza_Brocolis 

    def incrementar_Brocolis(self): 
        if (int(self.ids.quantidade_Brocolis.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Brocolis.text = str(int(self.ids.quantidade_Brocolis.text) + 1) 
            self.pizza_Brocolis()
                
            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)

    def decrementar_Brocolis(self):
        if (int(self.ids.quantidade_Brocolis.text)) > 0:
            self.ids.quantidade_Brocolis.text = str(int(self.ids.quantidade_Brocolis.text) - 1) 
            self.pizza_Brocolis()

            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)



    ## Funções da Pizza Champignon
    def pizza_Champignon(self):
        valorUnitarioDaPizza_Champignon = (float(self.ids.valor_Champignon.text))
        quantidadeDePizza_Champignon = (float(self.ids.quantidade_Champignon.text))
        valorTotalDaPizza_Champignon = quantidadeDePizza_Champignon * valorUnitarioDaPizza_Champignon
        return valorTotalDaPizza_Champignon 

    def incrementar_Champignon(self): 
        if (int(self.ids.quantidade_Champignon.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Champignon.text = str(int(self.ids.quantidade_Champignon.text) + 1) 
            self.pizza_Champignon()
                
            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)

    def decrementar_Champignon(self):
        if (int(self.ids.quantidade_Champignon.text)) > 0:
            self.ids.quantidade_Champignon.text = str(int(self.ids.quantidade_Champignon.text) - 1) 
            self.pizza_Champignon()

            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
              
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)



    ## Funções da Pizza Cinco Queijos
    def pizza_CincoQueijos(self):
        valorUnitarioDaPizza_CincoQueijos = (float(self.ids.valor_CincoQueijos.text))
        quantidadeDePizza_CincoQueijos = (float(self.ids.quantidade_CincoQueijos.text))
        valorTotalDaPizza_CincoQueijos = quantidadeDePizza_CincoQueijos * valorUnitarioDaPizza_CincoQueijos
        return valorTotalDaPizza_CincoQueijos 

    def incrementar_CincoQueijos(self): 
        if (int(self.ids.quantidade_CincoQueijos.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_CincoQueijos.text = str(int(self.ids.quantidade_CincoQueijos.text) + 1) 
            self.pizza_CincoQueijos()
                
            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)

    def decrementar_CincoQueijos(self):
        if (int(self.ids.quantidade_CincoQueijos.text)) > 0:
            self.ids.quantidade_CincoQueijos.text = str(int(self.ids.quantidade_CincoQueijos.text) - 1) 
            self.pizza_CincoQueijos()

            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)



    ## Funções da Pizza Salaminho
    def pizza_Salaminho(self):
        valorUnitarioDaPizza_Salaminho = (float(self.ids.valor_Salaminho.text))
        quantidadeDePizza_Salaminho = (float(self.ids.quantidade_Salaminho.text))
        valorTotalDaPizza_Salaminho = quantidadeDePizza_Salaminho * valorUnitarioDaPizza_Salaminho
        return valorTotalDaPizza_Salaminho

    def incrementar_Salaminho(self): 
        if (int(self.ids.quantidade_Salaminho.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Salaminho.text = str(int(self.ids.quantidade_Salaminho.text) + 1) 
            self.pizza_Salaminho()
              
            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
               
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)

    def decrementar_Salaminho(self):
        if (int(self.ids.quantidade_Salaminho.text)) > 0:
            self.ids.quantidade_Salaminho.text = str(int(self.ids.quantidade_Salaminho.text) - 1) 
            self.pizza_Salaminho()

            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
              
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)



    ## Funções da Pizza Vegetariana
    def pizza_Vegetariana(self):
        valorUnitarioDaPizza_Vegetariana = (float(self.ids.valor_Vegetariana.text))
        quantidadeDePizza_Vegetariana = (float(self.ids.quantidade_Vegetariana.text))
        valorTotalDaPizza_Vegetariana = quantidadeDePizza_Vegetariana * valorUnitarioDaPizza_Vegetariana
        return valorTotalDaPizza_Vegetariana

    def incrementar_Vegetariana(self): 
        if (int(self.ids.quantidade_Vegetariana.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Vegetariana.text = str(int(self.ids.quantidade_Vegetariana.text) + 1) 
            self.pizza_Vegetariana()
                
            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)

    def decrementar_Vegetariana(self):
        if (int(self.ids.quantidade_Vegetariana.text)) > 0:
            self.ids.quantidade_Vegetariana.text = str(int(self.ids.quantidade_Vegetariana.text) - 1) 
            self.pizza_Vegetariana()

            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)



    # PIZZAS DOCES

    ## Funções da Pizza Acai
    def pizza_Acai(self):
        valorUnitarioDaPizza_Acai = (float(self.ids.valor_Acai.text))
        quantidadeDePizza_Acai = (float(self.ids.quantidade_Acai.text))
        valorTotalDaPizza_Acai = quantidadeDePizza_Acai * valorUnitarioDaPizza_Acai
        return valorTotalDaPizza_Acai 

    def incrementar_Acai(self): 
        if (int(self.ids.quantidade_Acai.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Acai.text = str(int(self.ids.quantidade_Acai.text) + 1) 
            self.pizza_Acai()
                
            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
               
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)

    def decrementar_Acai(self):
        if (int(self.ids.quantidade_Acai.text)) > 0:
            self.ids.quantidade_Acai.text = str(int(self.ids.quantidade_Acai.text) - 1) 
            self.pizza_Acai()

            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)



    ## Funções da Pizza Banana
    def pizza_Banana(self):
        valorUnitarioDaPizza_Banana = (float(self.ids.valor_Banana.text))
        quantidadeDePizza_Banana = (float(self.ids.quantidade_Banana.text))
        valorTotalDaPizza_Banana = quantidadeDePizza_Banana * valorUnitarioDaPizza_Banana
        return valorTotalDaPizza_Banana 

    def incrementar_Banana(self): 
        if (int(self.ids.quantidade_Banana.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Banana.text = str(int(self.ids.quantidade_Banana.text) + 1) 
            self.pizza_Banana()
                
            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)

    def decrementar_Banana(self):
        if (int(self.ids.quantidade_Banana.text)) > 0:
            self.ids.quantidade_Banana.text = str(int(self.ids.quantidade_Banana.text) - 1) 
            self.pizza_Banana()

            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
             
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)



    ## Funções da Pizza Brigadeiro
    def pizza_Brigadeiro(self):
        valorUnitarioDaPizza_Brigadeiro = (float(self.ids.valor_Brigadeiro.text))
        quantidadeDePizza_Brigadeiro = (float(self.ids.quantidade_Brigadeiro.text))
        valorTotalDaPizza_Brigadeiro = quantidadeDePizza_Brigadeiro * valorUnitarioDaPizza_Brigadeiro
        return valorTotalDaPizza_Brigadeiro 

    def incrementar_Brigadeiro(self): 
        if (int(self.ids.quantidade_Brigadeiro.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Brigadeiro.text = str(int(self.ids.quantidade_Brigadeiro.text) + 1) 
            self.pizza_Brigadeiro()
                
            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)

    def decrementar_Brigadeiro(self):
        if (int(self.ids.quantidade_Brigadeiro.text)) > 0:
            self.ids.quantidade_Brigadeiro.text = str(int(self.ids.quantidade_Brigadeiro.text) - 1) 
            self.pizza_Brigadeiro()

            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)



    ## Funções da Pizza Prestigio
    def pizza_Prestigio(self):
        valorUnitarioDaPizza_Prestigio = (float(self.ids.valor_Prestigio.text))
        quantidadeDePizza_Prestigio = (float(self.ids.quantidade_Prestigio.text))
        valorTotalDaPizza_Prestigio = quantidadeDePizza_Prestigio * valorUnitarioDaPizza_Prestigio
        return valorTotalDaPizza_Prestigio 

    def incrementar_Prestigio(self): 
        if (int(self.ids.quantidade_Prestigio.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Prestigio.text = str(int(self.ids.quantidade_Prestigio.text) + 1) 
            self.pizza_Prestigio()
                
            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)

    def decrementar_Prestigio(self):
        if (int(self.ids.quantidade_Prestigio.text)) > 0:
            self.ids.quantidade_Prestigio.text = str(int(self.ids.quantidade_Prestigio.text) - 1) 
            self.pizza_Prestigio()

            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)



    ## Funções da Pizza Romeu e Julieta
    def pizza_RomeuAndJulieta(self):
        valorUnitarioDaPizza_RomeuAndJulieta = (float(self.ids.valor_RomeuAndJulieta.text))
        quantidadeDePizza_RomeuAndJulieta = (float(self.ids.quantidade_RomeuAndJulieta.text))
        valorTotalDaPizza_RomeuAndJulieta = quantidadeDePizza_RomeuAndJulieta * valorUnitarioDaPizza_RomeuAndJulieta
        return valorTotalDaPizza_RomeuAndJulieta

    def incrementar_RomeuAndJulieta(self): 
        if (int(self.ids.quantidade_RomeuAndJulieta.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_RomeuAndJulieta.text = str(int(self.ids.quantidade_RomeuAndJulieta.text) + 1) 
            self.pizza_RomeuAndJulieta()
                
            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
               
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)

    def decrementar_RomeuAndJulieta(self):
        if (int(self.ids.quantidade_RomeuAndJulieta.text)) > 0:
            self.ids.quantidade_RomeuAndJulieta.text = str(int(self.ids.quantidade_RomeuAndJulieta.text) - 1) 
            self.pizza_RomeuAndJulieta()

            ### Pizzas Tradicionais
            pizza_Ads = self.pizza_Ads()
            pizza_Baiana = self.pizza_Baiana()
            pizza_Bolonhesa = self.pizza_Bolonhesa()
            pizza_Calabresa = self.pizza_Calabresa()
            pizza_FrangoComCatupiry = self.pizza_FrangoComCatupiry()
            pizza_Ituiutaba = self.pizza_Ituiutaba()
            pizza_Mucarela = self.pizza_Mucarela()
            pizza_QuatroQueijos = self.pizza_QuatroQueijos()
            pizza_TresQueijos = self.pizza_TresQueijos()

            ### Pizzas Especiais
            pizza_Brocolis = self.pizza_Brocolis()
            pizza_Champignon = self.pizza_Champignon()
            pizza_CincoQueijos = self.pizza_CincoQueijos()
            pizza_Salaminho = self.pizza_Salaminho()
            pizza_Vegetariana = self.pizza_Vegetariana()

            ### Pizzas Doces
            pizza_Acai = self.pizza_Acai()
            pizza_Banana = self.pizza_Banana()
            pizza_Brigadeiro = self.pizza_Brigadeiro()
            pizza_Prestigio = self.pizza_Prestigio()
            pizza_RomeuAndJulieta = self.pizza_RomeuAndJulieta()
                
            self.valorTotalDoPedido(pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta)



    ## Função que faz a contabilidade do pedido 
    def valorTotalDoPedido(self, pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta): # Será chamada sempre que for apertado + ou - em qualquer pizza
        valorTotalDoPedido = pizza_Ads + pizza_Baiana + pizza_Bolonhesa + pizza_Calabresa + pizza_FrangoComCatupiry + pizza_Ituiutaba + pizza_Mucarela + pizza_QuatroQueijos + pizza_TresQueijos + pizza_Brocolis + pizza_Champignon + pizza_CincoQueijos + pizza_Salaminho + pizza_Vegetariana + pizza_Acai + pizza_Banana + pizza_Brigadeiro + pizza_Prestigio + pizza_RomeuAndJulieta # Faz a soma de todas as pizzas
        valorTotalDoPedidoFormatado = "{:.2f}".format(valorTotalDoPedido) # Deixa o valor total do pedido com apenas duas casas decimais
        self.ids.valorTotalDoPedido.text = str(valorTotalDoPedidoFormatado) # Mostra o valor total do pedido na tela
        
    


class Finalizar_Pedido(Screen):
    def spinner_Clicado(self, value):
        self.ids.forma_de_pagamento.text = value
    pass



class app_kivy_pizzaria(App):
    def build(self):
        return Gerente_das_telas()



if __name__ == '__main__':
    app_kivy_pizzaria().run()