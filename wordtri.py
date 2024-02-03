from typing import List


def insert(data, s: str)-> None:
    if s == "":
        return
    if len(s) == 1:
        if s in data:
            data[s][1] = True
        else:
            data[s] = [{}, True]
    if s[0] in data:
        insert(data[s[0]][0], s[1:])
    else:
        data[s[0]]= [{}, False]
        insert(data[s[0]][0], s[1:])

def count_words(data)->int:
    """
    Returns the number of words encoded in data. You may assume
    data is a valid trie.
    """
    sum = 0
    if len(data) == 0:
        return sum
    for key in data:
        sum += count_words(data[key][0])
        if data[key][1]:
            sum += 1
    return sum




def contains(data, s: str)-> bool:
    """
    Returns True if and only if s is encoded within data. You may
    assume data is a valid trie.
    """
    if s == "":
        return True
    if s[0] not in data:
        return False
    if len(s) == 1:
        return data[s][1]
    return contains(data[s[0]][0],s[1:])



def height(data)->int:
    """
    Returns the length of longest word encoded in data. You may
    assume that data is a valid trie.
    """
    if data == {}:
        return 0
    L = []
    for key in data:
        if data[key] == [{}, False]:
            L.append(height(data[key][0]))
        else:
            L.append(1 + height(data[key][0]))
    return max(L)


    

def count_from_prefix(data, prefix: str)-> int:
    """
    Returns the number of words in data which starts with the string
    prefix, but is not equal to prefix. You may assume data is a valid
    trie.
    """
    if prefix == "":
        return count_words(data)
    elif prefix[0] in data:
        return count_from_prefix(data[prefix[0]][0],prefix[1:])
    else:
        return 0



def get_suggestions(data, prefix:str)-> List[str]:
    """
    Returns a list of words which are encoded in data, and starts with
    prefix, but is not equal to prefix. You may assume data is a valid
    trie.
    """
    def add_to_each(L, s):
        n = []
        for i in range(len(L)):
            n.append(s + L[i])
        return n
    L = [] 
    if data == {}:
        return []
    if prefix != "":
        if prefix[0] not in data:
            return []
        return add_to_each(get_suggestions(data[prefix[0]][0],prefix[1:]), prefix[0])
    for key in data:
        if data[key][1]:
            L += [key]
        L += add_to_each(get_suggestions(data[key][0],prefix), key)
    return L




