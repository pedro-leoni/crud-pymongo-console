from pymongo import MongoClient


class TasksDB:
    def __init__(self):
        """CREAR BASE DE DATOS, COLECCION E INSERTAR OBJETO MANUALMENTE DESDE CONSOLA O UI DE PREFERENCIA
        TODO automatizar el proceso anterior, crear la db si no existiera y hacer que sea visible introduciendo
        un elemento"""
        print('loading DB')
        self.client = MongoClient('localhost')
        self.db = self.client['todo_console']
        self.tasks = self.db['tasks']
        print('DB ready')

    def find(self):
        tasks_list = list(self.tasks.find({}))
        return tasks_list

    def find_one(self, task_id):
        task = dict(self.tasks.find({'_id': task_id}))
        return task

    def insert_one(self, payload):
        try:
            self.tasks.insert_one(payload)
            return True
        except Exception as err:
            print(err)
            raise 'raise'

    def edit_one(self, payload, task_id):
        try:
            self.tasks.find_one_and_update({'_id': task_id}, {"$set": payload})
        except Exception as err:
            print(err)
            raise 'error editando'

    def delete_one(self, task_id):

        print(task_id)
        result = self.tasks.delete_one({'_id': task_id})
        if result.deleted_count == 1:
            return 'tarea eliminada'
        else:
            return 'tarea no encontrada'


    def delete_many(self):
        try:
            result = self.tasks.delete_many({})
            return result.deleted_count
        except Exception as err:
            print(err)
            raise 'error delete many'