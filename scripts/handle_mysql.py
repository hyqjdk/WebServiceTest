# -*- coding: utf-8 -*-
# 处理数据库
# @Time    : 2019/7/10 21:01
# @Author  : YoYo
import pymysql
from scripts.handle_config import ConfigLoader


class HandleMySql:
    """数据库处理类"""

    def __init__(self):
        config = ConfigLoader()
        self.conn = pymysql.connect(host=config.get_value("mysql", "host"),
                                    user=config.get_value("mysql", "user"),
                                    password=config.get_value("mysql", "password"),
                                    db=config.get_value("mysql", "db"),
                                    port=config.get_int("mysql", "port"),
                                    charset="utf8",
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def get_value(self, sql, args=None, is_more=False):
        """
        获取数据库的值
        :param sql: sql语句
        :param args: 其他参数
        :param is_more: 是否显示全部，默认显示一套条数据
        :return: 字典为item的列表数据
        """
        self.cursor.execute(sql, args)
        self.conn.commit()
        if is_more:
            return self.cursor.fetchall()
        else:
            return self.cursor.fetchone()

    def close(self):
        """关闭"""
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    handle_sql = HandleMySql()
    sql = "select * from member where MobilePhone = %s;"
    single_data = handle_sql.get_value(sql, "15828641020")
    print(single_data)