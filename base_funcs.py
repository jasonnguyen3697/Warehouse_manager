from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Line
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window

class ShelfScroll(ScrollView):
    def __init__(self, reps, **kwargs):
        super().__init__(**kwargs)
        self.inner_grid = GridLayout(cols=1, size_hint_y=None)
        self.inner_grid.bind(minimum_height=self.inner_grid.setter('height'))
        for i in range(reps):
            btn = Button(text=str(i), size_hint_y=None, height=40, background_color=[0,0,1,1])
            self.inner_grid.add_widget(btn)
        self.add_widget(self.inner_grid)

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        label = Label(text='Tap to continue', font_size = 50)
        self.add_widget(label)

    def on_touch_up(self, touch):
        app = App.get_running_app()
        app.root.current = 'main'
        return True

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.outer_grid = GridLayout(cols=2, rows=1)
        self.scroll = ShelfScroll(reps=10, size_hint=(0.5, None), size=(Window.width, Window.height))
        self.outer_grid.add_widget(self.scroll)
        self.scroll2 = ShelfScroll(reps=3, size_hint=(1, None), size=(Window.width, Window.height))
        self.outer_grid.add_widget(self.scroll2)

        self.add_widget(self.outer_grid)


class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(StartScreen(name='start'))
        self.add_widget(MainScreen(name='main'))
        self.transition = FadeTransition()

presentation = Builder.load_file("simplekivy.kv")

class MainApp(App):
    def build(self):
        return presentation

if __name__ == "__main__":
    MainApp().run()