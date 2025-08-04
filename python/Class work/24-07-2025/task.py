d1 = {'p': 600, 'q': 300, 'r': '400'}
d2 = {'p': 300, 'q': 200}
ans = {}

for key in d2:
    if key in d1 and isinstance(d1[key], (int, float)) and isinstance(d2[key], (int, float)):
        ans[key] = d1[key] + d2[key]

print(ans)
