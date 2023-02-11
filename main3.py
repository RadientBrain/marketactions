from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import requests


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.from_date_input = TextInput(
            hint_text="From Date (dd-mm-yyyy)", size_hint_y=None, height=60)
        self.to_date_input = TextInput(
            hint_text="To Date (dd-mm-yyyy)", size_hint_y=None, height=60)
        self.submit_button = Button(text="Submit", size_hint_y=None, height=60)
        self.result_label = Label(text="", size_hint_y=None, height=400)

        self.submit_button.bind(on_press=self.get_response)
        self.add_widget(self.from_date_input)
        self.add_widget(self.to_date_input)
        self.add_widget(self.submit_button)
        self.add_widget(self.result_label)

    def get_response(self, instance):
        from_date = self.from_date_input.text
        to_date = self.to_date_input.text
        baseurl = "https://www.nseindia.com/"
        url = f"https://www.nseindia.com/api/corporates-corporateActions?index=equities&from_date={from_date}&to_date={to_date}"
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                   'like Gecko) '
                   'Chrome/80.0.3987.149 Safari/537.36',
                   'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
        session = requests.Session()
        req = session.get(baseurl, headers=headers, timeout=5)
        cookies = dict(req.cookies)
        resp = session.get(url, headers=headers, timeout=5, cookies=cookies)
        response_json = resp.json()

        text = "Symbol\t\tSeries\t\tCompany\t\tSubject\t\tFace Value\t\tRecord Date\t\tExpiry Date\n"
        for action in response_json:
            text += f"{action['symbol']}\t\t{action['series']}\t\t{action['comp']}\t\t{action['subject']}\t\t{action['faceVal']}\t\t{action['recDate']}\t\t{action['exDate']}\n"

        self.result_label.text = text


class NSEIndiaApp(App):
    def build(self):
        return MainLayout()


if __name__ == '__main__':
    NSEIndiaApp().run()
