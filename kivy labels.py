import kivy
# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App
# if you not import label and use it it through error
from kivy.uix.label import Label
 
# defining the App class
class MyLabelApp(App):
    def build(self):
        # label display the text on screen
        lbl = Label(text ="Label is Added on screen !!:):)")
        lb2 = Label(text ="Label is Added on \n screen !! and its Multi\nLine", font_size ='20sp',color =(0.41, 0.42, 0.74, 1))
        return lb2
    
 
# creating the object
label = MyLabelApp()
# run the window
label.run()