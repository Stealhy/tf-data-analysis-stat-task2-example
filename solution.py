import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 144141432 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    import scipy.stats as st
    alpha = 1 - p
    n = np.size(x)
    a = np.sqrt(n*np.mean(x**2)/(34*st.chi2.ppf(1 - alpha / 2, 2*n)))
    b = np.sqrt(n*np.mean(x**2)/(34*st.chi2.ppf(alpha / 2, 2*n)))
    return a, \
           b
