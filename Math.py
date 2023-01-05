class Math:
    def append_sums(self, given_list):

        for i in range(25):
            sum_three = given_list[-1] + given_list[-2] + given_list[-3]
            given_list.append(sum_three)


if __name__ == '__main__':
    practice = Math()
    given_list = [0, 1, 2]
    practice.append_sums(given_list)
    print(given_list[20])
