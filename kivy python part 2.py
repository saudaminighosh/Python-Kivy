from kivy.app import App
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget

class MyLabel(Label):
    def __init__(self, text):
        super().__init__()
        self.text=text
        
class MyApp(App):
    def build(self):
        self.thislabel= MyLabel('Hi')
        return self.thislabel
    
if __name__=='__main__':
    MyApp().run()