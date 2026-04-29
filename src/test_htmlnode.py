import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html(self):
        dummy = HTMLNode("h1", "heading", props={"href": "https://www.dummy.com"})

        self.assertEqual(
            dummy.props_to_html(),
            'href="https://www.dummy.com", '
                         )
    
    def test_no_props(self):
        dummy = HTMLNode("p", "paragraph")

        self.assertEqual(dummy.props_to_html(), "")

    
    def test_print(self):
        dummy1 = HTMLNode("p", "paragraph")
        dummy2 = HTMLNode("b", "bold")
        dummy = HTMLNode("h1", "heading", [dummy1, dummy2], {"href": "https://www.dummy.com"})

        self.assertEqual(
            dummy.__repr__(),
            'HTMLNode(h1, heading, children=[paragraph, bold, ], props=[href="https://www.dummy.com", ])'
                         )
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_children_none(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.children, None)
    
    def test_leaf_print(self):
        node = LeafNode("a", "I am a link!", {"href": "https://www.example.link"})
        self.assertEqual(node.__repr__(),
                         'LeafNode(a, I am a link!, props=[href="https://www.example.link", ])'
                         )
    
    
