dsa = int(input('Enter DSA Marks: '))
os = int(input('Enter OS Marks: '))
math = int(input('Enter Math Marks: '))
english = int(input('Enter English Marks: '))

if dsa <= 100 and os <= 100 and math <= 100 and english <= 100:
    avg = float((dsa + os + math + english) / 4)
    if avg >= 80:
        print('Science admission')
    elif avg >= 60:
        print('Commerce admission')
    elif avg >= 40:
        print('Arts admission')
    else:
        print('Not eligible for any stream')
else:
    print('Enter numbers out of 100')
