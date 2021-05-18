

def listSample(lstInput, seed=1, selectionSize=5):
    # select a random sample without replacement
    import random

    random.seed(seed)
    # seed random number generator
    # select a subset without replacement

    subset = random.sample(set(lstInput), selectionSize)
    print(list(subset))

    return list(subset)
