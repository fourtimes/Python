# 1 - 99 => tens
# 100 - 999 = > hundreds
# 1000 - 9999 => thousands
# 10000 - 99999 => ten thousands
# 100000 - 999999 => lakhs
# 1000000 - 9999999 => ten lakhs
# 10000000 - 99999999 => cores

number = 10975

if number >= 10000000:
    print('crores')
elif number <= 9999999 and number >= 1000000:
    print('tens of lakhs')
elif number <= 999999 and number >= 100000:
    print('lakhs')
elif number <= 99999 and number >= 10000:
    print('tens of thousand')
elif number <= 9999 and number >= 1000:
    print('thousands')
elif number <= 999 and number >= 100:
    print('hundreds')
else:
    print('tens')


# number = 109000
# value = print('one core') if number == 10000000 else (print('ten lakhs') if number <= 9999999 and number >= 1000000 else (print('lakhs') if number <= 999999 and number >= 100000 else (
#     print('ten thousands') if number <= 99999 and number >= 10000 else (print('thousand') if number <= 9999 and number >= 1000 else (print('hundreds') if number <= 999 and number >= 100 else (
#         print('tens') if number <= 999 and number >= 100 else print('limit exceeds')))))))
