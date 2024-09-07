import unittest
from textnode import (TextNode,text_type_bold,text_type_code,text_type_image,text_type_italic,text_type_link,text_type_text)
from parse_md import split_nodes_delimiter,extract_markdown_images,extract_markdown_links

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

    def test_single_image(self):
        text = "Here is an image ![alt text](https://example.com/image.png)"
        expected = [("alt text", "https://example.com/image.png")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_multiple_images(self):
        text = "![image1](https://example.com/1.png) and ![image2](https://example.com/2.png)"
        expected = [("image1", "https://example.com/1.png"), ("image2", "https://example.com/2.png")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_no_images(self):
        text = "This is text without images."
        expected = []
        self.assertEqual(extract_markdown_images(text), expected)

    def test_no_alt_in_images(self):
        text="![](https://www.boot.dev)"
        expected=[('', 'https://www.boot.dev')]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_single_link(self):
        text = "Here is a [link](https://example.com)"
        expected = [("link", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_multiple_links(self):
        text = "[link1](https://example.com/1) and [link2](https://example.com/2)"
        expected = [("link1", "https://example.com/1"), ("link2", "https://example.com/2")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_no_links(self):
        text = "This is text without links."
        expected = []
        self.assertEqual(extract_markdown_links(text), expected)
    
           

if __name__ == "__main__":
    unittest.main()