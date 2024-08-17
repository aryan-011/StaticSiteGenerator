import unittest
from textnode import (TextNode,text_type_bold,text_type_code,text_type_image,text_type_italic,text_type_link,text_type_text)
from parse_md import split_nodes_delimiter

class TestParsing(unittest.TestCase):
    def test_code_parse(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        expected_nodes = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ]
        for i, node in enumerate(new_nodes):
            self.assertEqual(node.text, expected_nodes[i].text)
            self.assertEqual(node.text_type, expected_nodes[i].text_type)

    def test_bold_parse(self):
        node = TextNode("This is text with a **code block** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        expected_nodes = [
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_bold),
            TextNode(" word", text_type_text),
        ]
        for i, node in enumerate(new_nodes):
            self.assertEqual(node.text, expected_nodes[i].text)
            self.assertEqual(node.text_type, expected_nodes[i].text_type)
    
    def test_raiseException(self):
        with self.assertRaises(ValueError):
            node = TextNode("This is text with a **code block word", text_type_text)
            new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
            
    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", text_type_text
        )
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded word", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("italic", text_type_italic),
            ],
            new_nodes,
        )
           

if __name__ == "__main__":
    unittest.main()