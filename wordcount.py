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
    word_count[word] = word_count.get(word, 0) + 1  

# create empty dictionary to hold words and counts
word_count = {}
count_words ={}

def main():
    # open file
    filename = open("twain.txt")

    # loop through file reading lines and separate lines into words
    for line in filename: 
        # split line into list of separate words
        words =line.rstrip().split()
        # strip & format words, and add to dictionary with counts
        strip_words(words)

    # loop through existing word:count dictionary to create new dictionary with count:word key:value pairs
    for word, count in word_count.iteritems():
        # add word to list for that count
        count_words[count] = count_words.get(count, []) + [word]

    # create a key_list of the count keys
    count_list = count_words.keys()
    # sort key list
    count_list.sort()
    # reverse key list
    count_list.reverse()
    # loop through key list, and print associated list of words from count_words dictionary
    for count in count_list: 
        print "Words that occur %d times:" % count
        count_words[count].sort()
        for word in count_words[count]:
            print word  


if __name__ == "__main__":
    main()