import csv

def read_csv(path):
  with open(path, 'r', encoding='Latin-1') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      laptop_dict = {key: value for key, value in iterable}
      data.append(laptop_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./laptop_price.csv')
  print(data[0])




 