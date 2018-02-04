# -*- coding: UTF-8 -*-
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pytesseract
from PIL import Image
import os
from Tesserast_ocr import tesseractChinese
from Tesserast_ocr import tesseractSex
from Tesserast_ocr import tesseractNationality
from Tesserast_ocr import tesseractDate
from Tesserast_ocr import tesseractID
def box_get(img,imgHeight,imgWidth,index):
    PATH='C:\pylearning\card_ocr_cv\idcard_identification_1\\'+str(index)
    if not os.path.exists(str(PATH)):
        os.makedirs(PATH)



    name_height = int(imgHeight / 10.8)
    name_width = int(imgWidth / 5.7)
    name_addHeight = int(imgHeight / 10.8 + imgHeight / 6.75)
    name_addWidth = int(imgWidth / 5.7 + imgWidth / 2.31)
    name = img[name_height:name_addHeight, name_width:name_addWidth]
    cv2.imwrite(str(PATH)+'\\'+"name.png", name)




    # 性别

    sex_height = int(imgHeight / 4.5)
    sex_width = int(imgWidth / 5.7)
    sex_addHeight = int(imgHeight / 4.5 + imgHeight / 7.71)
    sex_addWidth = int(imgWidth / 5.7 + imgWidth / 12.22)
    sex = img[sex_height:sex_addHeight, sex_width:sex_addWidth]
    cv2.imwrite(str(PATH) + '\\' + "sex.png", sex)



    # 民族

    nationality_height = int(imgHeight / 4.5)
    nationality_width = int(imgWidth / 2.55)
    nationality_addHeight = int(imgHeight / 4.5 + imgHeight / 7.71)
    nationality_addWidth = int(imgWidth / 2.55 + imgWidth / 4.28)
    nationality = img[nationality_height:nationality_addHeight, nationality_width:nationality_addWidth]
    cv2.imwrite(str(PATH) + '\\' + "nationality.png", nationality)


    # 生日 年

    birth_year_height = int(imgHeight / 2.84)
    birth_year_width = int(imgWidth / 5.35)
    birth_year_addHeight = int(imgHeight / 2.84 + imgHeight / 7.71)
    birth_year_addWidth = int(imgWidth / 5.35 + imgWidth / 8.56)
    birth_year = img[birth_year_height:birth_year_addHeight, birth_year_width:birth_year_addWidth]
    cv2.imwrite(str(PATH) + '\\' + "birth_year.png", birth_year)


    # 生日 月

    birth_month_height = int(imgHeight / 2.84)
    birth_month_width = int(imgWidth / 2.85)
    birth_month_addHeight = int(imgHeight / 2.84 + imgHeight / 7.71)
    birth_month_addWidth = int(imgWidth / 2.85 + imgWidth / 21.4)
    birth_month = img[birth_month_height:birth_month_addHeight, birth_month_width:birth_month_addWidth]
    cv2.imwrite(str(PATH) + '\\' + "birth_month.png", birth_month)


    # 生日 日

    birth_day_height = int(imgHeight / 2.84)
    birth_day_width = int(imgWidth / 2.31)
    birth_day_addHeight = int(imgHeight / 2.84 + imgHeight / 7.71)
    birth_day_addWidth = int(imgWidth / 2.31 + imgWidth / 17.12)
    birth_day = img[birth_day_height:birth_day_addHeight, birth_day_width:birth_day_addWidth]
    cv2.imwrite(str(PATH) + '\\' + "birth_day.png", birth_day)


    # 地址

    address_height = int(imgHeight / 2.07)
    address_width = int(imgWidth / 5.7)
    address_addHeight = int(imgHeight / 2.07 + imgHeight / 3.17)
    address_addWidth = int(imgWidth / 5.7 + imgWidth / 2.25)
    address = img[address_height:address_addHeight, address_width:address_addWidth]
    cv2.imwrite(str(PATH) + '\\' + "address.png", address)


    # 身份证号码

    ID_height = int(imgHeight / 1.27)
    ID_width = int(imgWidth / 3.06)
    ID_addHeight = int(imgHeight / 1.27 + imgHeight / 6.75)
    ID_addWidth = int(imgWidth / 3.06 + imgWidth / 1.55)
    ID = img[ID_height:ID_addHeight, ID_width:ID_addWidth]
    cv2.imwrite(str(PATH) + '\\' + "ID.png", ID)

    return name,sex,nationality,birth_year,birth_month,birth_day,address,ID


# 文字识别
def text_get(Name, Sex, Nationality, Birth_year, Birth_month, Birth_day, Address, ID_number):
    out_name = tesseractChinese(Name)
    # 性别信息现在无法识别
    # out_sex = tesseractSex(Sex)
    out_nationality = tesseractNationality(Nationality)
    out_birth_year = tesseractDate(Birth_year)
    out_birth_month = tesseractDate(Birth_month)
    out_birth_day = tesseractDate(Birth_day)
    out_address = tesseractChinese(Address)
    out_ID_number = tesseractID(ID_number)
    if (int(out_ID_number[16]) % 2 == 1):
        out_sex = "男"
    elif (int(out_ID_number[16]) % 2 == 0):
        out_sex = "女"
    else:
        out_sex='dk'
    information=[out_name,out_sex,out_nationality,out_birth_year,out_birth_month,out_birth_day,out_address,out_ID_number]
    return information

if __name__=="__main__":
    paths=['test1.png']
    for path in paths:
        Index=paths.index(path)
        img = cv2.imread(path)
        height, width = img.shape[:2]
        imgWidth = width
        imgHeight = height
        img = cv2.resize(img, (imgWidth, imgHeight))
        Name, Sex, Nationality, Birth_year, Birth_month, Birth_day, Address, ID_number=box_get(img,imgHeight,imgWidth,Index)
        #show the img
        f, axarr = plt.subplots(3, 3)
        axarr[0, 0].set_title('origin img')
        axarr[0, 1].set_title('Name')
        axarr[0, 2].set_title('Sex')
        axarr[1, 0].set_title('Nationality')
        axarr[1, 1].set_title('Birth_year')
        axarr[1, 2].set_title('Birth_month')
        axarr[2, 0].set_title('Birth_day')
        axarr[2, 1].set_title('Address')
        axarr[2, 2].set_title('ID_number')
        axarr[0, 0].imshow(img)
        axarr[0, 1].imshow(Name)
        axarr[0, 2].imshow(Sex)
        axarr[1, 0].imshow(Nationality)
        axarr[1, 1].imshow(Birth_year)
        axarr[1, 2].imshow(Birth_month)
        axarr[2, 0].imshow(Birth_day)
        axarr[2, 1].imshow(Address)
        axarr[2, 2].imshow(ID_number)
        plt.show()
        Information=text_get(Name, Sex, Nationality, Birth_year, Birth_month, Birth_day, Address, ID_number)
        print('the information is as following\n',
              '-------------------------------\n',
              'the name is {} \n'.format(Information[0]),
              'the sex is {} \n'.format(Information[1]),
              'the Nationality is {} \n'.format(Information[2]),
              'the birth is {} 年 {} 月 {} 日 \n'.format(Information[3],Information[4],Information[5]),
              'the Address is {} \n'.format(Information[6]),
              'the ID_number is {} \n'.format(Information[7]),
              '-------------------------------\n\n')

