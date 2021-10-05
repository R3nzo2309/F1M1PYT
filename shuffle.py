import random

original = input("type a word to shuffle: ")
randomised = ''.join(random.sample(original, len(original)))
print(randomised)
woord = input("type a word to shuffle: ")
randomised = ''.join(random.sample(woord, len(woord)))
print(randomised)
order = input("type a word to shuffle: ")
randomised = ''.join(random.sample(order, len(order)))
print(randomised)
recover = input("type Return to restore the word: ")
if recover == "Return" or recover == "return":
    print(original +" " + woord +" " + order)
