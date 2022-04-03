from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class Basic_UX(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.Btn = Button(text="Hello", size=(200, 100),
                          pos=(300, 100), background_color=(.2, .3, .4, 1))
        self.Btn.bind(on_press=self.remover)

    def remover(self, event):
        self.ids.checker.active = False
        self.remove_widget(self)

    def checking(self, Info):
        if Info.active:
            print("You have checked")
            self.add_widget(self.Btn)
        if not Info.active:
            print("You have unchecked")
            self.remove_widget(self.Btn)


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
