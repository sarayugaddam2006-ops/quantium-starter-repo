import pandas as pd

# List of input files
files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

all_data = []

for file in files:
    # Read CSV
    df = pd.read_csv(file)

    # Filter only pink morsel (safe matching)
    df = df[df["product"].str.strip().str.lower() == "pink morsel"]

    # Clean price column (remove $ and convert to float)
    df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)

    # Ensure quantity is integer
    df["quantity"] = df["quantity"].astype(int)

    # Create Sales column (correct multiplication)
    df["Sales"] = df["price"] * df["quantity"]

    # Keep only required columns
    df = df[["Sales", "date", "region"]]

    # Append cleaned data
    all_data.append(df)

# Combine all files into one DataFrame
final_df = pd.concat(all_data, ignore_index=True)

# Save output
final_df.to_csv("output.csv", index=False)

print("✅ Data processing complete. Output saved as output.csv")