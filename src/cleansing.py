import re
import unicodedata

if __name__ == '__main__':
    text = '    CLEANSING  によりﾃｷｽﾄを変換すると　トラブルが少なくなる'
    print('before:', text)

    text = unicodedata.normalize('NFKC', text)
    text = re.sub(r'¥s+', ' ', text)
    print('after:', text)