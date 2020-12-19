import pandas as pd
import matplotlib.pyplot as plt
cov_dat = 'raw_datasets/Covid.csv'
main_dat = 'raw_datasets/countries.csv'
arr_dat = 'raw_datasets/arrival.csv'
dep_dat = 'raw_datasets/departure.csv'
cov = pd.read_csv(cov_dat)
datesCov = pd.DataFrame({
    'year': cov["year"],
    'month': cov["month"],
    "day": cov["day"]

})
cov["dates"] = pd.to_datetime(datesCov)
cov = cov.drop(columns=['dateRep', 'day', 'month', 'year'])
arrDf = pd.read_csv(arr_dat, encoding="ISO-8859-1")
depDf = pd.read_csv(dep_dat, encoding="ISO-8859-1")
arrDf = arrDf.rename(columns={'Country of citizenship(a)': 'Country'})
arrDf = arrDf.drop(columns=["SACC code(a)"])
depDf = depDf.rename(columns={'Country of citizenship(a)': 'Country'})
depDf = depDf.drop(columns=["SACC code(a)"])
cov = cov.set_index('dates')
covCo = pd.DataFrame()
covCo = cov.groupby(['Code']).sum()
covCo = covCo.drop(columns=["popData2019"])
countries = pd.read_csv(main_dat, sep=',', thousands=',')
countries = countries.set_index('Code')
df1 = covCo
df2 = countries
df3 = df1.join(df2, how='inner')
df3 = df3.drop(columns=["Coastline (coast/area ratio)",
                        "Phones (per 1000)", "Net migration"])
df4 = arrDf
df5 = depDf
df3 = df3.fillna(0)


def removeSpace(dataset):
    for x in range(len(dataset.index)):
        if dataset["Country"][x][-1] == " ":
            dataset["Country"][x] = dataset["Country"][x][:-1]


removeSpace(df3)
df3["Codes"] = df3.index
codeDict = {}
for x in range(len(df3.index)):
    codeDict[df3["Country"][x]] = df3["Codes"][x]

codeDict["Zimbabwe"]
df4['Code'] = ["UNKNOWN" for x in range(len(df4.index))]
df5['Code'] = ["UNKNOWN" for x in range(len(df5.index))]
unknown = []


unknown = []


def standardize(dataset):
    dict1 = codeDict
    for x in range(len(dataset.index)):
        for k, v in dict1.items():
            if k == dataset["Country"][x]:
                dataset["Code"][x] = v
            elif dataset['Country'][x] == "Total":
                dataset["Code"][x] = "TOT"
            else:
                pass


standardize(df4)
standardize(df5)
df4 = df4.drop(df4[df4["Code"] == "UNKNOWN"].index)
df5 = df5.drop(df4[df4["Code"] == "UNKNOWN"].index)
#### INDEXED BY DATES #####################
df1  # COVID Cases ranging from 31/12/2019 - 10/10/2020

######333#INDEXED BY COUNTRY CODE#########
df2  # Country Data (gdp, birthrate)
df3  # Combined dataframe from df1 and df2 (cases, gdp...)
df4  # Dataframe for all arrivals in Australia from 2016-2020 Month Format
df5  # Dataframe for all departures in Australia from 2016-2020 Month Format
rd = cov
dfContCode = pd.DataFrame({
    "Code": rd["Code"],
    "Continent": rd["continentExp"]
}, index=rd.index)
# making integers in df4 (arrival dataset)
for column in df4.columns[1:len(df4.columns) - 2]:
    df4[column] = df4[column].str.replace(',', '')

for column in df4.columns[1:len(df4.columns) - 2]:
    df4[column] = df4[column].astype(int)


# Arrival dataset for first 6 months from 2017-2020
df4["6Months-17"] = df4["17-Jan"] + df4["17-Feb"] + \
    df4["17-Mar"] + df4["17-Apr"] + df4["17-May"] + df4["17-Jun"]
df4["6Months-18"] = df4["18-Jan"] + df4["18-Feb"] + \
    df4["18-Mar"] + df4["18-Apr"] + df4["18-May"] + df4["18-Jun"]
df4["6Months-19"] = df4["19-Jan"] + df4["19-Feb"] + \
    df4["19-Mar"] + df4["19-Apr"] + df4["19-May"] + df4["19-Jun"]
df4["6Months-20"] = df4["20-Jan"] + df4["20-Feb"] + \
    df4["20-Mar"] + df4["20-Apr"] + df4["20-May"] + df4["20-Jun"]


# converting df5 (departure)
for column in df5.columns[1:len(df5.columns) - 2]:
    df5[column] = df5[column].str.replace(',', '')

for column in df5.columns[1:len(df5.columns) - 2]:
    df5[column] = df5[column].astype(int)


df5["6Months-17"] = df5["Jan-17"] + df5["Feb-17"] + \
    df5["Mar-17"] + df5["Apr-17"] + df5["May-17"] + df5["Jun-17"]
df5["6Months-18"] = df5["Jan-18"] + df5["Feb-18"] + \
    df5["Mar-18"] + df5["Apr-18"] + df5["May-18"] + df5["Jun-18"]
df5["6Months-19"] = df5["Jan-19"] + df5["Feb-19"] + \
    df5["Mar-19"] + df5["Apr-19"] + df5["May-19"] + df5["Jun-19"]
df5["6Months-20"] = df5["Jan-20"] + df5["Feb-20"] + \
    df5["Mar-20"] + df5["Apr-20"] + df5["May-20"] + df5["Jun-20"]


arrDf4 = pd.DataFrame({
    "Code": df4["Code"],
    "Country": df4["Country"],
    "2017-Arr": df4["6Months-17"],
    "2018-Arr": df4["6Months-18"],
    "2019-Arr": df4["6Months-19"],
    "2020-Arr": df4["6Months-20"]
}, index=df4.index)


depDf5 = pd.DataFrame({
    "Code": df5["Code"],
    "Country": df5["Country"],
    "2017-Dep": df5["6Months-17"],
    "2018-Dep": df5["6Months-18"],
    "2019-Dep": df5["6Months-19"],
    "2020-Dep": df5["6Months-20"]
}, index=df5.index)


dfContCode = dfContCode.drop_duplicates()
dfContCode = dfContCode.set_index("Code")
ArrDepdf = pd.merge(depDf5, arrDf4)
ArrDepdf = ArrDepdf.set_index("Code")
ArrDepdf = ArrDepdf.join(dfContCode, how="inner")
