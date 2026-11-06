# SugarSense – Early Diabetes Risk Screening

**A Machine Learning project for identifying potential diabetes risk using patient health measurements.**

## Project Overview

SugarSense is a supervised Machine Learning project that predicts the likelihood of diabetes based on medical measurements such as glucose level, BMI, age, blood pressure, and other health-related features.

The project explores data preprocessing, exploratory data analysis, feature engineering, model comparison, hyperparameter tuning, and threshold optimization.

## Objectives

- Analyze diabetes screening data.
- Identify and handle invalid and missing values.
- Perform exploratory data analysis (EDA).
- Build and compare multiple Machine Learning models.
- Improve diabetes detection using threshold optimization.

## Dataset

- Dataset: Pima Indians Diabetes Dataset
- Total Records: 768
- Original Input Features: 8
- Target Variable: Outcome
- 0 – Non-diabetic
- 1 – Diabetic

Note: The dataset contains records of female patients aged 21 years and above.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Google Colab
- Jupyter Notebook

## Machine Learning Algorithms

The following algorithms were implemented and compared:

1. Logistic Regression
2. K-Nearest Neighbors (KNN)
3. Decision Tree
4. Random Forest
5. Support Vector Machine (SVM)
6. XGBoost

## Project Workflow

1. Data Collection and Data Audit
2. Exploratory Data Analysis
3. Feature Engineering
4. Data Preprocessing
5. Train-Test Split
6. Model Training and Cross-Validation
7. Hyperparameter Tuning
8. Model Evaluation
9. Threshold Optimization
10. Feature Importance Analysis

## Model Performance

Logistic Regression was selected after cross-validation and hyperparameter tuning.

### Test Set Results – Default Threshold

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 74.68% |
| Precision | 61.19% |
| Recall    | 75.93% |
| F1 Score  | 67.77% |
| ROC-AUC   | 82.15% |

### Threshold Optimization

The classification threshold was adjusted from 0.50 to 0.36 using training out-of-fold predictions.

| Metric          | Default |  Tuned |
| --------------- | ------: | -----: |
| Precision       |  61.19% | 55.42% |
| Recall          |  75.93% | 85.19% |
| F1 Score        |  67.77% | 67.15% |
| False Negatives |      13 |      8 |

Threshold tuning improved recall, helping identify more potentially diabetic cases.

## How to Run the Project

1. Clone or download this repository.
2. Open `SugarSense_Complete_Project.ipynb` in Google Colab or Jupyter Notebook.
3. Upload the diabetes dataset when prompted.
4. Run all notebook cells from beginning to end.
5. View the model comparison, evaluation metrics, and visualizations.

## Repository Contents

- `SugarSense_Complete_Project.ipynb` – Complete project implementation.
- `sugarsense_model.joblib` – Saved trained model (if included).
- `SugarSense_One_Page_Summary.md` – Project summary.

## Limitations

- The dataset contains only 768 records.
- The dataset represents female patients aged 21 years and above.
- Some medical measurements contain invalid zero values.
- Model performance may vary on different populations.

## Future Enhancements

- Use larger and more diverse datasets.
- Explore additional Machine Learning algorithms.
- Develop a web-based diabetes risk screening application.
- Improve model performance and fairness.

## Disclaimer

This project is developed for educational purposes only. It is not intended to replace professional medical advice, diagnosis, or treatment.

## Author

**Theerdamai Konkipudi**

GitHub: [theerdamai9](https://github.com/theerdamai9)

Project: [SugarSense – Early Diabetes Risk Screening](https://github.com/theerdamai9/SugarSense-Diabetes-Prediction)

