# image_to_RGB565
将jpg/png图片批量转换为TFT_eSPI库所需要的RGB565格式。

## 背景
当使用TFT_eSPI库驱动TFT屏幕时,需要使用RGB565格式的图片,而普通的图片处理软件导出的图片格式通常是RGB888格式,不符合要求。

## 功能
- 批量转换普通JPG/PNG图片为RGB565格式
- 直接生成img.h文件,可以直接在单片机程序中引入使用

## 使用
1. 安装Pillow library:
```sh
pip install Pillow
```
2. 运行脚本: 
```sh
python image_to_RGB565.py
```
3. 输入要转换的图片文件夹路径,脚本会自动转换文件夹内所有图片 
4. 转换完成后,项目文件夹下会生成img.h文件,直接将该文件加入单片机程序使用即可 
5. 在单片机程序中调用pushImage函数显示图片:
```
#include "img.h"  
tft.pushImage(0, 0, width, height, "pic1");
```
## 示例 
输入要转换的图片文件夹路径:
```
输入图片文件夹路径: images  
```
转换完成后,项目文件夹下会生成img.h文件:
```
#include <pgmspace.h>
typedef struct image{
    int width;
    int height;
    uint16_t pixels[];
}image;

const image pic1 = {
    64,
    63,
    { 
    0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 
    ...
	0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00049f, 0x00049f, 0x00049f, 0x00049f, 0x00049f, 0x00049f, 
    }
}

const image pic2 = {
    128,
    128,
    { 
    0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 
    ...
	0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00ffff, 0x00049f, 0x00049f, 0x00049f, 0x00049f, 0x00049f, 0x00049f, 
    }
}	
```
直接在单片机程序使用: 
```
#include "img.h"   
tft.pushImage(0, 0, pic1.width, pic1.height, pic1.pixels);
tft.pushImage(0, 80, pic2.width, pic2.height, pic2.pixels);
```
