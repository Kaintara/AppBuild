from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivy.core.text import LabelBase
from kivy.metrics import sp
from kivy.animation import Animation
from game import game
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton, MDButton, MDButtonText
from kivymd.uix.textfield import MDTextField
from kivymd.uix.textfield import MDTextFieldHintText
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
import sys, os
from kivy.core.window import Window

#Screens
class SM(MDScreenManager):
    pass

class MainMenu(MDScreen):
    pass

class InGame(MDScreen):
    pass

class Rules(MDScreen):
    pass

class GamePlay(MDScreen):
    pass

class Players(MDBoxLayout):
    pass

class CircleLabel(MDCard):
    def __init__(self, text="", **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (150, 150)
        self.radius = [75,]

        self.label = MDLabel(
            text=text,
            halign="center",
            valign="center",
            size_hint=(None, None),
            size=self.size,
            pos=self.pos, 
            font_style = "cataway",
        )

        self.add_widget(self.label)

class TurnBtn(MDButton):
    def __init__(self,text="", **kwargs):
        super().__init__(**kwargs)
        self.style ="tonal"
        self.size_hint = (None, None)
        self.size = (200, 50)
        self.pos_hint= {"center_x":0.5,"top":0.3}
        self.elevation= 0
        self.radius= [25, 25, 25, 25]
        self.label = MDButtonText(
            text=text,
            font_style = "cataway",
            role="small",
        )
        self.add_widget(self.label)

class Overlay(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(0, 0, 0, 0.2) 
            self.rect = Rectangle(pos=self.pos, size=self.size)

#App Bulid
class QuestionsApp(MDApp):
    def resource_path(self,relative_path):
            try:
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")
            return os.path.join(base_path, relative_path)
    
    def build(self):

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.primary_hue = "1000"

        Window.set_icon(self.resource_path("icon.png"))

        LabelBase.register(
            name="cataway",
            fn_regular=self.resource_path("Catways.ttf"),
        )

        self.theme_cls.font_styles["cataway"] = {
            "large" : {
                "line-height": 1.64,
                "font-name": "cataway",
                "font-size": sp(50),
            },
            "medium": {
                "line-height": 1.52,
                "font-name": "cataway",
                "font-size": sp(45),
            },
            "small": {
                "line-height": 1.44,
                "font-name": "cataway",
                "font-size": sp(36),
            },
        }

        sm = SM()
        sm.add_widget(MainMenu(name="Menu"))
        sm.add_widget(InGame(name="InGame"))
        sm.add_widget(Rules(name="Rules"))
        sm.add_widget(GamePlay(name="GamePlay"))
        sm.current = "Menu"
        return sm
    
    def shake_animation(self, widget):
        anim = Animation(pos_hint={"center_x": 0.48}, duration=0.05) + Animation(pos_hint={"center_x": 0.52}, duration=0.05) + Animation(pos_hint={"center_x": 0.48}, duration=0.05) + Animation(pos_hint={"center_x": 0.52}, duration=0.05)
        anim += Animation(pos_hint={"center_x": 0.5}, duration=0.05)
        anim.start(widget)

    def get_widget(self, widget, screen):
        return self.root.get_screen(screen).ids[widget]

    def hide(self,widget):
        widget.size_hint = 0,0
        widget.opacity = 0
        widget.disabled = True
    
    def show(self,widget):
        widget.opacity = 1
        widget.disabled = False

    def reveal_liar(self):
        games = self.get_widget('GamePY', 'GamePlay')
        games.clear_widgets()
        img = FitImage(source=self.resource_path('S.png'))
        games.add_widget(img)
        reveal = MDLabel(
        text=f"The Liar was....",
        font_style="cataway",
        theme_font_size = "Custom",
        font_size = f"{sp(25)}",
        halign="center",
        valign="middle",
        pos_hint={"center_x": 0.5, "center_y": 0.9})
        question_label = MDLabel(
        text=f"Liar's Question: {game.current_liarQ}",
        font_style="cataway",
        theme_font_size = "Custom",
        font_size = f"{sp(25)}",
        halign="center",
        valign="middle",
        pos_hint={"center_x": 0.5, "center_y": 0.4})

        x = game.playerAns[game.liar]

        card = MDCard(
            size_hint=(0.8, None),
            height=50,
            radius=[12.5],
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            theme_bg_color="Custom",
            md_bg_color=x["colour"],
            elevation=4
        )

        name_label = MDLabel(
            text=x["name"],
            font_style="cataway",
            theme_font_size = "Custom",
            font_size = f"{sp(20)}",
            halign="left",
            valign="center",
            size_hint_x=0.4
        )

        answer_label = MDLabel(
            text=x["ans"],
            halign="right",
            valign="center",
            font_style="cataway",
            theme_font_size = "Custom",
            font_size = f"{sp(20)}",
            role = "small"
        )

        again_btn = TurnBtn(text="Play Again?")
        again_btn.pos_hint = {"center_x": 0.5, "center_y": 0.2}
        again_btn.bind(on_release=lambda x: self.game_start())

        quit_btn = TurnBtn(text="Quit")
        quit_btn.pos_hint = {"center_x": 0.5, "center_y": 0.05}
        quit_btn.bind(on_release=lambda x: self.stop())

        card.add_widget(name_label)
        card.add_widget(answer_label)
        games.add_widget(card)
        games.add_widget(question_label)
        games.add_widget(reveal)
        games.add_widget(again_btn)
        games.add_widget(quit_btn)

        



    def voting(self):
        games = self.get_widget('GamePY', 'GamePlay')
        games.clear_widgets()
        img = FitImage(source=self.resource_path('S.png'))
        games.add_widget(img)
        question_label = MDLabel(
        text=f"Question: {game.current_question}",
        font_style="cataway",
        theme_font_size = "Custom",
        font_size = f"{sp(25)}",
        halign="center",
        valign="middle",
        pos_hint={"center_x": 0.5, "center_y": 0.2}
    )
        
        y = 0.9
        for x in game.playerAns:
            card = MDCard(
            size_hint=(0.8, None),
            height=50,
            radius=[12.5],
            pos_hint={"center_x": 0.5, "center_y": y},
            theme_bg_color="Custom",
            md_bg_color=x["colour"],
            elevation=4
        )

            name_label = MDLabel(
                text=x["name"],
                font_style="cataway",
                theme_font_size = "Custom",
                font_size = f"{sp(20)}",
                halign="left",
                valign="center",
                size_hint_x=0.4
            )

            answer_label = MDLabel(
                text=x["ans"],
                halign="right",
                valign="center",
                font_style="cataway",
                theme_font_size = "Custom",
                font_size = f"{sp(20)}",
                role = "small"
            )

            card.add_widget(name_label)
            card.add_widget(answer_label)
            games.add_widget(card)
            y -= 0.1

        games.add_widget(question_label)
        reveal_btn = TurnBtn(text="Reveal Liar")
        reveal_btn.pos_hint = {"center_x": 0.5, "center_y": 0.05}
        reveal_btn.bind(on_release=lambda x: self.reveal_liar())
        games.add_widget(reveal_btn)

               



    def next_turn(self,instance):
        if game.current_turn >= len(game.turn):
            self.voting()
        x = game.turn[game.current_turn]
        color = game.colours[game.current_turn]
        anss = instance.text.strip()
        l = game.liar
        game.playerAns.append({
            "name":x,
            "ans": anss,
            "colour": color
        }
        )
        game.current_turn += 1
        if game.current_turn >= len(game.turn):
            self.voting()
        else:
            self.turn_widgets()

    def pressed(self,btn,wid):
        x = game.turn[game.current_turn]
        games = self.get_widget('GamePY','GamePlay')
        self.hide(wid)
        self.hide(btn)
        nam = MDTextField(
            text = f"Enter Your Answer!",
            pos_hint= {"center_y":0.45,"center_x":0.5},
            mode = "filled",)
        nam.width = 0.5*(games.width)
        namehint = MDTextFieldHintText(text=f"{game.playersQ[x]}")
        nam.add_widget(namehint)
        nam.bind(on_text_validate=self.next_turn)
        games.add_widget(nam)


    def turn_widgets(self):
        games = self.get_widget('GamePY','GamePlay')
        games.clear_widgets()
        x = game.turn[game.current_turn]
        i = game.current_turn
        img = FitImage(source=self.resource_path('S.png'))
        wid = Overlay(size_hint=(10,10),pos=(0,0))
        cir = CircleLabel(text=f"{x[0]}",pos_hint={"center_x":0.5,"center_y":0.75})
        cir.theme_bg_color = "Custom"
        cir.md_bg_color = game.colours[i]
        names = MDLabel(
        text=f"{x}",
        font_style="cataway",
        halign="center",
        valign="middle",
        size_hint=(None,None),
        pos_hint={"center_x": 0.5, "center_y": 0.55})
        names.text_size = (None, None)
        names.size = (250, 50)
        btn = TurnBtn(text=f"I am {x}!")
        btn.theme_bg_color = "Custom"
        btn.md_bg_color = game.colours[i]
        btn.bind(on_release=lambda *_: self.pressed(btn,wid))
        games.add_widget(img)
        games.add_widget(wid)
        games.add_widget(cir)
        games.add_widget(names)
        games.add_widget(btn)
        

    def game_start(self):
        games = self.get_widget('GamePY','GamePlay')
        games.clear_widgets()
        game.playerAns = []
        game.turn = []
        game.current_turn = 0
        game.liar = None
        game.current_question = None
        game.current_liarQ = None
        game.turn = []
        game.set_up()
        game.Qsort()
        self.root.current = "GamePlay"
        self.turn_widgets()

    def remove(self, widget):
        play = self.get_widget('Players','InGame')
        game.players.remove(widget.children[1].text)
        play.remove_widget(widget)
        self.player_input()

    def on_enter(self,instance):
        play = self.get_widget('Players','InGame')
        names = instance.text.strip()
        game.players.append(names)
        if not names:
            return
        print(game.players)
        entry_box = MDBoxLayout(size_hint_y=None, height="40dp")
        label = MDLabel(text=names, halign="center")
        removebtn = MDIconButton(icon="close",on_release=lambda x: self.remove(entry_box))
        entry_box.add_widget(label)
        entry_box.add_widget(removebtn)
        play.add_widget(entry_box, index=0)
        play.remove_widget(instance)

        if len(game.players) < game.num_of_players:
            self.player_input()
        else:
            self.game_start()
        

    def player_input(self):
        play = self.get_widget('Players','InGame')
        names = MDTextField(
            text = f"Player {len(game.players)+1}",
            pos_hint= {"center_y":0.5,"center_x":0.5},
            mode = "filled",)
        namehint = MDTextFieldHintText(text=f"Player {len(game.players)+1} name")
        names.add_widget(namehint)
        names.bind(on_text_validate=self.on_enter)
        play.add_widget(names, index=0)


    def start(self):
        num = self.root.get_screen('InGame').ids.Input
        err = self.get_widget('error','InGame')
        if num.text.isnumeric():
            game.num_of_players = int(num.text)
            if game.num_of_players < 3:
                num.error = True
                err.text = "Must be a number greater than 3!"
                self.shake_animation(num)
                return
            start = self.get_widget('StartBtn','InGame')
            self.hide(start)
            til = self.get_widget('GameTitle','InGame')
            til.text = "Enter each player's name!"
            num.pos_hint = {"top":0.3, "center_x":0.5}
            self.hide(num)
            play = self.get_widget('Players','InGame')
            play.clear_widgets()
            game.players = []
            self.player_input()
                

        else:
            num.error = True
            err.text = "Must be a number greater than 3!"
            self.shake_animation(num)


QuestionsApp().run()