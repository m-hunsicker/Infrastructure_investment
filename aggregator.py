from enum import Enum, unique
from functools import reduce


@unique
class Operator(Enum):
    ADD = 1
    SUB = 2
    MULT = 3
    DIV = 4


class Aggregator(object):
    """
    This class represents the links between a parent component and one or more child(ren)
    This is required when
    parent: shall be a Component class
    parent: shall be a Component class or An Aggregator class
    """

    def __init__(self, parent, children, operator):
        """
        :param parent: A Component Class or an Aggregator
        :param children: A list of Components
        :param operator: A value listed in the Operator enumclass
        """
        self.parent = parent
        self.children = children
        self.operator = operator

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, operator):
        if not isinstance(operator, Operator):
            raise ValueError("Aggregator operator not in the list")
        self._operator = operator

    def aggregate(self):
        assert (self.children != []), "No existing sub-component to aggregate"
        data_list = [k.data for k in self.children]
        if self.operator == Operator.ADD:
            data = reduce((lambda x, y: x.add(y)), data_list)
        elif self.operator == Operator.SUB:
            assert len(data_list) == 2, "More than 2 sub-components to substract in aggregate"
            data = reduce((lambda x, y: x.sub(y)), data_list)
        elif self.operator == Operator.MULT:
            assert len(data_list) > 1, "Less than 2 sub-components to multiply in aggregate"
            data = reduce((lambda x, y: x.mul(y)), data_list)
        elif self.operator == Operator.DIV:
            assert len(data_list) == 2, "More than 2 sub-components to DIV in agregator"
            data = reduce((lambda x, y: x.div(y)), data_list)
        else:
            raise (Exception, "Aggregator Class: Operation not implemented")

        if self.parent.data is None:
            self.parent.data = data
        else:
            self.parent.data = self.parent.data.add(data, fill_na=0)
