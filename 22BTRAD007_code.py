import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Load and split the dataset
df = pd.read_csv("C:/Users/avani/OneDrive/Documents/University work/Class/3rd year/term 15/PCL/Crop_recommendation.csv")
X = df.drop('label', axis=1)
y = df['label']
#split into 80% training and 20% testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Step 2: Train Random Forest
#initialize a radom forest with 100 decision trees
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# Step 3: Accuracy Evaluation
#compares actual vs predicted crop types and prints the accuracy score 0-1
print("Accuracy:", accuracy_score(y_test, predictions))

# Step 4: Yield-Weighted Scoring (Example logic)
def yield_score(crop, rainfall, pH):
    yield_table = {
        'rice': 0.9, 'wheat': 0.85, 'mungbean': 0.6,
        'maize': 0.78, 'kidneybeans': 0.7  # Mock scores
    }
    #gets crop base yeild score. default to 0.5 if crop not found in the table
    score = yield_table.get(crop, 0.5)
    #boost rice field score if rainfall is high
    if crop == 'rice' and rainfall > 100:
        score += 0.05
        #adds bonus to the score if soil ph is optimal
    if 6 <= pH <= 7:
        score += 0.05
        
    return score

# Final Crop Recommendation based on max score
test_sample = X_test.iloc[0]
initial_crop = model.predict([test_sample])[0]
final_score = yield_score(initial_crop, test_sample['rainfall'], test_sample['ph'])
print("Recommended Crop:", initial_crop, "| Yield Score:", final_score)


from sklearn.metrics import classification_report

# After model prediction
report = classification_report(y_test, predictions, digits=4)
print(report)



