import pandas as pd
import matplotlib.pyplot as plt
# Datasets found on Kaggle at https://www.kaggle.com/datasets/mathchi/hitters-baseball-data

# Analyze the Average Batting Average for every year
def batting_analysis():
    batting = pd.read_csv("Hitters.csv")

    print(batting.head())
    # Remove All Na values from data
    batting.dropna(inplace=True)

    batting["Avg"] = batting["Hits"] / batting["AtBat"]
    batting["CAvg"] = batting["CHits"] / batting["CAtBat"]
    batting["AvgDiff"] = batting["Avg"] - batting["CAvg"]
    print(batting.head())

    # Average batting Avg for players in data
    print(batting["CAvg"].mean())

    # Find career average by years in league
    #batting.plot.scatter(x="Years", y="CAvg", figsize=(20, 10));
    #plt.show()

    # Check for visual correlation between salary and amount of home runs hit
    sort_by_salary = batting.sort_values(by="Salary")
    sort_by_salary.plot.bar(x = "Salary", y="HmRun")
    plt.show()

if __name__ == "__main__":
    batting_analysis()