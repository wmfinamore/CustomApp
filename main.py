from kivy.app import App
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class Basic_UX(Widget):
    SZ = NumericProperty()
    R = NumericProperty()
    G = NumericProperty()
    B = NumericProperty()

    def changing(self, info):
        self.SZ = info.value
        self.R = info.value
        print(info.value)

    def red(self, info):
        self.R = info.value

    def green(self, info):
        self.G = info.value

    def blue(self, info):
        self.B = info.value


class MainInterface(Widget):

    def S_pressing(self, s_img, SM):
        s_img.source = "Pressed_Start_Btn.png"
        if SM.current == "background_2" or SM.current == "background_3":
            SM.transition.direction = "right"
        SM.current = "background_1"

    def S_releasing(self, s_img):
        s_img.source = "Start_Btn.png"

    def ST_pressing(self, st_img, SM):
        st_img.source = "Pressed_Stats_Btn.png"
        if SM.current == "background_1":
            SM.transition.direction = "left"
        if SM.current == "background_3":
            SM.transition.direction = "right"
        SM.current = "background_2"

    def ST_releasing(self, st_img):
        st_img.source = "Stats_Btn.png"

    def L_pressing(self, l_img, SM):
        l_img.source = "Pressed_Likes_Btn.png"
        if SM.current == "background_1" or SM.current == "background_2":
            SM.transition.direction = "left"
        SM.current = "background_3"

    def L_releasing(self, l_img):
        l_img.source = "Likes_Btn.png"


class CustomApp(App):
    pass


CustomApp().run()
