from re import findall

def num_to_text(s):
    nums = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 0: 'ноль'}
    r = []
    for i in s:
        r.append(nums[int(i)])
    return ' '.join(r)

k = 2
buffer_len, res = 130, []
work_buffer_len = buffer_len
with open("text.txt", "r") as file:
    while True:
        buffer = file.read(buffer_len)
        if not buffer:
            break
        res.extend(findall(r'[0-9]{1,}', buffer))
        while len(res) >= 10:
            for el in res:
                if res.count(el) > k:
                    print(' '.join(res[:9]), num_to_text(res[9]))
                    break
            del res[:10]