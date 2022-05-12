from scripts import preprocessing
import os
import sys
import unittest

import numpy
import pandas as pd
from pandas._libs.tslibs.timestamps import Timestamp

sys.path.append(os.path.abspath(os.path.join('../')))


class TestPreprocessDf(unittest.TestCase):
    """A class for unit-testing function in the preprocess.py file.

    Args:
        unittest.TestCase this allows the new class to inherit
        from the unittest module
    """

    def setUp(self) -> pd.DataFrame:
        """Dataframe that contains the data from the covid19.json file.

        Returns:
            pd.DataFrame: DF from Economic_Twitter_data.json file.
        """
        self.df = self.df = pd.DataFrame({'start': [
                                         '4/4/2021 12:01'], 'total_dl_(bytes)': 1243, 'youtube_ul_(bytes)': 653443, 'netflix_dl_(bytes)': 0.921154, 'other_dl_(bytes)': 872215, 'total_ul_(bytes)': 341197}, {'start': [
                                             '6/2/2022 10:25'], 'total_dl_(bytes)': 76343, 'youtube_ul_(bytes)': 24464, 'netflix_dl_(bytes)': 0.671154, 'other_dl_(bytes)': 172215, 'total_ul_(bytes)': 671197})
        # tweet_df = self.df.get_tweet_df()

    def test_convert_to_datetime(self):
        """Test convert to datetime module."""
        df = preprocessing.PreProcess(
            self.df).convert_to_datetime(self.df, 'start')
        assert type(df['start'][0]) is Timestamp

    def test_rename_columns(self):
        """Test convert to number module."""
        df = preprocessing.PreProcess(self.df).rename_columns(
            self.df, 'youtube_ul_(bytes)', 'youtube')
        # Check if a column has been renamed
        assert 'youtube' in df.columns

    def test_drop_duplicates(self):
        """Test convert to datetime module."""
        df = preprocessing.PreProcess(self.df).drop_duplicates(self.df)
        assert df.shape[0] == 1


if __name__ == '__main__':
    unittest.main()
