# TODO Найдите количество книг, которое можно разместить на дискете

volume = 1.44
page = 100
line = 50
symbol = 25
keep = 4

print("Количество книг, помещающихся на дискету:", round((volume * 1024 * 1024) // (page * line * symbol * keep)))
