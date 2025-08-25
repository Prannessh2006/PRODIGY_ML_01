import pandas as pd
from sklearn.linear_model import HuberRegressor

train_data = pd.read_csv('Task 1/train.csv')
test_data = pd.read_csv('Task 1/test.csv')
train_data['TotalBathrooms'] = train_data['FullBath'] + 0.5 * train_data['HalfBath']
test_data['TotalBathrooms'] = test_data['FullBath'] + 0.5 * test_data['HalfBath']

input_features = ['GrLivArea', 'BedroomAbvGr', 'TotalBathrooms']
target = 'SalePrice'
X_train = train_data[input_features]
Y_train = train_data[target]
X_test = test_data[input_features]

model = HuberRegressor(epsilon=1.35, max_iter=100, alpha=0.0)
model.fit(X_train, Y_train)

predicted_prices = model.predict(X_test)
predictions = pd.DataFrame({
    'Id': test_data['Id'],
    'SalePrice': predicted_prices
})
predictions.to_csv('predicted_prices.csv', index=False)
result = pd.read_csv('predicted_prices.csv')
print(result.head())