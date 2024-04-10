S = int(input())

d = int((S / 3600) // 24)
h = int((S / 3600) % 24 )
S = S % 3600
m = int(S / 60)
s = int(S % 60)

ds = int(bool(d//2))
hs = int(bool(h//2))
ms = int(bool(m//2))
ss = int(bool(s//2))

dy = ["day","days"]
hr = ["hour","hours"]
mn = ["minute","minutes"]
sc = ["second.","seconds."]

print(d,dy[ds],h,hr[hs],m,mn[ms],s,sc[ss])
print(d,h,m,s)

'''
1 day 6 hours 50 minutes 1 second.
n = 8000;        // ค่าที่อินพุทเข้ามา
h = n / 3600;        // หาร 3600 จะได้จำนวนชั่วโมง = 2
n = n % 3600;        // หารเอาเศษ 3600 จะเหลือ 800 วินาที
m = n / 60;        // หาร 60 จะได้จำนวนนาที = 13
s = n % 60;        // หารเอาเศษ 60 จะเหลือ 20 วินาที
'''
