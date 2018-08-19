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
        sql = 'SELECT id, name, age from class'
        logging.debug(sql)
        cur.execute(sql)
        items = cur.fetchall()
        logging.debug(items)
    except pymysql.Error as e:
        logging.debug(e)

    aList = []
    aDict = {}
    for item in items:
        aDict['id'] = item[0]
        aDict['name'] = item[1]
        aDict['age'] = item[2]
        aList.append(dict.copy(aDict))
        logging.debug(aDict)
    logging.debug(aList)

    conn.close()
    return aList


if __name__ == "__main__":
    temp = queryUser()
    logging.debug(temp)
