import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition


class FirstPage(Button):
    def __init__(self):
        super().__init__()
        self.text='[color=6A1E55][b]Welcome ![/b]'
        self.markup=True
        self.font_size=60
        self.background_color =(0,0,0,1)
        self.bind(on_press=self.switch)
    
    def switch(self,item):
        myapp.screen_manager.transition=SlideTransition(direction="left")
        myapp.screen_manager.current='Second'
    
class SecondPage(Button):
    def __init__(self):
        super().__init__()
        self.text='[color=FFF7D1][b][i]Hello World[/i][/b]'
        self.markup=True
        self.font_size=60
        self.background_color =(2,1,1,1)
        self.bind(on_press=self.switch)
    
    def switch(self,item):
        myapp.screen_manager.transition=SlideTransition(direction="right")
        myapp.screen_manager.current='First'
    
class MyApp(App):
    def build(self):
        self.screen_manager=ScreenManager()
        self.fisrtpage=FirstPage()
        screen=Screen(name="First")
        screen.add_widget(self.fisrtpage)
        self.screen_manager.add_widget(screen)
        
        self.secondpage=SecondPage()
        screen=Screen(name="Second")
        screen.add_widget(self.secondpage)
        self.screen_manager.add_widget(screen)   
        
        return self.screen_manager
    
myapp = MyApp()
# run the window
myapp.run()