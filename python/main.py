import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("resources/users.csv",header=0,sep=';')
    print(df)
    print(df.columns)


    print(df['name'].count())

    print(df['name'].where(df['age'] > 50))



