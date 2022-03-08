
def calc_missing_vals(input_df):
    N=len(input_df)
    missing_df=input_df.isnull().sum()/N*100
    missing_df=missing_df[missing_df!=0]
    return(missing_df)