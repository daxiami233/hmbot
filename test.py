from dista.device import Device
from dista.connector.hdc import HDC
from dista.vht import VHTParser
import cv2
import uiautomator2
from dista.event import KeyEvent
from dista.proto import SystemKey
from dista.ptg import PTG
from dista.page import Page

ptg = PTG()
p1 = Page()
p2 = Page()
ptg.add_edge(p1, p1, 2)
ptg.add_edge(p1, p2, 3)
ptg.add_edge(p1, p2, 1)
print(ptg._adj_list)
exit(0)

device1 = Device('127.0.0.1:5557', 'harmony')
event = KeyEvent(page='', device=device1, key=SystemKey.BACK)
event.execute()
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