def strip_words(word_list):
    for word in word_list:
        word = word.upper()
        word = word.strip(".'?,!\"_-:;*()")

        if "--" in word:
            more_words = word.split("--")
            strip_words(more_words)
        else:
            add_word_to_dictionary(word)

def add_word_to_dictionary(word):
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# open file
filename = open("twain.txt")

# create empty dictionary to hold words and counts
word_count = {}

# loop through file reading lines and separate lines into words
for line in filename: 
    # split line into list of separate words
    words =line.rstrip().split()
    # strip & format words, and add to dictionary with counts
    strip_words(words)

# get items (count values) from word_count
item_list = word_count.values()

# remove duplicates & sort from highest to lowest
item_list = list(set(item_list))
item_list.sort()
item_list.reverse()

# iterate over item list of word count values
for value in item_list:
    key_list_for_value = []
    print "***********************"
    print "Words that occur %d times:" % value
    # print key/value pairs with that value
    for word, count in word_count.iteritems():
        if count == value:
            key_list_for_value.append(word)
    key_list_for_value.sort()
    
    # print formatted list of words for this value
    for word in key_list_for_value: 
        print word 
