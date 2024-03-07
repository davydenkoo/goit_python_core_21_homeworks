#  FIRST
#
# def all_sub_lists(data):
#     result = [[]]

#     for i in range(len(data)):
#         result.append([data[i]])
#         tmp = [data[i]]
#         for j in range(i + 1, len(data)):
#             tmp.append(data[j])
#             result.append(tmp.copy())
#     return result

# print(all_sub_lists([4, 6, 1, 3]))

#  SECOND
#
def all_sub_lists(data):
    result = [[]]
    sub_list_size = 1

    while sub_list_size <= len(data):

        for i in range(len(data)):
            if i + sub_list_size > len(data):
                break
            tmp_list = []
            for j in range(sub_list_size):
                tmp_list.append(data[i + j])
            result.append(tmp_list)

        sub_list_size += 1

    return result

print(all_sub_lists([4, 6, 1, 3]))
