def file_man(action, name, data_process):
    if action is "read":
        try:
            with open(name, 'r+') as file:
                data_read = file.read()
                return data_read
        except OSError:
            return "File not found."
    if action is "write":
        try:
            with open(name, 'r+') as file:
                file.write(data_process)
        except OSError:
            return "File already exists. Overwrite?"

    if action is "overwrite":
        with open(name, 'r+') as file:
            file.write(data_process)
        return "File saved."
