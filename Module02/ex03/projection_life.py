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

    #life expectancy data for year x
    print("check: ", income['1900'])
    income = income.T
    datax = income.values[index_inc][0:]
    print(datax)


    #income data for year x
    print("check: ", life_expectancy['1900'])
    life_expectancy = life_expectancy.T
    print(life_expectancy)
    datay = life_expectancy.values[index_inc][0:]
    print(datay)

    df = pd.DataFrame({'x': datax, 'y': datay})
    df.plot.scatter(x='x', y='y', color='blue', marker='o')

    # plot
    #plt.plot(datax, datay, color="lightblue")
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.title(y)
    #plt.xticks(years[::10])
    plt.show()

def main():
    projection_life("1900")

if __name__ == "__main__":
    main()