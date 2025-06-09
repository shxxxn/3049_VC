# 視覺密碼學圖片加密分享系統

## 專案介紹
本專案提供一個基於視覺密碼學 (Visual Cryptography) 的圖片加密與分享平台。使用者可以將加密貨幣助記詞隱寫至 QR Code，再透過視覺密碼學切割成兩張看似雜訊的分享圖層，只有同時擁有兩張分享圖層才能還原出原始助記詞。

## 主要功能

1. **助記詞隱寫與加密**  
   - 使用者透過 GUI 輸入欲隱寫的助記詞文字。  
   - 系統將文字轉換為 QR Code 圖檔。  
   - 以視覺密碼學算法切割 QR Code，生成兩張分享圖層。

2. **視覺密碼學分層**  
   - 將同尺寸的 QR Code 圖拆分為兩個 share 圖，單獨檢視時僅為雜訊。  
   - 兩張 share 圖按位重疊即可還原 QR Code 圖像。

3. **圖層合成與解密**  
   - 使用者可透過檔案選取介面選擇兩張分享圖層。  
   - 系統合成出還原後的結果圖。  
   - 自動掃描並解析 QR Code，還原出原始助記詞。

4. **GUI 操作介面**  
   - 主視窗以 Tkinter 實作，提供「輸入助記詞並加密」和「選擇兩層圖層並解密」兩個按鈕。  
   - 圖片顯示區會動態顯示剛生成或合成後的圖像（縮放至 400×400）。

## 系統需求

- Python 3.10+  
- 必要套件：  
  ```bash
  pip install pillow pyzbar qrcode tkinter
  # Homebrew
brew install zbar

# 或 Conda
conda install -c conda-forge zbar
├── main.py         # 程式入口與 GUI
├── encrypt.py      # 視覺密碼學加密邏輯
├── decrypt.py      # 視覺密碼學解密邏輯
├── qr_utils.py     # QR Code 生產與解析
└── README.md       # 專案說明（本文件）