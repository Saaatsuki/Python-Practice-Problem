import random

def getRandomSample1(argSequence,argK):

    sample_li = []
    argSequence_li = list(argSequence)

    for _ in range(argK):
        index = random.randint(0,len(argSequence_li)-1)
        sample_li.append(argSequence_li.pop(index))
    return sample_li

def getRandomSample2(argSequence,argK):
    if len(argSequence)<argK:
        raise ValueError("エラー")
    
    sample_li = []
    argSequence_li = list(argSequence)

    while len(sample_li)<argK:
        index = random.randint(0,len(argSequence_li)-1)
        random_sel = argSequence_li[index]

        if random_sel not in sample_li:
            sample_li.append(random_sel)
        argSequence_li.remove(random_sel)

    return sample_li