def string_array(array, searchstr):
    print(array.count(searchstr))

string_array(('banana is an good ann food banana for banana ann'), 'an')




from collections import defaultdict

words = "apple banana apple strawberry banana lemon"

d = defaultdict(int)
for word in words.split():
    d[word] += 1
print(d)




def reverseWordSentence(Sentence):
    return ' '.join(word[::-1] for word in Sentence.split(" ")) 
Sentence = "dog is god subrat is subrat"
print(reverseWordSentence(Sentence))    
