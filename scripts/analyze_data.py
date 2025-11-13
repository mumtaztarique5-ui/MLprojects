import pandas as pd
import numpy as np
from scipy import stats

def get_basic_stats(df: pd.DataFrame):
    """Return basic summary statistics and null value count."""
    print("\n📊 Data Summary:")
    print(df.describe(include='all'))
    print("\n❓ Missing Values:")
    print(df.isnull().sum())

def correlation_matrix(df: pd.DataFrame):
    """Compute correlation matrix for numeric columns."""
    print("\n🔗 Correlation Matrix:")
    print(df.corr(numeric_only=True))
