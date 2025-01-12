import kivy
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

#Builder.load_file("hello.kv")

class helloWorld(Widget):
    layout=FloatLayout()
    myInput=ObjectProperty(None)
    #myInput=ObjectProperty(None)
    def printOut(self):
        lb3=Label(text='[color=FFF7D1][b][i]Hello World[/i][/b]',font_size=50,markup=True,pos_hint={'center_x':0.5,'center_y':0.58})
        self.layout.add_widget(lb3)
        self.remove_widget(self.myInput)
        #self.myInput.disabled= True
        
        

class helloApp(App):
    def build(self):
        return helloWorld()
    
myapp = helloApp()
# run the window
myapp.run()