import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        # Create a GridLayout inside another GridLayout
        self.inside = GridLayout()
        self.inside.cols = 2
        # Creating Form Objects
        self.inside.add_widget(Label(text='First Name: '))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text='Last Name: '))
        self.lastname = TextInput(multiline=False)
        self.inside.add_widget(self.lastname)

        self.inside.add_widget(Label(text='Email: '))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)
        # Insert GridLayout to main GridLayout
        self.add_widget(self.inside)
        # Adding a Button on the main GridLayout
        self.submit = Button(text='Submit', font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text
        last = self.lastname.text
        email = self.email.text
        print("Name: ", name, "Last Name: ", last, "Email: ", email)
        self.name.text = ''
        self.lastname.text = ''
        self.email.text = ''


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    MyApp = MyApp()
    MyApp.run()
