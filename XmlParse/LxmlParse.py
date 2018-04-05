# coding: utf-8

from lxml import etree

class LxmlParse:
    """Dom解析xml文件类"""

    def __init__(self, xml_obj, obj_type=False):
        parser = etree.XMLParser(strip_cdata=False)
        if obj_type:
            self.tree = etree.parse(xml_obj, parser)
        else:
            self.tree = etree.fromstring(xml_obj, parser) 
        self.root = self.tree.getroot()
    
    def get_node_list(self, node, xpath):
        if node is not None:
            return node.xpath(xpath)
        else:
            return []

    def get_node_attr_value(self, node, attr_name):
        if node is not None:
            return node.get(attr_name)
        else:
            return ''
        
    def get_node_all_attr_value(self, node):
        if node is not None:
            return node.items()
        else:
            return {}

    def get_node_value(self, node):
        if node is not None:
            return node.text
        else:
            return ''

    def creat_element(self, name):
        self.root = etree.Element(name)
    
    def creat_sub_element(self, node, name):
        etree.SubElement(node, 'child1')
        
if __name__ == "__main__":
    lxml_obj = LxmlParse("Example.xml")
    node_list = lxml_obj.get_node_list(lxml_obj.root, "//user")
    for index, node in enumerate(node_list):
        attr_value = lxml_obj.get_node_attr_value(node, "id")
        print "user %d, id=%s" % (index, attr_value)
        child_node_list = lxml_obj.get_node_list(node, "//username")
        for child_node in child_node_list:
            node_value = lxml_obj.get_node_value(child_node)
            print "user %d, username=%s" % (index, node_value)
            
        child_node_list = lxml_obj.get_node_list(node, "//info")
        for child_node in child_node_list:
            cdata = lxml_obj.get_node_value(child_node)
            print "user %d, info_cdata=%s" % (index, cdata)