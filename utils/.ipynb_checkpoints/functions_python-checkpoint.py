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