from generator.tree.nodes.node import Node
from generator.tree.helpers.basictype import BasicType
from generator.tree.errors import InvalidConstantValueError

class Constant(Node):
    def __init__(self, name, properties=None, own_schema=None):
        super(Constant, self).__init__(name=name, properties=properties)
        self._own_schema = own_schema
        self._value = int(properties.value, 0)
        if self.type.bits_required(self.value) > self.type.width:
            raise InvalidConstantValueError(name=name, value=self.value)

    @staticmethod
    def create(properties, own_schema, definition):
        result = Constant(name=properties.name, properties=properties, own_schema=own_schema)
        return result

    @property
    def type(self):
        return BasicType(self._properties.type)

    @property
    def doc(self):
        return self._properties.doc

    @property
    def value(self):
        return self._value
