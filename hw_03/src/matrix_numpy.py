import numbers

import numpy as np


class StrNdarrayMixin:
    def to_str_value(self):
        return self.value.__str__()


class ToFileMixin:
    def to_file(self, filepath):
        with open(filepath, "w") as f:
            f.write(self.__str__())


class NdarrayValueProperties:
    @property
    def shape(self):
        return self.value.shape

    @property
    def data(self):
        return self.value

    @data.setter
    def data(self, new_value):
        if not isinstance(new_value, np.ndarray):
            raise TypeError("new value is not ndarray")
        self.value = new_value


class MatrixNumpy(np.lib.mixins.NDArrayOperatorsMixin, StrNdarrayMixin, ToFileMixin, NdarrayValueProperties):
    def __init__(self, value):
        self.value = np.asarray(value)

    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        inputs = tuple(x.value if isinstance(x, MatrixNumpy) else x
                       for x in inputs)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)

    def __str__(self):
        return self.to_str_value()
