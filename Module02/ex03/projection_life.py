from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def projection_life(y: str):
    year = int(y)
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy = load("life_expectancy_years.csv")

    # year index
    index_inc = income.columns.get_loc(y)

    # life expectancy data for year y
    income = income.T #transposes data set so that each row is the data for a year
    datax = income.values[index_inc][0:]

    # income data for year x
    life_expectancy = life_expectancy.T
    datay = life_expectancy.values[index_inc][0:]

    # creates data set relating income data and life expectancy for every contry in year y
    df = pd.DataFrame({'x': datax, 'y': datay})

    # plot
    df.plot.scatter(x='x', y='y', color='blue', marker='o')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.title(y)
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
    plt.show()

def main():
    projection_life("1900")

if __name__ == "__main__":
    main()