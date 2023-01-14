from db import TasksDB

db = TasksDB()
# print('DB READY')

prompt = '> '
separator = '----------------------------------------------'
welcome = 'hola, esta es la consola, elegi una opcion'
main_menu = f'1 - ver tareas\n2 - insertar tarea\n3 - editar tarea\n4 - eliminar tarea \n5 - vaciar lista de tareas\n0 - salir\n{prompt}'
edit_task_menu = f'\n-Elegi una opcion: \n1 - Nombre \n2 - Descripcion \n3 - Estado \n0 - volver\n{prompt}'


def main():
    print(separator)
    print(welcome)
    op = input(main_menu)
    while op != '0':
        if op != 'await':
            resp, op = switch(op)
            print(separator)
            if type(resp) != bool:
                for task in resp:
                    print(f'$ - {task}')
            else:
                print(f'$ - Accion: {resp}')
        else:
            print(separator)
            print('\nhola, esta es la consola de la lista de tareas, elegi una opcion')
            op = input(main_menu)
    else:
        print('Hasta luego')


def switch(op):
    """"TODO op 3 & 4, hacer diccionario y que el usuario interactue con una lista de opciones en vez de
    tener que copiar y pegar el id"""
    if op == '1':
        tasks_list = db.find()
        op = 'await'
        return tasks_list, op

    elif op == '2':
        payload = {}
        payload['name'] = input(f'Escribi el nombre de la tarea\n{prompt}')
        check_is_empty(payload['name'], '2')
        payload['description'] = input(f'Escribi la descripcion de la tarea\n{prompt}')
        check_is_empty(payload['description'], '2')
        payload['ready'] = False
        resp = db.insert_one(payload)
        op = 'await'
        return resp, op

    elif op == '3':
        payload = {}
        tasks_id = []
        tasks = create_select_menu()
        for task in tasks:
            tasks_id.append(str(task['_id']))
        db_id = input(f'pega el id aqui: {prompt}')
        check_is_empty(db_id, '3')
        if db_id in tasks_id:
            task = next((x for x in tasks if str(x['_id']) == db_id), None)
            id_for_console = task['_id']
            status_for_arg = task['ready']
            print(separator)
            print(f'Editando la tarea {id_for_console}')
            int_op = input(edit_task_menu)
            while int_op != '0':
                if int_op == '1':
                    nombre = input(f'Inserta el nuevo nombre: {prompt}')
                    db.edit_one({'name': nombre}, id_for_console)
                    print(separator)
                    print('nombre actualizado')
                if int_op == '2':
                    descripcion = input(f'Inserta la nueva descripcion: {prompt}')
                    db.edit_one({'description': descripcion}, id_for_console)
                    print(separator)
                    print('Descripcion actualizada')
                if int_op == '3':
                    confirmation = input(f'Pulsa 1 para confirmar\n')
                    if confirmation == '1':
                        db.edit_one({'ready': not status_for_arg}, id_for_console)
                        print(separator)
                        print(f'Se cambio el {status_for_arg}, ahora es {not status_for_arg}')
                        int_op = 'invalid'
                    else:
                        print('No se confirmo la modificacion')
                        int_op = 'invalid'
                else:
                    print(separator)
                    print(f'Editando la tarea {id_for_console}')
                    int_op = input(edit_task_menu)
            else:
                main()

        else:
            print(separator)
            print('id incorrecto')
            switch('3')
            raise 'tarea no encontrada'

    elif op == '4':
        tasks_id = []
        tasks = create_select_menu()
        for task in tasks:
            tasks_id.append(str(task['_id']))

        db_id = input(f'pega el id aqui: {prompt}')
        check_is_empty(db_id, '4')

        if db_id in tasks_id:
            task = next((x for x in tasks if str(x['_id']) == db_id), None)
            id_for_console = task['_id']
            resp = db.delete_one(id_for_console)
            print(separator)
            print(resp)
            main()
        else:
            print(separator)
            print('id incorrecto')
            switch('4')

    elif op == '5':
        result = db.delete_many()
        print(separator)
        print(f'{result} tareas eliminadas')
        main()

    elif op == '0':
        return

    else:
        print(separator)
        print('la opcion que elegiste no es correcta, o todavia no esta lista')
        main()


def check_is_empty(prop, op):
    if len(prop) < 2:
        print('el campo insertado es muy corto, vamos de nuevo')
        switch(op)
    else:
        pass


def create_select_menu():
    print(separator)
    print('A continuacion veras una lista de tareas y su id, copia y pega el id de la tarea que quieras editar')
    tasks = db.find()
    for task in tasks:
        task_id = task['_id']
        task_name = task['name']
        print(f' - {task_id} {task_name}')
    return tasks


if __name__ == "__main__":
    main()