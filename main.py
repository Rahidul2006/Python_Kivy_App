from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.scrollview import MDScrollView
from kivymd.color_definitions import colors
from kivy.metrics import dp


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "🎨 Rahidul's Kivy App"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
        self.counter = 0

    def build(self):
        # Main container
        main_layout = MDBoxLayout(orientation="vertical", padding="12dp", spacing="12dp")

        # Top toolbar
        toolbar = MDTopAppBar(
            title="Welcome to KivyMD",
            pos_hint={"top": 1},
            md_bg_color=self.theme_cls.primary_color
        )
        main_layout.add_widget(toolbar)

        # Scrollable content area
        scroll = MDScrollView()
        content = MDBoxLayout(
            orientation="vertical",
            spacing="16dp",
            padding="16dp",
            size_hint_y=None,
            height=dp(900)
        )

        # Welcome Card
        welcome_card = MDCard(
            orientation="vertical",
            padding="16dp",
            spacing="12dp",
            size_hint_y=None,
            height=dp(180)
        )
        welcome_card.add_widget(MDLabel(
            text="👋 Hello Rahidul Khan!",
            font_size="28sp",
            bold=True,
            halign="center"
        ))
        welcome_card.add_widget(MDLabel(
            text="Welcome to your Modern KivyMD Application",
            font_size="14sp",
            halign="center",
            size_hint_y=None,
            height=dp(30)
        ))
        welcome_card.add_widget(MDLabel(
            text="Build beautiful cross-platform apps with Python",
            font_size="12sp",
            halign="center",
            size_hint_y=None,
            height=dp(25)
        ))
        content.add_widget(welcome_card)

        # Stats Grid
        stats_card = MDCard(
            orientation="vertical",
            padding="16dp",
            spacing="10dp",
            size_hint_y=None,
            height=dp(150)
        )
        
        grid = MDGridLayout(
            cols=3,
            spacing="12dp",
            size_hint_y=None,
            height=dp(100)
        )
        
        stats = [
            ("🚀", "Fast", "High Performance"),
            ("🎨", "Beautiful", "Material Design"),
            ("📱", "Mobile", "Cross-Platform")
        ]
        
        for emoji, title, subtitle in stats:
            stat_box = MDBoxLayout(orientation="vertical", spacing="5dp")
            stat_box.add_widget(MDLabel(
                text=emoji,
                font_size="24sp",
                halign="center",
                size_hint_y=None,
                height=dp(30)
            ))
            stat_box.add_widget(MDLabel(
                text=title,
                font_size="12sp",
                bold=True,
                halign="center",
                size_hint_y=None,
                height=dp(20)
            ))
            grid.add_widget(stat_box)
        
        stats_card.add_widget(grid)
        content.add_widget(stats_card)

        # Interactive Counter Card
        counter_card = MDCard(
            orientation="vertical",
            padding="16dp",
            spacing="12dp",
            size_hint_y=None,
            height=dp(160)
        )
        
        counter_card.add_widget(MDLabel(
            text="⭐ Counter Demo",
            font_size="18sp",
            bold=True,
            halign="center",
            size_hint_y=None,
            height=dp(30)
        ))
        
        self.counter_label = MDLabel(
            text=f"Count: {self.counter}",
            font_size="32sp",
            bold=True,
            halign="center",
            size_hint_y=None,
            height=dp(50)
        )
        counter_card.add_widget(self.counter_label)
        
        button_layout = MDBoxLayout(spacing="10dp", size_hint_y=None, height=dp(40))
        button_layout.add_widget(MDRaisedButton(
            text="Increment",
            size_hint_x=0.5,
            on_press=self.increment_counter
        ))
        button_layout.add_widget(MDFlatButton(
            text="Reset",
            size_hint_x=0.5,
            on_press=self.reset_counter
        ))
        counter_card.add_widget(button_layout)
        content.add_widget(counter_card)

        # Features Card
        features_card = MDCard(
            orientation="vertical",
            padding="16dp",
            spacing="10dp",
            size_hint_y=None,
            height=dp(200)
        )
        
        features_card.add_widget(MDLabel(
            text="✨ Key Features",
            font_size="18sp",
            bold=True,
            halign="left",
            size_hint_y=None,
            height=dp(30)
        ))
        
        features = [
            "✅ Modern Material Design Components",
            "✅ Responsive Layouts",
            "✅ Beautiful Color Themes",
            "✅ Cross-Platform Support"
        ]
        
        for feature in features:
            features_card.add_widget(MDLabel(
                text=feature,
                font_size="12sp",
                halign="left",
                size_hint_y=None,
                height=dp(25)
            ))
        
        content.add_widget(features_card)

        scroll.add_widget(content)
        main_layout.add_widget(scroll)

        # Footer
        footer = MDBoxLayout(
            size_hint_y=None,
            height=dp(50),
            padding="10dp",
            spacing="10dp"
        )
        footer.add_widget(MDLabel(
            text="💻 Built with Kivy & KivyMD",
            halign="center",
            theme_text_color="Hint"
        ))
        main_layout.add_widget(footer)

        return main_layout

    def increment_counter(self, instance):
        self.counter += 1
        self.counter_label.text = f"Count: {self.counter}"

    def reset_counter(self, instance):
        self.counter = 0
        self.counter_label.text = f"Count: {self.counter}"


if __name__ == "__main__":
    MainApp().run()
