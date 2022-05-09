import numpy as np
import pandas as pd


class Overview:
    def __init__(self, df: pd.DataFrame):
        """Initialize the PreProcess class.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
        """
        self.df = df

    # how many missing values exist or better still what is the % of missing values in the dataset?

    def percent_missing(df: pd.DataFrame):
        """Get the percentage of missing values in the dataset.

        Args:
            df (pd.DataFrame): a dataframe to be preprocessed

        Returns:
            pd.DataFrame: the dataframe
        """
        # Calculate total number of cells in dataframe
        totalCells = np.product(df.shape)

        # Count number of missing values per column
        missingCount = df.isnull().sum()

        # Calculate total number of missing values
        totalMissing = missingCount.sum()

        # Calculate percentage of missing values
        print("The telecom dataset contains", round(
            ((totalMissing/totalCells) * 100), 2), "%", "missing values.")

        return df

    def get_skewness(df: pd.DataFrame):
        """Return the skewness of the dataset.

        Args:
            df (pd.DataFrame): a dataframe to be analyzed
        """
        # calculate skewness
        skewness = df.skew(axis=0, skipna=True)

        return skewness
