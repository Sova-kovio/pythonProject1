#!/usr/bin/kivy
from kivy.app import App
__version__ = "0.1"
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.recycleview import RecycleView


Window.size=(320,500)
Window.clearcolor=(255/255,186/255,3/255,1)
Window.title="Приложение"

class ScreenOne(Screen):
    pass

class Sem1k(Screen):
    pass

class Sem2k(Screen):
    pass

class Sem3k(Screen):
    pass

class Sem4k(Screen):
    pass

class Sem5k(Screen):
    pass

class Dis1k1s(Screen):
    pass

class Manager(ScreenManager):
    screen_one=ObjectProperty(None)
    sem1k = ObjectProperty(None)
    sem2k = ObjectProperty(None)
    sem3k = ObjectProperty(None)
    sem4k = ObjectProperty(None)
    sem5k = ObjectProperty(None)
    dis1k1s=ObjectProperty(None)

class MyApp(App):

    def build(self):
        return Manager()

MyApp().run()