class Phase(pd.Series):
    """
    Aims at defining the operation of each non ponctual phase of an infrastructure
    project (eg. permitting, construction, operations...)
    components
    """

    def __init__(self, name, duration, period_step, previous=None, start_date=None):
        """
        Args:
            name(string): the name of the phase. Must be unique for each project.
            duration(datetime.Duration): number of periods of the phase
            period_step(int): lenght of each period of the phase.
            previous(Phase): reference of the previous phase if any (used to determine the start date)
            start_date(datetime.Date): beginning of the date
        """
        self.name = name
        self.previous = None
        if previous != None:
            self.time_series = Time_Series(previous.date_end + 1, time_step)
        elif date_start != None:
            self.time_series = Time_Series(previous.date_end + 1, time_step)
        else:
            raise Exception("Start date cours not be initiated")  #

    def add_component(self, new_component):
        for k in self.components:
            if k.name == new_component.name:
                raise (ValueError, "Component name already taken")
            self.components.append(new_component)

    def delete_component(self, component_name):
        for k in self.components:
            if k.name == component_name:
                self.components.remove(k)
