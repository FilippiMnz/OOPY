import numpy as np
# Dados dos tempos para os fornos
forno_a = np.array([40, 40, 46, 42, 43])
forno_b = np.array([39, 43, 45, 37, 49])

# Função para calcular média, desvio padrão e coeficiente de variação (CV)
def calcular_cv(tempos):
    media = np.mean(tempos)
    desvio_padrao = np.std(tempos, ddof=1)  # ddof=1 para amostra
    cv = (desvio_padrao / media) * 100
    return media, desvio_padrao, cv

# Calcular métricas par Forno A e Forno 
media_a, desvio_a, cv_a = calcular_cv(forno_a)
media_b, desvio_b, cv_b = calcular_cv(forno_b)

(media_a, desvio_a, cv_a), (media_b, desvio_b, cv_b)

