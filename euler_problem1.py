"""
if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Date: 08/15/16
"""


if __name__=='__main__':
    answer = 0

    multiples_of_three = int(999/3)
    multiples_of_five = int(999/5)
    multiples_of_fifteen = int(999/15)

    for i in range(0, 1000, 3):
       answer += i

    for i in range(0, 1000, 5):
        answer += i

    for i in range(0, 1000, 15):
        answer -= i

    print(answer)

