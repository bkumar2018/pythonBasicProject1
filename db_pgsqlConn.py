import psycopg2
print('Db connection program')



def getAllUsersData():
        
    try:
            
        ## Obtain a database connection
        conn = psycopg2.connect(user='postgres',password='********',host='127.0.0.1', port = '5432', database='sample_db')

        # Obtain a database cursor
        cur = conn.cursor()

        # print all data source name parameters of db connections
        print(conn.get_dsn_parameters())

        # Determine query to get rows
        query= 'select * from users'
        cur.execute(query)
        
        #record = cur.fetchone()   #to get one record
        record = cur.fetchall()    # to get all the records

        #Empty list to store the name from db
        names = []
        #print('The record', record)   # print all records
        for data in record:
            print(data)
            names.append(data[1])

        for name in names:
            print(name)

    except Exception as e:
        print(e)
    finally:
        if(conn):
            cur.close()
            conn.close()
            print("PostgresSql connection is closed.!")


def insertUserData(iquery):

    try:
       ## Obtain a database connection
        conn = psycopg2.connect(user='postgres',password='*******',host='127.0.0.1', port = '5432', database='sample_db')
        
        # Obtain a database cursor
        cur = conn.cursor()
        
        cur.execute(iquery)
        conn.commit()
        
        sqlSelect = "select * from users"
        cur.execute(sqlSelect)
        rows = cur.fetchall()
        # Print rows
        
        for row in rows:
            print(row)
    except Exception as e:
        print(e)
    finally:
        if(conn):
            cur.close()
            conn.close()
            print("PostgresSql connection is closed.!")



def deleteUserData(dquery):
    
    try:
       ## Obtain a database connection
        conn = psycopg2.connect(user='postgres',password='********',host='127.0.0.1', port = '5432', database='sample_db')
        
        # Obtain a database cursor
        cur = conn.cursor()    

        # execte query 
        cur.execute(dquery)

        #verify delete works
        squery = "Select * from users"
        cur.execute(squery)

        records = cur.fetchall()
        for data in records:
            print(data)
    except Exception as e:
        print(e)
    finally:
        cur.close()
        conn.close()
        print("PostgresSql connection is closed.!")






#getAllUsersData():
#insertUserData("insert into users values (8,'Vijay','Chavan','Satra',456123)")
#deleteUserData("delete from users where id=7")

