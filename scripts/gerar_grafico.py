import pandas as pd
import matplotlib.pyplot as plt

# Carrega o arquivo CSV (você pode alterar o caminho)
df = pd.read_csv("dados/velocidade_14_do_06_2025.csv")
df.columns = ["DataHora", "Download_Mbps", "Upload_Mbps", "Ping_ms"]
df["DataHora"] = pd.to_datetime(df["DataHora"])

# Cria gráfico
plt.figure(figsize=(12, 6))
plt.plot(df["DataHora"], df["Download_Mbps"], label="Download (Mbps)", color="blue")
plt.plot(df["DataHora"], df["Upload_Mbps"], label="Upload (Mbps)", color="green")
plt.plot(df["DataHora"], df["Ping_ms"], label="Ping (ms)", color="red")

plt.title("Desempenho da Conexão em 14/06/2025")
plt.xlabel("Horário")
plt.ylabel("Medição")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Salva imagem
plt.savefig("scripts/grafico_14_junho_2025.png")
print("Gráfico gerado com sucesso!")

