import sys

data = [['Туника "Линда" сухая роза ', 'rash.su/files/catalog/photos/2043/img/tunika-linda-suhaya-roza-2043-4-2.jpg',
         'Хлопок 100% (кулирка)', ['490', '490'], ['46', '56']],
        [
            'Туника "Линда" голубая ', 'rash.su/files/catalog/photos/2042/img/tunika-linda-golubaya-2042-3-2.jpg', 'Хлопок 100 % (кулирка)', [
                '490', '490', '490', '490', '490', '490'], ['46', '48', '50', '52', '54', '56']],
        [
            'Туника "Юкатан" ', 'rash.su/files/catalog/photos/2034/img/tunika-yukatan-2034-6-2.jpg', 'Хлопок 100% (кулирка)', [
                '600', '600', '600'], ['50', '58', '60']],
        [
            'Туника "Оригами" ', 'rash.su/files/catalog/photos/2026/img/tunika-origami-2026-5-2.jpg', 'Хлопок 100% (кулирка)', [
                '490', '490', '490'], ['44', '46', '58']],
        [
            'Туника "Руслана" ', 'rash.su/files/catalog/photos/2020/img/tunika-ruslana-2020-3-2.jpg', 'Хлопок 100% (кулирка)', [
                '700', '700', '700', '700', '700'], ['50', '52', '54', '56', '58']],
        [
            'Туника "Джейн" ', 'rash.su/files/catalog/photos/1993/img/tunika-djeyn-1993-2-2.jpg', 'Хлопок 100% (кулирка)', [
                '515', '515', '515', '515', '515', '515'], ['46', '48', '50', '52', '54', '56']],
        [
            'Туника "Этника" ', 'rash.su/files/catalog/photos/1958/img/tunika-etnika-1958-5-2.jpg', 'Хлопок 100% (кулирка)', [
                '600', '600', '600', '600', '600', '600'], ['50', '52', '54', '56', '58', '60']],
        [
            'Туника "Узелки" ', 'rash.su/files/catalog/photos/1923/img/tunika-uzelki-1923-16-2.jpg', 'Хлопок 100% (кулирка)', [
                '390', '390', '390', '390', '390', '390'], ['46', '48', '50', '52', '54', '56']],
        [
            'Туника "Терри" ', 'rash.su/files/catalog/photos/1914/img/tunika-terri-1914-3-2.jpg', 'Хлопок 100% (кулирка)', [
                '525', '525', '525', '525', '525', '525', '525'], ['48', '50', '52', '54', '56', '58', '60']],
        [
            'Туника "Тигрица" ', 'rash.su/files/catalog/photos/1899/img/tunika-tigrica-1899-1-2.jpg', 'Хлопок 100% (кулирка)', [
                '450', '450', '450', '450'], ['48', '50', '52', '54']],
        [
            'Туника "Уэльс" ', 'rash.su/files/catalog/photos/1884/img/tunika-uels-1884-2-2.jpg', 'Хлопок 73%, п/э 22%, лайкра 5%', [
                '550', '550'], ['46', '56']],
        [
            'Туника "Равенна" ', 'rash.su/files/catalog/photos/1882/img/tunika-ravenna-1882-4-2.jpg', 'Хлопок 73%, п/э 22%, лайкра 5%', [
                '730', '730', '730', '730', '730'], ['48', '50', '52', '54', '56']],
        [
            'Туника "Керри" ', 'rash.su/files/catalog/photos/1864/img/tunika-kerri-1864-1-2.jpg', 'Вискоза 100% (штапель)', [
                '875', '875'], ['46', '48']],
        [
            'Туника "Океан" ', 'rash.su/files/catalog/photos/1832/img/tunika-okean-1832-1-2.jpg', 'Хлопок 100% (кулирка)', [
                '420', '420', '420', '420', '420'], ['46', '48', '50', '52', '54']],
        ['Туника "Юна" ', 'rash.su/files/catalog/photos/1784/img/tunika-yuna-1784-5-2.jpg', 'Хлопок 100% (кулирка)', [
        '570', '570', '570', '570', '570', '570'], ['46', '48', '50', '52', '54', '56']],
        [
            'Туника "Nobby" ', 'rash.su/files/catalog/photos/1741/img/tunika-Nobby-1741-1-2.jpg', 'Хлопок 100% (кулирка)', [
                '390', '390', '390', '390', '390', '390'], ['46', '48', '50', '52', '54', '56']],
        [
            'Туника "Санта" II ', 'rash.su/files/catalog/photos/1711/img/tunika-santa-II-1711-4-2.jpg', 'Хлопок 100% (кулирка)', [
                '840', '840', '840', '840', '840', '840', '840'], ['46', '48', '50', '52', '54', '56', '58']],
        [
            'Туника "Иволга" ', 'rash.su/files/catalog/photos/1707/img/tunika-ivolga-1707-1-2.jpg', 'Хлопок 100% (кулирка)', [
                '360', '360', '360', '360', '360', '360'], ['46', '48', '50', '52', '54', '56']],
        [
            'Туника "Бергамо" ', 'rash.su/files/catalog/photos/1693/img/tunika-bergamo-1693-4-2.jpg', 'Хлопок 100% (кулирка)', [
                '400', '400', '400', '400', '400'], ['46', '48', '50', '52', '54']],
        [
            'Туника "Magic" ', 'rash.su/files/catalog/photos/1618/img/tunika-Magic-1618-5-2.jpg', 'Хлопок 100% (кулирка)', [
                '540', '540', '540', '540', '540', '540'], ['46', '48', '50', '52', '54', '56']],
        [
            'Туника "Авокадо" ', 'rash.su/files/catalog/photos/1609/img/tunika-avokado-1609-1-2.jpg', 'Хлопок 100% (кулирка)', [
                '450'], ['46']],
        [
            'Туника "Суоми" ', 'rash.su/files/catalog/photos/1237/img/tunika-suomi-1237-1-2.jpg', 'Хлопок 100% (интерлок)', [
                '500', '500', '500'], ['50', '52', '54']],
        [
            'Туника "Узелки" II ', 'rash.su/files/catalog/photos/610/img/tunika-uzelki-II-610-2-2.jpg', '\xa0Хлопок 100% (кулирка)', [
                '435'], ['46']]],


def write(mas):
    result = open('outfile.csv', mode='a', encoding='utf8')
    for line in mas[0]:
        for i in range(len(line[-1])):
            res = [line[0], line[1], line[2], line[3][i], line[4][i]]
            for elem in res:
                result.write(str(elem) + (";" if res.index(elem) < len(res) - 1 else '\n'))
    result.close()

    #     for i in range(len(line[-1]) - 1):
    #         res = [line[0], line[1], line[2], line[3][i], line[4][i]]
    #         result.write(str(res) + (";" if line.index(elem) < len(line) - 1 else '\n'))
    # result.close()
    #

write(data)
