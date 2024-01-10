def convert_list_to_tuple(data: list[list]) -> list[tuple]:
  converted_data = []
  data = data[1:]
  for item in data:
    list_item = item[0:3]
    list_item.append(int(item[3]))
    list_item.append(item[4])
    list_item.append(int(item[5]))
    converted_data.append(tuple(item))
  return converted_data