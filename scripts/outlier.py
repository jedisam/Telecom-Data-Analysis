import numpy as np
import pandas as pd
import numpy as np
import pandas as pd


class Outlier:
    def __init__(self, df: pd.DataFrame):
        """Initialize the PreProcess class.

        Args:
            df (pd.DataFrame): dataframe to be preprocessed
        """
        self.df = df

    # how many missing values exist or better still what is the % of missing values in the dataset?

    def handle_outliers(self, df: pd.DataFrame, cols):
        """Handle outliers in the dataset.

        Args:
            df (pd.DataFrame): a dataframe to be preprocessed

        Returns:
            pd.DataFrame: the dataframe
        """
        # Get numerical columns
        # num_cols = df.select_dtypes(include=np.number).columns
        for col in cols:
            # Computing 10th, 90th percentiles and replacing the outliers
            df[col] = [np.log(x) for x in df[col]]

    def calculate_num_outliers_zscore(self, df, cols):
        """Return the number of outliers for each numerical col.

        Args:
            df (pd.DataFrame): a dataframe to be analyzed
        """
        # calculate skewness

        outliersTot = {}
        for col in cols:
            outliers = []
            # def detect_outliers_zscore(data):
            thres = 3
            mean = np.mean(df[col])
            std = np.std(df[col])
            # print(mean, std)
            for i in df[col]:
                z_score = (i-mean)/std
                if (np.abs(z_score) > thres):
                    outliers.append(i)
            outliers[col] = len(outliers)
        return outliersTot  # Driver code

        # sample_outliers = detect_outliers_zscore(
        #     df['nb_of_sec_with_vol_ul_<_1250b'])
        # print("Outliers from Z-scores method: ", len(sample_outliers))

    def calculate_num_outliers_iqr(self, df, cols):
        """Return the number of outliers for each col.

        Args:
            df (pd.DataFrame): a dataframe to be analyzed
        """
        # calculate skewness

        outliersTot = {}
        for col in cols:
            outliers = []
            df[col] = sorted(df[col])
            q1 = np.percentile(df[col], 25)
            q3 = np.percentile(df[col], 75)
            # print(q1, q3)
            IQR = q3-q1
            lwr_bound = q1-(1.5*IQR)
            upr_bound = q3+(1.5*IQR)
            # print(lwr_bound, upr_bound)
            for i in df[col]:
                if (i < lwr_bound or i > upr_bound):
                    outliers.append(i)
            outliers[col] = len(outliers)
        return outliersTot  # Driver code

    def outlier_overview(self, df, col):
        """Get outlier overview.

        Args:
            df (pd.DataFrame): a dataframe to be analyzed
        """

        # calculate upper and lower limits
        upper_limit = df[col].mean() + 3 * df['total_ul_(bytes)'].std()
        lower_limit = df[col].mean() - 3 * df['total_ul_(bytes)'].std()

        # select outliers
        return df[~((df[col] < upper_limit) & (df[col] > lower_limit))]

        # # outliers removed
        # display(df[(df[col] < upper_limit) & (df[col] > lower_limit)])
