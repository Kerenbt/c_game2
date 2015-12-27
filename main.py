from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.properties import ObjectProperty
import xml.etree.ElementTree as ET
from kivy.core.window import Window

class InputForm(BoxLayout):
    title=ObjectProperty()
    body=ObjectProperty()
    checkbox_agree=ObjectProperty()
    checkbox_txt=ObjectProperty()
    button=ObjectProperty()
    def __init__(self):
        super(InputForm, self).__init__()
        dict = {'title':self.title,
                'body':self.body,
                'checkbox_txt':self.checkbox_txt,
                'button':self.button}
        f = open('agreement.xml','r', encoding='utf-8')
        txt = f.read()
        tree = ET.fromstring(txt)
        for child in tree:
            dict[child.tag].text = child.text[::-1]
            print(child.tag, child.text)

    def contin(self):
        if self.checkbox_agree.active:
            print("im working")
        else:
            print("pls mark checkbox")

    # def on_checkbox_active(checkbox, value):
    #     if value:
    #         print('The checkbox', checkbox, 'is active')
    #     else:
    #         print('The checkbox', checkbox, 'is inactive')



        #self.body.text= txt[1:len(txt)-2]
        # self.checkbox_agree.text= txt[len(txt)-2]
        # self.button.text= txt[len(txt)-1]
        # print(txt[0],txt[1:len(txt)-2],txt[len(txt)-2],txt[len(txt)-1])
        #for line in txt:
        #txt_combine = txt_combine + line + "\n"




class AgreementApp(App):
    pass
    # def build(self):
    #     f = open('hebrew.txt','r', encoding='utf-8')
    #     txt = f.readlines()
    #     print(txt)
    #     print(self.root)
    #     pass

if __name__ == '__main__':
    AgreementApp().run()


