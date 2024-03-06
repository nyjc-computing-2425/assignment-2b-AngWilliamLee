num = input('Enter a number (decimal only): ')
# type your code here


index = num.find('.')
num1 = num[index+1:]

dp = len(num1)

# do not change any code beyond this point
print('The number', num, 'has', dp, 'decimal places.')
