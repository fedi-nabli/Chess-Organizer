def convert_list_to_dicts(spreadsheet_items: list[list[str]]) -> list[dict]:
  column_names: list[str] = spreadsheet_items[0]
  rows: list[list[str]] = spreadsheet_items[1:]
  
  json_list: list[dict] = []

  for row in rows:
    row_dict = {}
    for idx in range(len(column_names)):
      if column_names[idx]:
        row_dict[column_names[idx]] = row[idx]
      else:
        row_dict[f'unknown_{idx}'] = row[idx]
    if row_dict is not None:
      json_list.append(row_dict)

  return json_list