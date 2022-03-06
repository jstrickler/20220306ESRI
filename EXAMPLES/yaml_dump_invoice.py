from pprint import pprint
import yaml


with open('../DATA/invoice.yaml') as invoice_in:
    invoice_data = yaml.load(invoice_in, Loader=yaml.BaseLoader)

pprint(invoice_data)


