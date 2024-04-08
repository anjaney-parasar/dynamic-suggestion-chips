from gemini import chipgenerator

def separator(res):
  chip1, chip2, chip3= str.split(res, "\n")
  return chip1, chip2, chip3

result= chipgenerator("Jaipur")
print(separator(result)[0])