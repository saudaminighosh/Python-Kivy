import kivy
# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App
# if you not import label and use it it through error
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MyLabelApp(App):
    def build(self):
        # label display the text on screen
        layout = BoxLayout(orientation='horizontal')
        lbl = Label(text ="Label is Added on screen !!:):)")
        lb2 = Label(text ="Label is Added on \n screen !! and its Multi\nLine", font_size ='20sp',color =(0.41, 0.42, 0.74, 1))
        layout.add_widget(lbl)
        layout.add_widget(lb2)
        return layout

label = MyLabelApp()
# run the window
label.run()