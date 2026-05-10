from functions.split_nodes import *
from textnode import *

def text_to_textnodes(text):
    text_nodes = [TextNode(text, TextType.TEXT)]
    text_nodes_b = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    text_nodes_i = split_nodes_delimiter(text_nodes_b, "_", TextType.ITALIC)
    text_nodes_c = split_nodes_delimiter(text_nodes_i, "`", TextType.CODE)
    text_nodes_img = split_nodes_image(text_nodes_c)
    text_nodes_final = split_nodes_link(text_nodes_img)
    
    return text_nodes_final
