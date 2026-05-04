import unittest
from functions.text_to_html import text_node_to_html_node
from textnode import TextNode, TextType

class TestTextToHTML(unittest.TestCase):


    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("I am a link", TextType.LINK, url="example.link")
        html_node = text_node_to_html_node(node)
        self.assertEqual(
            html_node.to_html(),
            '<a href="example.link">I am a link</a>'
        )
