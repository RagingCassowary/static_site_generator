from textnode import *
from htmlnode import *
from functions.text_to_textnode import *

def main():
    text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")

print(main())

