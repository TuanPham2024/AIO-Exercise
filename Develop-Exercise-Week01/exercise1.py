#1/  Viết function thực hiện đánh giá classification model bằng F1-Score
# try:
#   tp = int(input("Nhập vào giá trị (True  Positive) tp = "))
#   fp = int(input("Nhập vào giá trị (False Positive) fp = "))
#   fn = int(input("Nhập vào giá trị (False Negative) fn = "))
#   # tn = int(input("Nhập vào giá trị (True Negative)  tn = "))

#   if tp <= 0 or fp <= 0 or fn <= 0:
#     print(f"Error data, tp = {tp} and fp = {fp} and fn = {fn} must be greater than 0")
# except ValueError:
#   print("tp, fp, fn must be int!")

def precision(tp, fp):
  return tp / (tp + fp)

def recall(tp, fn):
  return tp / (tp + fn)

def f1_score(tp, fp, fn):
  result_precision = precision(tp, fp)
  result_recall = recall(tp, fn)
  return (2 * result_precision * result_recall) / (result_precision + result_recall)

def exercise1(tp, fp, fn):
  """
  ## Parameter
    tp: True Positive
    fp: False Positive
    fn: False Negative
  -----------------------
  ## Return
    Return message precision, recall, f1_score
  """
  list_input = [tp, fp, fn]
  list_error = ["tp", "fp", "fn"]

  for i in range(len(list_input)):
    if not(isinstance(list_input[i], int)):
      print(list_error[i] + " must be int!")
      return

  if tp <= 0 or fp <= 0 or fn <= 0:
    print(f"Data Error, tp = {tp} and fp = {fp} and fn = {fn} must be greater than 0")
    return
  
  print("Data is good, tp = {tp} and fp = {fp} and fn = {fn}")
  print(f"Precision is {precision(tp, fp)}")
  print(f"Recall is {recall(tp, fn)}")
  print(f"F1_score is {f1_score(tp, fp, fn)}")

exercise1(2, 3, 4)

exercise1 (tp="a", fp =3, fn =4)

exercise1(2.1,3,0)

exercise1(1,3,2)

exercise1(1,3,-2)