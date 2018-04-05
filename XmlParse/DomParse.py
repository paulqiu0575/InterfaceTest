# coding: utf-8

from xml.dom import minidom

class DomParse:
    """Dom解析xml文件类"""

    def __init__(self, xml_path):
        self.doc = minidom.parse(xml_path)
        self.root = self.doc.documentElement
        
    def get_node_list(self, node, name):
        if node:
            return node.getElementsByTagName(name)
        else:
            return []

    def get_node_attr_value(self, node, attr_name):
        if node:
            return node.getAttribute(attr_name)
        else:
            return ''

    def get_node_value(self, node, index=0):
        if node:
            return node.childNodes[index].nodeValue
        else:
            return ''

    def get_node_cdata(self, node):
        if node:
            return node.firstChild.wholeText
        else:
            return []

if __name__ == "__main__":
    dom_obj = DomParse("Example.xml")
    node_list = dom_obj.get_node_list(dom_obj.root, "user")
    for index, node in enumerate(node_list):
        attr_value = dom_obj.get_node_attr_value(node, "id")
        print "user %d, id=%s" % (index, attr_value)
        child_node_list = dom_obj.get_node_list(node, "username")
        for child_node in child_node_list:
            node_value = dom_obj.get_node_value(child_node)
            print "user %d, username=%s" % (index, node_value)
            
        child_node_list = dom_obj.get_node_list(node, "info")
        for child_node in child_node_list:
            cdata = dom_obj.get_node_cdata(child_node)
            print "user %d, info_cdata=%s" % (index, cdata)

