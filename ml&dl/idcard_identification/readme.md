idcard identification 0
======
身份证号码识别ocr，从身份证图片中自动提取身份证号。
目前只进行到第一版，只能从特定环境下识别单个身份证号码。

# 依赖
* opencv
* pytesseract
* numpy
* matplotlib

#特别注意要安装Tesseract-OCR，并将其路径加入到系统环境变量中

# 流程
* 获取身份证号区域

image-》灰度=》反色=》膨胀=》findContours

* 数字识别

采用tesseract识别，由于本项目所处的环境较为简单，所以使用pytesseract.image_to_string(image, lang='ocrb', config=tessdata_dir_config)函数即可识别

# 引用
* https://github.com/JinpengLI/deep_ocr/