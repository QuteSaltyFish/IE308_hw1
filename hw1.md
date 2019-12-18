# 图像处理与内容分析作业一
## 直方图规定化

### 原理

图像直方图是图像处理中一种十分重要的分析工具，它描述了一幅图像的灰度级内容。从数学上来说，图像直方图是图像各灰度值统计特性与图像灰度值的函数，它统计一幅图像中各个灰度级出现的次数或概率；从图形上来说，它是一个二维图，横坐标表示图像中各个像素点的灰度级，纵坐标为各个灰度级上图像像素点出现的次数或概率，它是图像最基本的统计特征。

直方图有以下性质：

- 直方图是一幅图像中各像素灰度出现频次的统计结果，它只反映图像中不同灰度值出现的次数，而不反映某一灰度所在的位置。
- 任何一幅图像，都有惟一确定的与它对应的直方图，但不同的图像可能有相同的直方图
- 由于直方图是对具有相同灰度值的像素统计得到的，因此，一幅图像各子区的直方图之和就等于该图像全图的直方图

直方图规定化的目的就是调整原始图像的直方图使之符合某一规定直方图的要求.设 Pr（r）和Pz（z）分别表示原始灰度图像和目标图像的灰度分布概率密度函数.根据直方图规 定化的特点与要求，应使原始图像的直方图具有Pz（z）所表示的形状。因此.建立Pr（r）和 Pz（z）之间的关系是直方图规定化必须解决的问题



直方图规定化就是对src与dst都进行直方图均衡之后，通过进行反映射，把src映射到dst的像素色彩分布。我再实验过程中使用了2张色彩完全不同以及2张色彩相近的照片进行实现，首先先上原图。

![](/Users/albertwang/Desktop/HomeWork/图像1/src/img.jpg)
![](/Users/albertwang/Desktop/HomeWork/图像1/src/img2.jpg)

![](/Users/albertwang/Desktop/HomeWork/图像1/src/img3.jpg)

![](/Users/albertwang/Desktop/HomeWork/图像1/src/img4.jpg)

### 两两进行直方图匹配后的结果

![](/Users/albertwang/Desktop/HomeWork/图像1/result1/1.jpg)

![](/Users/albertwang/Desktop/HomeWork/图像1/result1/2.jpg)

![](/Users/albertwang/Desktop/HomeWork/图像1/result1/3.jpg)

![](/Users/albertwang/Desktop/HomeWork/图像1/result1/4.jpg)

![](/Users/albertwang/Desktop/HomeWork/图像1/result1/5.jpg)

![](/Users/albertwang/Desktop/HomeWork/图像1/result1/6.jpg)

可以看出，色彩相近的图片经过直方图均衡化之后的色彩表现依旧不错，而色彩差距比较大的图片经过均衡化之后的色彩偏向于dst的色彩表现。



## Canny算子

原图

![](/Users/albertwang/Desktop/HomeWork/图像1/src/img.jpg)

经过canny算子后

![](/Users/albertwang/Desktop/HomeWork/图像1/result2/edge_img.jpg)

可以看出图像的边界保留比较好。