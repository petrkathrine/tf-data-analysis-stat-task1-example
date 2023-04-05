import pandas as pd
import numpy as np


chat_id = 140576679 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    x = np.array(list(map(lambda x: x - 627, x)))
    return np.log(np.median(x)) # Ваш ответ
