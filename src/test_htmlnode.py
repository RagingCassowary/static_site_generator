import unittest

from htmlnode import HTMLNode

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
    
    
