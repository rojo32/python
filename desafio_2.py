def fix_me(nested_list):
 
  final_list = []
  for idx, a_list in enumerate(nested_list):
    partial_sum = 0
    for basic_element in a_list:
      partial_sum += basic_element

    if idx % 2 == 0:
      partial_sum *= -1

    final_list.append(partial_sum)

  return final_list

a = {'nested_list': [[1, 2], [3, 4]]}

fixed_list = fix_me(a['nested_list'])
print(fixed_list)