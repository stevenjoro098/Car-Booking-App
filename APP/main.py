from datetime import datetime
import requests
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import  AsyncImage
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import  RiseInTransition
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.button import MDIconButton, MDFillRoundFlatButton, MDFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window


Window.size = (320, 600)
CAR_DETAILS = {}
CAROUSEL_OBJECTS = []

url = "http://127.0.0.1:8000"


# Color:0.59,0.6,0.6,1

class Success(BoxLayout):
    pass


class MyGrid(MDScreen):
    dialog = None
    from_label = ObjectProperty(None)

    # =====================Define Carousel Card ============================================
    def carousel_objects(self, image, name, model, year, cc, transmission, top_speed, load_capacity, pass_capacity,
                         category, charge, registration):
        car_card = MDCard(pos_hint={"center_x": .5, "center_y": .7},
                          size_hint_x=None,
                          size_hint_y=None,
                          size=(260, 240),
                          border_radius=20,
                          radius=[20, ],
                          md_bg_color=[0.59, 0.6, 0.6, 1]
                          )
        car_card.md_bg_color = (0.59, 0.6, 0.6, 1)
        rl = RelativeLayout()
        car_image = AsyncImage(source=image,
                               pos_hint={"center_x": .4, "center_y": .68})
        name_label = MDLabel(pos_hint={"center_x": .6, "center_y": .3},
                             text=name,
                             font_style="H4",
                             theme_text_color="Custom",
                             text_color=(1, 1, 1, 1),
                             bold=True)
        model_label = MDLabel(pos_hint={"center_x": .6, "center_y": .18},
                              text=model,
                              font_style="Caption",
                              theme_text_color="Custom",
                              text_color=(1, 1, 1, 1),
                              bold=True)
        year_label = MDLabel(pos_hint={"center_x": .73, "center_y": .18},
                             text=year,
                             font_style="Caption",
                             theme_text_color="Custom",
                             text_color=(1, 1, 1, 1),
                             bold=True)
        like_icon = MDIconButton(pos_hint={"center_x": .85, "center_y": .9},
                                 icon="heart")
        info_icon = MDIconButton(pos_hint={"center_x": .85, "center_y": .75},
                                 icon="information-variant",
                                 on_release=lambda a: details_screen())
        book_button = MDFillRoundFlatButton(pos_hint={"center_x": .5, "center_y": .01},
                                            text="Book NOW",
                                            on_release=lambda a: home()
                                            )

        def details_screen():
            self.screen_manager.current = 'details'
            self.screen_manager.transition.direction = 'left'
            self.screen_manager.transition = RiseInTransition()

            self.transmission.text = transmission
            self.top_speed.text = top_speed
            self.seats.text = pass_capacity

            self.image.source = image
            self.cc.text = cc

            self.booking_title.text = registration
            self.booking_rate.text = str(charge)
            self.booking_image.source = image

        def home():
            self.screen_manager.current = 'book'
            self.screen_manager.transition = RiseInTransition()
            self.booking_title.text = registration
            self.booking_rate.text = str(charge)
            self.booking_image.source = image

            CAR_DETAILS["registration"] = registration
            CAR_DETAILS["image"] = image
            CAR_DETAILS["charge"] = charge

        rl.add_widget(car_image)
        rl.add_widget(name_label)
        rl.add_widget(model_label)
        rl.add_widget(year_label)
        rl.add_widget(like_icon)
        rl.add_widget(book_button)
        rl.add_widget(info_icon)
        car_card.add_widget(rl)

        self.carousel.add_widget(car_card)

    # ======================= Fetch data from API =======================================
    def update_carousel(self):

        try:
            # print(content.json())
            content = requests.get(url).json()
            for items in content:
                image = items["image"]
                name = items["name"]
                model = items["model"]
                year = items["year"]
                cc = items["cc"]
                transmission = items["transmission"]
                top_speed = items["top_speed"]
                load_capacity = items["load_capacity"]
                pass_capacity = items["pass_capacity"]
                category = items["category"]
                charge = items["charge"]
                available = items["available"]
                registration = items["registration"]
                slug = items["slug"]
                CAROUSEL_OBJECTS.append(slug)
                if slug not in CAROUSEL_OBJECTS:
                    self.carousel_objects(image, name, model, year, cc, transmission, top_speed,
                                          load_capacity, pass_capacity, category, charge,
                                          registration)
                else:
                    self.carousel_objects(image, name, model, year, cc, transmission, top_speed,
                                          load_capacity, pass_capacity, category, charge,
                                          registration)

            toast("Carousel Updated")
            #print(CAROUSEL_OBJECTS)
        except:
            toast("Cannot Fetch Data")

    # ==================== Clear Booking details
    # ========================================================================#
    def clear_booking_details(self):
        self.first_name.text = ""
        self.last_name.text = ""
        self.phone_number.text = ""
        self.to_label.text = ""
        self.from_label.text = ""
        self.no_days.text = ""
        self.booking_title.text = ""
        self.booking_rate.text = ""
        self.booking_image.text = ""
        CAR_DETAILS.clear()

    def set_date_from(self):
        date_dialog = MDDatePicker(
            callback=self.select_from_date,
        )
        date_dialog.open()

    def select_from_date(self, date):
        self.from_label.text = str(date)
        self.from_date = date
        print(date)
        return date

    def set_date_to(self):
        date_dialog = MDDatePicker(
            callback=self.select_to_date,
        )
        date_dialog.open()

    def select_to_date(self, date):
        self.to_label.text = str(date)
        self.to_date = date
        print(date)
        self.calc_days()
        return date

    # ========================== Calculate Delta =============================================================#
    def calc_days(self):
        date_format = '%Y-%m-%d'
        a = datetime.strptime(str(self.from_date), date_format)
        b = datetime.strptime(str(self.to_date), date_format)
        no_days = b - a
        print("Days: ", no_days.days)
        self.no_days.text = str(no_days.days) + " Days"



    def book(self):
        first_name = self.first_name.text
        last_name = self.last_name.text
        phone_number = self.phone_number.text
        period = self.no_days.text
        book_url = url + '/book/'
        try:
            json_data = {'first_name': str(first_name), 'second_name': str(last_name), 'telephone': str(phone_number),
                         'from_date': str(self.from_date), 'to_date': str(self.to_date), 'period': period,
                         'registration': CAR_DETAILS['registration'],
                         'charges': CAR_DETAILS['charge']}
            r = requests.post(book_url, json=json_data)

            if r.status_code == 201:
                toast("Booking Successful!!")
                if not self.dialog:
                    self.dialog = MDDialog(
                        type='custom',
                        content_cls=Success(),
                        size_hint=(.9, .9),
                        radius=[20, 7, 20, 7],
                        buttons=[
                            MDFlatButton(text="OK")

                        ]
                    )
                self.dialog.open()
            else:
                toast("Booking Failed")

            # print(CAR_DETAILS)

        except:
            toast("Booking Process Failed")

    # Clock.schedule_once(self.update_carousel,1)


class BookingApp(MDApp):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    BookingApp().run()
