from textnode import TextNode
from htmlnode import HTMLNode

def main():
    # create objects of the classes imported above
    node = TextNode("this is a test text node", "bold", "https://www.boot.dev")
    html_n = HTMLNode("a", "test value", None, None)
    # print objects of the classes above
    print(node)
    print(html_n)

if __name__ == "__main__":
    main()