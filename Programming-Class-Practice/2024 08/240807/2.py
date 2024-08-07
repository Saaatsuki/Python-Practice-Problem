#  `pygame.Rect` 클래스には、衝突を検出するための便利なメソッドがいくつかあります。以下は、`colliderect()`、`collidelist()`、`collidelistall()`の具体的な説明です。

'''
1. **colliderect()**
    - **概要**：2つの `Rect` オブジェクトが衝突しているかどうかを判定します。
    - **使い方**：
        ```python
'''
import pygame
rect1 = pygame.Rect(0, 0, 50, 50)
rect2 = pygame.Rect(25, 25, 50, 50)
collision = rect1.colliderect(rect2)  # Trueを返す
'''
    - **戻り値**：衝突している場合は `True`、していない場合は `False`。

2. **collidelist()**
    - **概要**：複数の `Rect` オブジェクトのリストの中で、少なくとも1つの `Rect` が衝突しているかどうかを判定します。
    - **使い方**：
        ```python
'''
rect = pygame.Rect(0, 0, 50, 50)
rect_list = [pygame.Rect(60, 60, 50, 50), pygame.Rect(10, 10, 50, 50), pygame.Rect(100, 100, 50, 50)]
index = rect.collidelist(rect_list)  # 1を返す（2つ目のRectが衝突しているため）
'''
    - **戻り値**：衝突している最初の `Rect` のインデックスを返し、衝突していない場合は `-1` を返します。

3. **collidelistall()**
    - **概要**：複数の `Rect` オブジェクトのリストの中で、衝突しているすべての `Rect` のインデックスをリストで返します。
    - **使い方**：
        ```python
'''
rect = pygame.Rect(0, 0, 50, 50)
rect_list = [pygame.Rect(60, 60, 50, 50), pygame.Rect(10, 10, 50, 50), pygame.Rect(25, 25, 50, 50)]
indices = rect.collidelistall(rect_list)  # [1, 2]を返す（2つ目と3つ目のRectが衝突しているため）
'''
    - **戻り値**：衝突しているすべての `Rect` のインデックスをリストで返し、衝突していない場合は空のリスト `[]` を返します。

これらのメソッドは、ゲーム内での衝突判定や、特定の領域内でのオブジェクトの検出に非常に役立ちます。
'''