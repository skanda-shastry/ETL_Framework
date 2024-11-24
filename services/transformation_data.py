def clean_column_names(df):
      # Implementation here
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df

def filter_data(df, column: str, value):
      # Implementation here
    return df[df[column] == value]

def add_calculated_column(df, new_col: str, calculation):
    df[new_col] = df.apply(calculation, axis=1)
      # Implementation here
    return df
