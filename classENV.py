import pymysql
import logging
import dbConfig

conn = pymysql.connect(host=dbConfig.HOST, port=dbConfig.PORT,
                       user=dbConfig.USER, password=dbConfig.PASSWORD,
                       db=dbConfig.DB, charset=dbConfig.CHARSET)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s %(funcName)s line[%(lineno)d] %(levelname)s %(message)s')


def queryUser():
    items = None
    try:
        cur = conn.cursor()
        sql = 'SELECT id, name, age from class;'
        logging.debug(sql)
        cur.execute(sql)
        items = cur.fetchall()
        logging.debug(items)
    except pymysql.Error as e:
        logging.debug(e)
        conn.rollback()
    finally:
        conn.close()

    aList = []
    aDict = {}
    if not items:
        return aList

    for item in items:
        aDict['id'] = item[0]
        aDict['name'] = item[1]
        aDict['age'] = item[2]
        aList.append(dict.copy(aDict))
        logging.debug(aDict)
    logging.debug(aList)
    return aList

def addUser(name, age):
    try:
        cur = conn.cursor()
        sql = 'INSERT INTO class(name, age) VALUES ("%s", %s);'%(name, age)
        logging.debug(sql)
        cur.execute(sql)
        conn.commit()
        logging.debug("SQL Insert success!")
        return True
    except pymysql.Error as e:
        logging.debug(e)
        conn.rollback()
    finally:
        conn.close()

def updateUser(id, name, age):
    try:
        cur = conn.cursor()
        sql = 'UPDATE class SET name = "%s", age=%s WHERE id = %s'%(name,age,id)
        logging.debug(sql)
        cur.execute(sql)
        conn.commit()
        logging.debug("SQL Update success!")
        return True
    except pymysql.Error as e:
        logging.debug(e)
        conn.rollback()
    finally:
        conn.close()

def deleteUser(id):
    try:
        cur = conn.cursor()
        sql = 'DELETE FROM class WHERE id=%s'%(id)
        logging.debug(sql)
        cur.execute(sql)
        conn.commit()
        logging.debug("SQL Delete success!")
        return True
    except pymysql.Error as e:
        logging.debug(e)
        conn.rollback()
    finally:
        conn.close()



if __name__ == "__main__":
    #temp = queryUser()
    #logging.debug(temp)
    #addUser(name="小明", age=23)
    #updateUser(id=1, name="许多", age=13)
    deleteUser(1)