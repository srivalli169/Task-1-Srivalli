import pandas as pd

# Load dataset
df = pd.read_excel(r"C:\Users\peddi\Downloads\Dataset for Data Analytics.xlsx")

print("===== DATASET OVERVIEW =====")
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)

# Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Fill missing CouponCode values
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

# Check duplicate rows
print("\n===== DUPLICATE ROWS =====")
print("Duplicate Rows:", df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Check duplicate Order IDs
duplicate_ids = df["OrderID"].duplicated().sum()

print("\n===== DUPLICATE ORDER IDs =====")
print("Duplicate IDs:", duplicate_ids)

# Convert Date column to proper format
df["Date"] = pd.to_datetime(df["Date"])

# Verify date format
print("\n===== DATE FORMAT CHECK =====")
print(df["Date"].head())

# Convert Product names to proper text format
df["Product"] = df["Product"].str.title()

# Save cleaned dataset
df.to_excel("Cleaned_Dataset.xlsx", index=False)

print("\n===== FINAL VERIFICATION =====")
print("Missing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())
print("Duplicate IDs:", df["OrderID"].duplicated().sum())

print("\nCleaned dataset saved as 'Cleaned_Dataset.xlsx'")
print("Project 1 Completed Successfully!")