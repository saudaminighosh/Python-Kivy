#import Pylance
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class MyLayout(BoxLayout):
    def __init__(self):
        super().__init__()
        self.button=Button(text="Press Me")
        self.button.bind(on_press=self.new_label)
        self.add_widget(self.button)
    
    def new_label(self,button):
        self.label=Label(text="Hello, my new label")
        self.add_widget(self.label)
        self.remove_widget(button)

class MyApp(App):
    def build(self):
        #layout=BoxLayout(orientation='vertical')
        #label2=Label(text='Button')
        #label1=Label(text='Hello World')
        #button=Button(text='Press Me')
        #layout.add_widget(label1)
        #layout.add_widget(label2)
        #layout.add_widget(button)
        #return layout
        layout=FloatLayout()
        label1=Label(text='Hello', size_hint=(0.3,0.2), pos_hint={'center_x':0.2,'center_y':0.5})
        label2=Label(text='there', size_hint=(0.5,0.7), pos_hint={'center_x':0.5,'center_y':0.1})
        layout.add_widget(label1)
        layout.add_widget(label2)
        
        return layout
        #return MyLayout()
        
if __name__== '__main__':
    MyApp().run()


