# Import package
import wikipediaapi
import re
import difflib

# CALLS THE PAGE BY PAGE TITLE
wiki = wikipediaapi.Wikipedia('en')
wiki1 = wiki.page('anime')          
wiki2 = wiki.page('dragon ball')

# EXTRACT THE TEXT FROM THE WIKI PAGE
# original text
text1 = wiki1.text;
text1 = re.sub(r'==.*?==+', '', text1)  # take any "" out
text1 = text1.replace('\n', '')         # take out all \n
textOriginal = text1.split(' ');        # splits the text into an array of words
# other text to be considered
text2 = wiki2.text;
text2 = re.sub(r'==.*?==+', '', text2)  # take any "" out
text2 = text2.replace('\n', '')         # take out all \n
textOther = text2.split(' ');           # splits the text into an array of words

# COMPARE THE TWO TEXTS, WORD BY WORD
matcher = difflib.SequenceMatcher(a=textOriginal, b=textOther)
print("\nMatching Sequences:")
counter = 0;
for match in matcher.get_matching_blocks():
    counter = counter+1;
    print("Match             : {}\n".format(match))
    print("Matching Sequence : {}\n".format(textOriginal[match.a:match.a+match.size]))
print("There are {} matching phrases or words\n".format(counter))
