'''

PROBLEM: 

You're given a sentence consisting of words and a dictionary of root words. 
Your task is to find all the words in the sentence whose prefix matches with 
a root word present in the dictionary, and then to replace each matching word 
with the root word.

If a word in a sentence matches more than one root word in the dictionary, 
replace it with the shortest matching root word, and if the word doesn't match 
any root word in the dictionary, leave the word unchanged. Return the modified 
sentence as the output.

---------------
PATTERN: TRIE
---------------

'''





from trie import Trie
from trie_node import TrieNode


def replace_words(sentence, dictionary):

   split_sentence = sentence.split()
   # print("split_sentence:", split_sentence)
   result = []
   trie_dict = create_new_dict(dictionary)

   for word in split_sentence :
      # print("word:", word)
      curr = []
      node = trie_dict
      children  = node.children

      for index, c in enumerate(word) :
         # print("0 - char:", c)
         if c not in children :
            # print("0 - char:", c)
            if index == 0 or not node.end_of_word : 
               result.append(word)
               break
            # print("curr:", curr)
            new_word = "".join(curr)
            result.append(new_word)
            break
         else :
            # print("1 - char:", c)
            curr.append(c) 
            node = children[c]
            children  = node.children
            # print("curr:", curr)

            if node.end_of_word :
               new_word = "".join(curr)
               # print("new_word:", new_word)
               result.append(new_word)
               break

            

         


   return " ".join(result)





def create_new_dict(prefixes) :

   new_trie = Trie()
   
   for prefix in prefixes :
      # print("prefix:", prefix)
      node = new_trie.root
      for c in prefix :
         if c not in node.children :
            new_node = TrieNode()
            node.children[c] = new_node

            node = new_node
         else : node = node.children[c]
      node.end_of_word = True

   return new_trie.root























