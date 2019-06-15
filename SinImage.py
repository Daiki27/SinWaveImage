#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#キャンバス生成
Width = 512
Height = 512
img = Image.new("RGB", (Width, Height))

#各パラメータの定義
Amp = 255.0      #振幅
T = 32.0       #周期
f = 1.0 / 32.0 #周波数
sec = 1        #サンプリング時間
f_s = 1000     #サンプリング周波数
offset = 255   #sin波を0から255の間で描画するため.

#輝度値
Brightness=[]
for t in np.arange(f_s * sec):
    y = Amp * np.sin(2.0 * np.pi * f * t) + offset
    y = y / 2
    Brightness.append(y)

#出力画像の設定.
plt.grid(True)
plt.xlabel('t', fontsize = 15)
plt.ylabel('Brightness', fontsize = 15)
plt.plot(Brightness[0:100], color = 'red')
plt.show()

#画素の書き換え.
for x in range(Width):
    for y in range(Height):

        #putpixcelの引数が整数のみなので,四捨五入して整数化した.
        r = int(round(Brightness[x]))
        g = int(round(Brightness[x]))
        b = int(round(Brightness[x]))

        img.putpixel((x,y),(r,g,b))

#正弦縞画像の表示
plt.imshow(img)
plt.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False)
plt.tick_params(bottom=False, left=False, right=False, top=False)
plt.savefig('SinImage.png', bbox_inches="tight",dpi=300)
plt.show()


# In[ ]:




