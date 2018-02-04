# -*- coding:utf-8 -*-

# 引入依赖
import pytesseract
from PIL import Image

# 通用中文信息识别
def tesseractChinese(img):
    """
        lang：指定识别语言
    """
    """
       psm
       0 =仅定向和脚本检测（OSD）。
       1 =自动页面分割与OSD。
       2 =自动页面分割，但没有OSD或OCR。
       3 =全自动页面分割，但没有OSD。（默认）
       4 =假设可变大小的单列文本。
       5 =假设垂直排列文本的单个统一块。
       6 =假设单个统一的文本块。
       7 =将图像视为单个文本行。
       8 =将图像视为单个字。
       9 =将图像视为一个单一的单词。
       10 =将图像视为单个字符。
    """
    result = pytesseract.image_to_string(Image.fromarray(img),
                                             lang='chi_sim',
                                             config='-psm 3')
    # 替换空格 以及回车符
    return result.replace("\n", "").replace(" ", "")

# 性别中文信息识别
def tesseractSex(img):
    tessdata_dir_config = '--tessdata-dir "C:\pylearning\card_ocr_cv\idcard_identification_1\\tessdata"'
    result = pytesseract.image_to_string(Image.fromarray(img),
                                             lang='chi_sim',
                                            config="tessdata_dir_config"
                                             )
    # 替换空格

    # 替换空格
    return result.replace(" ", "")

# 民族中文信息识别
def tesseractNationality(img):

    result = pytesseract.image_to_string(Image.fromarray(img),
                                             lang='chi_sim',
                                             config="-psm 7")
    return result.replace(" ", "")

# 日期英文信息识别
def tesseractDate(img):

    result = pytesseract.image_to_string(Image.fromarray(img),
                                             lang='eng',
                                             config="-c tessedit_char_whitelist=0123456789 -psm 7")

    # 替换空格
    return result.replace(" ", "")

# 身份证号码英文信息识别
def tesseractID(img):

    result = pytesseract.image_to_string(Image.fromarray(img),
                                             lang='eng',
                                             config="-c tessedit_char_whitelist=0123456789X -psm 7")

    # 替换空格
    return result.replace(" ", "")

# 有效期中文信息识别
def tesseractValidperriod(img):

    result = pytesseract.image_to_string(Image.fromarray(img),
                                             lang='chi_sim',
                                             config="-c tessedit_char_whitelist=0123456789长期 -psm 7")


    # 替换空格
    return result.replace(" ", "")