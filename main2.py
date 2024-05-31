class MyClass:
    def __init__(self, param1=None, param2=None):
        if param1 is not None and param2 is not None:
            self.__param1 = param1
            self.__param2 = param2
        elif param1 is not None:
            self.__param1 = param1
            self.__param2 = "default"
        else:
            self.__param1 = "default"
            self.__param2 = "default"

    @property
    def param1(self):
        return self.__param1

    @param1.setter
    def param1(self, value):
        self.__param1 = value

    @property
    def param2(self):
        return self.__param2

    @param2.setter
    def param2(self, value):
        self.__param2 = value

# Создание объектов
obj1 = MyClass()  # оба параметра имеют значение по умолчанию
obj2 = MyClass("test")  # param1 = "test", param2 имеет значение по умолчанию
obj3 = MyClass("test", "example")  # param1 = "test", param2 = "example"

print(obj1.param1)
print(obj2.param1)
print(obj3.param2)