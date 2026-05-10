import unittest
from functions.text_to_textnode import *
from textnode import *

class TestTextToTextNode(unittest.TestCase):

    def test_text_splits_all(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            nodes,
            [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
            ]
        )
    
    def test_plain_text(self):
        nodes = text_to_textnodes("This is a single text string.")
        self.assertListEqual(
            nodes,
            [TextNode("This is a single text string.", TextType.TEXT)]
        )
    
    def test_empty_string(self):
        nodes = text_to_textnodes("")
        self.assertListEqual(
            nodes,
            []
        )