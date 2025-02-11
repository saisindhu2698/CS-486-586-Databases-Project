import psycopg2
import pandas as pd

def initialize():
    connection = psycopg2.connect(
        user = "postgres", #username that you use
        password = "********", 
        host = "localhost", 
        port = "5432", 
        database = "postgres"
    )
    connection.autocommit = True
    return connection
    
   

def runQuery(conn):
    select_Query =  "select sum(\"VersionNum\"),avg(\"VersionNum\") from rate where \"BussinessYear\" ='2014';"
    rate_df = pd.DataFrame(columns = ['VersionNum'])
    with conn.cursor() as cursor:
        cursor.execute(select_Query)
        records = cursor.fetchall()
        
        for row in records:
            output_df = {'Sum': row[0],'Avg': row[1]}
            rate_df = rate_df.append(output_df, ignore_index=True)
    
        print(rate_df)

def main():
    conn = initialize()
    runQuery(conn)


if __name__ == "__main__":
    main()

#sample_code.py
#Displaying sample_code.py.
