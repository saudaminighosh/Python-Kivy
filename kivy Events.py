import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


'''class MyLayout(BoxLayout):

    def __init__(self):
        super().__init__()
        self.button1 = Button(text='Press Meeee')
        self.button1.bind(on_press=self.func1)
        self.add_widget(self.button1)
    
    def func1(self,button1):
        #self.layout2=FloatLayout()
        self.lb3=Label(text='Welcome')
        self.add_widget(self.lb3)
        
class MyLabelApp(App):
    
    def build(self):
        return MyLayout()

if __name__=='__main__':
            
    label = MyLabelApp()
    # run the window
    label.run()'''
 
class MyLabelApp(App):
    
    layout=BoxLayout()
    def build(self):   
        #layout=BoxLayout()
        button = Button(text='Press Meeee', font_size=15)
        button.bind(on_press=self.func1)
        self.layout.add_widget(button)
        return self.layout
    
    def func1(self,button):
        lb3=Label(text='Welcome')
        self.layout.add_widget(lb3)
        self.layout.remove_widget(button)
        
label = MyLabelApp()
    # run the window
label.run()
