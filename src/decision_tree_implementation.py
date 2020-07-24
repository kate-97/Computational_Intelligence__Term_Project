
class NodeInDecisionTree:
    def __init__(self):
        content = 0 # Which question.
        node_type = 'T'  # type of node: 'T' if it's test, 'X' if it's recognized object
        left_child = None
        right_child = None

    def __str__(self):
        string_content = "- Node content: " + self.content
        string_content += " , Node type: " + self.node_type
        return string_content


class DecisionTree:
    def __init__(self):
        content = NodeInDecisionTree() # nodes in decision tree
        depth = 0     # current depth of decision tree
        p_current_sum = 0 # utility information used for updating tree depth
        p_current_last_member = 1 # utility information used for updating current sum

    # TODO: Implement method for classification instances!
    # NOTE: It works with LISTS like instances!
    def classify(self, instance):
        current_node = self.content

        while current_node.node_type == 'T':
            if instance[current_node.content] == 0:
                current_node = current_node.left_child
            elif instance[current_node.content] == 1:
                current_node = current_node.right_child

        if current_node.node_type == 'X':
            return current_node.content

        else:
            return -1

    def __str__(self):
        string_content = "** Depth of decision tree: " + self.depth
        return string_content



