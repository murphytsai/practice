"""
1_2_3_45_67_8_9 = 100
_ can be + - * / 
Try to use brute-force method to check if formula match the result.
final output
1.0 + 2.0 + 3.0 - 45.0 + 67.0 + 8.0 * 9.0 = 100.0
1.0 * 2.0 + 3.0 + 45.0 + 67.0 - 8.0 - 9.0 = 100.0
1.0 * 2.0 * 3.0 - 45.0 + 67.0 + 8.0 * 9.0 = 100.0

"""

t='1.0 {0} 2.0 {1} 3.0 {2} 45.0 {3} 67.0 {4} 8.0 {5} 9.0'
o=['+', '-', '*', '/']

def gen_cal():
    for v0 in o:
        for v1 in o:
            for v2 in o:
                for v3 in o:
                    for v4 in o:
                        for v5 in o:
                            yield t.format(v0, v1, v2, v3 ,v4 ,v5)
for cal in gen_cal():
    if float(eval(cal))==100.0:
        print cal,'=',float(eval(cal))
        
