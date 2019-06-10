# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import pymysql

host = settings['MYSQL_HOST']
user = settings['MYSQL_USER']
database = settings['MYSQL_DATABASE']
passwd = settings['MYSQL_PASSWORD']

class BossPipeline1(object):
    def process_item(self, item, spider):
        my_sql = pymysql.connect(host=host, user=user, password=passwd, database=database, charset='utf8')
        cursor = my_sql.cursor()
        if item['come_from'] == 'company':
            company = item['company']
            # company_url = item['company_url']
            scale = item['scale']
            status = item['status']
            kind = item['kind']
            job_number = item['job_number']

            sql = """
                    insert into t_boss_company
                    (name,scale,status,kind,number)
                    VALUES 
                    ('%s','%s','%s','%s','%s')
                    """ %(company,scale,status,kind,job_number)
        elif item['come_from'] == 'job':
            company = item['company']
            job = item['job']
            salary = item['salary']
            work_place = item['work_place']
            experience = item['experience']
            education = item['education']
            sql = """
                    insert into t_boss_job
                    (company,name,salary,work_place,experience,education)
                    VALUES 
                    ('%s','%s','%s','%s','%s','%s')
                    """ %(company,job,salary,work_place,experience,education)
        elif item['come_from'] == 'job_class':
            company = item['company']
            name = item['job_classification']
            number = item['job_class_number']

            sql = """
                    insert into t_boss_jobclass
                    (company,name,number)
                    VALUES 
                    ('%s','%s','%s')
                    """ %(company,name,number)
        cursor.execute(sql)
        my_sql.commit()
        cursor.close()
        my_sql.close()
        return item

# class BossPipeline2(object):
#     def process_item(self, item, spider):
#         if item['come_from'] == 'job':
#             # date = item['date']
#             company = item['company']
#             job = item['job']
#             salary = item['salary']
#             work_place = item['work_place']
#             experience = item['experience']
#             education = item['education']
#
#             my_sql = pymysql.connect(host=host,user=user,password=passwd,database=database,charset='utf8')
#             cursor = my_sql.cursor()
#             sql = """
#                     insert into t_boss_job
#                     (company,name,salary,work_place,experience,education)
#                     VALUES
#                     ('%s','%s','%s','%s','%s','%s')
#                     """ %(company,job,salary,work_place,experience,education)
#             cursor.execute(sql)
#             my_sql.commit()
#             cursor.close()
#             my_sql.close()
#
#             # return item
#
# class BossPipeline3(object):
#     def process_item(self, item, spider):
#         if item['come_from'] == 'job_class':
#             # date = item['date']
#             company = item['company']
#             name = item['job_classification']
#             number = item['job_class_number']
#
#             my_sql = pymysql.connect(host=host,user=user,password=passwd,database=database,charset='utf8')
#             cursor = my_sql.cursor()
#             sql = """
#                     insert into t_boss_jobclass
#                     (company,name,number)
#                     VALUES
#                     ('%s','%s','%s')
#                     """ %(company,name,number)
#             cursor.execute(sql)
#             my_sql.commit()
#             cursor.close()
#             my_sql.close()
#
#             # return item

