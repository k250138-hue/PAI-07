import pandas as pd
import numpy as np


def make_data():
    """Builds the raw dataset given in the lab (same seed, same data every time)."""
    np.random.seed(42)
    n_rows = 150

    data = {
        'Customer_ID': [f'CUST_{1000 + i}' if i % 12 != 0 else np.nan for i in range(n_rows)],
        'Join_Date': pd.date_range(start='2023-01-01', periods=n_rows, freq='2D'),
        'Age': [np.random.randint(18, 65) if i % 7 != 0 else np.nan for i in range(n_rows)],
        'Gender': np.random.choice(['Male', 'Female', 'Other'], size=n_rows, p=[0.48, 0.48, 0.04]),
        'City': np.random.choice(['Karachi', 'Lahore', 'Islamabad', 'Peshawar'], size=n_rows),
        'Category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Books'], size=n_rows),
        'Order_Count': np.random.randint(1, 30, size=n_rows),
        'Total_Spent': [round(np.random.uniform(500, 50000), 2) if i % 9 != 0 else np.nan for i in range(n_rows)],
        'Is_VIP': np.random.choice([True, False], size=n_rows, p=[0.2, 0.8])
    }
    return pd.DataFrame(data)


def clean_data():
    """Applies Tasks 2 to 6 so the later tasks can start from a clean table."""
    df = make_data()
    df = df.dropna(subset=['Customer_ID']).reset_index(drop=True)
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Total_Spent'] = df['Total_Spent'].fillna(df['Total_Spent'].mean())
    df['Join_Date'] = pd.to_datetime(df['Join_Date'])
    df['Join_Year'] = df['Join_Date'].dt.year
    df['Join_Month'] = df['Join_Date'].dt.month_name()
    df['Avg_Order_Value'] = df['Total_Spent'] / df['Order_Count']
    df['High_Value_Customer'] = df['Avg_Order_Value'] > 2500
    return df
