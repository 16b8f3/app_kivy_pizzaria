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
        
    def mais(self):
        print('aumenta o numero da pizza em 1')
        self.ids.teste.text = str(int(self.ids.teste.text) + 1)

    def menos(self):
        if (int(self.ids.teste.text)) > 0:
            print('diminui o numero da pizza em 1')
            self.ids.teste.text = str(int(self.ids.teste.text) - 1)
            


class Finalizar_Pedido(Screen):
    pass


class app_kivy_pizzaria(App):
    def build(self):
        return Gerente_das_telas()



if __name__ == '__main__':
    app_kivy_pizzaria().run()
