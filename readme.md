# 合成大西瓜基础版本魔改并上线

使用本仓库的代码魔改合成大西瓜的要求是会运行python代码、会上传代码到github仓库。

## 文件概览

下载本仓库文件后，文件如下：

![image-20231125134155347](https://raw.githubusercontent.com/drinkwateronly/Image-Host/main/iimage/image-20231125134155347.png)

## 魔改

`src/extraSetting.js`中按需修改，要强调的是可以修改网页标题。

## 图片处理

两种处理方式，本文提供python脚本自动处理。手动处理较为繁琐，请查询网络教程，或使用他人提供的在线大西瓜图片处理工具。

### 自动处理

原本水果图片文件在`res/raw-assets`的位置、图片文件名等信息已按水果尺寸从小到大记录到`image_process/info.xlsx`中，具体如下。例如樱桃图片文件为`res/raw-assets/0c/0cbb3dbb-2a85-42a5-be21-9839611e5af7.png`。

![image-20231125104727166](https://raw.githubusercontent.com/drinkwateronly/Image-Host/main/iimage/image-20231125104727166.png)

定制水果图片为想要的图片，则需要将要定制的11张图片（对应11种水果）放到`image_process/origin`，并按水果尺寸从小到大的顺序命名为`1.jpg`, `2.jpg`..., `11.jpg`。

**注意，这些定制图片的尺寸最好是近似正方形，以免在后续图片处理中的缩放操作导致图片被拉伸，效果变差。**

随后运行`image_process/demo.py`即可自动将这些图片修改到原本水果图片的位置。其中该python脚本将图片先缩放到对应的正方形尺寸，并裁剪成圆形。

### 手动

略

## 本地预览

- 下载并安装Nod

  http://nodejs.cn/download/

- 进入命令行，检查npm是否安装成功

  ```bash
  npm -v
  ```

- 命令行安装serve工具

  ```bash
  npm i -g serve
  ```

- 从游戏文件夹进入命令行，启动serve

  ```bash
  serve
  ```

成功后浏览器输访问`localhost:5000`即可

## 部署

预览没问题后，可以开始部署上线。

- **首先代码要上传到github仓库**。

- 随后使用[4everland](https://dashboard.4everland.org?invite=49TRKU2D)进行静态网页托管，并使用github注册即可。

- 注册成功后，点击`new project`，创建一个新项目

  ![image-20231125111433974](https://raw.githubusercontent.com/drinkwateronly/Image-Host/main/iimage/image-20231125111433974.png)

- 然后在step 1，import保存了合成大西瓜代码的github的仓库

  ![image-20231125112002423](https://raw.githubusercontent.com/drinkwateronly/Image-Host/main/iimage/image-20231125112002423.png)

- step2，可选仓库的branch，意味着可以定制不同的合成大西瓜，上传到同一个仓库的不同branch管理。此处使用默认的branch，直接deploy即可。

  <img src="https://raw.githubusercontent.com/drinkwateronly/Image-Host/main/iimage/image-20231125112423795.png" alt="image-20231125112423795" style="zoom:67%;" />

- step3，耐心等待部署。完成后点击visit访问，并记录下url。首次加载该游戏可能比较慢。

![image-20231125112509144](https://raw.githubusercontent.com/drinkwateronly/Image-Host/main/iimage/image-20231125112509144.png)

- 拓展：

  [4everland](https://dashboard.4everland.org?invite=49TRKU2D)注册就送了1G的静态网页托管空间，一个合成大西瓜也就十几m，所以合理地管理好仓库的branch，可以上线很多个合成大西瓜游戏。

## Ref

[魔改大西瓜可替换的素材 (qq.com)](https://docs.qq.com/sheet/DS0d2VVVJYmpvZ0pZ?tab=BB08J2)

[魔改和上线你的合成大西瓜，最全教程！ (qq.com)](https://mp.weixin.qq.com/s/H9VR1MWn-9bKSC_1l_MkJw)

[全网最贴心的魔改合成大西瓜教程，从修改到发布！_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Vy4y1n7KW/?vd_source=9883419bb9939eb61834a63a38921b19)
