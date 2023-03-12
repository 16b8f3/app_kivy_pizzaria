from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.popup import Popup
from datetime import datetime

import requests
import json
import Verificar_email
import Verificar_telefone
import bancoDeDados

global quantidadeMaximaDePizzaDeUmSabor 
global horarioQuePizzariaComecaReceberPedidos
global horarioQuePizzariaParaDeReceberPedidos

quantidadeMaximaDePizzaDeUmSabor = 10 
horarioQuePizzariaComecaReceberPedidos = "19:00:00" 
horarioQuePizzariaParaDeReceberPedidos = "23:00:00"

class windowManager(ScreenManager):
    pass

class Login(Screen):
    email = ObjectProperty(None)
    senha = ObjectProperty(None)
    def validar(self):
        if self.email.text != "" and self.senha.text != "":
            verificaEmail = Verificar_email.check(self.email.text)
            if verificaEmail != 1: 
                proc = bancoDeDados.search_account_id(self.email.text)
                if proc != 0: 
                    status = bancoDeDados.search_account_status(self.email.text)
                    if status == 0:
                        senha = bancoDeDados.search_account_login(self.email.text, self.senha.text)
                        if senha != 13:
                            email = self.email.text
                            arquivo = open('./email.txt', 'w')
                            arquivo.write(email)
                            arquivo.close()
                            self.limparCamposLogin()
                            gerenciadorDeJanelas.current = 'menu'
                        else:
                            Popup_EmailOuSenhaIncorreto.popFun()
                    else:
                        Popup_ContaDesativada.popFun()
                else:
                    Popup_EmailOuSenhaIncorreto.popFun()
            else:
                Popup_EmailInvalido.popFun()
        else: 
            Popup_CampoVazio.popFun()

    def limparCamposLogin(self):
        self.ids.email.text = ''
        self.ids.senha.text = ''
    
class Cadastrar(Screen):
    nome = ObjectProperty(None)
    sobrenome = ObjectProperty(None)
    email = ObjectProperty(None)
    senha = ObjectProperty(None)
    confirmarSenha = ObjectProperty(None)
    def validar(self):
        if self.nome.text != "" and self.sobrenome.text != "" and self.email.text != "" and self.senha.text != "":
            verificaEmail = Verificar_email.check(self.email.text)
            if verificaEmail != 1:
                if len(self.senha.text) >= 6 and len(self.senha.text) <= 20:
                    if self.senha.text == self.confirmarSenha.text:
                        verifica = bancoDeDados.insert_table_Contas(self.nome.text, self.sobrenome.text, self.email.text, self.senha.text)
                        if verifica == 0:
                            Popup_CadastroRealizadoComSucesso.popFun() 
                            self.limparCamposCadastro()
                        else:
                            Popup_ErroInesperado.popFun()
                    else:
                        Popup_SenhasDiferentes.popFun()
                else:
                    Popup_LimiteDeCarateresNaSenha.popFun()
            else:
                Popup_EmailInvalido.popFun()
        else:
            Popup_CampoVazio.popFun()

    def limparCamposCadastro(self):
        self.ids.nome.text = ''
        self.ids.sobrenome.text = ''
        self.ids.email.text = ''
        self.ids.senha.text = ''
        self.ids.confirmarSenha.text = ''
    
class Menu(Screen):
    pass

