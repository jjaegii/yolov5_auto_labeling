# YOLOv5를 활용한 autolabeling

[YOLOv5](https://github.com/ultralytics/yolov5)의 pretrained model을 활용한 자동라벨링 기능입니다.
커스텀 모델을 활용하여 자동라벨링에 쓸 수 있습니다.

label_results/
autolabeling.sh
imagelist.py
imagelist.txt
를 중점적으로 보면 됩니다.

## 실행방법

autolabeling.sh에서

- python3 imagelist.py 라벨링할 이미지폴더경로를 설정
- python3 detect.py에서 --weights에 적용시킬 모델 파일 설정, --classes에 detect할 클래스 설정, --project에 라벨링 결과를 저장할 폴더명 설정
  후 실행하면 됩니다.
