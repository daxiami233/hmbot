from dista.device import Device
from dista.connector.hdc import HDC
from dista.vht import VHTParser
import cv2
import uiautomator2
from dista.event import KeyEvent
from dista.proto import SystemKey
from dista.ptg import PTG
from dista.page import Page
from dista.app.harmony_app import HarmonyApp
from dista.app.app import App


device1 = Device('127.0.0.1:5555', 'harmony')
app = HarmonyApp(device=device1)
print(app.bundle, app.entry, app.main_page, app.name)
print(isinstance(app, App))
print(isinstance(app, HarmonyApp))
# print(device1.connector.current_ability())
# device2 = Device('emulator-5554', 'android')
# print(device.connector._hidumper('AbilityManagerService', '-i 16'))
# print(device.connector.get_current_ability())
# VHTParser.dump(device.dump_hierarchy(), 'origin.json')
# img = device.screenshot()
# print(img.shape)

# VHTParser.dump(device2.automator.dump_hierarchy(), 'and1.json')
# print(device.automator._driver.app_current())
# device2.recent()
# print(device1.weight, )
# print(device.automator._driver.dump_hierarchy())

# window = device.dump_window()
# page = window.pages[0]
# cv2.imwrite('page.jpg', page.img)

# print(device.connector._hidumper('AbilityManagerService', '-i 16'))