# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

# Censor a word or phrase in a piece of text.
def censor_word(text,word):
    censor = ""
    # Make the sensor the same length as the original word (incl spaces).
    for letter in word:
        if letter == " ":
            censor += " "
        else:
            censor += "#"
    result = text.replace(word,censor)
    return result

# Censor a full list of words in a piece of text.
def censor_text(text,wordlist):
    result = text
    for word in wordlist:
        result = censor_word(result,word)
    return result

# Clean undesirable words from a list only if they appear more than twice.
def clean_text(text,wordlist):
    result = text
    textlist = text.split()
    wordcount = 0
    # Iterate though words to see if they occur in the list and check wordcount.
    for word in textlist:
        if word in wordlist and wordcount < 2:
            wordcount += 1
        elif word in wordlist and wordcount >= 2:
            result = censor_word(result,word)
    return result

# Censor a list of words from text, including the word before and after each word form the list.
def deep_censor(text,wordlist):
    result = text
    textlist = text.split()
    i = 0
    for i in range(0,len(textlist)-1):
        if textlist[i] in wordlist:
            textlist[i] = censor_word(textlist[i],textlist[i])
            textlist[i-1] = censor_word(textlist[i-1],textlist[i-1])
            textlist[i+1] = censor_word(textlist[i+1],textlist[i+1])
    result = ' '.join(textlist)
    return result

# Censor email one.
email_one_censored = censor_word(email_one,"learning algorithms")

# Censor email two.
email_two_censored = censor_text(email_two,proprietary_terms)

# Censor email three.
email_three_censored = clean_text(email_three,negative_words)
email_three_censored = censor_text(email_three_censored,proprietary_terms)

# Censor email four.
email_four_censored = deep_censor(email_four,negative_words)
email_four_censored = deep_censor(email_four_censored,proprietary_terms)
