import kivy
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyImage(Image,Widget):
    pass

class imageApp(App):
    def build(self):
        return MyImage()
    
myapp = imageApp()
# run the window
myapp.run()
    