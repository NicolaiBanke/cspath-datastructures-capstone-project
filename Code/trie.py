from data import types

class TrieNode:
  def __init__(self, value=None, end=False):
    self.value = value
    #maps a letter to a node containing that letter
    self.children = {}
    #a node is marked with True if it represents the end of a word even if it is not the end of a branch
    self.end = end
  
  def __repr__(self, level=0):
    # HELPER METHOD TO PRINT TRIE!
    ret = "--->" * level + repr(self.value) + "\n"
    for child in self.children:
      ret += self.children[child].__repr__(level+1)
    return ret
    
  def add_child(self, child_string, child_node):
    if not isinstance(child_node, TrieNode):
      return "child_node must be instance of TrieNode"
    self.children[child_string] = child_node
    
  def get_children(self):
    return self.children
  
  def get_value(self):
    return self.value

class Trie:
  def __init__(self, root_value = None):
    self.root = TrieNode(root_value)
    #this attribute is filled up by the .suggest() method below but included here for easier access
    self.words = []
  
  def get_root(self):
    return self.root
  
  def insert(self, word):
    #the word argument is a word given as a string so that each letter becomes a node in the trie
    current_node = self.get_root()
    while word:
      current_children = current_node.get_children()
      if word[0] not in current_children:
        current_children[word[0]] = TrieNode(word[0])
        current_node = current_children[word[0]]
      else:
        current_node = current_children[word[0]]
      word = word[1:]
    #when the word has been inserted, the node representing the last letter is marked as the end of a word
    current_node.end = True
  
  def make_trie(self, data):
    for datum in data:
      self.insert(datum)
  
  def search(self, word):
    #returns True or False based on whether the word has been found in the trie
    node = self.get_root()
    found = True
    while word:
      if not word[0] in node.children:
        found = False
        break
      node = node.children[word[0]]
      word = word[1:]
    return node and node.end and found
  
  def suggest(self, node, word):
    #recursive function where the base case is reached when a node represents the end of a word. The attribute self.words is filled with words with the prefix matching the word argument
    if node.end:
      self.words.append(word)
    for key, value in node.get_children().items():
      self.suggest(value, word + key)
  
  def return_suggestions(self, check):
    node = self.get_root()
    not_found = False
    temp_word = ''
    
    while check:
      letter = check[0]
      if not letter in node.children:
        not_found = True
        break
      
      temp_word += letter
      node = node.children[letter]
      check = check[1:]
    
    if not_found:
      return 0
    elif node.end and not node.children:
      return -1
    
    self.suggest(node, temp_word)
  
  def reset_words(self):
    #resets the list of words generated in .suggest()
    self.words = []
