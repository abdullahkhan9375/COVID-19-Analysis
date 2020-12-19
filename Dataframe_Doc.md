# Dataframes
Dataframes have been constructed from raw datasets in the raw_datasets folder. Irrelevant values, miniscule datapoints, and redundant values have been removed and 5 dataframes have been made as of 23.10.2020

## Usage
Simply import dataframes from the mainfolder. 

```python
    from dataframes import df1, df2, df3, df4, df5
```

## Df1
Df1 is the primary covid dataset. It has information for cases and deaths by each country. It's indexed by days ranging from 31.12.2019 to 10.10.2020.

## Df2 
Df2 is for country information. It has columns for gdp, population, birthrate, etc. Indexed by Country Codes.

## Df3 
Df3 is a combined dataset of df1 and df2. Indexed by country codes.

## Df4
Df4 captures all arrivals to Australia by nationalities. It has columns for every month from 2016 to Sep 2020. Indexed by Country codes.

## Df5 
Df5 captures all departures from Australia by nationalities. It has columns for every month from 2016 to Sep 2020. Indexed by Country codes.