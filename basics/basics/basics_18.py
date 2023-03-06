### В заданной строке расположить в обратном порядке все слова. Разделителями слов считаются пробелы.###
import string

list = ["London" "is" "the" "capital" "of" "Great" "Britain"]
print("London is the capital of Great Britain")
string = ["London", "is", "the", "capital", "of", "Great", "Britain"]

string[0:6:1]

string[::-6]
print(string[::-1])
