import psycopg2
import pandas as pd

def initialize():
    connection = psycopg2.connect(
        user = "postgres", #username that you use
        password = "S@!2698mss", 
        host = "localhost", 
        port = "5432", 
        database = "postgres"
    )
    connection.autocommit = True
    return connection
    
   

def runQuery(conn):
    select_Query =  "select \"VersionNum\", count(*) from rate where \"StateCode\" = 'AK' group by \"VersionNum\" having count(*) > '5';"
    rate_df = pd.DataFrame(columns = ['VersionNum'])
    with conn.cursor() as cursor:
        cursor.execute(select_Query)
        records = cursor.fetchall()
        
        for row in records:
            output_df = {'VersionNum': row[0],'count': row[1]}
            rate_df = rate_df.append(output_df, ignore_index=True)
    
        print(rate_df)

def main():
    conn = initialize()
    runQuery(conn)


if __name__ == "__main__":
    main()

#sample_code.py
#Displaying sample_code.py.
