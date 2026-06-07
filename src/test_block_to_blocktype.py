import unittest
from blocktype import BlockType
from functions.block_to_blocktype import block_to_blocktype

class TestBlockToBlocktype(unittest.TestCase):

    def test_paragraph_block(self):
        matches = block_to_blocktype(
            "this is just plain text"
        )
        self.assertEqual(
            matches,
            BlockType.PARAGRAPH
        )

    def test_heading_block(self):
        matches = block_to_blocktype(
            "# THIS IS A HEADING"
        )
        self.assertEqual(
            matches,
            BlockType.HEADING
        )

    def test_valid_list_unordered(self):
        matches = block_to_blocktype(
            "- this list\n- is unordered\n- but valid"
        )
        self.assertEqual(
            matches,
            BlockType.UNORDERED_LIST
        )
    
    def test_valid_list_ordered(self):
        matches = block_to_blocktype(
            "1. first item\n2. second item\n3. third item"
        )
        self.assertEqual(
            matches,
            BlockType.ORDERED_LIST
        )
    
    def test_invalid_list_unordered(self):
        self.assertRaises(
            Exception,
            block_to_blocktype,
            "- this item is valid\nbut this one is not"
        )