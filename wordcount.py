# open file
filename = open("twain.txt")

# create empty dictionary to hold words and counts
word_count = {}

# loop through file reading lines and separate lines into words
for line in filename: 
    words =line.rstrip().split()

    # check if words are already in dictionary, increment by 1
    for word in words:
        word = word.lower()
        word = word.strip(".'?,!\"_-:;")
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

# print key value pairs
for word, count in word_count.iteritems():
    print "%s: %d" % (word, count)

