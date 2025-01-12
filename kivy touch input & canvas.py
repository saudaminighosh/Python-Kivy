import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Line, Ellipse
from kivy.uix.widget import Widget
from kivy.core.window import Window



class MyWidget(Widget):
    def on_touch_down(self,touch):
        print('DOWN',touch)
        self.canvas.add(Rectangle(pos=(touch.x,touch.y), size=(50,98)))
        touch.ud['line']=Line(points=(touch.x, touch.y))
        self.canvas.add(touch.ud['line'])
        
    def on_touch_move(self, touch):
        touch.ud['line'].points+=[touch.x,touch.y]
 

class MyLabelApp(App):
    
    layout=BoxLayout()
    def build(self):   
        #layout=BoxLayout()
        button = Button(text='Press Meeee', font_size=15)
        button.bind(on_press=self.func1)
        self.layout.add_widget(button)
        l1=Label(text='HIIIIIiiiii')
        self.layout.add_widget(l1)
        x=MyWidget()
        self.layout.add_widget(x)
        #Window.clearcolor=(1,1,1,1)
        return self.layout
    
    def func1(self,button):
        lb3=Label(text='Welcome')
        self.layout.add_widget(lb3)
        self.layout.remove_widget(button)
           
label = MyLabelApp()
    # run the window
label.run()


'''class TouchInput(Widget):

    def on_touch_down(self, touch):
        if touch.is_double_tap:
            print("Double tapped")
        
class MyApp(App):
    def build(self):
        #self.thislabel=MyLabel('hi')
        return TouchInput()
    
if __name__=='__main__':
    MyApp().run()'''