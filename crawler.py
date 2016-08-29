import xml.dom.minidom
import requests

def __getElementByTagName(node,name):
    return [c for c in node.childNodes if c.tagName == name][0]

def __getElementListByTagName(node,name):
    return [c for c in node.childNodes if c.tagName == name]


def __get_clothes(app_id,cate_id):
    url = 'http://shopping.yahooapis.jp/ShoppingWebService/V1/itemSearch?appid={0}&category_id={1}&hits=50'.format(app_id,
                                                                                                               cate_id)
    r = requests.get(url)
    xml_data = r.text
    root = xml.dom.minidom.parseString(xml_data)
    resultNode = root.childNodes[0].childNodes[0]
    hidNodes = __getElementListByTagName(resultNode,'Hit')
    result = []
    for cate in hidNodes:
        name = __getElementByTagName(cate,'Name').childNodes[0].data
        code = __getElementByTagName(cate, 'Code').childNodes[0].data
        price = __getElementByTagName(cate, 'Price').childNodes[0].data
        img = __getElementByTagName(cate, 'Image')
        img_url = __getElementByTagName(img,'Medium').childNodes[0].data
        result.append({'name':name,'code':code,'price':price,'image':img_url})
    return result



if __name__ == '__main__':
    appid = 'dj0zaiZpPXRWQ3FKUURTMDVwWCZzPWNvbnN1bWVyc2VjcmV0Jng9Yzk-'

    data = []
    with open('categories.csv','r') as f:
        lines = f.readlines()
        for line in lines:
            data.append(line)

    with open('clothes.csv', 'w') as f:
        f.write('\"cloth_name\",\"cloth_code\",\"price\",\"image_url\",\"2big_type\",\"small_type\"\n')
        for i,d in enumerate(data):
            if i == 0:
                continue
            line = d.split(',')
            big_code = line[0]
            big_name = line[1]
            small_code = line[2]
            small_name = line[3].replace('\n','')
            result = __get_clothes(appid,small_code)

            for r in result:
                f.write('\"'+r['name']+'\",\"'+r['code']+'\",\"'+r['price']+'\",\"'+r['image']+'\",\"'+big_name+'\",\"'+small_name+'\"\n')
            print('category {0}'.format(i))