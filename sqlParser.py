from re import compile

class MySqlParser:

    def __init__(self):

        self.__operation_map = {
            'SELECT': self.__select,
            'INSERT': self.__insert,
            'UPDATE': self.__update,
            'DELETE': self.__delete,
            'CREATE': self.__create,
            'DROP': self.__drop,
            'INDEX': self.__index,
            'USE': self.__use,
            'EXIT': self.__exit,
            'JOIN': self.__join,
            'SHOW': self.__show
        }

        self.__relation_map = {
            'SELECT': r'(SELECT|select) (.*) (FROM|from) (.*)',
            'INSERT': r'(INSERT|insert) (INTO|into) (.*) \((.*)\) (VALUES|values) \((.*)\)',
            'INSERT_2': r'(INSERT|insert) (INTO|into) (.*) (VALUES|values) \((.*)\)',
            'UPDATE': r'(UPDATE|update) (.*) (SET|set) (.*)',
            'DELETE': r'(DELETE|delete) (FROM|from) (.*)',
            'CREATE': r'(CREATE|create) (TABLE|table) (.*) \((.*)\)',
            'CREATE DATABASE': r'(CREATE|create) (DATABASE|database) (.*)',
            'CREATE INDEX': r'(CREATE|create) (INDEX|index) (.*) (ON|on) (.*) \((.*)\)',
            'DROP INDEX': r'(DROP|drop) (INDEX|index) (.*) (ON|on) (.*)',
            'GROUPBY': r'(.*) (GROUP|group) (BY|by) (.*)'
        }

    # remove the space in sql
    def __remove_space(self, s):
        res = []
        for word in s:
            if word.strip() == '' or word == 'AND':
                continue
            res.append(word)
        return res

    # parse the sql
    def parse(self, sql):

        # seperate sql into base_statement and condition
        # sql = ['SELECT AAA FROM BBB ', ' CCC AND DDD']
        if "where" in sql:
            sql = sql.split("where")
        else:
            sql = sql.split("WHERE")

        base_statement = self.__remove_space(sql[0].split(' '))
        print(base_statement)

        # length of sql < 2 and not 'exit', error
        if len(base_statement) < 2 and base_statement[0].lower() != 'exit':
            print('Syntax Error')
            return

        if "JOIN" in base_statement or "join" in base_statement:
            operation_type = 'JOIN'
        else:
            # get operation type
            operation_type = base_statement[0].upper()

        # wrong operation type, error
        if operation_type not in self.__operation_map:
            print('Syntax Error')
            return

        operation = self.__operation_map[operation_type](base_statement)
        print(operation)

    def __select(self, statement): None
         

    def __insert(): None

    def __update(): None
    
    def __delete(self, statement): 
        return {
            'type' : 'delete',
            'table' : statement[2]
        }
    
    def __create(): None

    def __drop(self, statement):
        kinds = statement[1]
        if len(statement) < 3:
            print('Syntax Error')
            return
        
        if kinds.upper() == 'DATABASE':
            return {
                'type' : 'drop',
                'kind' : 'database',
                'name' : statement[2]
            }
        
        elif kinds.upper() == 'TABLE':
            return {
                'type' : 'drop',
                'kind' : 'table',
                'name' : statement[2]
            }
        
        elif kinds.upper() == 'INDEX':
            return{}
        
        print('Syntax Error')
        return


    def __index(): None

    def __use(self, statement):
        return {
            "type": 'use',
            "datebase": statement[1]
        }
    
    def __exit(self, _):
        return {
            'type' : 'exit'
        }

    def __join(): None

    def __show(self, statement):
        kinds = statement[1]

        if kinds.upper() == 'DATABASES':
            return {
                'type' : 'show',
                'kind' : 'databases'
            }
        
        if kinds.upper() == 'TABLES':
            return {
                'type' : 'show',
                'kind' : 'tables'
            }




        

        





