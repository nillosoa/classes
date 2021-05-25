import matplotlib.pyplot as plt
import pandas as pd

data = [
    { "name": "Nick", "jan_ir": 124, "feb_ir": 100, "mar_ir": 165 },
    { "name": "Panda", "jan_ir": 112, "feb_ir": 143, "mar_ir": 3 }
]

raw_data = {
    "names": ["Nick", "Panda", "&", "Ari", "Vales"],
    "jan_ir": [143, 122, 101, 106, 365],
    "feb_ir": [122, 132, 144, 98, 62],
    "mar_ir": [65, 88, 12, 32, 65]
}

df = pd.DataFrame(raw_data, columns=["names", "jan_ir", "feb_ir", "mar_ir"])
df["total_ir"] = df["jan_ir"] + df["feb_ir"] + df["mar_ir"]

print(df)