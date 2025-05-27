import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Generate summary statistics
print("Summary Statistics:")
print(df.describe())

# Create histograms and boxplots for numeric features
numeric_cols = ['Age', 'Fare', 'SibSp', 'Parch']

# Histograms
for col in numeric_cols:
    plt.figure(figsize=(6, 4))
    sns.histplot(df[col], kde=True, bins=30)
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# Boxplots
for col in numeric_cols:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.tight_layout()
    plt.show()

# Correlation matrix and pairplot
plt.figure(figsize=(8, 6))
corr_matrix = df[numeric_cols].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

# Pairplot
sns.pairplot(df[['Age', 'Fare', 'SibSp', 'Parch']])
plt.suptitle("Pairplot of Numeric Features", y=1.02)
plt.tight_layout()
plt.show()
