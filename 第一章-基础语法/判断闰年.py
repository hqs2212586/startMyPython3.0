year = int(input("type the year:"))
if year % 4 == 0 and year %100 != 0:
    print(year, "is 闰年！")
elif year % 400 ==0:
    print(year, "is 闰年！")
else:
    print(year, "is 平年！")