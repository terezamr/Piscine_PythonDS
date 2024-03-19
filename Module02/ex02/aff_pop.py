from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#replaces k and M for the whole number
def parse(nb: str) -> str:
    if nb[-1] == 'k':
        return (float(nb[:-1]) * 1000)
    elif nb[-1] == 'M':
        return (float(nb[:-1]) * 1000000)
    else:
        return (float(nb[:-1]))

def aff_pop(ct1: str, ct2:str):
    df = load("population_total.csv")

    # year limit
    index_lim = df.columns.get_loc('2050')

    # country 1
    data1 = df.loc[df['country'] == ct1]
    ages1 = data1.values[0][1:index_lim]
    new1 = [parse(x) for x in ages1]

    # country 2
    data2 = df.loc[df['country'] == ct2]
    ages2 = data2.values[0][1:index_lim]
    new2 = [parse(x) for x in ages2]

    #years
    years = data1.columns[1:index_lim]
    years = np.array(years)

    # plot
    plt.plot(years, new1, label=ct1, color="lightblue")
    plt.plot(years, new2, label=ct2, color="green")
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title("Population Projections")
    plt.xticks(years[::40])
    plt.legend(loc='lower right')
    plt.show()

def main():
    aff_pop("Portugal", "France")

if __name__ == "__main__":
    main()