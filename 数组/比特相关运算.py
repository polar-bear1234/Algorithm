num = 3
result = bin(num)[2:]

origin_num = int(result, 2)
print(type(result), origin_num)
# print('0' * 3)
# def insertBits(N, M, i, j):
#     N_bin = bin(N)[2:]
#     M_bin = bin(M)[2:]
#     n_size = len(N_bin)
#     m_size = len(M_bin)
#     if m_size < j - i + 1:
#         add_num = j - i + 1 - m_size
#         M_bin = '0' * add_num + M_bin
#     N_bin = list(N_bin)
#     N_bin[n_size - j - 1: n_size - i] = list(M_bin)
#     return int(''.join(N_bin), 2)


N = 1143207437
M = 1017033
i = 11
j = 31
result = insertBits(N, M, i, j)
print(result)