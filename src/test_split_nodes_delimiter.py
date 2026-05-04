import unittest

from functions.split_nodes_delimiter import split_nodes_delimiter
from textnode import *

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_bold_text(self):
        node = TextNode("This is **bold** text!", TextType.TEXT)
        old_nodes = [node]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

        self.assertEqual(
            new_nodes[0],
            TextNode("This is ", TextType.TEXT)
        )

        self.assertEqual(
            new_nodes[1],
            TextNode("bold", TextType.BOLD)
        )

        self.assertEqual(
            new_nodes[2],
            TextNode(" text!", TextType.TEXT)
        )
    
    def test_multiple_nodes(self):
        node1 = TextNode("This is all italic", TextType.ITALIC)
        node2 = TextNode("Only _this_ is italic", TextType.TEXT)
        old_nodes = [node1, node2]
        new_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)

        self.assertEqual(
            new_nodes[0],
            TextNode("This is all italic", TextType.ITALIC)
        )

        self.assertEqual(
            new_nodes[1],
            TextNode("Only ", TextType.TEXT)
        )

        self.assertEqual(
            new_nodes[2],
            TextNode("this", TextType.ITALIC)
        )

        self.assertEqual(
            new_nodes[3],
            TextNode(" is italic", TextType.TEXT)
        )

