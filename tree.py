class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode) -> str:
        def helper(node):
            if node:
                vals.append(str(node.val))
                helper(node.left)
                helper(node.right)
            else:
                vals.append('#')
        
        vals = []
        helper(root)
        return ' '.join(vals)

    def deserialize(self, data: str) -> TreeNode:
        def helper():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node
        
        vals = iter(data.split())
        return helper()

# Example Usage
# Serialize and deserialize example:
codec = Codec()
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
serialized = codec.serialize(root)
print(serialized)  # Output: "1 2 # # 3 4 # # 5 # #"
deserialized = codec.deserialize(serialized)
