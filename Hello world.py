import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout



class MyLabelApp(App):
    #layout=FloatLayout()
    def build(self):
        self.layout=FloatLayout()
        self.l1=Label(text='[color=6A1E55][b]Welcome ![/b]',font_size=60,markup=True,pos_hint={'center_x':0.5,'center_y':0.7})
        self.layout.add_widget(self.l1)
        self.button = Button(text='[b]Press Me[/b]',markup=True, font_size=40,size_hint=(.2,.1),pos_hint={'center_x':0.5,'center_y':0.49},background_color =(1,0,1,1))
        self.button.bind(on_press=self.func1) 
        self.layout.add_widget(self.button)
        Window.clearcolor=(0,0,0,1)
        return self.layout
    
    def func1(self,button):
        #lb3=Label(text='[color=FFF7D1][b][i]Hello World[/i][/b]',font_size=50,markup=True,pos_hint={'center_x':0.5,'center_y':0.58})
        #self.layout.add_widget(lb3)
        self.l1.text="[color=FFF7D1][b][i]Hello World[/i][/b]"
        self.l1.pos_hint={'center_x':0.5,'center_y':0.58}
        self.layout.remove_widget(button)

label = MyLabelApp()
# run the window
label.run()