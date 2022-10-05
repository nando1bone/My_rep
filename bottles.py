word = 'бутылок путча '
for beer_num in range(99,0,-1):
    print(beer_num, word, 'пива на стене.')
    print(beer_num, word, 'пива.')
    print('возьми одну.'); print('пусти по кругу.')
    if beer_num == 1:
        print('нет бутылок пива на стене.')
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = 'bottle'
            print(new_num, word, 'of beer on the wall.')
    print()
