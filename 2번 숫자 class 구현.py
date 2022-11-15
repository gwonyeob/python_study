class Calculator :
    special = ()
    sum= 0

    def __init__(number, *num):
        number.special = num
        for i in number.special:
            number.sum += i

    def sum_(number):
        return number.sum
    
    def avg_(number):
        return number.sum/len(number.special)

cal_1 = Calculator(1,2,3,4,5)
print(cal_1.sum_())
print(cal_1.avg_())
cal_2 = Calculator(4,5,6)
print(cal_2.sum_())
print(cal_2.avg_())