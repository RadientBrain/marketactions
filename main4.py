from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.core.window import Window
import requests
import json

# f = open('resp.json')
# data = json.load(f)


class SelectableLabel(RecycleDataViewBehavior, Label):
    ''' Add selection support to the Label '''
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        ''' Catch and handle the view changes '''
        self.index = index
        return super(SelectableLabel, self).refresh_view_attrs(rv, index, data)

    def on_touch_down(self, touch):
        ''' Add selection on touch down '''
        if super(SelectableLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        ''' Respond to the selection of items in the view. '''
        self.selected = is_selected


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stack = StackLayout(
            orientation='rl-tb', size_hint_y=None, height=1000, width=1000)
        self.from_date_input = TextInput(
            hint_text="From Date (dd-mm-yyyy)", size_hint_y=None, height=60)
        self.to_date_input = TextInput(
            hint_text="To Date (dd-mm-yyyy)", size_hint_y=None, height=60)
        self.submit_button = Button(text="Submit", size_hint_y=None, height=60)
        self.result_rv = RecycleView()

        self.submit_button.bind(on_press=self.get_response)

        # self.result_label = Label(
        #     text="", size_hint_y=None, height=400, halign="center", valign="center")

        self.grid = GridLayout(cols=7, size_hint_y=None, height=60)
        self.grid.bind(minimum_height=self.grid.setter("height"),
                       minimum_width=self.grid.setter("width"))
        header = ["Symbol", "Series", "Company", "Subject",
                  "Face Value", "Record Date", "Expiry Date"]
        self.clear_widgets()
        for h in header:
            self.grid.add_widget(
                Label(text=h, size_hint_y=None, height=60))

        # self.add_widget(ScrollView(size_hint=(1, None), size=(1500, 1500)))
        # self.result_rv.add_widget(ScrollView(
        #     size_hint=(1, None), size=(1500, 1500)))

        self.scroll = ScrollView(
            size_hint=(1, None), size=(Window.width, Window.height))
        self.scroll.add_widget(self.stack)
        self.add_widget(self.scroll)

        self.stack.add_widget(self.result_rv, 0, ScrollView(
            size_hint=(1, None), size=(self.stack.width, self.stack.height)))
        self.result_rv.add_widget(self.grid)

        self.stack.add_widget(self.from_date_input)
        self.stack.add_widget(self.to_date_input)
        self.stack.add_widget(self.submit_button)

    def get_response(self, instance):
        from_date = self.from_date_input.text
        to_date = self.to_date_input.text
        baseurl = "https://www.nseindia.com/"
        url = f"https://www.nseindia.com/api/corporates-corporateActions?index=equities&from_date={from_date}&to_date={to_date}"
        headers = {'user-agent': 'Mozilla/4.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                   'like Gecko) '
                   'Chrome/80.0.3987.149 Safari/537.36',
                   'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
        session = requests.Session()
        req = session.get(baseurl, headers=headers, timeout=5)
        cookies = dict(req.cookies)
        resp = session.get(url, headers=headers, timeout=5, cookies=cookies)
        response_json = resp.json()
        # response_json = data
        # f.close()

        # text = "Symbol\t\tSeries\t\tCompany\t\tSubject\t\tFace Value\t\tRecord Date\t\tExpiry Date\n"
        # for action in response_json:
        #     text += f"{action['symbol']}\t\t{action['series']}\t\t{action['comp']}\t\t{action['subject']}\t\t{action['faceVal']}\t\t{action['recDate']}\t\t{action['exDate']}\n"

        # self.result_label.text = text

        for action in (response_json):
            scroll1 = ScrollView(
                do_scroll_y=True,  size_hint=(1, None), size=(1, 100))
            self.grid.add_widget(scroll1)
            scroll1.add_widget(Label(text=action['symbol'], text_size=(
                200, None),  size_hint_y=None, height=60))

            scroll2 = ScrollView(
                do_scroll_y=True,  size_hint=(1, None), size=(1, 100))
            self.grid.add_widget(scroll2)
            scroll2.add_widget(Label(text=action['series'], text_size=(
                200, None),  size_hint_y=None, height=60))

            scroll3 = ScrollView(
                do_scroll_y=True,  size_hint=(1, None), size=(1, 100))
            self.grid.add_widget(scroll3)
            scroll3.add_widget(Label(text=action['comp'], text_size=(
                200, None),  size_hint_y=None, height=60))

            scroll4 = ScrollView(
                do_scroll_y=True,  size_hint=(1, None), size=(1, 100))
            self.grid.add_widget(scroll4)
            scroll4.add_widget(Label(text=action['subject'], text_size=(
                200, None),  size_hint_y=None, height=60))

            scroll5 = ScrollView(
                do_scroll_y=True,  size_hint=(1, None), size=(1, 100))
            self.grid.add_widget(scroll5)
            scroll5.add_widget(Label(text=action['faceVal'], text_size=(
                200, None),  size_hint_y=None, height=60))

            scroll6 = ScrollView(
                do_scroll_y=True,  size_hint=(1, None), size=(1, 100))
            self.grid.add_widget(scroll6)
            scroll6.add_widget(Label(text=action['recDate'], text_size=(
                200, None),  size_hint_y=None, height=60))

            scroll7 = ScrollView(
                do_scroll_y=True,  size_hint=(1, None), size=(1, 100))
            self.grid.add_widget(scroll7)
            scroll7.add_widget(Label(text=action['exDate'], text_size=(
                200, None),  size_hint_y=None, height=60))

        # scroll = ScrollView(size_hint_y=None, do_scroll_x=False, height=300)
        # self.clear_widgets()
        # scroll.add_widget(grid)
        # self.result_rv.add_widget(scroll)
        # self.add_widget(scroll)


class NSEIndiaApp(App):
    def build(self):
        return MainLayout()


if __name__ == '__main__':
    NSEIndiaApp().run()
