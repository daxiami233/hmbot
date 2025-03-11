from xml.etree.ElementTree import Element
from .exception import*
import json, re
class VHT(object):
    """
    The class describes a view hierarchy tree
    """
    def __init__(self, node=None, page=None):
        self._root = node

class VHTNode(object):
    """
    The class describes a node of view hierarchy tree
    """
    def __init__(self, attrib={}, **extra):
        if not isinstance(attrib, dict):
            raise TypeError("attrib must be dict, not %s" % (attrib.__class__.__name__,))
        self.attrib = {**attrib, **extra}
        self._children = []

    def __str__(self):
        return str(self.attrib)
    
    def __len__(self):
        return len(self._children)
    
    def __getitem__(self, index):
        return self._children[index]
    
    def __setitem__(self, index, node):
        if isinstance(index, slice):
            for child in node:
                self._assert_is_node(child)
        else:
            self._assert_is_node(node)
        self._children[index] = node
    
    def __delitem__(self, index):
        del self._children[index]
    
    def append(self, node):
        self._assert_is_node(node)
        self._children.append(node)
    
    def extend(self, nodes):
        for node in nodes:
            self._assert_is_node(node)
            self._children.append(node)
    
    def all(self, **attrib):
        nodes = []
        if self._satisfy(attrib):
            nodes.append(self)
        for child in self._children:
            nodes.extend(child.all(**attrib))
        return nodes
    
    def _assert_is_node(self, node):
        if not isinstance(node, VHTNode):
            raise TypeError('expected a VHTNode, not %s' % type(node).__name__)

    def _dict(self):
        children_dict = [child._dict() for child in self._children]
        return {
            'attributes': self.attrib,
            'children': children_dict
        }
    
    def _satisfy(self, attrib):
        for key, value in attrib.items():
            if key not in self.attrib or self.attrib[key] != value:
                return False
        return True
    

class VHTParser(object):
    """
    The class describes a parser for view hierarchy tree
    """
    def __init__(self):
        pass

    @classmethod
    def parse(cls, source):
        if isinstance(source, Element):
            pass
        elif isinstance(source, dict):
            return VHTParser._parse_hdc_json(source)
        else:
            raise TypeError('expected a dict or Element, not %s' % type(source).__name__)

    @classmethod
    def dump(cls, root, file, indent=2):
        with open(file, 'w') as write_file:
            json.dump(root._dict(), write_file, indent=indent)
    
    @classmethod
    def _parse_hdc_json(cls, source):
        if 'attributes' in source:
            attribs = source['attributes']
            bound_re = '\[(\d+),(\d+)\]\[(\d+),(\d+)\]'
            match = re.match(bound_re, attribs['bounds'])
            if match:
                (x1, y1, x2, y2) = map(int, match.groups())
            else: 
                raise BoundsError('%s is not in form [x1,y1][x2,y2]' % attribs['bounds'])
            root = VHTNode(bounds = [[x1,y1],[x2 - x1,y2 - y1]],
                           clickable = attribs['clickable'],
                           longClickable = attribs['longClickable'],
                           selected = attribs['selected'],
                           type = attribs['type'],
                           text = attribs['text'],
                           center = [(x1 + x2)/2, (y1 + y2)/2])
            if 'children' in source:
                children = source['children']
                for child in children:
                    root.append(VHTParser._parse_hdc_json(child))
            return root
        else:
            raise JsonKeyError('expected key: attributes')
