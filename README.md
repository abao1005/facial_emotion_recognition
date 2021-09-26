# 臉部情緒辨識
「影像處理、電腦視覺及深度學習概論」課程之期末專題。

## 動機
人類和機器最大的不同就是我們具有感情、行為動機也時常含有不理性的成分，  
因此，若能夠讓機器精準辨識出人類的臉部表情，相信不管在需要緊抓人性的廣告投放公司，或是行銷公司，  
甚至是未來針對強AI的發展所需，一定都能作出偌大的貢獻。  
我們小組使用Fer2013的資料集，搭配mini Xception的架構，建構出一款辨識五種情緒正確率達61%左右的模型。

## 資料集
Kaggel facial expression recognition (FER) challenge 2013  

<img src="https://github.com/abao1005/facial_emotion_recognition/blob/main/Picture/FER2013%E6%83%85%E7%B7%92%E7%A4%BA%E4%BE%8B.png" alt="Cover" width="50%"/>
<table>
  <tr>
    <th rowspan="2">情緒分類
    <th>0</th>
    <th>1</th>
    <th>2</th>
    <th>3</th>
    <th>4</th>
    <th>5</th>
    <th>6</th>
  </tr>
  <tr>
    <th>Angry</th>
    <th>Disgust</th>
    <th>Fear</th>
    <th>Happy</th>
    <th>Sad</th>
    <th>Surprise</th>
    <th>Neutral</th>
  </tr>
</table>  

<img src="https://github.com/abao1005/facial_emotion_recognition/blob/main/Picture/FER2013%E5%90%84%E6%83%85%E7%B7%92%E8%B3%87%E6%96%99%E5%88%86%E5%B8%83.png" alt="Cover" width="50%"/>

* 圖片大小： 48 x 48 pixels
* 34034張灰階臉部圖檔
* 缺乏 Disgust 資料

## 深度學習模型 - mini Xception
![image](https://github.com/abao1005/facial_emotion_recognition/blob/main/Picture/miniXceptionArchitecture.png)

## 實驗流程
![image](https://github.com/abao1005/facial_emotion_recognition/blob/main/Picture/workflow.png)

## 實驗結果
![image](https://github.com/abao1005/facial_emotion_recognition/blob/main/Picture/ExperimentResult.png)  
* Accuracy：0.6106
* Loss：1.0382
* Val_accuracy：0.6054
* Val_loss：1.0599
