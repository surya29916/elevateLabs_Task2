# ElevateLabs_Task2
# Titanic Dataset - Exploratory Data Analysis (EDA)

This project performs exploratory data analysis (EDA) on the cleaned Titanic dataset. The goal is to better understand the structure, distribution, and relationships between features using visual and statistical tools.

## ✅ Steps Performed

### 1. Summary Statistics
Used pandas.describe() to generate descriptive statistics (mean, median, min, max, standard deviation) for all numeric features. This helps identify data distribution and any irregularities in scale or range.

### 2. Histograms & Boxplots
- *Histograms* were created using seaborn.histplot() to visualize the frequency distribution of numeric features (Age, Fare, SibSp, Parch).
- *Boxplots* were used to identify potential outliers and understand value spread in the same columns.

### 3. Correlation Matrix & Pairplot
- A *correlation matrix* was plotted using seaborn.heatmap() to assess linear relationships between numeric features.
- A *pairplot* was generated to visualize scatter plots between each pair of numeric features, with histograms on the diagonal.

---

## 🔍 Observations & Insights

Although not shown in code, these are key patterns observed during analysis:

- Age and Fare are *right-skewed*, with most passengers being young and paying lower fares.
- The majority of passengers had **0 siblings/spouses (SibSp) and 0 parents/children (Parch)** on board — most likely traveling alone.
- *Strong correlation* observed between SibSp and Parch, indicating families or groups often traveled together.
- The *Fare feature had outliers*, but these were already removed during the preprocessing step.
- No strong linear correlation among all features, but *visual clusters* suggest interesting relationships that could help in modeling.

---

## 🔧 Tools & Libraries
- Python
- Pandas
- Seaborn
- Matplotlib

---# elevateLabs_Task2
