class SingletonValue(type):
    """
        Метакласс для уменьшения потребления памяти повторяющимися инстансами соответствующих классов (кэширование)
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        hash_ = hash((cls, *args, *kwargs.items()))
        if hash_ not in cls._instances:
            cls._instances[hash_] = super(SingletonValue, cls).__call__(*args, **kwargs)
        return cls._instances[hash_]
