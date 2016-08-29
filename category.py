import requests
import xml.dom.minidom

def __getElementByTagName(node,name):
    return [c for c in node.childNodes if c.tagName == name][0]

def __getElementListByTagName(node,name):
    return [c for c in node.childNodes if c.tagName == name]


def __get_category(app_id,cate_id):
    url = 'http://shopping.yahooapis.jp/ShoppingWebService/V1/categorySearch?appid={0}&category_id={1}'.format(app_id,
                                                                                                               cate_id)
    r = requests.get(url)
    xml_data = r.text
    root = xml.dom.minidom.parseString(xml_data)
    categoriesNode = root.childNodes[0].childNodes[0].childNodes[0].childNodes
    bigCategory = ''
    result = []
    for cate in categoriesNode:

        if cate.tagName == 'Current':
            title = __getElementByTagName(cate, 'Title')
            short = __getElementByTagName(title, 'Short')
            data = short.childNodes[0].data
            bigCategory = data
        if cate.tagName == 'Children':
            childs = __getElementListByTagName(cate,'Child')
            for c in childs:

                title = __getElementByTagName(c, 'Title')
                short = __getElementByTagName(title, 'Short')
                data = short.childNodes[0].data
                result.append((bigCategory,data))
    return result





if __name__ == '__main__':
    appid = 'dj0zaiZpPXRWQ3FKUURTMDVwWCZzPWNvbnN1bWVyc2VjcmV0Jng9Yzk-'

    #categories for fashion
    categories = ['2494','2495','2496']
    all_result = []
    for cate in categories:
        result = __get_category(appid,cate)
        all_result.extend(result)

    with open('categories.csv','w') as f:
        for data in all_result:
            f.write(data[0]+','+data[1]+'\n')

    print('owari')

