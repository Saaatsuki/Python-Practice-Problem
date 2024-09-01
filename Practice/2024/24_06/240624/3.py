import random

def randomSample(argSequence , argK):
    if len(argSequence)<argK:
        raise ValueError("エラー")
    
    sample = []
    argSequence_copy = argSequence.copy()

    for _ in range(argK):
        index = random.randint(0,len(argSequence_copy)-1)
        sample.append(argSequence_copy.pop(index))
    return sample

li = [num for num in range(25)]
print(randomSample(li,5))