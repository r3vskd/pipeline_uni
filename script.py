import sys
for line in sys.stdin:
raw_phone_number = line.strip()
    
    
    area_code = raw_phone_number[0:3]
    first_three = raw_phone_number[3:6]
    
    last_four = raw_phone_number[6:]
    
    print('(%s) %s-%s' % (area_code, first_three, last_four))