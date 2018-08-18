import pymysql
import logging
import dbConfig

conn = pymysql.connect(host=dbConfig.CHARSET, port=dbConfig.PORT,
                       user=dbConfig.USER, password=dbConfig.PASSWORD,
                       db=dbConfig.DB, charset=dbConfig.CHARSET)

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s %(funcName)s %(lineno)d %(levelname)s %(message)s',
                    filename='demo.log')


def test():
    cur = conn.cursor()
    sql = 'SELECT * from class WHERE id="1"'
    cur.execute(sql)
    temp = cur.fetchone()
    logging.debug(temp)
    conn.close()


if __name__ == "__main__":
    test()
