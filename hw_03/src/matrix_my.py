class HashDataMixin:
    def sum_squares_hash(self):
        """
            Вычисляет хэш путём подсчёта сумм квадратов элементов
        """
        return sum(sum(x * x for x in line) for line in self._data)


class ToFileMixin:
    def to_file(self, filepath):
        with open(filepath, "w") as f:
            f.write(self.__str__())


class MatrixMy(HashDataMixin, ToFileMixin):
    _matmul_cache = {}

    @property
    def shape(self):
        return self._shape

    def __init__(self, data):
        self._shape = (len(data), len(data[0]))
        self._data = []
        for line in data:
            if len(line) != self._shape[1]:
                raise Exception("Incorrect dimensions")
            self._data.append(list(line))

    def __eq__(self, o: object) -> bool:
        return isinstance(o, MatrixMy) and self._data == o._data

    def __add__(self, other):
        if not isinstance(other, MatrixMy):
            raise Exception("Other is not MatrixMy")
        if self._shape != other._shape:
            raise Exception(
                "Matrix must have same dimensions " + self._shape.__str__() + " vs " + other._shape.__str__())
        return MatrixMy(
            [[self._data[i][j] + other._data[i][j] for j in range(self._shape[1])] for i in range(self._shape[0])]
        )

    def __mul__(self, other):
        if not isinstance(other, MatrixMy):
            raise Exception("Other is not MatrixMy")
        if self._shape != other._shape:
            raise Exception(
                "Matrix must have same dimensions " + self._shape.__str__() + " vs " + other._shape.__str__())
        return MatrixMy(
            [[self._data[i][j] * other._data[i][j] for j in range(self._shape[1])] for i in range(self._shape[0])]
        )

    def __matmul__(self, other):
        if not isinstance(other, MatrixMy):
            raise Exception("Other is not MatrixMy")
        if self._shape[1] != other._shape[0]:
            raise Exception(
                "Incompatible dimensions" + self._shape.__str__() + " and " + other._shape.__str__())
        key = (self.__hash__(), other.__hash__())
        if key not in self._matmul_cache:
            self._matmul_cache[key] = MatrixMy([
                [sum(a * b for a, b in zip(self_row, other_col)) for other_col in zip(*other._data)]
                for self_row in self._data])
        return self._matmul_cache[key]

    def __str__(self) -> str:
        return "[" + ",\n".join(str(line) for line in self._data) + "]"

    def __hash__(self):
        return self.sum_squares_hash()
