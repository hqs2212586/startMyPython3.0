rate = 3.25 * 0.01
count_year = 0
fund = 10000
n = 0
while fund < 20000:
    fund = fund * (1+rate)
    n += 1
    print("第",n,"年后本息为",fund)
