import pandas as pd


def data_basic_treatment (df: "pd.DataFrame")-> "pd.DataFrame":
    """
    Rename all to lower case letters, feature and data, and removing all blank spaces
    """
    # replace uppercase letters with lowercase letters in features
    df = df.rename(columns = (lambda x:x.lower()))
    # put all data in lowercase leters
    df = df.applymap(lambda x:x.lower() if isinstance(x, str) else x)
    # remove blank spaces in data
    df = df.applymap(lambda x:x.strip() if isinstance(x, str) else x)
    
    return df

def data_types (df: "pd.DataFrame") -> "pd.DataFrame":
    """
    Changing data types
    """
    float_columns = ["balance", "estimatedsalary"]
    for col in float_columns:
        df[col] = df[col].astype("float")

    int_columns = ["creditscore", "age", "tenure", "numofproducts", "hascrcard", "isactivemember", "exited"]
    for col in int_columns:
        df[col] = df[col].astype("int")

    str_columns = ["customerid", "geography"]
    for col in str_columns:
        df[col] = df[col].astype("str")
    
    return df

def basic_eda(df):
    """
    Function to return dataframe with summarized result containing n total values, n unique values and missing percent in each feature.
    """
    summary_data = []
    for col in df.columns:
        # calculate n total values, n unique values and missing percent in each feature
        ntotal_values = df[col].count()
        nunique_values = df[col].nunique()
        missing_percent = ((df[col].isnull().sum() + df[col][df[col] == ""].sum()) / ntotal_values) *100
        summary_data.append((col, nunique_values, missing_percent, ntotal_values))

    # create DataFrame with results
    df = pd.DataFrame(summary_data, columns = ["feature", "nunique_values", "missing_percent", "ntotal_values"])

    return df