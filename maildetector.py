import pickle as c
import os
import sklearn 
from collections import Counter
import easyimap as e

passw="SUSHMAemail0311"
user="sushmabalankl@gmail.com"
server=e.connect("imap.gmail.com",user,passw)
server.listids()
print(server.listids())
email=server.mail(server.listids()[0])


def load(clf_file):
    #fileof = open(clf_file,encoding='cp437')
    with open(clf_file,'rb',buffering=0) as fp:
        clf = c.load(fp)
    return clf


def make_dict():
    direc = "emails/"
    files = os.listdir(direc)
    emails = [direc + email for email in files]
    words = []
    c = len(emails)

    for email in emails:
        f = open(email,encoding='cp437')
        blob = f.read()
        words += blob.split(" ")
        print(c)
        c -= 1

    for i in range(len(words)):
        if not words[i].isalpha():
            words[i] = ""

    dictionary = Counter(words)
    del dictionary[""]
    return dictionary.most_common(3000)


clf = load("spam-classifier.mdl")
d = make_dict()

ch=email.body
#ch="i hope you enjoted the dinner last night?"
#chr=str(email.body)
print(ch)
while True:
    features = []
    
    inp = ch.split()
    if inp[0] == "exit":
        break
    for word in d:
        features.append(inp.count(word[0]))
    res = clf.predict([features])
    print(["Not Spam", "Spam!"][res[0]])
    break