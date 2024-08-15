import json
class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None) -> None:
        self.tag=tag
        self.value=value
        self.children=children if children is not None  else []
        self.props=props if props is not None else {}

    def to_html(self):
        return NotImplementedError

    def __repr__(self):
        props_str = json.dumps(self.props, ensure_ascii=False)
        return f'HTMLNode(tag="{self.tag}", value="{self.value}", children={self.children}, props={props_str})'

    def props_to_html(self):
        return ("").join(f' {key}="{value}"' for key,value in self.props.items())
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        if value is None :
            raise ValueError("Leaf Node requires a value")
        super().__init__(tag, value, children=[], props=props)
    
    def to_html(self):
        if self.tag is None:
            return self.value
        props_str=self.props_to_html()
        # print(props_str)
        return f'<{self.tag}{props_str}>{self.value}</{self.tag}>'
    
class ParentNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        if children is None:
            raise ValueError("Parent Node must have a child")
        if tag is None:
            raise ValueError("Parent Node must have tag")

        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):

        props_str = self.props_to_html()
        children_html = "".join(child.to_html() for child in self.children)
        return f'<{self.tag}{props_str}>{children_html}</{self.tag}>'
