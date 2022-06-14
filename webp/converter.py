import os

from PIL import Image


def to_webp(src_dir, dist_dir, img):
    img_path = os.path.join(src_dir, img)
    dist_path = os.path.join(dist_dir, img.split(".")[0] + ".webp")
    if os.path.exists(dist_path):
        return
    image = Image.open(img_path)
    image.save(dist_path, format="webp")
    print(img_path + ' convert to ' + dist_path)


def convert(src_dir, dist_dir):
    print("Convert: start")
    images = os.listdir(src_dir)
    images.sort(key=lambda x: int(x[:-4]))
    for img in images:
        to_webp(src_dir, dist_dir, img)
    print("Convert: end")


def rename(dir_path):
    print("Rename: start")
    num = 1
    files = os.listdir(dir_path)
    files.sort(key=lambda x: int(x[:-4]))
    for file in files:
        src_path = os.path.join(dir_path, file)
        dist_path = os.path.join(dir_path, str(num)) + os.path.splitext(file)[-1]
        num = num + 1
        if src_path == dist_path:
            # print("Skip: " + src_path)
            continue
        os.rename(src_path, dist_path)
        print(src_path + ' rename to ' + dist_path)
    print("Rename: end")


if __name__ == '__main__':
    srcDir = r"E:\Onedrive\图片\次元壁纸"
    distDir = 'pc'

    rename(srcDir)
    convert(srcDir, distDir)
