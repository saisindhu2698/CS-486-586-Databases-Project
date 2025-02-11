import psycopg2
import pandas as pd

def initialize():
    connection = psycopg2.connect(
        user = "postgres", #username that you use
        password = "*******", 
        host = "localhost", 
        port = "5432", 
        database = "postgres"
    )
    connection.autocommit = True
    return connection
    
   

def runQuery(conn):
    select_Query =  "select \"IssuerId\",\"IssuerId2\" from servicearea where (\"IssuerId\" + \"IssuerId2\")>'80000' and \"VersionNum\" > '7';"
    servicearea_df = pd.DataFrame(columns = ['IssuerId','IssuerId2'])
    with conn.cursor() as cursor:
        cursor.execute(select_Query)
        records = cursor.fetchall()
        
        for row in records:
            output_df = {'IssuerId': row[0],'IssuerId2': row[1]}
            servicearea_df = servicearea_df.append(output_df, ignore_index=True)
    
        print(servicearea_df)

def main():
    conn = initialize()
    runQuery(conn)


if __name__ == "__main__":
    main()

#sample_code.py
#Displaying sample_code.py.
