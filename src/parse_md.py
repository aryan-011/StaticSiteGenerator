from textnode import TextNode,text_type_text,text_type_bold,text_type_italic
import re
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    newNodes=[]
    for old_node in old_nodes:
        if(old_node.text_type !=text_type_text):
            newNodes.append(old_node)
            continue
        split_list = old_node.text.split(delimiter)
        if len(split_list) % 2 == 0:
            raise ValueError(f"Unclosed delimiter '{delimiter}' detected in text.")
        for i,value in enumerate(split_list):
            # print(i)
            if value:
                if i%2==0:
                    newNodes.append(TextNode(value,old_node.text_type))
                else :
                    newNodes.append(TextNode(value,text_type))

        return newNodes
    
def extract_markdown_images(text):
    images=[]
    images = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return images

def extract_markdown_links(text):
    links=[]
    links = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    return links

text = "This is text with a ![](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
print(extract_markdown_images(text))
# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
print(extract_markdown_links(text))
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]