# import random
# # test_list = [[random.randint(0,3) for i in range(3)] for i in range(100)]

# # for i in test_list:
# #     print(i)


# # test_list_sorted = sorted(test_list, key =  lambda x: (x[0],x[2], x[1]))
# # print("=====================")
# # for i in test_list_sorted:
# #     print(i)


# test_list = [[random.randint(0,3) for i in range(3)] for i in range(3)]
# for row in test_list:
#     print(row)
# print("=====================")
# # print(list(zip(*test_list[::-1])))
# new_list = list(zip(*test_list[::1]))
# for row in new_list:
#     print(row)
# print("=====================")
# # print(list(zip(*test_list)))
# # test_col = list(zip(*test_list))
# # print(test_col)
# # print("=====================")

# # print(list(zip(*test_col)))

# # test_list = [1,23,-1, -2, 10, 9, 123]
# # print([test for test in test_list if test > 0])


# input = [ 
# [2, 2, -1, 3, 1],
# [-2, -2, 2, 0, -1],
# [-2, -1, -2, 1, 2],
# [-1, -2, 1, 3, 2],
# [-2, -2, 2, 2, 1]]
# input = [
# (-2, -1, -2, -2, 2),
# (-2, -2, -2, -2, 2),
# (2, 1, -2, 2, -1),
# (2, 3, 1, 0, 3),
# (1, 2, 2, -1, 1),
# ]
# input_column = list(zip(*input[::-1]))
# for i in input_column:
#     print(i)
# for column in input_column:
#     list_of_black = [i for i in range(len(column)) if column[i] == -1]
#     # list_of_black = [i for i in input_column if i == -1]
#     print("=================")
#     print(column)
#     if(len(list_of_black) > 0):
#         i = 0
#         new_row = []
#         for black_index in list_of_black:
#             sliced_row = list(column[i:black_index])
#             sliced_new_row = [node for node in sliced_row if node > -2]
#             sliced_new_row += [-2 for i in range(len(sliced_row)-len(sliced_new_row))]
#             new_row += sliced_new_row
#             i = black_index
#         sliced_row = sliced_row = list(column[i:])
#         sliced_new_row = [node for node in sliced_row if node > -2]
#         sliced_new_row += [-2 for i in range(len(sliced_row)-len(sliced_new_row))]
#         new_row += sliced_new_row
#         print(new_row) 
# direction_list = [(-1,0),(1,0),(0,-1),(0,1)]
# def make_student_spare_map_dict(N):
#     student_spare_map = dict()
#     for y in range(N):
#         for x in range(N):
#             cnt = 0
#             for direction in direction_list:
#                 next_y = y+direction[0]
#                 next_x = x+direction[1]
#                 if not next_y < 0 and not next_x < 0 and not next_y >= N and not next_x >= N:
#                     cnt += 1
#                 student_spare_map[(y,x)] = cnt
#     return student_spare_map

# # print(make_student_spare_map_dict(3))
# result = make_student_spare_map_dict(3)

# items = result.items()
# print(items)
# items_sorted = sorted(items, key = lambda x : (-x[1], x[0][0], x[0][1]))
# print(items_sorted)

# result.clear()
# print(result)

import math
print(math.pow(10,0))