import matplotlib.pyplot as plt
import pandas as pd

df_12 = pd.read_csv("dados/velocidade_12_do_06_2025.csv")
df_14 = pd.read_csv("dados/velocidade_14_do_06_2025.csv")

plt.figure(figsize=(10, 6))
plt.plot(pd.to_datetime(df_12["DataHora"]), df_12["Download_Mbps"], label="Download 12/06", color="blue")
plt.plot(pd.to_datetime(df_14["DataHora"]), df_14["Download_Mbps"], label="Download 14/06", color="green")
plt.title("Velocidade de Download (Mbps)")
plt.xlabel("Horário")
plt.ylabel("Download")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("scripts/grafico_download.png")
