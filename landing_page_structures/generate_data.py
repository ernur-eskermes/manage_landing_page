import requests
from lxml import html

from .models import Block, Text, Image

PARAMS = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}
URL = 'https://therealschool.ru/'


def get_html(url, params):
    req = requests.get(url=url, params=params)
    return req.text


def get_data_from_landing_page(landing_html):
    landing_html = get_html(url=URL, params=PARAMS)

    tree = html.fromstring(landing_html)

    block_data = {}

    block1_text1 = ''.join(tree.xpath('//*[@id="rec266956626"]/div/div/div[3]/h1/span[1]/text()')) + \
                   ''.join(tree.xpath('//*[@id="rec266956626"]/div/div/div[3]/h1[1]/text()')) + \
                   ''.join(tree.xpath('//*[@id="rec266956626"]/div/div/div[3]/h1[2]/text()')) + \
                   ''.join(tree.xpath('//*[@id="rec266956626"]/div/div/div[3]/h1/span[2]/text()'))
    block1_text2 = ''.join(tree.xpath('//*[@id="rec266956626"]/div/div/div[4]/div/text()'))
    block1_text3 = ''.join(tree.xpath('//*[@id="rec266956626"]/div/div/div[5]/a/text()'))
    block1_text4 = ''.join(tree.xpath('//*[@id="rec266956626"]/div/div/div[9]/a/text()'))
    block1_image1 = ''.join(tree.xpath('//*[@id="rec266956626"]/div/div/div[8]/div/img/@src'))
    block_data['block1'] = {'text': [block1_text1, block1_text2, block1_text3, block1_text4],
                            'image': [block1_image1]}

    block2_text1 = ''.join(tree.xpath('//*[@id="rec266966303"]/div/div/div[3]/div/text()'))
    block2_text2 = ''.join(tree.xpath('//*[@id="rec266966303"]/div/div/div[6]/div/text()'))
    block2_text3 = ''.join(tree.xpath('//*[@id="rec266966303"]/div/div/div[4]/div[1]/text()')) + \
                   ''.join(tree.xpath('//*[@id="rec266966303"]/div/div/div[4]/div/span/text()')) + \
                   ''.join(tree.xpath('//*[@id="rec266966303"]/div/div/div[4]/div[2]/text()'))
    block2_image1 = ''.join(tree.xpath('//*[@id="rec266966303"]/div/div/div[5]/div/img/@src'))
    block2_image2 = ''.join(tree.xpath('//*[@id="rec266966303"]/div/div/div[9]/div/img/@src'))
    block2_image3 = ''.join(tree.xpath('//*[@id="rec266966303"]/div/div/div[7]/div/img/@src'))
    block2_image4 = ''.join(tree.xpath('//*[@id="rec266966303"]/div/div/div[8]/div/img/@src'))
    block_data['block2'] = {'text': [block2_text1, block2_text2, block2_text3],
                            'image': [block2_image1, block2_image2, block2_image3, block2_image4]}

    block3_text1 = ''.join(tree.xpath('//*[@id="rec267037254"]/div/div/div[15]/div/text()'))
    block3_text2 = ''.join(tree.xpath('//*[@id="rec267037254"]/div/div/div[16]/div/text()'))
    block3_text3 = ''.join(tree.xpath('//*[@id="rec267037254"]/div/div/div[8]/div/text()'))
    block3_text4 = ''.join(tree.xpath('//*[@id="rec267037254"]/div/div/div[9]/div/text()'))
    block3_text5 = ''.join(tree.xpath('//*[@id="rec267037254"]/div/div/div[12]/div/text()'))
    block3_text6 = ''.join(tree.xpath('//*[@id="rec267037254"]/div/div/div[14]/div/text()'))
    block3_text7 = ''.join(tree.xpath('//*[@id="rec267037254"]/div/div/div[21]/div/text()'))
    block3_text8 = ''.join(tree.xpath('//*[@id="rec267037254"]/div/div/div[22]/div/text()'))
    block3_text9 = ''.join(tree.xpath('//*[@id="rec267037254"]/div/div/div[25]/div/text()'))
    block3_text10 = ''.join(tree.xpath('//*[@id="rec267037254"]/div/div/div[28]/div/text()'))
    block_data['block3'] = {'text': [block3_text1, block3_text2, block3_text3, block3_text4, block3_text5,
                                     block3_text6, block3_text7, block3_text8, block3_text9, block3_text10],
                            'image': []}

    block4_text1 = ''.join(tree.xpath('//*[@id="rec267044041"]/div/div/div[4]/div/text()'))
    block4_text2 = ''.join(tree.xpath('//*[@id="rec267044041"]/div/div/div[5]/div/text()'))
    block4_text3 = ''.join(tree.xpath('//*[@id="rec267044041"]/div/div/div[6]/a/text()'))
    block_data['block4'] = {'text': [block4_text1, block4_text2, block4_text3],
                            'image': []}

    return block_data


def set_data_to_db():
    data = get_data_from_landing_page(landing_html=html)
    block1, _ = Block.objects.get_or_create(sorting=1)
    block2, _ = Block.objects.get_or_create(sorting=2)
    block3, _ = Block.objects.get_or_create(sorting=3)
    block4, _ = Block.objects.get_or_create(sorting=4)

    for block, texts_and_images in data.items():
        for key, value in data.items():
            if key == 'text' and value:
                if block == 'block1':
                    text, _ = Text.objects.get_or_create(block=block1, text=value)
                elif block == 'block2':
                    text, _ = Text.objects.get_or_create(block=block2, text=value)
                elif block == 'block3':
                    text, _ = Text.objects.get_or_create(block=block3, text=value)
                elif block == 'block4':
                    text, _ = Text.objects.get_or_create(block=block4, text=value)
            elif key == 'image' and value:
                if block == 'block1':
                    image, _ = Image.objects.get_or_create(block=block1, text=value)
                elif block == 'block2':
                    image, _ = Image.objects.get_or_create(block=block2, text=value)
                elif block == 'block3':
                    image, _ = Image.objects.get_or_create(block=block3, text=value)
                elif block == 'block4':
                    image, _ = Image.objects.get_or_create(block=block4, text=value)
