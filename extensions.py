file_name = input('File name: ').lower()

if '.' not in file_name:
    print("application/octet-stream")
else:
    file_name_split  = file_name.split('.')

    name_file = file_name_split[0].strip() # Selects the first element and cleans the string
    extension = file_name_split[-1].strip() # Selects the last element and cleans the string

    dict_extensions = {'gif': 'image/gif',
                       'jpg': 'image/jpeg',
                       'jpeg': 'image/jpeg',
                       'png': 'image/png',
                       'pdf': 'application/pdf',
                       'txt': f'text/{name_file}',
                       'zip': 'application/zip'}

    if extension in dict_extensions.keys(): # Checks if the extension is in the dictionary
        print(dict_extensions[extension])
    else:
        print('application/octet-stream')
