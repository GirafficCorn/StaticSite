from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *

def main():
    Test_Object = TextNode("anchor text", TextType.LINK, "https://www.boot.dev")
    print(Test_Object.__repr__())


main()