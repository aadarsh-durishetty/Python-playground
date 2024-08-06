# tuple for confidential data table

lab_reading = {}
n = int(input('enter no of tests to run:'))
for i in range(n):
    test_name = input()
    min = int(input())
    max = int(input())
    lab_reading[test_name] = (min,max)
print(lab_reading)

# patients record logic
check1 = input('enter the test:')
value1 = int(input('enter value:'))
for data in lab_reading.values():
    min = data[0]
    max = data[1]
print(max,min)
if (min < value1 < max):
    print('normal')
else:
    print('abnormal')


















