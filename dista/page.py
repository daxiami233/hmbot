class Page(object):
    def __init__(self, name='', vht=None, img=None, ability='', **resource):
        self.name = name
        self.vht = vht
        self.img = img
        self.resource = {**resource}
        self.ability = ability
    
    def _is_same(self, page):
        #todo
        return False
    