"""Generate Markov text from text files."""

import random
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open(file_path)
    file = file.read()


    return file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    text_list = text_string.split() 
    text_list.append(None)

    # your code goes here
    for word in range(len(text_list) - 2):
        key = (text_list[word], text_list[word+1])
        value = text_list[word+2]

        #chains[key] = [value]
        chains[key] = chains.get(key, [])
        chains[key].append(value)




    return chains

        

    #return chains


def make_text(chains):
    """Return text from chains."""

    keys = choice(list(chains.keys()))
    words = [keys[0], keys[1]]
    word = choice(chains[keys])

    # your code goes here
    while word is not None:
        # if keys == ('I', 'am?'):
        #     return False
        keys = (keys[1], word)
        words.append(word)
        word = choice(chains[keys])

            

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
