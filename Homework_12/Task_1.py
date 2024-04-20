
class Google:

    projects = ['Chrome', 'Android', 'Drive', 'Gmail', 'YouTube']

    def __init__(self, projects, income, stocks_is_rise=True):
        self.projects = projects
        self.income = income
        self.stocks_is_rise = stocks_is_rise

    def check_stocks(self):
        if self.stocks_is_rise is True:
            return 'stocks is falling'
        else:
            return 'stocks is rising'


    def get_income(self):
        return self.income

    def get_projects(self):
        return self.projects


