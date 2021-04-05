import power as pow
import root as sqrt
import module as mod
import division as div
#import multiplication as mult

a = int(input('Введите a: '))
b = int(input('Введите b: '))

def formula(num1, num2):
    res = div.division(pow.power(num1)+sqrt.root(pow.power(pow.power(num2)-mod.module(num1)+5*num1*num2)),sqrt.root(pow.powe(pow.power(num1)-mod.module(num2)+5*num2*num1))-5)
    return res
