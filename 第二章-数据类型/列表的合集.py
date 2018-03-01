iphone7 = ['alex','rain','jack','old_driver']
iphone8 = ['alex','shanshan','jack','old_boy']

both_list = []

for name in iphone8:
    if name in iphone7:
        both_list.append(name)

print(both_list)