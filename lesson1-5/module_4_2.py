def test_function():
    def inner_fuction():
        print("Я в области видимости функции test_function")
        return
    inner_fuction()
    return
test_function()
# inner_function() NameError: name 'inner_function' is not defined.
# Did you mean: 'test_function'?
#Функция 'inner_function' находится в нутри локальной области ф-ии 'test_function'
#Из глобальной области она не видима name 'inner_function' is not defined