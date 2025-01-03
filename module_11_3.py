import inspect

def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)

    def methods():
        return methods.__dir__()

    module = obj.__class__.__module__
    function = inspect.getmembers(obj, inspect.isfunction)

    dictionary = {'type': obj_type, 'attributes': attributes, 'methods': methods(), 'module': module}
    return dictionary


info = introspection_info(55)
print(info)
string_info = introspection_info('Tест')
print(string_info)
dict_info = introspection_info({'Тест': 1})
print(dict_info)