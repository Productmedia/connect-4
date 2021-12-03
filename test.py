object = {"row": "", "col": "", "value": ""}
storing_values = []


for i in range(0, 20, 2):
  object["row"] = i + i
  object["col"] = 20
  object["value"] = "hi there"
  storing_values.append(object)



print(storing_values)