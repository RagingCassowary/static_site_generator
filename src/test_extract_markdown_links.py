import unittest
from functions.extract_markdown_links import *

class TestExtractLinks(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.site)"
        )
        self.assertListEqual([("link", "https://example.site")], matches)

    def test_link_isolation(self):
        matches = extract_markdown_links(
            "This is a [link](https://example.site) and this is an ![image](https://image.img)"
        )
        self.assertListEqual([("link", "https://example.site")], matches)
    
    def test_image_isolation(self):
        matches = extract_markdown_images(
            "This is a [link](https://example.site) and this is an ![image](https://image.img)"
        )
        self.assertListEqual([("image", "https://image.img")], matches)
    
    def test_no_links(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)
    
    def test_multiple_links(self):
        matches = extract_markdown_links(
            "This is a [link](https://example.site) and this is a [second link](https://link.web)"
        )
        self.assertListEqual([("link", "https://example.site"), ("second link", "https://link.web")], matches)