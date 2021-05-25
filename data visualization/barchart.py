
import matplotlib.pyplot as plt
import numpy as np

col_count = 3

korea_scores = (554, 536, 538)
canada_scores = (518, 523, 525)
china_scores = (613, 570, 580)
france_scores = (495, 505, 499)

index = np.arange(col_count)

k1 = plt.bar(
    index, korea_scores, .5)
plt.grid(True)

plt.show()