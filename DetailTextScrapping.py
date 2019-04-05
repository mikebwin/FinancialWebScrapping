from bs4 import BeautifulSoup

import os
import re

path = "SC-I Forms/"


#file = BeautifulSoup(open("SC-I Forms/0001174281.txt"), 'html.parser')
#trans_value = file.find('B', string="Transaction valuation")
#print trans_value

for filename in os.listdir(path):
    txt_file_detail = BeautifulSoup(open(path + filename), "html.parser")
    text_file = open(path + filename, "r")
    contents = text_file.read()
    trans_act_index = contents.lower().find("transaction valuation")

    dollar_index = contents.find("$", trans_act_index + 1)

    m = re.search("[^0-9,]+", contents[dollar_index+1:])

    space_index = contents.find(m.group(), dollar_index + 1)

    print contents[dollar_index:space_index]
