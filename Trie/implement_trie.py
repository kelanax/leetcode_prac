'''

PROBLEM: 

Trie is a tree-like data structure used to store strings. The tries are also called 
prefix trees because they provide very efficient prefix matching operations. 

Implement a trie data structure with three functions that perform the following 
tasks:

- Insert a string.
- Search a string.
- Search for a given prefix in a string.

---------------
PATTERN: TRIE
---------------

'''



from trie_node import *


class Trie():
    def __init__(self):
        self.root = TrieNode()
        pass
    
    def insert(self, string):
        node = self.root
        for c in string :
            if c not in node.children :
                new_node = TrieNode()
                node.children[c] = new_node
                node = new_node
            else : node = node.children[c]
        
        node.is_word = True


    
    def search(self, string):

        node = self.root
        for c in string : 
            if c not in node.children : return False
            else :
                node = node.children[c]
        return node.is_word


    
    def search_prefix(self, prefix):
        node = self.root
        for c in prefix : 
            if c not in node.children : return False
            else :
                node = node.children[c]
        return True

        pass



'''


from trie_node import *

class Trie():
    def __init__(self):
        self.root = TrieNode()

    # inserting string in trie
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children.get(c)
        node.is_word = True  

    # searching for a string
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children.get(c)
        return node.is_word

    def search_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children.get(c)
        return True



'''









