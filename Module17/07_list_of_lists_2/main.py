nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

# TODO здесь писать код
new_list = [nice_list[idx_1][idx_2][idx_3] for idx_1 in range(2) for idx_2 in range(3) for idx_3 in range(3)]
print('Ответ: ', new_list)


