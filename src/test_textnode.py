import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_no_url(self):
        node = TextNode("This is a link", TextType.LINK)
        self.assertEqual(node.url, None)

    def test_print(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node.__repr__(), "TextNode(This is a text node, text, None)")
    
    def test_enum(self):
        node = TextNode("This is an image node", "image")
        self.assertEqual(node.text_type, TextType.IMAGE)


if __name__ == "__main__":
    unittest.main()