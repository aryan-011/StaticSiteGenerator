from textnode import TextNode,text_type_text,text_type_link,text_type_image
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


def split_nodes_link(old_nodes):
    link_pattern = r'\[(.*?)\]\((.*?)\)'

    new_nodes = []

    for node in old_nodes:
        if node.text_type == text_type_text:
            parts = re.split(link_pattern, node.text)

            # print(parts)
            for i in range(0, len(parts), 3):
                if parts[i]:  
                    new_nodes.append(TextNode(parts[i], text_type_text))

                if i + 1 < len(parts):  # Link text
                    new_nodes.append(TextNode(parts[i + 1], text_type_link, parts[i + 2]))
                    
        else:
            new_nodes.append(node)

    return new_nodes

def split_nodes_images(old_nodes):
    link_pattern = r'!\[(.*?)\]\((.*?)\)'

    new_nodes = []

    for node in old_nodes:
        if node.text_type == text_type_text:
            parts = re.split(link_pattern, node.text)

            # print(parts)
            for i in range(0, len(parts), 3):
                if parts[i]:  
                    new_nodes.append(TextNode(parts[i], text_type_text))

                if i + 1 < len(parts):  # Link text
                    new_nodes.append(TextNode(parts[i + 1], text_type_image, parts[i + 2]))
                    
        else:
            new_nodes.append(node)

    return new_nodes

def extract_markdown_images(text):
    images=[]
    images = re.findall(r"!\[(.*?)\]\((.*?)\)",text)
    return images

def extract_markdown_links(text):
    links=[]
    links = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    return links


