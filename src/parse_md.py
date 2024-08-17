from textnode import TextNode,text_type_text,text_type_bold,text_type_italic

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


node = TextNode("**bold** and *italic*", text_type_text)
new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
print(new_nodes)