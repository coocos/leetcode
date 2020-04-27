import unittest
import json
from typing import Dict

from leetcode.common import TreeNode


class Codec:
    """
    This solution serializes the binary tree by doing a depth-first
    recursive traversal of the tree and building a dictionary which
    looks like this

    {
        "l1": {
            "l2": {
                "l4": {}
            },
            "r3": {}
        }
    }

    and where the prefix indicates whether the node is the left or
    the right child of its parent. Once the dictionary is built, it's
    dumped into JSON.

    Deserialization is done by first deserializing the JSON into a
    dictionary. Then the dictionary is recursively traversed through and
    nodes are created as the traversal progresses. A fake root is used
    to kickstart the recursion.
    """
    def serialize(self, root: TreeNode) -> str:

        def tree_as_dict(node: TreeNode, parent: Dict, prefix: str) -> Dict:
            """Converts the tree into a dictionary"""
            if not node:
                return {}

            children: Dict[str, Dict] = {}
            parent[f'{prefix}{node.val}'] = children

            if node.left:
                tree_as_dict(node.left, children, 'l')
            if node.right:
                tree_as_dict(node.right, children, 'r')

            return parent

        return json.dumps(tree_as_dict(root, {}, 'l'))

    def deserialize(self, data: str) -> TreeNode:

        def dict_as_tree(tree: Dict, node: TreeNode) -> TreeNode:
            """Converts the dictionary into a tree"""
            for value, children in tree.items():
                if value[0] == 'l':
                    node.left = TreeNode(int(value[1:]))
                    dict_as_tree(children, node.left)
                else:
                    node.right = TreeNode(int(value[1:]))
                    dict_as_tree(children, node.right)

            return node

        fake_root = TreeNode(None)
        return dict_as_tree(json.loads(data), fake_root).left


class TestCodec(unittest.TestCase):

    def test_serializing(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        serialized = '{"l1": {"l2": {}, "r3": {"l4": {}, "r5": {}}}}'
        self.assertEqual(Codec().serialize(root), serialized)

    def test_serializing_just_root(self):

        root = TreeNode(1)
        self.assertEqual(Codec().serialize(root), '{"l1": {}}')

    def test_deserializing(self):

        serialized = '{"l1": {"l2": {}, "r3": {"l4": {}, "r5": {}}}}'
        root = Codec().deserialize(serialized)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertIsNone(root.left.left)
        self.assertIsNone(root.left.right)
        self.assertEqual(root.right.val, 3)
        self.assertEqual(root.right.left.val, 4)
        self.assertEqual(root.right.right.val, 5)

    def test_deserializing_empty_tree(self):

        root = Codec().deserialize('{}')
        self.assertIsNone(root)

    def test_serializing_empty_tree(self):
        self.assertEqual(Codec().serialize(None), '{}')

    def test_deserializing_just_root(self):

        root = Codec().deserialize('{"l1": {}}')
        self.assertEqual(root.val, 1)

    def test_simple_tree(self):

        original_root = TreeNode(1)
        original_root.left = TreeNode(2)

        serialized = Codec().serialize(original_root)
        self.assertEqual(serialized, '{"l1": {"l2": {}}}')

        root = Codec().deserialize(serialized)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertIsNone(root.right)

    def test_left_leaning_tree(self):

        original_root = TreeNode(1)
        original_root.left = TreeNode(2)
        original_root.left.left = TreeNode(3)
        original_root.left.left.left = TreeNode(4)
        original_root.left.left.left.left = TreeNode(5)

        serialized = '{"l1": {"l2": {"l3": {"l4": {"l5": {}}}}}}'
        self.assertEqual(Codec().serialize(original_root), serialized)

        root = Codec().deserialize(serialized)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.left.left.val, 3)
        self.assertEqual(root.left.left.left.val, 4)
        self.assertEqual(root.left.left.left.left.val, 5)
