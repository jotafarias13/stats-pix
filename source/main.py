import matplotlib.pyplot as plt
import pandas as pd

pix1 = pd.read_csv("../data/PIX liquidados no SPI.csv")
pix2 = pd.read_csv(
    "../data/PIX liquidados no SPI - Distribuição Intradia - Média dos últimos 30 dias.csv"
)

pix2["Horario"] = pd.to_datetime(pix2["Horario"])
pix2["Horario"] = pix2["Horario"].dt.strftime("%H:%M")

pix2.plot("Horario", "QuantidadeMedia")
plt.show()

pix1["Data"] = pd.to_datetime(pix1["Data"])

pix1["Total"] = pix1["Total"].str.replace(",", ".").astype(float)

pix1["Media"] = pix1["Media"].str.replace(",", ".").astype(float)

pix1 = pix1.sort_values("Data")

fev_2022_mask = (pix1["Data"].dt.year == 2022) & (pix1["Data"].dt.month == 2)
fev_2022 = pix1[fev_2022_mask]

fev_2023_mask = (pix1["Data"].dt.year == 2023) & (pix1["Data"].dt.month == 2)
fev_2023 = pix1[fev_2023_mask]

# comparando mes de carnaval (fevereiro)
fig, ax = plt.subplots(1, 3, figsize=(12, 6))

ax[0].plot(
    fev_2022["Data"].dt.day, fev_2022["Quantidade"], color="blue", label="2022"
)
ax[0].plot(
    fev_2023["Data"].dt.day, fev_2023["Quantidade"], color="red", label="2023"
)
ax[0].legend()
ax[0].set_title("Quantidade")

ax[1].plot(
    fev_2022["Data"].dt.day, fev_2022["Total"], color="blue", label="2022"
)
ax[1].plot(
    fev_2023["Data"].dt.day, fev_2023["Total"], color="red", label="2023"
)
ax[1].legend()
ax[1].set_title("Total")

ax[2].plot(
    fev_2022["Data"].dt.day, fev_2022["Media"], color="blue", label="2022"
)
ax[2].plot(
    fev_2023["Data"].dt.day, fev_2023["Media"], color="red", label="2023"
)
ax[2].legend()
ax[2].set_title("Média")

plt.show()


# comparando ano pandemia/sem pandemia
ano_2021 = pix1[pix1["Data"].dt.year == 2021]
ano_2022 = pix1[pix1["Data"].dt.year == 2022]

fig, ax = plt.subplots(3, 1, figsize=(10, 7))

ax[0].plot(
    ano_2021["Data"].dt.dayofyear,
    ano_2021["Quantidade"],
    color="blue",
    label="2021",
)
ax[0].plot(
    ano_2022["Data"].dt.dayofyear,
    ano_2022["Quantidade"],
    color="red",
    label="2022",
)
ax[0].legend()
ax[0].set_title("Quantidade")

ax[1].plot(
    ano_2021["Data"].dt.dayofyear,
    ano_2021["Total"],
    color="blue",
    label="2021",
)
ax[1].plot(
    ano_2022["Data"].dt.dayofyear,
    ano_2022["Total"],
    color="red",
    label="2022",
)
ax[1].legend()
ax[1].set_title("Total")

ax[2].plot(
    ano_2021["Data"].dt.dayofyear,
    ano_2021["Media"],
    color="blue",
    label="2021",
)
ax[2].plot(
    ano_2022["Data"].dt.dayofyear,
    ano_2022["Media"],
    color="red",
    label="2022",
)
ax[2].legend()
ax[2].set_title("Média")

plt.show()
