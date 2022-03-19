duration = int(input("Введите время в секундах: "))
s = duration
d = duration // 86400
h = duration % 86400 // 3600
m = duration % 86400 % 3600 // 60
s = duration % 86400 % 3600 % 60
if 86400 > duration >= 3600:
    print(h, "час", m, "мин", s, "сек")
elif 3600 > duration >= 60:
    print(m, "мин", s, "сек")
elif duration < 60:
    print(s, "сек")
else:
    print(d, "дн", h, "час", m, "мин", s, "сек")
