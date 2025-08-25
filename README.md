ouse Price Prediction Project
This project predicts house prices using a Huber Regression model. It's designed to be robust against data outliers, providing more reliable predictions.

What's in the Folder
train.csv: This is our training data. It's what the model uses to learn the relationship between house features and their sale price.

test.csv: This is the testing data. It contains house features, but the sale prices are unknown. Our goal is to predict these prices.

predicted_prices.csv: This is the file that gets created when you run the code. It contains the predicted sale prices for all the houses in the test.csv file.

How It Works
The script uses a machine learning model called HuberRegressor. It's a type of linear regression that's particularly good at handling unusual data points (outliers).

The model uses these features to make its predictions:

GrLivArea: The living area of the house above ground.

BedroomAbvGr: The number of bedrooms.

TotalBathrooms: A combined count of full and half bathrooms.

The code trains the model on the train.csv file and then uses it to generate price predictions for the test.csv data. The final predictions are saved in the predicted_prices.csv file.
