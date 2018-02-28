# 錄影展示
## Detect Digit
`python3 detect_digit.py j左旋k右旋 旋轉秒數`
## https://youtu.be/GzUc8UqjBCY
## Detect Faces
`python3 detect_faces.py j左旋k右旋 旋轉秒數`
## https://youtu.be/Jat1UAIJuQo
# 活動展示
## 小Pi孩 懂數喔
展示操作流程：
1. ssh進pi，cd到Pi，python3 detect_digit.py j或k 約1.1秒
2. 請參觀者寫一個阿拉伯數字
3. 展示者給小Pi孩看數字並按下Enter(即按下樹莓派相機快門)
4. 小Pi孩會立即用旋轉表達所看到的數字
5. 展示者用筆電秀遠端桌面的 digit.jpg
6. 重複2~5
## 別讓Pi孩不開心
展示操作流程：
1. ssh進pi，cd到Pi，python3 detect_faces.py j或k 約1.1秒
2. 請參觀者一或多人聽到西瓜甜不甜(或隨便什麼拍照口令)對小Pi孩做表情
3. 展示者按下Enter(即按下樹莓派相機快門)
4. 等待Google大神的表情分析
5. 參觀者中只要有一人沒有很開心，小Pi孩就會嚇到抖三下
6. 否則，小Pi孩看到幾個人就會開心的轉幾圈
7. 展示者用筆電秀遠端桌面的 faces_highlight.jpg，紅框內的就是Google大神認為沒有很開心的臉
8. 重複2~7