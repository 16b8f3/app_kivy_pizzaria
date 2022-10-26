from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen



class Gerente_das_telas(ScreenManager):
    pass


class Login(Screen):
    pass


class Cadastrar(Screen):
    pass


class Menu(Screen):
    pass


class Pedido(Screen):
    def pizzaTeste(self): # nome da pizza_TAMANHO
        valor = 47.99 # valor da pizza
        quantidade = (float(self.ids.teste.text)) # quantidade da pizza
        a = valor * quantidade # valor total
        total = "{:.2f}".format(a) # valor total limitado a duas casas decimais
        self.ids.testeValor.text = str(total) # mudando o valor do total para o novo valor transformado em str
        # a copia tem uma baita melhoria
        # passar toda essa função para um arquivo a parte e importar aqui e usar so as funções
        
    def mais(self):
        print('aumenta o numero da pizza em 1')
        self.ids.teste.text = str(int(self.ids.teste.text) + 1)
        self.pizzaTeste()

    def menos(self):
        if (int(self.ids.teste.text)) > 0:
            print('diminui o numero da pizza em 1')
            self.ids.teste.text = str(int(self.ids.teste.text) - 1)
            self.pizzaTeste()


class Finalizar_Pedido(Screen):
    pass


class app_kivy_pizzaria(App):
    def build(self):
        return Gerente_das_telas()



if __name__ == '__main__':
    app_kivy_pizzaria().run()
