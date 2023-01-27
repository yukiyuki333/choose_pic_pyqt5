# choose_pic_pyqt5
- 套件：pyqt5
- 有選擇圖片功能的 GUI 模板
  - ![image](https://user-images.githubusercontent.com/84313696/215020178-f0220997-d05c-4db4-80b2-f2b2293a2b8c.png)
- qt designer 拉介面，用以下指令轉成 py 檔
  - ```pyuic5 -o xxx.py ooo.ui```
  - xxx、ooo 為檔名
- 裝套件 pyinstaller，用以下指令生成 exe
  - ```pyinstaller -F main.py -p UI.py -p other.py -i pochita.ico --noconsole```
  - 檔名自己填
