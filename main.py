import pandas as pd

# Datasets found on Kaggle at https://www.kaggle.com/datasets/open-source-sports/baseball-databank

# Analyze the Average Batting Average for every year
def batting_analysis():
    batting = pd.read_csv("Batting.csv")
    # Remove NA values from data
    batting.dropna(inplace=True)

    # Remove any player with no recorded AB's
    for index in batting.index:
        if batting.loc[index, "AB"] < 1 or batting.loc[index, "yearID"] < 1950:
            batting.drop(index, inplace=True)

    batting["AVG"] = batting["H"] / batting["AB"]


    print(batting)


if __name__ == "__main__":
    batting_analysis()