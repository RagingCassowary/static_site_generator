from htmlnode import *
from textnode import *

def text_node_to_html_node(text_node):
    if text_node.text_type is None:
        raise Exception("Invalid text node: missing type")
    match text_node.text_type(Enum):
        case "text":
            html_node = LeafNode(value=text_node.text)
        case "bold":
            html_node = LeafNode(tag="b", value=text_node.text)
        case "italic":
            html_node = LeafNode(tag="i", value=text_node.text)
        case "code":
            html_node = LeafNode(tag="code", value=text_node.text)
        case "link":
            html_node = LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case "image":
            html_node = LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("Invalid text node: type not recognised")

    return html_node

        
