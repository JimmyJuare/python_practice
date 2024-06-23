from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_duplicate_subtrees(root):
    def serialize(node):
        if not node:
            return "#"
        serial = "{},{},{}".format(node.val, serialize(node.left), serialize(node.right))
        count[serial] += 1
        if count[serial] == 2:
            duplicates.append(node)
        return serial
    
    count = defaultdict(int)
    duplicates = []
    serialize(root)
    return duplicates

# Example usage
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4))
root.right = TreeNode(3, TreeNode(2, TreeNode(4)), TreeNode(4))

duplicates = find_duplicate_subtrees(root)
print([node.val for node in duplicates])  # Output: [2, 4]
