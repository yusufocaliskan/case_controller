from kivy.app import App
from kivy.uix.label import Label


class Panel(App):

    def build(self):
        
        return Label(text='Silavvvv Rêz!')

if __name__ == '__main__':
    Panel().run()