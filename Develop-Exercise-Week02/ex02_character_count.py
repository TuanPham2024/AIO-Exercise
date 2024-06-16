
# Câu hỏi 2.  Hoàn thành chương trình sau với mô tả bài toán từ câu I.2. Đầu ra của chương trình dưới đây là gì?
def character_count(word):
  character_statistic = {} # character_statistic = dict()
  # Your Code Here
  for character in word:
    if character != ' ':
      character_statistic[character] = character_statistic.get(character, 0) + 1
    # print(character_statistic
  return character_statistic

# Examples
# string = 'Happiness'
# print(character_count( string ))

assert character_count ("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(character_count ('smiles'))