class Pedido(Screen):
    # PIZZAS TRADICIONAIS
    def pizza_Ads(self): 
        valorUnitarioDaPizza_Ads = (float(self.ids.valor_Ads.text)) 
        quantidadeDePizza_Ads = (float(self.ids.quantidade_Ads.text)) 
        valorTotalDaPizza_Ads = quantidadeDePizza_Ads * valorUnitarioDaPizza_Ads 
        return valorTotalDaPizza_Ads 

    def incrementar_Ads(self): 
        if (int(self.ids.quantidade_Ads.text)) < quantidadeMaximaDePizzaDeUmSabor: 
            self.ids.quantidade_Ads.text = str(int(self.ids.quantidade_Ads.text) + 1)
            self.pizza_Ads() 
            self.atualizaValores()
        elif (int(self.ids.quantidade_Ads.text)) == 10:
            Popup_LimiteMaximoPorPizza.popFun()

    def decrementar_Ads(self):
        if (int(self.ids.quantidade_Ads.text)) > 0:
            self.ids.quantidade_Ads.text = str(int(self.ids.quantidade_Ads.text) - 1) 
            self.atualizaValores()

    def pizza_Baiana(self):
        valorUnitarioDaPizza_Baiana = (float(self.ids.valor_Baiana.text))
        quantidadeDePizza_Baiana = (float(self.ids.quantidade_Baiana.text))
        valorTotalDaPizza_Baiana = quantidadeDePizza_Baiana * valorUnitarioDaPizza_Baiana
        return valorTotalDaPizza_Baiana 

    def incrementar_Baiana(self): 
        if (int(self.ids.quantidade_Baiana.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Baiana.text = str(int(self.ids.quantidade_Baiana.text) + 1) 
            self.pizza_Baiana()   
            self.atualizaValores()
        elif (int(self.ids.quantidade_Baiana.text)) == 10:
            Popup_LimiteMaximoPorPizza.popFun()

    def decrementar_Baiana(self):
        if (int(self.ids.quantidade_Baiana.text)) > 0:
            self.ids.quantidade_Baiana.text = str(int(self.ids.quantidade_Baiana.text) - 1) 
            self.pizza_Baiana()
            self.atualizaValores()

    def pizza_Bolonhesa(self):
        valorUnitarioDaPizza_Bolonhesa = (float(self.ids.valor_Bolonhesa.text))
        quantidadeDePizza_Bolonhesa = (float(self.ids.quantidade_Bolonhesa.text))
        valorTotalDaPizza_Bolonhesa = quantidadeDePizza_Bolonhesa * valorUnitarioDaPizza_Bolonhesa
        return valorTotalDaPizza_Bolonhesa

    def incrementar_Bolonhesa(self): 
        if (int(self.ids.quantidade_Bolonhesa.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Bolonhesa.text = str(int(self.ids.quantidade_Bolonhesa.text) + 1) 
            self.pizza_Bolonhesa()
            self.atualizaValores()
        elif (int(self.ids.quantidade_Bolonhesa.text)) == 10:
            Popup_LimiteMaximoPorPizza.popFun()

    def decrementar_Bolonhesa(self):
        if (int(self.ids.quantidade_Bolonhesa.text)) > 0:
            self.ids.quantidade_Bolonhesa.text = str(int(self.ids.quantidade_Bolonhesa.text) - 1) 
            self.pizza_Bolonhesa()
            self.atualizaValores()

    def pizza_Calabresa(self):
        valorUnitarioDaPizza_Calabresa = (float(self.ids.valor_Calabresa.text))
        quantidadeDePizza_Calabresa = (float(self.ids.quantidade_Calabresa.text))
        valorTotalDaPizza_Calabresa = quantidadeDePizza_Calabresa * valorUnitarioDaPizza_Calabresa
        return valorTotalDaPizza_Calabresa 

    def incrementar_Calabresa(self): 
        if (int(self.ids.quantidade_Calabresa.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Calabresa.text = str(int(self.ids.quantidade_Calabresa.text) + 1) 
            self.pizza_Calabresa()
            self.atualizaValores()
        elif (int(self.ids.quantidade_Calabresa.text)) == 10:
            Popup_LimiteMaximoPorPizza.popFun()

    def decrementar_Calabresa(self):
        if (int(self.ids.quantidade_Calabresa.text)) > 0:
            self.ids.quantidade_Calabresa.text = str(int(self.ids.quantidade_Calabresa.text) - 1) 
            self.pizza_Calabresa()
            self.atualizaValores()

    def pizza_FrangoComCatupiry(self):
        valorUnitarioDaPizza_FrangoComCatupiry = (float(self.ids.valor_FrangoComCatupiry.text))
        quantidadeDePizza_FrangoComCatupiry = (float(self.ids.quantidade_FrangoComCatupiry.text))
        valorTotalDaPizza_FrangoComCatupiry = quantidadeDePizza_FrangoComCatupiry * valorUnitarioDaPizza_FrangoComCatupiry
        return valorTotalDaPizza_FrangoComCatupiry

    def incrementar_FrangoComCatupiry(self): 
        if (int(self.ids.quantidade_FrangoComCatupiry.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_FrangoComCatupiry.text = str(int(self.ids.quantidade_FrangoComCatupiry.text) + 1) 
            self.pizza_FrangoComCatupiry()
            self.atualizaValores()
        elif (int(self.ids.quantidade_FrangoComCatupiry.text)) == 10:
            Popup_LimiteMaximoPorPizza.popFun()

    def decrementar_FrangoComCatupiry(self):
        if (int(self.ids.quantidade_FrangoComCatupiry.text)) > 0:
            self.ids.quantidade_FrangoComCatupiry.text = str(int(self.ids.quantidade_FrangoComCatupiry.text) - 1) 
            self.pizza_FrangoComCatupiry()
            self.atualizaValores()

    def pizza_Ituiutaba(self):
        valorUnitarioDaPizza_Ituiutaba = (float(self.ids.valor_Ituiutaba.text))
        quantidadeDePizza_Ituiutaba = (float(self.ids.quantidade_Ituiutaba.text))
        valorTotalDaPizza_Ituiutaba = quantidadeDePizza_Ituiutaba * valorUnitarioDaPizza_Ituiutaba
        return valorTotalDaPizza_Ituiutaba 

    def incrementar_Ituiutaba(self): 
        if (int(self.ids.quantidade_Ituiutaba.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Ituiutaba.text = str(int(self.ids.quantidade_Ituiutaba.text) + 1) 
            self.pizza_Ituiutaba()  
            self.atualizaValores()
        elif (int(self.ids.quantidade_Ituiutaba.text)) == 10:
            Popup_LimiteMaximoPorPizza.popFun()

    def decrementar_Ituiutaba(self):
        if (int(self.ids.quantidade_Ituiutaba.text)) > 0:
            self.ids.quantidade_Ituiutaba.text = str(int(self.ids.quantidade_Ituiutaba.text) - 1) 
            self.pizza_Ituiutaba()
            self.atualizaValores()

    def pizza_Mucarela(self):
        valorUnitarioDaPizza_Mucarela = (float(self.ids.valor_Mucarela.text))
        quantidadeDePizza_Mucarela = (float(self.ids.quantidade_Mucarela.text))
        valorTotalDaPizza_Mucarela = quantidadeDePizza_Mucarela * valorUnitarioDaPizza_Mucarela
        return valorTotalDaPizza_Mucarela 

    def incrementar_Mucarela(self): 
        if (int(self.ids.quantidade_Mucarela.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Mucarela.text = str(int(self.ids.quantidade_Mucarela.text) + 1) 
            self.pizza_Mucarela() 
            self.atualizaValores()
        elif (int(self.ids.quantidade_Mucarela.text)) == 10:
            Popup_LimiteMaximoPorPizza.popFun()

    def decrementar_Mucarela(self):
        if (int(self.ids.quantidade_Mucarela.text)) > 0:
            self.ids.quantidade_Mucarela.text = str(int(self.ids.quantidade_Mucarela.text) - 1) 
            self.pizza_Mucarela()
            self.atualizaValores()

    def pizza_QuatroQueijos(self):
        valorUnitarioDaPizza_QuatroQueijos = (float(self.ids.valor_QuatroQueijos.text))
        quantidadeDePizza_QuatroQueijos = (float(self.ids.quantidade_QuatroQueijos.text))
        valorTotalDaPizza_QuatroQueijos = quantidadeDePizza_QuatroQueijos * valorUnitarioDaPizza_QuatroQueijos
        return valorTotalDaPizza_QuatroQueijos 

    def incrementar_QuatroQueijos(self): 
        if (int(self.ids.quantidade_QuatroQueijos.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_QuatroQueijos.text = str(int(self.ids.quantidade_QuatroQueijos.text) + 1) 
            self.pizza_QuatroQueijos()
            self.atualizaValores()
        elif (int(self.ids.quantidade_QuatroQueijos.text)) == 10:
            Popup_LimiteMaximoPorPizza.popFun()

    def decrementar_QuatroQueijos(self):
        if (int(self.ids.quantidade_QuatroQueijos.text)) > 0:
            self.ids.quantidade_QuatroQueijos.text = str(int(self.ids.quantidade_QuatroQueijos.text) - 1) 
            self.pizza_QuatroQueijos()
            self.atualizaValores()

    def pizza_TresQueijos(self):
        valorUnitarioDaPizza_TresQueijos = (float(self.ids.valor_TresQueijos.text))
        quantidadeDePizza_TresQueijos = (float(self.ids.quantidade_TresQueijos.text))
        valorTotalDaPizza_TresQueijos = quantidadeDePizza_TresQueijos * valorUnitarioDaPizza_TresQueijos
        return valorTotalDaPizza_TresQueijos 

    def incrementar_TresQueijos(self): 
        if (int(self.ids.quantidade_TresQueijos.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_TresQueijos.text = str(int(self.ids.quantidade_TresQueijos.text) + 1) 
            self.pizza_TresQueijos()
            self.atualizaValores()
        elif (int(self.ids.quantidade_TresQueijos.text)) == 10:
            Popup_LimiteMaximoPorPizza.popFun()

    def decrementar_TresQueijos(self):
        if (int(self.ids.quantidade_TresQueijos.text)) > 0:
            self.ids.quantidade_TresQueijos.text = str(int(self.ids.quantidade_TresQueijos.text) - 1) 
            self.pizza_TresQueijos()
            self.atualizaValores()

    # PIZZAS ESPECIAIS
    def pizza_Brocolis(self):
        valorUnitarioDaPizza_Brocolis = (float(self.ids.valor_Brocolis.text))
        quantidadeDePizza_Brocolis = (float(self.ids.quantidade_Brocolis.text))
        valorTotalDaPizza_Brocolis = quantidadeDePizza_Brocolis * valorUnitarioDaPizza_Brocolis
        return valorTotalDaPizza_Brocolis 

    def incrementar_Brocolis(self): 
        if (int(self.ids.quantidade_Brocolis.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Brocolis.text = str(int(self.ids.quantidade_Brocolis.text) + 1) 
            self.pizza_Brocolis()
            self.atualizaValores()
        elif (int(self.ids.quantidade_Brocolis.text)) == 10:
            Popup_LimiteMaximoPorPizza.popFun()

    def decrementar_Brocolis(self):
        if (int(self.ids.quantidade_Brocolis.text)) > 0:
            self.ids.quantidade_Brocolis.text = str(int(self.ids.quantidade_Brocolis.text) - 1) 
            self.pizza_Brocolis()
            self.atualizaValores()

    def pizza_Champignon(self):
        valorUnitarioDaPizza_Champignon = (float(self.ids.valor_Champignon.text))
        quantidadeDePizza_Champignon = (float(self.ids.quantidade_Champignon.text))
        valorTotalDaPizza_Champignon = quantidadeDePizza_Champignon * valorUnitarioDaPizza_Champignon
        return valorTotalDaPizza_Champignon 

    def incrementar_Champignon(self): 
        if (int(self.ids.quantidade_Champignon.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Champignon.text = str(int(self.ids.quantidade_Champignon.text) + 1) 
            self.pizza_Champignon()   
            self.atualizaValores()
        elif (int(self.ids.quantidade_Champignon.text)) == 10:
            Popup_LimiteMaximoPorPizza.popFun()

    def decrementar_Champignon(self):
        if (int(self.ids.quantidade_Champignon.text)) > 0:
            self.ids.quantidade_Champignon.text = str(int(self.ids.quantidade_Champignon.text) - 1) 
            self.pizza_Champignon()
            self.atualizaValores()

    def pizza_CincoQueijos(self):
        valorUnitarioDaPizza_CincoQueijos = (float(self.ids.valor_CincoQueijos.text))
        quantidadeDePizza_CincoQueijos = (float(self.ids.quantidade_CincoQueijos.text))
        valorTotalDaPizza_CincoQueijos = quantidadeDePizza_CincoQueijos * valorUnitarioDaPizza_CincoQueijos
        return valorTotalDaPizza_CincoQueijos 

    def incrementar_CincoQueijos(self): 
        if (int(self.ids.quantidade_CincoQueijos.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_CincoQueijos.text = str(int(self.ids.quantidade_CincoQueijos.text) + 1) 
            self.pizza_CincoQueijos()
            self.atualizaValores()
        elif (int(self.ids.quantidade_CincoQueijos.text)) == 10:
            Popup_LimiteMaximoPorPizza.popFun()

    def decrementar_CincoQueijos(self):
        if (int(self.ids.quantidade_CincoQueijos.text)) > 0:
            self.ids.quantidade_CincoQueijos.text = str(int(self.ids.quantidade_CincoQueijos.text) - 1) 
            self.pizza_CincoQueijos()
            self.atualizaValores()

    def pizza_Salaminho(self):
        valorUnitarioDaPizza_Salaminho = (float(self.ids.valor_Salaminho.text))
        quantidadeDePizza_Salaminho = (float(self.ids.quantidade_Salaminho.text))
        valorTotalDaPizza_Salaminho = quantidadeDePizza_Salaminho * valorUnitarioDaPizza_Salaminho
        return valorTotalDaPizza_Salaminho

    def incrementar_Salaminho(self): 
        if (int(self.ids.quantidade_Salaminho.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Salaminho.text = str(int(self.ids.quantidade_Salaminho.text) + 1) 
            self.pizza_Salaminho()
            self.atualizaValores()
        elif (int(self.ids.quantidade_Salaminho.text)) == 10:
            Popup_LimiteMaximoPorPizza.popFun()

    def decrementar_Salaminho(self):
        if (int(self.ids.quantidade_Salaminho.text)) > 0:
            self.ids.quantidade_Salaminho.text = str(int(self.ids.quantidade_Salaminho.text) - 1) 
            self.pizza_Salaminho()
            self.atualizaValores()

    def pizza_Vegetariana(self):
        valorUnitarioDaPizza_Vegetariana = (float(self.ids.valor_Vegetariana.text))
        quantidadeDePizza_Vegetariana = (float(self.ids.quantidade_Vegetariana.text))
        valorTotalDaPizza_Vegetariana = quantidadeDePizza_Vegetariana * valorUnitarioDaPizza_Vegetariana
        return valorTotalDaPizza_Vegetariana

    def incrementar_Vegetariana(self): 
        if (int(self.ids.quantidade_Vegetariana.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Vegetariana.text = str(int(self.ids.quantidade_Vegetariana.text) + 1) 
            self.pizza_Vegetariana()
            self.atualizaValores()
        elif (int(self.ids.quantidade_Vegetariana.text)) == 10:
            Popup_LimiteMaximoPorPizza.popFun()

    def decrementar_Vegetariana(self):
        if (int(self.ids.quantidade_Vegetariana.text)) > 0:
            self.ids.quantidade_Vegetariana.text = str(int(self.ids.quantidade_Vegetariana.text) - 1) 
            self.pizza_Vegetariana()
            self.atualizaValores()

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
            self.atualizaValores()
        elif (int(self.ids.quantidade_Acai.text)) == 10:
            Popup_LimiteMaximoPorPizza.popFun()

    def decrementar_Acai(self):
        if (int(self.ids.quantidade_Acai.text)) > 0:
            self.ids.quantidade_Acai.text = str(int(self.ids.quantidade_Acai.text) - 1) 
            self.pizza_Acai()
            self.atualizaValores()

    def pizza_Banana(self):
        valorUnitarioDaPizza_Banana = (float(self.ids.valor_Banana.text))
        quantidadeDePizza_Banana = (float(self.ids.quantidade_Banana.text))
        valorTotalDaPizza_Banana = quantidadeDePizza_Banana * valorUnitarioDaPizza_Banana
        return valorTotalDaPizza_Banana 

    def incrementar_Banana(self): 
        if (int(self.ids.quantidade_Banana.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Banana.text = str(int(self.ids.quantidade_Banana.text) + 1) 
            self.pizza_Banana()
            self.atualizaValores()
        elif (int(self.ids.quantidade_Banana.text)) == 10:
            Popup_LimiteMaximoPorPizza.popFun()

    def decrementar_Banana(self):
        if (int(self.ids.quantidade_Banana.text)) > 0:
            self.ids.quantidade_Banana.text = str(int(self.ids.quantidade_Banana.text) - 1) 
            self.pizza_Banana()
            self.atualizaValores()

    def pizza_Brigadeiro(self):
        valorUnitarioDaPizza_Brigadeiro = (float(self.ids.valor_Brigadeiro.text))
        quantidadeDePizza_Brigadeiro = (float(self.ids.quantidade_Brigadeiro.text))
        valorTotalDaPizza_Brigadeiro = quantidadeDePizza_Brigadeiro * valorUnitarioDaPizza_Brigadeiro
        return valorTotalDaPizza_Brigadeiro 

    def incrementar_Brigadeiro(self): 
        if (int(self.ids.quantidade_Brigadeiro.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Brigadeiro.text = str(int(self.ids.quantidade_Brigadeiro.text) + 1) 
            self.pizza_Brigadeiro()    
            self.atualizaValores()
        elif (int(self.ids.quantidade_Brigadeiro.text)) == 10:
            Popup_LimiteMaximoPorPizza.popFun()

    def decrementar_Brigadeiro(self):
        if (int(self.ids.quantidade_Brigadeiro.text)) > 0:
            self.ids.quantidade_Brigadeiro.text = str(int(self.ids.quantidade_Brigadeiro.text) - 1) 
            self.pizza_Brigadeiro()
            self.atualizaValores()

    def pizza_Prestigio(self):
        valorUnitarioDaPizza_Prestigio = (float(self.ids.valor_Prestigio.text))
        quantidadeDePizza_Prestigio = (float(self.ids.quantidade_Prestigio.text))
        valorTotalDaPizza_Prestigio = quantidadeDePizza_Prestigio * valorUnitarioDaPizza_Prestigio
        return valorTotalDaPizza_Prestigio 

    def incrementar_Prestigio(self): 
        if (int(self.ids.quantidade_Prestigio.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_Prestigio.text = str(int(self.ids.quantidade_Prestigio.text) + 1) 
            self.pizza_Prestigio()
            self.atualizaValores()
        elif (int(self.ids.quantidade_Prestigio.text)) == 10:
            Popup_LimiteMaximoPorPizza.popFun()

    def decrementar_Prestigio(self):
        if (int(self.ids.quantidade_Prestigio.text)) > 0:
            self.ids.quantidade_Prestigio.text = str(int(self.ids.quantidade_Prestigio.text) - 1) 
            self.pizza_Prestigio()
            self.atualizaValores()

    def pizza_RomeuAndJulieta(self):
        valorUnitarioDaPizza_RomeuAndJulieta = (float(self.ids.valor_RomeuAndJulieta.text))
        quantidadeDePizza_RomeuAndJulieta = (float(self.ids.quantidade_RomeuAndJulieta.text))
        valorTotalDaPizza_RomeuAndJulieta = quantidadeDePizza_RomeuAndJulieta * valorUnitarioDaPizza_RomeuAndJulieta
        return valorTotalDaPizza_RomeuAndJulieta

    def incrementar_RomeuAndJulieta(self): 
        if (int(self.ids.quantidade_RomeuAndJulieta.text)) < quantidadeMaximaDePizzaDeUmSabor:
            self.ids.quantidade_RomeuAndJulieta.text = str(int(self.ids.quantidade_RomeuAndJulieta.text) + 1) 
            self.pizza_RomeuAndJulieta()
            self.atualizaValores()
        elif (int(self.ids.quantidade_RomeuAndJulieta.text)) == 10:
            Popup_LimiteMaximoPorPizza.popFun()

    def decrementar_RomeuAndJulieta(self):
        if (int(self.ids.quantidade_RomeuAndJulieta.text)) > 0:
            self.ids.quantidade_RomeuAndJulieta.text = str(int(self.ids.quantidade_RomeuAndJulieta.text) - 1) 
            self.pizza_RomeuAndJulieta()
            self.atualizaValores()

    def atualizaValores(self):
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
                
            self.valorTotalDoPedido(pizza_Ads, 
                                    pizza_Baiana, 
                                    pizza_Bolonhesa, 
                                    pizza_Calabresa, 
                                    pizza_FrangoComCatupiry, 
                                    pizza_Ituiutaba, 
                                    pizza_Mucarela, 
                                    pizza_QuatroQueijos, 
                                    pizza_TresQueijos, 
                                    pizza_Brocolis, 
                                    pizza_Champignon, 
                                    pizza_CincoQueijos, 
                                    pizza_Salaminho, 
                                    pizza_Vegetariana, 
                                    pizza_Acai, 
                                    pizza_Banana, 
                                    pizza_Brigadeiro, 
                                    pizza_Prestigio, 
                                    pizza_RomeuAndJulieta
                                   )

    def valorTotalDoPedido(self, pizza_Ads, pizza_Baiana, pizza_Bolonhesa, pizza_Calabresa, pizza_FrangoComCatupiry, pizza_Ituiutaba, pizza_Mucarela, pizza_QuatroQueijos, pizza_TresQueijos, pizza_Brocolis, pizza_Champignon, pizza_CincoQueijos, pizza_Salaminho, pizza_Vegetariana, pizza_Acai, pizza_Banana, pizza_Brigadeiro, pizza_Prestigio, pizza_RomeuAndJulieta): # Será chamada sempre que for apertado + ou - em qualquer pizza
        valorTotalDoPedido = pizza_Ads + pizza_Baiana + pizza_Bolonhesa + pizza_Calabresa + pizza_FrangoComCatupiry + pizza_Ituiutaba + pizza_Mucarela + pizza_QuatroQueijos + pizza_TresQueijos + pizza_Brocolis + pizza_Champignon + pizza_CincoQueijos + pizza_Salaminho + pizza_Vegetariana + pizza_Acai + pizza_Banana + pizza_Brigadeiro + pizza_Prestigio + pizza_RomeuAndJulieta # Faz a soma de todas as pizzas
        valorTotalDoPedidoFormatado = "{:.2f}".format(valorTotalDoPedido) # Deixa o valor total do pedido com apenas duas casas decimais
        self.ids.valorTotalDoPedido.text = str(valorTotalDoPedidoFormatado) # Mostra o valor total do pedido na tela

        arquivo = open('./valorTotalDoPedido.txt', 'w')
        arquivo.write(valorTotalDoPedidoFormatado)
        arquivo.close()

        def salvandoEmTxt(self):
            n = "\n"
            arquivo = open('./quantidadeDePizzas.txt', 'w')
            arquivo.writelines([
                self.ids.quantidade_Ads.text, 
                n, 
                self.ids.quantidade_Baiana.text, 
                n, 
                self.ids.quantidade_Bolonhesa.text, 
                n, 
                self.ids.quantidade_Calabresa.text, 
                n, 
                self.ids.quantidade_FrangoComCatupiry.text, 
                n, 
                self.ids.quantidade_Ituiutaba.text, 
                n, 
                self.ids.quantidade_Ituiutaba.text, 
                n, 
                self.ids.quantidade_Mucarela.text, 
                n, 
                self.ids.quantidade_QuatroQueijos.text, 
                n, 
                self.ids.quantidade_TresQueijos.text, 
                n, 
                self.ids.quantidade_Brocolis.text, 
                n, 
                self.ids.quantidade_Champignon.text, 
                n, 
                self.ids.quantidade_CincoQueijos.text, 
                n, 
                self.ids.quantidade_Salaminho.text, 
                n, 
                self.ids.quantidade_Vegetariana.text, 
                n, 
                self.ids.quantidade_Acai.text, 
                n, 
                self.ids.quantidade_Banana.text, 
                n, 
                self.ids.quantidade_Brigadeiro.text, 
                n, 
                self.ids.quantidade_Prestigio.text, 
                n, 
                self.ids.quantidade_RomeuAndJulieta.text
            ])
            arquivo.close()

    def verificarHorario(self):
        horario_Pedido = datetime.today().strftime('%H:%M:%S')

        if horario_Pedido >= horarioQuePizzariaComecaReceberPedidos and horario_Pedido <= horarioQuePizzariaParaDeReceberPedidos:
            gerenciadorDeJanelas.current = 'finalizar_pedido'
        else:
            Popup_ForaHorarioDePedido.popFun() # pop-up avisando que ainda não estão recebendo pedidos
        
class Finalizar_Pedido(Screen):
    enderecoParaEntregaDoPedido = ObjectProperty(None)
    numeroParaEntregaDoPedido = ObjectProperty(None)
    bairroParaEntregaDoPedido = ObjectProperty(None)
    telefoneParaContato = ObjectProperty(None)
    forma_de_pagamento = ObjectProperty(None)
    
    def on_spinner_select(self, text):
        return text
    
    def validar(self):
        quantidadeDeCaracteres = len(str(self.enderecoParaEntregaDoPedido.text))

        data_Pedido = datetime.today().strftime('%Y-%m-%d')
        horario_Pedido = datetime.today().strftime('%H:%M:%S')

        if horario_Pedido >= horarioQuePizzariaComecaReceberPedidos and horario_Pedido <= horarioQuePizzariaParaDeReceberPedidos:
            if self.enderecoParaEntregaDoPedido.text != "" and self.numeroParaEntregaDoPedido.text != "" and self.bairroParaEntregaDoPedido.text != "" and self.telefoneParaContato.text != "":
                verificaTelefone = Verificar_telefone.check(self.telefoneParaContato.text)
                if verificaTelefone == 0:
                    if self.forma_de_pagamento.text != "Selecione a forma de pagamento" and (self.forma_de_pagamento.text == "Cartão de Credito" or self.forma_de_pagamento.text == "Cartão de Debito" or self.forma_de_pagamento.text == "Pix"):
                        if quantidadeDeCaracteres >= 3:
                            link = f"https://viacep.com.br/ws/MG/Ituiutaba/{self.enderecoParaEntregaDoPedido.text}/json/"
                            endereco = requests.get(link)
                            resultado_endereco = endereco.json()
                            resultado_endereco = str(resultado_endereco)
                            if resultado_endereco != '[]':
                                data_Pedido = datetime.today().strftime('%Y-%m-%d')
                                horario_Pedido = datetime.today().strftime('%H:%M:%S')

                                arquivo = open('./telefone.txt', 'w')
                                arquivo.write(self.ids.telefoneParaContato.text)
                                arquivo.close()

                                arquivo = open('./telefone.txt', 'r')
                                leia_me = (arquivo.readline())
                                telefone_Pedido = leia_me
                                arquivo.close()

                                endereco_Pedido = self.ids.enderecoParaEntregaDoPedido.text
                                formaDePagamento_Pedido = self.ids.forma_de_pagamento.text

                                arquivo = open('./valorTotalDoPedido.txt', 'r')
                                leia_me = (arquivo.readline())
                                valorTotal_Pedido = leia_me
                                arquivo.close()

                                arquivo = open('./email.txt', 'r')
                                leia_me = (arquivo.readlines())
                                email = leia_me[0]
                                arquivo.close()
                                Contas_id_Pedido = bancoDeDados.search_account_id(email)

                                file = open("./quantidadeDePizzas.txt", "r") 
                                leia = file.readlines()
                                pizza_Ads_Pedido = leia[0]
                                pizza_Baiana_Pedido = leia[1]
                                pizza_Bolonhesa_Pedido = leia[2]
                                pizza_Calabresa_Pedido = leia[3]
                                pizza_FrangoComCatupiry_Pedido = leia[4]
                                pizza_Ituiutaba_Pedido = leia[5]
                                pizza_Mucarela_Pedido = leia[6]
                                pizza_QuatroQueijos_Pedido = leia[7]
                                pizza_TresQueijos_Pedido = leia[8]
                                pizza_Brocolis_Pedido = leia[9]
                                pizza_Champignon_Pedido = leia[10]
                                pizza_CincoQueijos_Pedido = leia[11]
                                pizza_Salaminho_Pedido = leia[12]
                                pizza_Vegetariana_Pedido = leia[13]
                                pizza_Acai_Pedido = leia[14]
                                pizza_Banana_Pedido = leia[15]
                                pizza_Brigadeiro_Pedido = leia[16]
                                pizza_Prestigio_Pedido = leia[17]
                                pizza_RomeuAndJulieta_Pedido = leia[18]
                                file.close()

                                bancoDeDados.insert_table_Pedidos(
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
                                Popup_PedidoRealizadoComSucesso.popFun()
                                limparCamposFinalizarPedido()
                            else:
                                Popup_EnderecoNaoEncontrado.popFun()
                        else:
                            Popup_EnderecoNaoEncontrado.popFun()
                    else:
                        Popup_FormaDePagamentoNaoDefinida.popFun()
                else:
                    Popup_NumeroInvalido.popFun()
            else:
                Popup_CampoVazio.popFun()
        else:
            Popup_ForaHorarioDePedido.popFun() 

    def limparCamposFinalizarPedido(self):
        self.ids.enderecoParaEntregaDoPedido.text = ''
        self.ids.numeroParaEntregaDoPedido.text = ''
        self.ids.bairroParaEntregaDoPedido.text = ''
        self.ids.telefoneParaContato.text = ''
        self.ids.forma_de_pagamento.text = 'Selecione a forma de pagamento'

class Popup_CampoVazio(Screen):
    popupWindow = None
    
    def popFun():
        show = Popup_CampoVazio()
        Popup_CampoVazio.popupWindow = Popup(
                              title = "Popup", 
                              content = show, 
                              size_hint = (None, None), 
                              size = (400, 200), 
                              auto_dismiss=False, 
                              title_size = 16,
                              background_color=(22/255, 184/255, 243/255, 1)
                             )
        Popup_CampoVazio.popupWindow.open()

class Popup_EmailInvalido(Screen):
    popupWindow = None
    
    def popFun():
        show = Popup_EmailInvalido()
        Popup_EmailInvalido.popupWindow = Popup(
                              title = "Popup", 
                              content = show, 
                              size_hint = (None, None), 
                              size = (400, 200), 
                              auto_dismiss=False, 
                              title_size = 16,
                              background_color=(22/255, 184/255, 243/255, 1)
                             )
        Popup_EmailInvalido.popupWindow.open()

class Popup_EmailOuSenhaIncorreto(Screen):
    popupWindow = None
    
    def popFun():
        show = Popup_EmailOuSenhaIncorreto()
        Popup_EmailOuSenhaIncorreto.popupWindow = Popup(
                              title = "Popup", 
                              content = show, 
                              size_hint = (None, None), 
                              size = (400, 200), 
                              auto_dismiss=False, 
                              title_size = 16,
                              background_color=(22/255, 184/255, 243/255, 1)
                             )
        Popup_EmailOuSenhaIncorreto.popupWindow.open()

class Popup_ContaDesativada(Screen):
    popupWindow = None
    
    def popFun():
        show = Popup_ContaDesativada()
        Popup_ContaDesativada.popupWindow = Popup(
                              title = "Popup", 
                              content = show, 
                              size_hint = (None, None), 
                              size = (400, 200), 
                              auto_dismiss=False, 
                              title_size = 16,
                              background_color=(22/255, 184/255, 243/255, 1)
                             )
        Popup_ContaDesativada.popupWindow.open()

class Popup_CadastroRealizadoComSucesso(Screen):
    popupWindow = None
    
    def popFun():
        show = Popup_CadastroRealizadoComSucesso()
        Popup_CadastroRealizadoComSucesso.popupWindow = Popup(
                              title = "Popup", 
                              content = show, 
                              size_hint = (None, None), 
                              size = (400, 200), 
                              auto_dismiss=False, 
                              title_size = 16,
                              background_color=(22/255, 184/255, 243/255, 1)
                             )
        Popup_CadastroRealizadoComSucesso.popupWindow.open()

class Popup_LimiteDeCarateresNaSenha(Screen):
    popupWindow = None
    
    def popFun():
        show = Popup_LimiteDeCarateresNaSenha()
        Popup_LimiteDeCarateresNaSenha.popupWindow = Popup(
                              title = "Popup", 
                              content = show, 
                              size_hint = (None, None), 
                              size = (400, 200), 
                              auto_dismiss=False, 
                              title_size = 16,
                              background_color=(22/255, 184/255, 243/255, 1)
                             )
        Popup_LimiteDeCarateresNaSenha.popupWindow.open()

class Popup_SenhasDiferentes(Screen):
    popupWindow = None
    
    def popFun():
        show = Popup_SenhasDiferentes()
        Popup_SenhasDiferentes.popupWindow = Popup(
                              title = "Popup", 
                              content = show, 
                              size_hint = (None, None), 
                              size = (400, 200), 
                              auto_dismiss=False, 
                              title_size = 16,
                              background_color=(22/255, 184/255, 243/255, 1)
                             )
        Popup_SenhasDiferentes.popupWindow.open()

class Popup_EmailJaExiste(Screen):
    popupWindow = None
    
    def popFun():
        show = Popup_EmailJaExiste()
        Popup_EmailJaExiste.popupWindow = Popup(
                              title = "Popup", 
                              content = show, 
                              size_hint = (None, None), 
                              size = (400, 200), 
                              auto_dismiss=False, 
                              title_size = 16,
                              background_color=(22/255, 184/255, 243/255, 1)
                             )
        Popup_EmailJaExiste.popupWindow.open()

class Popup_ErroInesperado(Screen):
    popupWindow = None
    
    def popFun():
        show = Popup_ErroInesperado()
        Popup_ErroInesperado.popupWindow = Popup(
                              title = "Popup", 
                              content = show, 
                              size_hint = (None, None), 
                              size = (400, 200), 
                              auto_dismiss=False, 
                              title_size = 16,
                              background_color=(22/255, 184/255, 243/255, 1)
                             )
        Popup_ErroInesperado.popupWindow.open()

class Popup_LimiteMaximoPorPizza(Screen):
    popupWindow = None
    
    def popFun():
        show = Popup_LimiteMaximoPorPizza()
        Popup_LimiteMaximoPorPizza.popupWindow = Popup(
                              title = "Popup", 
                              content = show, 
                              size_hint = (None, None), 
                              size = (400, 200), 
                              auto_dismiss=False, 
                              title_size = 16,
                              background_color=(22/255, 184/255, 243/255, 1)
                             )
        Popup_LimiteMaximoPorPizza.popupWindow.open()

class Popup_ForaHorarioDePedido(Screen):
    popupWindow = None
    
    def popFun():
        show = Popup_ForaHorarioDePedido()
        Popup_ForaHorarioDePedido.popupWindow = Popup(
                              title = "Popup", 
                              content = show, 
                              size_hint = (None, None), 
                              size = (400, 200), 
                              auto_dismiss=False, 
                              title_size = 16,
                              background_color=(22/255, 184/255, 243/255, 1)
                             )
        Popup_ForaHorarioDePedido.popupWindow.open()

class Popup_NumeroInvalido(Screen):
    popupWindow = None
    
    def popFun():
        show = Popup_NumeroInvalido()
        Popup_NumeroInvalido.popupWindow = Popup(
                              title = "Popup", 
                              content = show, 
                              size_hint = (None, None), 
                              size = (400, 200), 
                              auto_dismiss=False, 
                              title_size = 16,
                              background_color=(22/255, 184/255, 243/255, 1)
                             )
        Popup_NumeroInvalido.popupWindow.open()

class Popup_FormaDePagamentoNaoDefinida(Screen):
    popupWindow = None
    
    def popFun():
        show = Popup_FormaDePagamentoNaoDefinida()
        Popup_FormaDePagamentoNaoDefinida.popupWindow = Popup(
                              title = "Popup", 
                              content = show, 
                              size_hint = (None, None), 
                              size = (400, 200), 
                              auto_dismiss=False, 
                              title_size = 16,
                              background_color=(22/255, 184/255, 243/255, 1)
                             )
        Popup_FormaDePagamentoNaoDefinida.popupWindow.open()

class Popup_EnderecoNaoEncontrado(Screen):
    popupWindow = None
    
    def popFun():
        show = Popup_EnderecoNaoEncontrado()
        Popup_EnderecoNaoEncontrado.popupWindow = Popup(
                              title = "Popup", 
                              content = show, 
                              size_hint = (None, None), 
                              size = (400, 200), 
                              auto_dismiss=False, 
                              title_size = 16,
                              background_color=(22/255, 184/255, 243/255, 1)
                             )
        Popup_EnderecoNaoEncontrado.popupWindow.open()
    
class Popup_PedidoRealizadoComSucesso(Screen):
    popupWindow = None
    
    def popFun():
        show = Popup_PedidoRealizadoComSucesso()
        Popup_PedidoRealizadoComSucesso.popupWindow = Popup(
                              title = "Popup", 
                              content = show, 
                              size_hint = (None, None), 
                              size = (400, 200), 
                              auto_dismiss=False, 
                              title_size = 16,
                              background_color=(22/255, 184/255, 243/255, 1)
                             )
        Popup_PedidoRealizadoComSucesso.popupWindow.open()
    
# Arquivo de carregamento do construtor    
kv = Builder.load_file('app_kivy_pizzaria.kv')
kv = Builder.load_file('popup.kv')
gerenciadorDeJanelas = windowManager()

# Adicionando telas
gerenciadorDeJanelas.add_widget(Login(name='login'))
gerenciadorDeJanelas.add_widget(Cadastrar(name='cadastrar'))
gerenciadorDeJanelas.add_widget(Menu(name='menu'))
gerenciadorDeJanelas.add_widget(Pedido(name='pedido'))
gerenciadorDeJanelas.add_widget(Finalizar_Pedido(name='finalizar_pedido'))

class app_kivy_pizzaria(App):
    def build(self):
        return gerenciadorDeJanelas

if __name__ == "__main__": 
	app_kivy_pizzaria().run()