def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj)
                  if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    methods = [method for method in dir(obj)
               if callable(getattr(obj, method)) and not method.startswith("__")]
    obj_module = obj.__class__.__module__
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': obj_module
    }
    return info

obj_info = introspection_info('hello')
print(obj_info)

