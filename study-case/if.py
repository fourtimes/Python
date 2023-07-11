# 1 - 99 => tens
# 100 - 999 = > hundreds
# 1000 - 9999 => thousands
# 10000 - 99999 => ten thousands
# 100000 - 999999 => lakhs
# 1000000 - 9999999 => ten lakhs
# 10000000 - 99999999 => cores

value = 100088000999

if value >= 10000000:
    print("crores")
elif value >= 1000000 and value <= 9999999:
    print("tens of lakhs")
elif value >= 100000 and value <= 999999:
    print("lakhs")
elif value >= 10000 and value <= 99999:
    print("tens of thousands")
elif value >= 1000 and value <= 9999:
    print("thousands")
elif value >= 100 and value <= 999:
    print("hundreds")
else:
    print("tens")
