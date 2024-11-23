from pprint import pprint
import inspect

class Introsp:
    def __init__(self, obj):
        self.obj = obj

    def introspection_info(self):
        dic_obj = {}
        dic_obj['type'] = type(self.obj).__name__
        list_a = []
        list_m = []
        for dat in dir(self.obj):
            if callable(getattr(self.obj, dat)):
                list_m.append(dat)

            else:
                list_a.append(dat)
        dic_obj['methods'] = list_m
        dic_obj['attributes'] = list_a
        dic_obj['module'] = inspect.getmodule(self)
        dic_obj['length_str'] = len(str(self.obj))
        print(f'Объект <<{self.obj}>>:')
        return dic_obj

obj1 = Introsp(42)
obj2 = Introsp('some_function_module')
obj3 = Introsp([1, 2, 3, 4])
obj4 = Introsp(pprint)

pprint(obj1.introspection_info())
pprint(obj2.introspection_info())
pprint(obj3.introspection_info())
pprint(obj4.introspection_info())