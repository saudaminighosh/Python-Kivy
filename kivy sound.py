from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout


class SoundPlayer(BoxLayout):
    
    def play_sound(self):
        sound=SoundLoader.load('click.mp3')
        if sound:
            sound.volume=0.5
            sound.play()

class soundApp(App):
    def build(self):
        return SoundPlayer()
    
soundApp().run()