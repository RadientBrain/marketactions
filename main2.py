from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import requests
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.from_date = None
        self.to_date = None
        self.baseurl = "https://www.nseindia.com/"
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                        'like Gecko) '
                        'Chrome/80.0.3987.149 Safari/537.36',
                        'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
        self.add_widget(Label(text="From Date"))
        self.from_date = TextInput()
        self.add_widget(self.from_date)
        self.add_widget(Label(text="To Date"))
        self.to_date = TextInput()
        self.add_widget(self.to_date)
        self.submit_button = Button(text="Submit", on_press=self.get_actions)
        self.add_widget(self.submit_button)
        self.result_label = Label()
        self.add_widget(self.result_label)

    def get_actions(self, instance):
        session = requests.Session()
        req = session.get(self.baseurl, headers=self.headers, timeout=5)
        cookies = dict(req.cookies)
        url = f"https://www.nseindia.com/api/corporates-corporateActions?index=equities&from_date={self.from_date.text}&to_date={self.to_date.text}"
        resp = session.get(url, headers=self.headers,
                           timeout=5, cookies=cookies)
        response_json = resp.json()
        self.result_label.text = str(response_json)


class MyApp(App):
    def build(self):
        return MainScreen()


if __name__ == "__main__":
    MyApp().run()
