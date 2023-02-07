from pytest import fixture
from scripts.script_ukol import MyParser
import os

@fixture
def path():
    return os.path.abspath('./fixtures/testing_xml.xml')

def test_count(path):
    parser = MyParser(path_to_xml=path)
    r = parser.get_count_of_products()
    assert r == 2

def test_list_of_products(path):
    parser = MyParser(path_to_xml=path)
    r = parser.parse_products()
    assert r[0].attrib['name'] == 'Arrma motor střídavý BLX3660 4P 3200ot/V'
    assert r[1].attrib['name'] == 'NO_PARTS_PRODUCT'

def test_list_of_products_with_parts(path):
    parser = MyParser(path_to_xml=path)
    r = parser.parse_products_with_parts()
    assert r['Arrma motor střídavý BLX3660 4P 3200ot/V'] == {'Kuličkové ložisko 4 x 13 x 5mm MR624ZZ (2)', 'Kuličkové ložisko 5x16x5mm 625ZZ (2)'}
    assert len(r) == 1



    







