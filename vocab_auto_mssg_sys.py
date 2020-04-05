import fbchat;
from fbchat import Client;
import pandas as pd;
import random;

vocabs = pd.read_csv("vocab_csv.csv")
while True:
    vocab_random = random.randint(0, len(vocabs.index) - 1)
    for index, row in vocabs.iterrows():
        if (index == vocab_random):
            print(row[1])
            print(row[2])
            vocab_question = row[1]
            vocab_answer = row[2]
    class CustomClient(Client):
        def onMessage(self, message_object=None, **kwargs):
            if (message_object.text == vocab_answer):
                client.send(fbchat.models.Message("Correct Answer"), uid)
                if (client.searchForUsers("khateewooda.showvet")[0].uid == message_object.author):
                    client.stopListening()
            else:
                client.send(fbchat.models.Message("No! The answer is " + vocab_answer), uid)
                print(message_object)
                if (client.searchForUsers("khateewooda.showvet")[0].uid == message_object.author):
                    client.stopListening()
            print(message_object.text)
            print(vocab_answer)


    client = CustomClient("utsaha.joshi.7", "bpdn11dspy", vocab_answer)
    friend = client.searchForUsers("khateewooda.showvet")
    uid = friend[0].uid
    client.send(fbchat.models.Message("What is the meaning of " + vocab_question+"?"), uid)
    client.listen()
