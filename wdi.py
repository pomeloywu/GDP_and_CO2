import pandas as pd

df_media = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

df_new = df_media[
    [
        "Mortality rate, infant (per 1,000 live births)",
        "GDP per capita (constant 2010 US$)",
        "Country Name",
    ]
]
df_new.plot(
    x="GDP per capita (constant 2010 US$)",
    y="Mortality rate, infant (per 1,000 live births)",
)
