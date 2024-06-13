
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class signin_window(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        uname = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = uname.text
        passw = pwd.text

        if uname == '' or passw == '':
           info.text = '[color=#FF0000]Username or Password required[/color]'
        else:
            if uname == 'admin' and passw == 'admin':
              info.text =  '[color=#00FF00]Login Successful[/color]'
            else:
              info.text = '[color=#FF0000]Username or Password required[/color]'

        

class signinapp(App):
    def build(self):
        return signin_window()

if __name__ == '__main__':
    signinapp().run()
