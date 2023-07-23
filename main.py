class GraduationCeremonySolution:

    def __init__(self, no_of_days, absent_limit):
        """
        :param no_of_days: No of days in Graduation year
        :param absent_limit: No of allowed absent limit days
        """
        self.no_of_days = no_of_days
        self.allowed_limit = absent_limit
        self.no_of_ways_to_attend_classes, self.prob_to_skip_grad_ceremony = self.solve()

    def solve(self):
        """
        This method will compute the total no of ways to attend the college and return the probability
        to skip the graduation ceremony.
        """
        dp = [1 for _ in range(self.allowed_limit + 1)]
        temp = [0 for _ in range(self.allowed_limit + 1)]
        dp[self.allowed_limit] = 0

        for i in range(1, self.no_of_days + 1):
            for index in range(self.allowed_limit+1):
                temp[index] = 0
            for j in range(self.allowed_limit):
                temp[j] = dp[0] + dp[j + 1]
            temp, dp = dp, temp

        total_no_of_ways_to_attend_class = dp[0]
        no_of_ways_to_miss_last_day = temp[1]
        prob_to_skip_grad_ceremony = f"{no_of_ways_to_miss_last_day}/{total_no_of_ways_to_attend_class}"
        print("#"*50)
        print(f"1. The number of ways to attend classes over {self.no_of_days} days.: {total_no_of_ways_to_attend_class}")
        print(f"2. The probability to miss your grad ceremony for {self.no_of_days} days.: {prob_to_skip_grad_ceremony}")
        print("#" * 50)
        return total_no_of_ways_to_attend_class, prob_to_skip_grad_ceremony


def run_test_cases():
    test_cases = [5, 10, 100, 1000, 10000]
    for college_days in test_cases:
        GraduationCeremonySolution(no_of_days=college_days, absent_limit=4)


if __name__ == '__main__':
    no_of_days = int(input("No of days in Graduation year: "))
    absent_limit = int(input("No of absent limit days: "))

    GraduationCeremonySolution(no_of_days, absent_limit)
