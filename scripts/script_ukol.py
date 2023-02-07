import requests, zipfile, io
import xml.etree.ElementTree as ET
import sys
from pprint import pprint
from collections import defaultdict

class MyParser:

    def __init__(self, url_of_file=None, path_fox_xml=None, path_to_xml=None) -> None:
        self._url_of_file = url_of_file or 'https://www.retailys.cz/wp-content/uploads/astra_export_xml.zip' 
        self._path_for_xml = path_fox_xml or './xml'
        self._path_to_xml = path_to_xml or './xml/export_full.xml'
    def download_n_unzip(self):

        try: 
            r = requests.get(self._url_of_file, stream=True)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall(self._path_for_xml)
        except Exception as e:
            return f'Something went wrong with dowload and unpacking of xml file... {e}'
        else:
            return ('File successfuly downloaded and unziped into ./xml location...')

    def _get_root(self):
        tree = ET.parse(self._path_to_xml)
        return tree.getroot()

    def parse_products(self): 
        products = self._get_root().findall('./items/item')
        return products

    def parse_products_with_parts(self):
        res = defaultdict(set)
        root = self._get_root()
        
        for item in root.findall('./items/item'):
            for part in item.findall("./parts/part[@name='Náhradní díly']/item"):
                res[item.attrib['name']].add(part.attrib['name'])
        
        return res

    def get_count_of_products(self):
        return len(self._get_root()[0])

    
if __name__=='__main__':
    parser = MyParser()

    try:
        if sys.argv[1] == '-c':
            print(f'Count of products in xml file is: {parser.get_count_of_products()}')
        
        elif sys.argv[1] == '-l':
            for product in parser.parse_products():
                print(product.attrib['name'])

        elif sys.argv[1] == '-ln': 
            for key, products in parser.parse_products_with_parts().items():
                print(f'{key}\n{len(products)} náhradích dílu\n')
                pprint(products, indent=2, width=150)

        elif sys.argv[1] == '-it': 
            for key, products in parser.parse_products_with_parts().items():
                print(f'{key}\n{len(products)} náhradích dílu\n')
                pprint(products, indent=2, width=150)
                input()

        elif sys.argv[1] == '-d':
            print(parser.download_n_unzip())

        else:
            print('Run script with single param: python script.py -x x[-c (count products), -l (listing products), -ln (nested list), -it (nested list partialy) -d (download)]')
            
    except IndexError:
        print('Run script with single param: python script.py -x x[-c (count products), -l (listing products), -ln (nested list), -it (nested list partialy) -d (download)]')
    
    except Exception as e:
        print(e)
















    
        
