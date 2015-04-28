from textblob import TextBlob

text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''
text = '''i am good.
you are bad.
'''
text = 'Avengers was so good! Why kill off my hottie though'
blob = TextBlob(text)
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])
print blob.sentences[0].sentiment.polarity
# 0.060
# -0.341
