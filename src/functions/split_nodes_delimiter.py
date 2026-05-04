from textnode import TextType, TextNode

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


