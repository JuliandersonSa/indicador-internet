import os
import speedtest
import csv
from datetime import datetime

# Diretório do próprio script (pasta onde ele está)
dir_script = os.path.dirname(os.path.abspath(__file__))
arquivo_csv = os.path.join(dir_script, "velocidade.csv")

st = speedtest.Speedtest()
st.download()
st.upload()

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
download_speed = round(st.results.download / 1_000_000, 2)
upload_speed = round(st.results.upload / 1_000_000, 2)
ping = st.results.ping

existe = os.path.isfile(arquivo_csv)

with open(arquivo_csv, "a", newline="") as file:
    writer = csv.writer(file)
    if not existe:
        writer.writerow(["Data/Hora", "Download (Mbps)", "Upload (Mbps)", "Ping (ms)"])
    writer.writerow([now, download_speed, upload_speed, ping])



