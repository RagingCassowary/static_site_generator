import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html(self):
        dummy = HTMLNode("h1", "heading", props={"href": "https://www.dummy.com"})

        self.assertEqual(
            dummy.props_to_html(),
            'href="https://www.dummy.com"'
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
            'HTMLNode(h1, heading, children=[paragraph, bold, ], props=[href="https://www.dummy.com"])'
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
                         'LeafNode(a, I am a link!, props=[href="https://www.example.link"])'
                         )
    
    def test_leaf_link(self):
        node = LeafNode("a", "I am a link!", {"href": "https://www.example.link"})
        self.assertEqual(node.to_html(),
                         '<a href="https://www.example.link">I am a link!</a>'
                         )
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_mult_children(self):
        child1 = LeafNode(value="HEADING")
        grandchild1 = LeafNode(value="This should be plain text, but")
        grandchild2 = LeafNode("a", "this", {"href": "https://www.example.link"})
        grandchild3 = LeafNode(value="should be a link.")
        child2 = ParentNode("p", [grandchild1, grandchild2, grandchild3])
        

        parent = ParentNode("h1", [child1, child2])

        self.assertEqual(
            parent.to_html(),
            '<h1>HEADING<p>This should be plain text, but<a href="https://www.example.link">this</a>should be a link.</p></h1>'
        )
