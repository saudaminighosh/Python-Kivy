from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout

class Calculator(App):
    def build(self):
        self.window= GridLayout()
        self.window.cols=4
        self.window.size_hint=(0.5,0.5)
        self.window.pos_hint={"center_x": 0.5, "center_y": 0.4}
        self.layout=FloatLayout()
        self.data=TextInput(multiline=False, padding_y=(30,30), size_hint=(2.5, 1.0),pos_hint={"center_x": 1.25, "center_y": 3.52}, font_size=30)
        self.data.text=""
        self.layout.add_widget(self.data)
        self.addition=Button(text='+', size_hint= (0.5, 0.5), bold=True, font_size=30)
        self.addition.bind(on_press=self.dispAdd)
        self.window.add_widget(self.addition)
        self.b1=Button(text='1', size_hint= (0.5, 0.5), bold=True, font_size=30)
        self.b1.bind(on_press=self.disp1)
        self.window.add_widget(self.b1)
        self.b2=Button(text='2', size_hint= (0.5, 0.5), bold=True, font_size=30)
        self.b2.bind(on_press=self.disp2)
        self.window.add_widget(self.b2)
        self.b3=Button(text='3', size_hint= (0.5, 0.5), bold=True, font_size=30)
        self.b3.bind(on_press=self.disp3)
        self.window.add_widget(self.b3)
        self.sub=Button(text='-', size_hint= (0.5, 0.5), bold=True, font_size=30)
        self.sub.bind(on_press=self.dispSub)
        self.window.add_widget(self.sub)
        self.b4=Button(text='4', size_hint= (0.5, 0.5), bold=True, font_size=30)
        self.b4.bind(on_press=self.disp4)
        self.window.add_widget(self.b4)
        self.b5=Button(text='5', size_hint= (0.5, 0.5), bold=True, font_size=30)
        self.b5.bind(on_press=self.disp5)
        self.window.add_widget(self.b5)
        self.b6=Button(text='6', size_hint= (0.5, 0.5), bold=True, font_size=30)
        self.b6.bind(on_press=self.disp6)
        self.window.add_widget(self.b6)
        self.mul=Button(text='*', size_hint= (0.5, 0.5), bold=True, font_size=30)
        self.mul.bind(on_press=self.dispMul)
        self.window.add_widget(self.mul)
        self.b7=Button(text='7', size_hint= (0.5, 0.5), bold=True, font_size=30)
        self.b7.bind(on_press=self.disp7)
        self.window.add_widget(self.b7)
        self.b8=Button(text='8', size_hint= (0.5, 0.5), bold=True, font_size=30)
        self.b8.bind(on_press=self.disp8)
        self.window.add_widget(self.b8)
        self.b9=Button(text='9', size_hint= (0.5, 0.5), bold=True, font_size=30)
        self.b9.bind(on_press=self.disp9)
        self.window.add_widget(self.b9)
        self.div=Button(text='/', size_hint= (0.5, 0.5), bold=True, font_size=30)
        self.div.bind(on_press=self.dispDiv)
        self.window.add_widget(self.div)
        self.equal=Button(text='=', size_hint= (0.5, 0.5), bold=True, font_size=30)
        self.equal.bind(on_press=self.equalto)
        self.window.add_widget(self.equal)
        self.delete=Button(text='DEL', size_hint= (0.5, 0.5), bold=True, font_size=30)
        self.delete.bind(on_press=self.remove)
        self.window.add_widget(self.delete)
        self.b0=Button(text='0', size_hint= (0.5, 0.5), bold=True, font_size=30)
        self.b0.bind(on_press=self.disp0)
        self.window.add_widget(self.b0)
        self.window.add_widget(self.layout)
        return self.window
    
    def disp1(self,x):
        self.data.text+=self.b1.text
             
    def disp2(self,x):
        self.data.text+=self.b2.text
        
    def disp3(self,x):
        self.data.text+=self.b3.text
        
    def disp4(self,x):
        self.data.text+=self.b4.text
        
    def disp5(self,x):
        self.data.text+=self.b5.text
        
    def disp6(self,x):
        self.data.text+=self.b6.text
        
    def disp7(self,x):
        self.data.text+=self.b7.text
        
    def disp8(self,x):
        self.data.text+=self.b8.text
        
    def disp9(self,x):
        self.data.text+=self.b9.text
        
    def disp0(self,x):
        self.data.text+=self.b0.text
    
    def dispAdd(self,x):
        if self.data.text!="" and self.data.text[-1]!="+":
            self.data.text+=self.addition.text
            
    def dispSub(self,x):
        if self.data.text!="" and self.data.text[-1]!="-":
            self.data.text+=self.sub.text
            
    def dispMul(self,x):
        if self.data.text!="" and self.data.text[-1]!="*":
            self.data.text+=self.mul.text
            
    def dispDiv(self,x):
        if self.data.text!="" and self.data.text[-1]!="/":
            self.data.text+=self.div.text
            
    def remove(self,x):
        if self.data.text!="":
            self.data.text=self.data.text[:-1]
            
    def equalto(self,x):
        print(self.data.text)
        self.data.text=str(eval(self.data.text))   
        
if __name__=="__main__":
    Calculator().run()