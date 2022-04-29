# statistics

import statistics as stat

ages = [34, 23, 55, 67, 33, 23, 87, 33, 54, 11, 16, 20, 35, 91, 75, 80]

print(f"Mean age : {stat.mean(ages)}")
print(f"Median age : {stat.median(ages)}")
print(f"Mode age : {stat.mode(ages)}")
print(f"Varaince : {stat.variance(ages)}")
print(f"Standard Deviation : {stat.stdev(ages)}")
