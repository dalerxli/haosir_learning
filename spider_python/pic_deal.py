from PIL import Image
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join
def single_test():
    img=input('原始图片：')
    img = Image.open(img)
    print('原始照片尺寸为： ',img.size)
    print('格式为: ',img.format)
    print('如果你想改变图片大小请输入1，想旋转图片请输入2')
    num = input('输出你的决定：')
    while(num):
        if int(num)==1:
            w=input('你想转变的宽度：')
            h=input('你想转变的高度：')
            name=input('新图片的名称')
            new_img= img.resize((int(w), int(h)),Image.ANTIALIAS)
            new_img.save(name)
            plt.figure('resize')

            plt.subplot(121)
            plt.title('before resize')
            plt.imshow(img)

            plt.subplot(122)
            plt.title('after resize')
            plt.imshow(new_img)
            plt.show()
            break
        elif int(num)==2:
            jiaodu=input('旋转的角度：')
            new_img = img.rotate(int(jiaodu))
            plt.figure('rotate')
            name = input('新图片的名称')
            new_img.save(name)

            plt.subplot(121)
            plt.title('before rotate ')
            plt.imshow(img)

            plt.subplot(122)
            plt.title('after rotate')
            plt.imshow(new_img)
            plt.show()
            break
        else:
            print('输错了，请重新输入\n')
            num = input('输出你的决定：')
def batch_test():
    path=input('输入图片的地址：')
    name = [f for f in listdir(path) if isfile(join(path, f))]
    fname=[join(path, f) for f in name]
    print('如果你想按比例改变图片大小请输入1，按固定大小请输入2，想改变图片的格式请输入3')
    num=input('你的决定：')
    while(num):
        if int(num)==1:
            k1 = input('输入宽的缩放比例')
            k2= input('输入高的缩放比例')
            for pic in fname:
                img = Image.open(pic)
                (x, y) = img.size
                new_img = img.resize((int(x*float(k1)), int(y*float(k1))),Image.ANTIALIAS)
                pic_name=join(path,'new1_'+name[fname.index(pic)])
                new_img.save(pic_name)
            break
        elif int(num)==2:
            w = input('输入宽')
            h= input('输入高')
            for pic in fname:
                img = Image.open(pic)
                (x, y) = img.size
                new_img = img.resize((int(w), int(h)),Image.ANTIALIAS)
                pic_name=join(path,'new2_'+name[fname.index(pic)])
                new_img.save(pic_name)
            break
        elif int(num) == 3:
            geshi=input('请输入你想要改变到的格式')
            for pic in fname:
                img = Image.open(pic)
                pic_name=join(path,'new3_'+name[fname.index(pic)].split('.')[0]+'.'+str(geshi))
                img.save(pic_name)
            break
        else:
            print('输错了，请重新输入\n')
            num = input('你的决定：')
if __name__=="__main__":
    yournum=int(input('___________1.single test__________\n___________2.batch test___________\n请选择'))
    while (yournum):
        if int(yournum)==1:
            single_test()
            print('任务完成了，快去查看吧')
            break
        elif int(yournum)==2:
            batch_test()
            print('任务完成了，快去查看吧')
            break
        else:
            print('重新输入\n')
            yournum = int(input('___________1.single test__________\n___________2.batch test___________\n请选择'))












