from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.slider import Slider
from kivy.core.audio import SoundLoader
from kivy.core.window import Window

# =========================
# APP SETTINGS
# =========================
Window.clearcolor = (0.08, 0.08, 0.08, 1)

# =========================
# FM STATIONS (BD + INT)
# =========================
stations = {
    "🇧🇩 Radio Foorti": "https://stream.zeno.fm/0c0y1f9p0k8uv",
    "🇧🇩 Radio Today": "https://stream.zeno.fm/2w1m5u8p0k8uv",
    "🇧🇩 Dhaka FM": "https://stream.zeno.fm/1t8r5m8p0k8uv",
    "BBC Radio 1": "http://stream.live.vc.bbcmedia.co.uk/bbc_radio_one",
    "BBC Radio 2": "http://stream.live.vc.bbcmedia.co.uk/bbc_radio_two",
    "Classic FM": "https://media-ssl.musicradio.com/ClassicFMMP3"
}

# =========================
# MAIN APP
# =========================
class UltraFM(App):
    def build(self):
        self.sound = None
        self.volume = 0.7

        root = BoxLayout(orientation="vertical", padding=20, spacing=15)

        self.status = Label(
            text="📻 Ultra FM Ready",
            font_size=20,
            color=(0, 1, 0, 1)
        )
        root.add_widget(self.status)

        self.spinner = Spinner(
            text="Select FM Station",
            values=list(stations.keys()),
            size_hint=(1, None),
            height=50
        )
        root.add_widget(self.spinner)

        play_btn = Button(
            text="▶ PLAY",
            font_size=18,
            background_color=(0.2, 0.6, 1, 1)
        )
        play_btn.bind(on_press=self.play_radio)
        root.add_widget(play_btn)

        stop_btn = Button(
            text="⏹ STOP",
            font_size=18,
            background_color=(1, 0.2, 0.2, 1)
        )
        stop_btn.bind(on_press=self.stop_radio)
        root.add_widget(stop_btn)

        root.add_widget(Label(text="🔊 Volume", font_size=16))
        self.slider = Slider(min=0, max=1, value=self.volume)
        self.slider.bind(value=self.change_volume)
        root.add_widget(self.slider)

        return root

    def play_radio(self, instance):
        station = self.spinner.text
        if station not in stations:
            self.status.text = "❌ Select a station first"
            return

        if self.sound:
            self.sound.stop()

        self.sound = SoundLoader.load(stations[station])
        if self.sound:
            self.sound.volume = self.volume
            self.sound.play()
            self.status.text = f"▶ Playing: {station}"
        else:
            self.status.text = "❌ Stream error"

    def stop_radio(self, instance):
        if self.sound:
            self.sound.stop()
            self.status.text = "⏹ Stopped"

    def change_volume(self, instance, value):
        self.volume = value
        if self.sound:
            self.sound.volume = value

UltraFM().run()
