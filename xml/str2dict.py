from xml.etree import ElementTree
import ast
from collections import Counter

def dump_node(node, indent=0):
    # print("{}{} {} {}".format('    ' * indent, node.tag, node.attrib, node.text))
    # print(type(node.text), node.text.replace('\n', ''))
    try:
        print('-----------------')
        after = node.text.replace('\n', '').replace(' ', '')
        print(after)
        print('before', Counter(node.text))
        print('after', Counter(after))
        print(ast.literal_eval(after))
    except:
        print('err')

    for child in node:
        dump_node(child, indent + 1)

if __name__ == '__main__':
    tree = ElementTree.parse('data.xml')
    dump_node(tree.getroot())