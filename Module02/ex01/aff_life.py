from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def aff_life(ct: str):
    df = load("life_expectancy_years.csv")

    # only include rows where the country is pt.
    country_dt = df.loc[df['country'] == ct]

    #print(country_dt)
    years = country_dt.columns[1:] #'classification' of each value
    ages = country_dt.values[0][1:] #returns an array with the first row of values
    
    # 'ages' is already a numpy array, so no need to convert it again
    years = np.array(years)

    plt.plot(years, ages)
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.title(ct + " Life expectancy Projections")
    plt.xticks(years[::40])
    plt.show()

def main():
    aff_life("Portugal")

if __name__ == "__main__":
    main()