"""
Utility helper functions for IntroMLCapstone.

This file contains small, reusable helpers for loading and preprocessing the tabular sample data.
Expand with image IO and dataset classes for VHR pipelines as the project grows.
"""

import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    """Load a CSV into a pandas DataFrame."""
    return pd.read_csv(path)

def basic_preprocess(df: pd.DataFrame, drop_na: bool = True) -> pd.DataFrame:
    """
    Basic preprocessing:
    - Optionally drop NA
    - Ensure numeric columns are numeric
    - (Placeholder) Add encoding/normalization as needed.
    """
    if drop_na:
        df = df.dropna()
    # Convert known numeric columns
    numeric_cols = ['flow_acc', 'slope', 'pop_density', 'road_distance', 'parcel_value']
    for c in numeric_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')
    return df