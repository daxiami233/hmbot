from .page import Page
from .vht import VHT

class Window(object):
    def __init__(self, vht, screen):
        roots = vht.roots()
        self._pages = []
        for root in roots:
            name = root.attribute['page']
            from .cv import _crop
            page = Page(name=name, vht=VHT(root), img=_crop(screen, root.attribute['bounds']), ability='')
            self._pages.append(page)
