import read_csv

def get_product(company_dict):
  labels = [item['Product'] for item in company_dict]
  #labels = [item['Product']+'-'+item['Cpu'] for item in company_dict]
  values = [item['Price_euros'] for item in company_dict]
  return labels, values


def product_by_company(data, company):
  result = list(filter(lambda item: item['Company'] == company, data))
  return result