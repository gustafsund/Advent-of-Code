class Node:
    def __init__(self,value):
        self.children = None
        self.value = value
        
        
class Tree:
    
    def create_node(self,data):
        return Node(data)
    
    # def insert