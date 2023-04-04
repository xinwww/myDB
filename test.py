from sqlParser import MySqlParser

myParser = MySqlParser()
sql = 'SELECT    AAA FROM    BBB WHERE  CCC=DDD'
sql_1 = 'SELECT'
sql_2 = 'SLEEET AAA FROM BBB'
# myParser.parse(sql)
# myParser.parse(sql_1)
# myParser.parse(sql_2)
sql_3 = 'DROP TABLE AAA'
sql_4 = 'DROP TABLE'
myParser.parse(sql_3)
sql_4 = 'USE BBB'
