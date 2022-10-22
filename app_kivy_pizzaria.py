from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen



class Gerente_das_telas(ScreenManager):
    pass


class Login(Screen):
    pass


class Cadastrar(Screen):
    pass



class app_kivy_pizzaria(App):
    def build(self):
        return Gerente_das_telas()



if __name__ == '__main__':
    app_kivy_pizzaria().run()
