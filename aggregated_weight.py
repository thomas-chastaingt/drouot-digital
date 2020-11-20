#define the node
class Node():
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.children = []

#instance of the five nodes
node_1 = Node(1, 5)
node_2 = Node(2, 10)
node_3 = Node(3, 60)
node_4 = Node(4, 10)
node_5 = Node(4, 5)
node_id = 1

#add childs to nodes
node_1.children = [node_2, node_3,]
node_3.children = [node_5]
node_5.children = [node_5]

#nodes is the list of node
nodes = [node_1, node_2, node_3, node_4, node_5]

#define the method which permits to return the root value and childrens value
def aggregated_weight(nodes, node_id):
    result = 0
    for node in nodes:
        if node.id == node_id:
            result += node.value
            for child in node.children:
                result += child.value
    print(result)
    return result
    

aggregated_weight(nodes, node_id)