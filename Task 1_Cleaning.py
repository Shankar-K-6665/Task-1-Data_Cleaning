import pandas as pd

# 1. Load the dataset
df = pd.read_csv("Mall_Customers.csv")  # Make sure file name matches exactly
print("\nInitial Dataset Shape:", df.shape)

# 2. Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

# Example: Fill missing Age values with median
if 'Age' in df.columns:
    df['Age'] = df['Age'].fillna(df['Age'].median())

# 3. Remove duplicates
df = df.drop_duplicates()

# 4. Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# 5. Clean text values (if gender exists)
if 'gender' in df.columns:
    df['gender'] = df['gender'].str.lower().str.strip()

# 6. Save cleaned data
df.to_csv("cleaned_dataset.csv", index=False)
print("\n✅ Cleaned dataset saved as cleaned_dataset.csv")
print("Final Dataset Shape:", df.shape)
