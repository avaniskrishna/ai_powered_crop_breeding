# AI-Powered Crop Breeding for Sustainable Agriculture

# Project Overview
This project, titled "AI-Powered Crop Breeding," aims to revolutionize agricultural practices by leveraging Artificial Intelligence (AI) to enhance crop yield and optimize crop selection. In response to the growing global population and changing climate conditions, traditional crop breeding methods often fall short due to their time-consuming nature and susceptibility to environmental variability.
Our system utilizes a real-world dataset from Kaggle, comprising crucial environmental and soil parameters such as temperature, humidity, pH, nitrogen (N), phosphorus (P), potassium (K), and rainfall. AI models are trained on these factors to recommend the most suitable crop with maximum yield potential. This data-driven approach empowers breeders and farmers to make informed decisions, reduces resource wastage, and promotes sustainable agriculture.
The core of our proposed system is a Hybrid Yield Optimization Algorithm (HYOA), which integrates a supervised machine learning model—specifically, a Random Forest Classifier—with a custom Yield-Weighted Post-Processing Layer. This post-processing layer adjusts initial crop predictions based on heuristic yield scores, soil compatibility, and environmental match, thereby optimizing the decision beyond pure classification.

# Features
Intelligent Crop Recommendation: Recommends the most suitable crop based on given environmental and soil conditions.
Yield Optimization: Incorporates a yield-weighted scoring layer to maximize potential crop yield.
Data-Driven Decision Making: Utilizes real-world agricultural data for robust predictions.
Hybrid AI Model: Combines Random Forest Classification with a custom post-processing layer for enhanced accuracy and practical relevance.
Performance Evaluation: Compares the hybrid model's performance against other algorithms like Support Vector Machines (SVM) and K-Nearest Neighbors (KNN).

# Dataset
The project utilizes the Crop Recommendation Dataset from Kaggle.
Source: Atharva Ingle. "Crop Recommendation Dataset." Kaggle.
Features: Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH, Rainfall.
Labels: 22 different crop types.
Size: Over 2200 rows of data.

# Technologies Used
Python 3.x
pandas: For data manipulation and analysis.
scikit-learn: For machine learning models (Random Forest Classifier, train_test_split, accuracy_score, classification_report).

