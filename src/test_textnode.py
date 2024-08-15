import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text", "bold")
        self.assertNotEqual(node, node2)
    def test_different_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)
    def test_url_none(self):
        node = TextNode("This is a text node", "bold","www.boot.dev")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node_to_html_node_for_plain_text(self):
        node = TextNode("This is a plain text", "text")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a plain text")
        self.assertEqual(html_node.props, {})

    def test_text_node_to_html_node_for_bold_text(self):
        node = TextNode("Bold text", "bold")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")
        self.assertEqual(html_node.props, {})

    def test_text_node_to_html_node_for_italic_text(self):
        node = TextNode("Italic text", "italic")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")
        self.assertEqual(html_node.props, {})

    def test_text_node_to_html_node_for_code_text(self):
        node = TextNode("Code snippet", "code")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code snippet")
        self.assertEqual(html_node.props, {})

    def test_text_node_to_html_node_for_link(self):
        node = TextNode("Click here", "link", url="https://www.example.com")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props, {"href": "https://www.example.com"})

    def test_text_node_to_html_node_for_image(self):
        node = TextNode("Alt text", "image", url="https://www.example.com/image.png")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": "https://www.example.com/image.png","alt": "Alt text"})

    def test_text_node_to_html_node_with_invalid_text_type(self):
        node =TextNode("Invalid text", text_type="unsupported_type")
        with self.assertRaises(ValueError):
            node.text_node_to_html_node()



if __name__ == "__main__":
    unittest.main()