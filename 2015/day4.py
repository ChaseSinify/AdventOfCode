from hashlib import md5
key = "yzbqklnj"
i = 0
while True:
    input = f'{key}{i}'
    result = md5(input.encode()).hexdigest()
    if str(result)[:6] == '000000': #part two just changes this to 6 ... | if str(result)[:5] == '00000':
        print(i)
        break
    i += 1