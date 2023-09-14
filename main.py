from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton,MDRectangleFlatIconButton,MDRaisedButton,MDTextButton,MDFillRoundFlatIconButton,MDFloatingActionButtonSpeedDial,MDRoundFlatButton,MDFillRoundFlatButton,MDRoundFlatIconButton,MDRectangleFlatButton,MDFloatingActionButton,MDFlatButton
from kivy.uix.screenmanager import ScreenManager, Screen
#from kivy.core.window import Window
#from demo import screen_helper
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

screen_helper = """

ScreenManager:
    MenuScreen:
    NorthScreen:
    SouthScreen:
    ChineScreen:
    ChatScreen:
    EggScreen:
    chickenScreen:
    IceScreen:
    JuiceScreen:
    OrderScreen:





<MenuScreen>:
    name: 'menu'
    MDRaisedButton:
        text: 'SOUTH INDIAN'
        size_hint:0.16,0.16
        pos_hint: {"x": 0.05, "y": 0.7}
        theme_text_color: "Custom" 
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 255/255.0,207/255.0,0/255.0,1
        on_press: root.manager.current = 'South'
    MDRaisedButton:
        text: 'NORTH INDIAN'
        size_hint:0.16,0.16
        pos_hint: {"x": 0.54, "y": 0.7}
        theme_text_color: "Custom" 
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 255/255.0,207/255.0,0/255.0,1
        on_press: root.manager.current = 'North'
    MDRaisedButton:
        text: "    CHINEESE     "
        size_hint:0.16,0.16
        size:200,100
        pos_hint: {"x": 0.05, "y": 0.5}
        theme_text_color: "Custom" 
        text_color:1/255.0,1/255.0,1/255.0,1
        md_bg_color: 255/255.0,207/255.0,0/255.0,1
        on_press: root.manager.current = 'Chine'
    MDRaisedButton:
        text: "        CHATS       "
        size_hint:0.16,0.16
        pos_hint: {"x": 0.54, "y": 0.5}
        theme_text_color: "Custom" 
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 255/255.0,207/255.0,0/255.0,1
        on_press: root.manager.current = 'Chat'
    MDRaisedButton:
        text: "     CHICKEN     "
        size_hint:0.16,0.16
        pos_hint: {"x": 0.05, "y": 0.3}
        theme_text_color: "Custom" 
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 255/255.0,207/255.0,0/255.0,1
        on_press: root.manager.current = 'Chicken'
    MDRaisedButton:
        text: "         JUICE        "
        size_hint:0.16,0.16
        pos_hint:{"x": 0.54, "y": 0.3}
        theme_text_color: "Custom" 
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 255/255.0,207/255.0,0/255.0,1
        on_press: root.manager.current = 'Juice'
    MDRaisedButton:
        text: "     ICE CREAM "
        size_hint:0.16,0.16
        pos_hint: {"x": 0.05, "y": 0.1}
        theme_text_color: "Custom" 
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 255/255.0,207/255.0,0/255.0,1
        on_press: root.manager.current = 'Ice'
    MDRaisedButton:
        text: "           EGG         "
        size_hint:0.16,0.16
        pos_hint: {"x": 0.54, "y": 0.1}
        theme_text_color: "Custom" 
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 255/255.0,207/255.0,0/255.0,1
        on_press: root.manager.current = 'Egg'
<NorthScreen>:
    name: 'North'

    MDRectangleFlatButton:
        text: 'North Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.8}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'North Speacial Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.7}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.6}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Chole Bature'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.5}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Sabzi'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.4}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'lkdal'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.3}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'pokldja'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.2}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'South Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.1}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'food items'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.9}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 165/255.0,124/255.0,26/255.0,1
        
    MDFillRoundFlatButton:
        text: 'Price'
        size_hint:0.4,0.01
        pos_hint: {'x':0.55,'y':0.9}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 165/255.0,124/255.0,26/255.0,1
        
        

    MDFloatingActionButton:
        text: 'Back'
        size_hint:0.09,0.05
        icon: "language-java"
        pos_hint: {'x':0.05,'y':0.015}
        on_press: root.manager.current = 'menu'

    MDLabel:
        text: '30'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.33}
    MDLabel:
        text: '40'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.23}
    MDLabel:
        text: '50'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.13}
    MDLabel:
        text: '70'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.03}
    MDLabel:
        text: '80'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.07}
    MDLabel:
        text: '90'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.17}
    MDLabel:
        text: '35'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.27}
    MDLabel:
        text: '45'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.37}

<SouthScreen>:
    name: 'South'
    MDRectangleFlatButton:
        text: 'North Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.8}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'North Speacial Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.7}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.6}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Chole Bature'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.5}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Sabzi'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.4}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'lkdal'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.3}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'pokldja'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.2}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'South Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.1}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'food items'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.9}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 165/255.0,124/255.0,26/255.0,1
        
    MDFillRoundFlatButton:
        text: 'Price'
        size_hint:0.4,0.01
        pos_hint: {'x':0.55,'y':0.9}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 165/255.0,124/255.0,26/255.0,1
        
        

    MDFloatingActionButton:
        text: 'Back'
        size_hint:0.09,0.05
        icon: "language-java"
        pos_hint: {'x':0.05,'y':0.015}
        on_press: root.manager.current = 'menu'

    MDLabel:
        text: '30'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.33}
    MDLabel:
        text: '40'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.23}
    MDLabel:
        text: '50'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.13}
    MDLabel:
        text: '70'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.03}
    MDLabel:
        text: '80'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.07}
    MDLabel:
        text: '90'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.17}
    MDLabel:
        text: '35'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.27}
    MDLabel:
        text: '45'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.37}
<ChineScreen>:
    name:'Chine'
    MDRectangleFlatButton:
        text: 'North Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.8}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'North Speacial Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.7}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.6}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Chole Bature'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.5}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Sabzi'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.4}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'lkdal'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.3}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'pokldja'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.2}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'South Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.1}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'food items'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.9}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 165/255.0,124/255.0,26/255.0,1
        
    MDFillRoundFlatButton:
        text: 'Price'
        size_hint:0.4,0.01
        pos_hint: {'x':0.55,'y':0.9}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 165/255.0,124/255.0,26/255.0,1
        
        

    MDFloatingActionButton:
        text: 'Back'
        size_hint:0.09,0.05
        icon: "language-java"
        pos_hint: {'x':0.05,'y':0.015}
        on_press: root.manager.current = 'menu'
    MDLabel:
        text: '30'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.33}
    MDLabel:
        text: '40'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.23}
    MDLabel:
        text: '50'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.13}
    MDLabel:
        text: '70'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.03}
    MDLabel:
        text: '80'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.07}
    MDLabel:
        text: '90'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.17}
    MDLabel:
        text: '35'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.27}
    MDLabel:
        text: '45'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.37}  
    MDLabel:
        text: '40'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.23}
    MDLabel:
        text: '50'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.13}
    MDLabel:
        text: '70'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.03}
    MDLabel:
        text: '80'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.07}
    MDLabel:
        text: '90'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.17}
    MDLabel:
        text: '35'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.27}
    MDLabel:
        text: '45'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.37}



<ChatScreen>:
    name: 'Chat'
    MDRectangleFlatButton:
        text: 'North Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.8}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'North Speacial Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.7}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.6}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Chole Bature'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.5}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Sabzi'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.4}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'lkdal'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.3}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'pokldja'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.2}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'South Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.1}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'food items'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.9}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 165/255.0,124/255.0,26/255.0,1
        
    MDFillRoundFlatButton:
        text: 'Price'
        size_hint:0.4,0.01
        pos_hint: {'x':0.55,'y':0.9}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 165/255.0,124/255.0,26/255.0,1
        
        

    MDFloatingActionButton:
        text: 'Back'
        size_hint:0.09,0.05
        icon: "language-java"
        pos_hint: {'x':0.05,'y':0.015}
        on_press: root.manager.current = 'menu'

    MDLabel:
        text: '30'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.33}
    MDLabel:
        text: '40'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.23}
    MDLabel:
        text: '50'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.13}
    MDLabel:
        text: '70'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.03}
    MDLabel:
        text: '80'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.07}
    MDLabel:
        text: '90'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.17}
    MDLabel:
        text: '35'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.27}
    MDLabel:
        text: '45'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.37}
<EggScreen>:
    name: 'Egg'
    MDRectangleFlatButton:
        text: 'North Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.8}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'North Speacial Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.7}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.6}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Chole Bature'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.5}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Sabzi'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.4}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'lkdal'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.3}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'pokldja'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.2}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'South Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.1}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'food items'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.9}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 165/255.0,124/255.0,26/255.0,1
        
    MDFillRoundFlatButton:
        text: 'Price'
        size_hint:0.4,0.01
        pos_hint: {'x':0.55,'y':0.9}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 165/255.0,124/255.0,26/255.0,1
        
        

    MDFloatingActionButton:
        text: 'Back'
        size_hint:0.09,0.05
        icon: "language-java"
        pos_hint: {'x':0.05,'y':0.015}
        on_press: root.manager.current = 'menu'

    MDLabel:
        text: '30'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.33}
    MDLabel:
        text: '40'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.23}
    MDLabel:
        text: '50'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.13}
    MDLabel:
        text: '70'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.03}
    MDLabel:
        text: '80'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.07}
    MDLabel:
        text: '90'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.17}
    MDLabel:
        text: '35'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.27}
    MDLabel:
        text: '45'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.37}
<chickenScreen>:
    name: 'Chicken'
    MDRectangleFlatButton:
        text: 'North Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.8}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'North Speacial Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.7}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.6}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Chole Bature'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.5}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Sabzi'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.4}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'lkdal'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.3}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'pokldja'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.2}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'South Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.1}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'food items'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.9}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 165/255.0,124/255.0,26/255.0,1
        
    MDFillRoundFlatButton:
        text: 'Price'
        size_hint:0.4,0.01
        pos_hint: {'x':0.55,'y':0.9}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 165/255.0,124/255.0,26/255.0,1
        
        

    MDFloatingActionButton:
        text: 'Back'
        size_hint:0.09,0.05
        icon: "language-java"
        pos_hint: {'x':0.05,'y':0.015}
        on_press: root.manager.current = 'menu'

    MDLabel:
        text: '30'
        pos_hint: {'x':0.75,'y':0.33}
    MDLabel:
        text: '30'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.33}
    MDLabel:
        text: '40'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.23}
    MDLabel:
        text: '50'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.13}
    MDLabel:
        text: '70'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.03}
    MDLabel:
        text: '80'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.07}
    MDLabel:
        text: '90'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.17}
    MDLabel:
        text: '35'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.27}
    MDLabel:
        text: '45'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.37}

<IceScreen>:
    name: 'Ice'
    MDRectangleFlatButton:
        text: 'North Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.8}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'North Speacial Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.7}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.6}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Chole Bature'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.5}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Sabzi'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.4}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'lkdal'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.3}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'pokldja'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.2}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'South Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.1}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'food items'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.9}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 165/255.0,124/255.0,26/255.0,1
        
    MDFillRoundFlatButton:
        text: 'Price'
        size_hint:0.4,0.01
        pos_hint: {'x':0.55,'y':0.9}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 165/255.0,124/255.0,26/255.0,1
        
        

    MDFloatingActionButton:
        text: 'Back'
        size_hint:0.09,0.05
        icon: "language-java"
        pos_hint: {'x':0.05,'y':0.015}
        on_press: root.manager.current = 'menu'

    MDLabel:
        text: '30'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.33}
    MDLabel:
        text: '40'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.23}
    MDLabel:
        text: '50'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.13}
    MDLabel:
        text: '70'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.03}
    MDLabel:
        text: '80'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.07}
    MDLabel:
        text: '90'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.17}
    MDLabel:
        text: '35'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.27}
    MDLabel:
        text: '45'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.37}

<JuiceScreen>:
    name: 'Juice'
    MDRectangleFlatButton:
        text: 'North Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.8}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'North Speacial Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.7}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Thali'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.6}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Chole Bature'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.5}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'Sabzi'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.4}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'lkdal'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.3}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'pokldja'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.2}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDRectangleFlatButton:
        text: 'South Mini Meals'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.1}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 185/255.0,21/255.0,0/255.0,1
        on_press: root.manager.current = 'Order'
    MDFillRoundFlatButton:
        text: 'food items'
        size_hint:0.4,0.01
        pos_hint: {'x':0.05,'y':0.9}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 165/255.0,124/255.0,26/255.0,1
        
    MDFillRoundFlatButton:
        text: 'Price'
        size_hint:0.4,0.01
        pos_hint: {'x':0.55,'y':0.9}
        text_color:   1/255.0,1/255.0,1/255.0,1
        md_bg_color: 165/255.0,124/255.0,26/255.0,1
        
        

    MDFloatingActionButton:
        text: 'Back'
        size_hint:0.09,0.05
        icon: "language-java"
        pos_hint: {'x':0.05,'y':0.015}
        on_press: root.manager.current = 'menu'

    MDLabel:
        text: '30'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.33}
    MDLabel:
        text: '40'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.23}
    MDLabel:
        text: '50'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.13}
    MDLabel:
        text: '70'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':0.03}
    MDLabel:
        text: '80'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.07}
    MDLabel:
        text: '90'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.17}
    MDLabel:
        text: '35'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.27}
    MDLabel:
        text: '45'
        text_color:   1/255.0,1/255.0,1/255.0,1
        pos_hint: {'x':0.75,'y':-0.37}
<OrderScreen>:
    name:'Order'
    MDLabel:
        text:'order placed'
        pos_hint:{'x':0.4}
    MDRaisedButton:
        text: 'GO BACK TO HOME PAGE'
        size_hint:0.09,0.05
        pos_hint: {'x':0.05,'y':0.2}
        on_press: root.manager.current = 'menu'





"""


class MenuScreen(Screen):
    pass


class NorthScreen(Screen):
    pass


class SouthScreen(Screen):
    pass
class OrderScreen(Screen):
    pass

class ChineScreen(Screen):
    pass
class ChatScreen(Screen):
    pass
class EggScreen(Screen):
    pass
class chickenScreen(Screen):
    pass
class IceScreen(Screen):
    pass
class JuiceScreen(Screen):
    pass
# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SouthScreen(name='South'))
sm.add_widget(NorthScreen(name='North'))
sm.add_widget(ChineScreen(name='Chine'))
sm.add_widget(ChatScreen(name='Chat'))
sm.add_widget(IceScreen(name='Ice'))
sm.add_widget(JuiceScreen(name='Juice'))
sm.add_widget(chickenScreen(name='Chicken'))
sm.add_widget(EggScreen(name='Egg'))
sm.add_widget(OrderScreen(name='Order'))


class MINGOES(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        #self.theme_cls.theme_style = "Dark"
        return screen





MINGOES().run()
