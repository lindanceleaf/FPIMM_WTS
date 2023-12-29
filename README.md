# 實作方法:
```
打開終端機 輸入指令 python Main.py

跳出畫面點出檔案。（audio的folder）
此時選擇音樂，
選擇五種你要分類出來的類型（可以復選）。
沒選（都會出warning：問你是否要取消）。
等待20秒，最後在你的audio檔案裡面會產生文字檔（你要的樂器的樂譜）和分離出來的音檔（.wav）
```

# 版本需求以及預先下載工具：
```
需求版本:
python 3.8.10
spleeter 2.0
protobuf 3.19.6
numpy 1.18.5, spleeter有函式使用到的numpy的complex形態，該形態在1.20後被刪除
```
