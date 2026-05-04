from htmlnode import *
from textnode import *

def text_node_to_html_node(text_node):
    if text_node.text_type is None:
        raise Exception("Invalid text node: missing type")
    match text_node.text_type:
        case TextType.TEXT:
            html_node = LeafNode(value=text_node.text)
        case TextType.BOLD:
            html_node = LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            html_node = LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            html_node = LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            html_node = LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case TextType.IMAGE:
            html_node = LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Invalid text node: type not recognised")

    return html_node

        
