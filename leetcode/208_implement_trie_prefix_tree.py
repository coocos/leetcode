import unittest

from typing import Dict


class TrieNode:
    """
    A node in the prefix tree / trie.

    If terminal is true then the node is the final node in a
    character sequence.
    """
    def __init__(self, terminal: bool = False) -> None:

        self.children: Dict[str, 'TrieNode'] = {}
        self.terminal = terminal


class Trie:
    """
    A simple prefix tree implementation using a tree of nodes
    which all contain a dictionary and a boolean flag.
    """
    def __init__(self):

        self._root = TrieNode()

    def insert(self, word: str) -> None:

        node = self._root

        for character in word:

            if character in node.children:
                node = node.children[character]
            else:
                node.children[character] = TrieNode()
                node = node.children[character]

        node.terminal = True

    def search(self, word: str) -> bool:

        node = self._root

        for character in word:
            try:
                node = node.children[character]
            except KeyError:
                return False

        return node.terminal

    def startsWith(self, prefix: str) -> bool:

        node = self._root

        for character in prefix:
            try:
                node = node.children[character]
            except KeyError:
                return False

        return True


class TestTrie(unittest.TestCase):

    def test_search_when_word_exists(self):

        trie = Trie()
        trie.insert('apple')
        self.assertTrue(trie.search('apple'))

    def test_search_when_word_does_not_exist(self):

        trie = Trie()
        trie.insert('apple')
        self.assertFalse(trie.search('pear'))

    def test_prefix_search(self):

        trie = Trie()
        trie.insert('apple')
        self.assertFalse(trie.search('app'))
        self.assertTrue(trie.startsWith('app'))
