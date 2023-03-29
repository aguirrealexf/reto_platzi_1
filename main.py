import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./laptop_price.csv')
  #print(data[0])
  
  company = input('Type Company => ')
  #print(company)
  result = utils.product_by_company(data, company)
  #print(result)

  if len(result) > 0:
    #products = result[0]
    #print(products)
    labels, values = utils.get_product(result)
    charts.generate_bar_chart(labels, values)
  else:
    print('No entro al IF')

if __name__ == '__main__':
  run()