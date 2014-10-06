# open file
filename = open("twain.txt")

# create empty dictionary to hold words and counts
word_count = {}

# loop through file reading lines and separate lines into words
for line in filename: 
    words =line.rstrip().split()

    # check if words are already in dictionary, increment by 1
    for word in words:
        word = word.upper()
        word = word.strip(".'?,!\"_-:;*()")

        # split words more - separate those containing --
        if "--" in word:
            more_words = word.split("--")
            for word in more_words:
                word = word.strip(".'?,!\"_-:;*()")
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        else:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

# get items (count values) from word_count
item_list = word_count.values()

# remove duplicates & sort from highest to lowest
item_list = list(set(item_list))
item_list.sort()
item_list.reverse()

# iterate
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
