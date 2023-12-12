import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Datasets found on Kaggle at https://www.kaggle.com/datasets/mathchi/hitters-baseball-data

def batting_analysis():
    batting = pd.read_csv("Hitters.csv")

    print(batting.head())
    # Remove All Na values from data
    batting.dropna(inplace=True)

    batting["Avg"] = batting["Hits"] / batting["AtBat"]
    batting["CAvg"] = batting["CHits"] / batting["CAtBat"]
    batting["AvgDiff"] = batting["Avg"] - batting["CAvg"]
    batting["OBP"] = (batting["Hits"] + batting["Walks"]) / (batting["AtBat"] + batting["Walks"])
    print(batting.head())

    # Average batting Avg for players in data
    print(batting["CAvg"].mean())

    salary_predictive_analysis(batting)

    # Find career average by years in league
    #batting.plot.scatter(x="Years", y="CAvg", figsize=(20, 10));
    #plt.show()


# Perform an operation to predict a players salary based on their On Base Percentage during the season
# Prediction - Players with higher OBP will have corresponding high Salary's
def salary_predictive_analysis(data):
    x = data['OBP']
    y = data['Salary']

    # Split the data into a test and training
    x_train, x_test, y_train, y_test, = train_test_split(x, y, test_size=0.25, random_state=50)

    # Create a Linear Regression model to solve problem
    model = LinearRegression()

    # Encountered error where fit and model functions looked for 2D array but found 1D array
    x_train_reshaped = x_train.values.reshape(-1, 1)
    x_test_reshaped = x_test.values.reshape(-1, 1)

    model.fit(x_train_reshaped, y_train)
    y_pred = model.predict(x_test_reshaped)

    # Calculate Mean Squared Error and R-Squared values
    mean_squared = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Mean Squared Error:" + str(mean_squared))
    print("R-Squared:" + str(r2))

    # Plot on a scatter plot with a Regression Line
    plt.scatter(x_test, y_test, color='blue', label="Actual")
    plt.plot(x_test, y_pred, color = 'red', linewidth=3, label="Regression Line")
    plt.xlabel("On Base Percentage")
    plt.ylabel("Salary")
    plt.title("Linear Regression of OBP v. Salary")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    batting_analysis()