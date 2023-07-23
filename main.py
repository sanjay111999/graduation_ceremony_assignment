class GraduationCeremonySolution:

    def __init__(self, no_of_days, absent_limit):
        self.N = no_of_days
        self.M = absent_limit


if __name__ == '__main__':
    no_of_days = int(input("No of days in Graduation year: "))
    absent_limit = int(input("No of absent limit days: "))

    GraduationCeremonySolution(no_of_days, absent_limit)
