import mysql.connector
from mysql.connector import Error



def makeDBConnection():
        
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='sys',
                                            user='root',
                                            password='********')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def createDB(dbname):
    try:
        conn = mysql.connector.connect(host='localhost',user='root',password='********', database='sample_db')
        if(conn.is_connected()):
            cur = conn.cursor()
            # cur.execute('select database()')
            # alldbs= cur.fetchall()
            # print(alldbs)
            # print(alldbs[0])
            createDBQuery = 'create database '+ dbname
            cur.execute(createDBQuery)
            # if 'sample_db' not in alldbs[0]:
            #     #cur.execute('create database sample_db')
            #     #print(cur.fetchone())
            #     print('run command to create db')
            # else:
            #     print('sample_db exists!')
    except Exception as e:
        print(e)
    finally:
        if(conn.is_connected()):
            cur.close()
            conn.close()
            print('Conncetion closed!')


def createTable(tblname):
    try:
        conn = mysql.connector.connect(host='localhost',user='root',password='*****',database='sample_db')
        if(conn.is_connected()):
            cur = conn.cursor()
            createTblQuery = 'create table '+tblname+'( id integer, name varchar(10))'
            cur.execute(createTblQuery)            
            conn.commit()  

    except Exception as e:
        print(e)
    finally:
        if(conn.is_connected()):
            cur.close()
            conn.close()
            print('Connection Closed!')


def insertDataInTbl(mySql_insert_query):
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='*********', database='sample_db')
        cur = conn.cursor()
        cur.execute(mySql_insert_query)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        if(conn.is_connected()):
            cur.close()
            conn.close()
            print('Connection closed')


def selectDataInTbl(mysql_select_query):
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='*******', database='sample_db')
        cur = conn.cursor()
        cur.execute(mysql_select_query)
        records = cur.fetchall()
        for record in records:
            print(record)
        return records
    except Exception as e:
        print(e)
    finally:
        if(conn.is_connected()):
            cur.close()
            conn.close()
            print('Connection closed')
            


#makeDBConnection()
#createDB('test_db')
#createTable('login1')

# mySql_insert_query = "insert into login values(2, 'abhi', '1234')"
# insertDataInTbl(mySql_insert_query)

# mysql_select_query = "select * from login"
# selectDataInTbl(mysql_select_query)





