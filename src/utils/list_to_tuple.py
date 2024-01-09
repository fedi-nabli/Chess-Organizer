def convert_list_to_tuple(data: list[list]) -> list[tuple]:
  converted_data = []
  for item in data:
    converted_data.append(tuple(item))
  return converted_data