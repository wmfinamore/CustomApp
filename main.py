from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget


Window.size = (480, 720)


class MainInterface(Widget):

    def S_pressing(self, s_img):
        s_img.source = "Pressed_Start_Btn.png"

    def S_releasing(self, s_img):
        s_img.source = "Start_Btn.png"

    def ST_pressing(self, st_img):
        st_img.source = "Pressed_Stats_Btn.png"

    def ST_releasing(self, st_img):
        st_img.source = "Stats_Btn.png"

    def L_pressing(self, l_img):
        l_img.source = "Pressed_Likes_Btn.png"

    def L_releasing(self, l_img):
        l_img.source = "Likes_Btn.png"


class CustomApp(App):
    pass


CustomApp().run()
