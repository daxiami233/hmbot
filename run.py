from dista.device import Device
from dista.vht import VHTParser
from dista.proto import OperatingSystem
import time
print()

device = Device('127.0.0.1:5555', OperatingSystem.HARMONY)
hierarchy = device.dump_hierarchy()
# print(hierarchy)
# root = VHTParser.parse(hierarchy)
# VHTParser.dump(root, 'test.json', 1)
nodes = hierarchy.all(clickable = 'true', type = 'Button')
for node in nodes:
    print(node.attrib['text'], node.attrib['bounds'], node.attrib['center'])
# device.click(nodes[0])
print(device.display_size())
print(device.display_rotation())
device.swipe(direction='right')
# device.recent()
# device.automator._driver.swipe_ext('up', scale=0.5)
# device.automator._driver.swipe_ext('up')
# device.drag(0.5, 0.5, 0.2, 0.5, 200)
# device.drag(630/1260, 2710/2720, 630/1260, 2400/2720, 200)
# device.drag(630, 2710, 630, 2400, 200)
# time.sleep(1)
# device.automator._driver.gesture.start(0.5, 0.93, interval = 0.5).move(0.5, 0.8).action()
# device.automator._driver.gesture.start(0.5, 0.99).move(0.5, 0.8).pause(interval=0.5).move(0.5, 0.8).action()
# device.screenshot('aaa.jpeg')
# print(hierarchy)

# from typing import List
# from pydantic import BaseModel, Field
# import json

# class ViewAttributes(BaseModel):
#     model_config = {'extra': 'allow'}
#     bounds : str

# class View(BaseModel):
#     model_config = {'extra': 'allow'}
#     attributes : ViewAttributes
#     children: List['View'] = Field(default_factory = list)

# f = open('hierarchy.json', 'r')
# model = View(**json.load(f))
# print(model.attributes.bounds)
