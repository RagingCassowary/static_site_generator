from textnode import *
from htmlnode import *

def main():
    dummyText = TextNode("Dummy anchor", "link", "https://wwww.fakelink.abc")
    dummychild = HTMLNode("p", "paragraph")
    dummyHTML = HTMLNode("h1", "heading", [dummychild], {"href": "https://www.dummy.com"})
    return dummyText, dummyHTML

print(main())

