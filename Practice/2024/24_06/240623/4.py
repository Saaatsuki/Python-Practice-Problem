import random

def getRandomSample(population, 個数):
    if 個数 > len(population):
        raise ValueError("Sample size cannot be larger than population size")
    
    sample = []
    population_copy = list(population)  # 元のリストを変更しないためにコピーを作成
    
    for _ in range(個数):
        index = random.randint(0, len(population_copy) - 1)
        sample.append(population_copy.pop(index))

    return sample

# テスト用の例
if __name__ == "__main__":
    population = [1, 2, 3, 4, 5]
    k = 3
    print(getRandomSample(population, k))  # 例: [4, 1, 5]


def getRandomSample(population, 個数):
    if 個数 > len(population):
        raise ValueError("Sample size cannot be larger than population size")
    
    sample = []
    population_copy = list(population)  # 元のリストを変更しないためにコピーを作成
    
    while len(sample) < 個数:
        index = random.randint(0, len(population_copy) - 1)
        selected_element = population_copy[index]
        
        # 選ばれた要素がすでにサンプルに含まれていないかを確認
        if selected_element not in sample:
            sample.append(selected_element)
        
        # 選ばれた要素を元のリストから削除
        population_copy.remove(selected_element)
    
    return sample

# テスト用の例
if __name__ == "__main__":
    population = [1, 2, 3, 4, 5]
    k = 3