import unittest
from htmlnode import HTMLNode,LeafNode,ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode("div", value="Content", props={"class": "container"})
        expected_repr = 'HTMLNode(tag="div", value="Content", children=[], props={"class": "container"})'
        self.assertEqual(repr(node), expected_repr)

    def test_children(self):
        parent = HTMLNode("ul", children=[
            HTMLNode("li", value="Item 1"),
            HTMLNode("li", value="Item 2")
        ])
        self.assertEqual(len(parent.children), 2)
        self.assertEqual(parent.children[0].tag, "li")
        self.assertEqual(parent.children[0].value, "Item 1")

    def test_leaf_node_to_html(self):
        leaf=LeafNode("p", "This is a paragraph of text.")
        leaf2=LeafNode("a", "Click me!", props={"href": "https://www.google.com"})
        self.assertEqual(leaf.to_html(),'<p>This is a paragraph of text.</p>')
        self.assertEqual(leaf2.to_html(),'<a href="https://www.google.com">Click me!</a>')

    def test_parent_node_without_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div",children=None)

    def test_parent_node_with_value(self):
        with self.assertRaises(ValueError):
            ParentNode("p",value="This is a para")

    def test_parent_node_with_leaf_node_as_children_to_html(self):
        node = ParentNode(
                    "p",
                    children=[
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                )
        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parent_node_with_nested_parent_node_to_html(self):
        node = ParentNode(
                    "div",
                    children=[
                        ParentNode(
                            "p",
                            children=[
                                LeafNode("b", "Bold text"),
                            ],
                        ),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        ParentNode(
                            "p",
                            children=[
                                LeafNode("b", "Bold text"),
                                LeafNode(None, "Normal text"),
                                LeafNode("i", "italic text"),
                                LeafNode(None, "Normal text"),
                            ],
                        ),
                    ],
                )
        self.assertEqual(node.to_html(),"<div><p><b>Bold text</b></p>Normal text<i>italic text</i><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>")


if __name__ == "__main__":
    unittest.main()
