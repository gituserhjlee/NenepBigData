# 빅데이터 - Word Embedding Team Project 

Project name: NenepBigData

Team name: 넵네

Leader: 20150711 송희성

Team Members: 20165968 맹채정, 20164980 유경민, 20173954 유진, 20176815 이현지


## 주제: 영화별 review를 보고 해당 영화의 장르를 예측해보기, review속의 keyword를 추출
Target Data: 영화 리뷰 데이터

## Data Scraping
imdb의 영화 리뷰 데이터

## Word Embedding : 사전 훈련된 Count기반 GloVe 사용
## stackedLSTM(2 Layer) - pytorch활용
 epoch = 10, LR = 0.003, min_freq = 4
 
 Min_freq(1,2,3,4,5,10) Dropout(0.1,0.2,0.3) 사이에서 가장 val_loss가 낮은 모델 사용

## Visualization
