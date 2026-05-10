import unittest

from functions.split_nodes import *
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

class TestSplitNodesImage(unittest.TestCase):

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_ignore_links(self):
        node = TextNode(
            "This is an [image](https://notanimage.link)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [node],
            new_nodes
        )
    
    def test_sandwiched_image(self):
        node = TextNode(
            "This ![image](https://image.img) is sandwiched in text.",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://image.img"),
                TextNode(" is sandwiched in text.", TextType.TEXT)
            ],
            new_nodes
        )
    
    def test_duplicate_images(self):
        node = TextNode(
            "This ![image](https://image.img) is the same as this ![image](https://image.img)",
            TextType.TEXT
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://image.img"),
                TextNode(" is the same as this ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://image.img"),
            ],
            new_nodes
        )

class TestSplitNodesLink(unittest.TestCase):

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://example.link) and another [second link](https://link.web)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.link"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://link.web"
                ),
            ],
            new_nodes,
        )
    
    def test_ignore_images(self):
        node = TextNode(
            "This is a ![link](https://image.img)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [node],
            new_nodes
        )
    
    def test_sandwiched_link(self):
        node = TextNode(
            "This [link](https://link.web) is sandwiched in text.",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://link.web"),
                TextNode(" is sandwiched in text.", TextType.TEXT)
            ],
            new_nodes
        )
    
    def test_multiple_nodes(self):
        old_nodes = [
            TextNode("I am a [link](https://example.link)", TextType.TEXT),
            TextNode("But I am a [different link](https://example2.link)", TextType.TEXT)
        ]
        new_nodes = split_nodes_link(old_nodes)
        self.assertEqual(
            [
                TextNode("I am a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://example.link"),
                TextNode("But I am a ", TextType.TEXT),
                TextNode("different link", TextType.LINK, "https://example2.link"),
            ],
            new_nodes
        )