import numpy as np
import pandas as pd


class PreProcess:
    def __init__(self, df: pd.DataFrame):
        """Initialize the PreProcess class.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
        """
        self.df = df

    def convert_to_datetime(self, df, column: str):
        """Convert a column to a datetime.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
            column (str): dataframe column to be converted
        """
        self.df[column] = pd.to_datetime(
           column)
        return self.df

    def convert_to_float(self, df, column: str):
        """Convert column to float.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
            column (str): Column to be converted to string
        """
        self.df[column] = df[column].astype(float)
        return self.df

    def drop_variables(self, df, column: str, percentage: int):
        """Drop variables based on a percentage.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
            column (str): Column to be dropped
            percentage(int): Percentage of variables to be dropped
        """
        df_before_filling = df
        df = df[df.columns[df.isnull().mean() < percentage / 100]]
        missing_cols = df.columns[df.isnull().mean() > 0]

        return df, df_before_filling, missing_cols

    def clean_feature_name(self, df):
        """Clean labels of the dataframe.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
        """
        df.columns = [column.replace(' ', '_').lower()
                      for column in df.columns]
        return df

    def rename_columns(self, df: pd.DataFrame, column: str, new_column: str):
        """Rename a column.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
            column (str): column to be renamed
            new_column (str): New column name
        """
        df = df[column].rename(new_column)
        return df

    def fill_numerical_variables(self, df):
        """Fill numerical variables.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
        """
        df_single = df
        cols = df_single.columns
        num_cols = df_single.select_dtypes(include=np.number).columns
        df_single.loc[:, num_cols] = df_single.loc[:, num_cols].fillna(
            df_single.loc[:, num_cols].median())
        print(num_cols)
        print(df_single.loc[:, num_cols].median())

        return cols, df_single, num_cols

    def fill_categorical_variables(self, df, cols, num_cols, df_single):
        """Fill categorical variables.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
            cols(list): List of columns
            num_cols(list): List of numerical columns
            df_single(pd.DataFrame): Dataframe with filled numerical variables
        """
        cat_cols = list(set(cols) - set(num_cols))
        df_single.loc[:, cat_cols] = df_single.loc[:, cat_cols].fillna(
            df.loc[:, cat_cols].mode().iloc[0])
        df_cols = df_single.columns
        print(cat_cols)
        print(df_single.loc[:, cat_cols].mode().iloc[0])

        return df_cols, df_single, cat_cols
