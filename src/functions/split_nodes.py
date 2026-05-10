from textnode import TextType, TextNode
from functions.extract_markdown_links import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            split_nodes = node.text.split(delimiter)
            if len(split_nodes) == 1:
                new_nodes.append(node)
            elif len(split_nodes) % 2 == 0:
                raise Exception("missing closing delimiter")
            else:
                for i in range(len(split_nodes)):
                    if i % 2 == 0:
                        split = TextNode(split_nodes[i], TextType.TEXT)
                    else:
                        split = TextNode(split_nodes[i], text_type)
                    new_nodes.append(split)
    
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        text = node.text

        images = extract_markdown_images(node.text)

        for image in images:
            alt, link = image
            sections = text.split(f"![{alt}]({link})", 1)

            if len(sections[0]) > 0:
                text_node = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(text_node)

            image_node = TextNode(alt, TextType.IMAGE, url=link)
            new_nodes.append(image_node)

            text = sections[1]

        if len(text) > 0:

            last_node = TextNode(text, TextType.TEXT)
            new_nodes.append(last_node)

        return new_nodes
                


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        text = node.text

        links = extract_markdown_links(node.text)

        for link in links:
            alt, link = link
            sections = text.split(f"[{alt}]({link})", 1)

            if len(sections[0]) > 0:
                text_node = TextNode(sections[0], TextType.TEXT)
                new_nodes.append(text_node)

            link_node = TextNode(alt, TextType.LINK, url=link)
            new_nodes.append(link_node)

            text = sections[1]

        if len(text) > 0:

            last_node = TextNode(text, TextType.TEXT)
            new_nodes.append(last_node)

    return new_nodes


