from enum import Enum, unique

from utils import is_subperiod, is_superperiod


@unique
class Type1(Enum):
    """
    Level: meaning it is equal over each sub period
    Quantity: quantity has to be divide by each sub period
    Singular: quantity can't be divided but should be deducted by the index that should be
    """
    LEVEL = 1  # speed metaphor
    QUANTITY = 2  # distance metaphor


@unique
class Type2(Enum):
    """
    Type financial
    """
    FINANCIAL = 1
    PHYSICAL = 2


@unique
class Category(Enum):
    HYPOTHESIS = 1
    COMPUTED = 2


class Component(object):
    def __init__(self, name, type_1, type_2, component_category, uom):
        self.name = name
        self.type_1 = type_1  # Financial or physical SEE if mandatory
        self.type_2 = type_2  # Level or quantity
        self.category = component_category  # Hypothesis or computed
        self.unit_of_measure = uom
        self.level = 0  # presentation level
        self.aggregator_list = []
        self.data = None
        self.data_adjusted = None

    @property
    def type_1(self):
        return self._type_1

    @type_1.setter
    def type_1(self, type_1):
        if not isinstance(type_1, Type1):
            raise ValueError("Component Type1 not in the list")
        self._type_1 = type_1

    @property
    def type_2(self):
        return self._type_2

    @type_2.setter
    def type_2(self, type_2):
        if not isinstance(type_2, Type2):
            raise ValueError("Component type2 value not in the list")
        self._type_2 = type_2

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(category, Category):
            raise ValueError("Category value not in the list")
        self._category = category

    @property
    def start_date(self):
        return self.data.index[0].start_time

    @property
    def end_date(self):
        return self.data.index[-1].end_time

    def time_adjust_data(self, period_index):
        """
        Adapts the original time index to a new time index whith different frequency and/or longer duration
        WARNING: loffset is used to adjust for an issue in resample that makes otherwise the previous month.
        :param period_index: Time index of the overall component
        :return: Nothing
        """
        # Adjust for frequency
        data_buffer = self.data.copy()
        # Transformation to daterequired because the M is not recognized as a sub-period of 3M for example
        data_buffer.index = data_buffer.index.astype('datetime64[ns]')
        # Warning
        sampler = data_buffer.resample(period_index.freq, closed='left', label='left', loffset='D')

        # Apply specific sampling operation depending of the case.

        if is_subperiod(self.data.freq, period_index.freq):
            if self.type_1 == Type1.LEVEL:
                data_buffer = sampler.mean()
            elif self.type_1 == Type1.QUANTITY:
                data_buffer = sampler.sum()
            else:
                raise (ValueError, "Type1 value not in list")

        if is_superperiod(self.data.freq, period_index.freq):
            if self.type_1 == Type1.LEVEL:
                data_buffer = sampler.bfill()  # TO BE CHECKED
            elif self.type_1 == Type1.QUANTITY:
                data_buffer = sampler.sum()  # TO BE CORRECTED
            else:
                raise (ValueError, "Type1 value not in list")

        # Period reconstruction since PeriodIndex was transformed to DatetimeIndex
        sampler.index.astype('period[' + period_index.freq + ']')

        # Adjust for duration
        pass

        self.data_adjusted = data_buffer
