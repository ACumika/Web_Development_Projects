from bs4 import BeautifulSoup
import unittest

def read_html(path_to_file):
    handle = open(path_to_file, "r", encoding='utf-8')
    html = handle.read()
    soup = BeautifulSoup(html, 'lxml')
    body = soup.find('div', id="bodyContent")
    handle.close()
    return body

def img_count(body):
    imgs = body.find_all('img', width = True)
    count = 0
    for i in imgs:
        if int(i['width'])>=200:
            count+=1
    return count

def headers_count(body):
    heads = body.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    count = 0
    for h in heads:
        if h.text[0]=='C' or h.text[0]=='T' or h.text[0]=='E':
            count +=1
    return count

def max_a(body):
    counts = []
    a_list = body.find_all('a')
    for ass in a_list:
        count = 1
        for sib in ass.find_next_siblings():
            if sib.name == 'a':
                count = count + 1
            else:
                break
            counts.append(count)
    return max(counts)

def olul_count(body):
    ou_list=body.find_all('ol')
    ou_list = ou_list + body.find_all('ul')
    print(len(ou_list))
    count = 0
    for ou in ou_list:
        #print(ou.parent.name)
        if not ou.find_parents(['ul', 'ol','li']):
            count = count +1
    print(count)
    return count

def parse(path_to_file):
    body = read_html(path_to_file)
    imgs = img_count(body)
    headers = headers_count(body)
    linkslen = max_a(body)
    lists = olul_count(body)

    return [imgs, headers, linkslen, lists]

if __name__ == '__main__':
    parse('wiki/Artificial_intelligence')

class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
        )

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


#if __name__ == '__main__':
#    unittest.main()
