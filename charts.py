import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots(figsize=(10, 8))
  ax.bar(labels, values)
  plt.xticks(rotation=45)
  plt.show()

def generate_pie_chart(labels, values):
  fig, ax = plt.subplots(figsize=(10, 8))
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  generate_bar_chart(labels, values)
  #generate_pie_chart(labels, values)