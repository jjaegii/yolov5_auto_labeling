# python3 imagelist.py 이미지폴더경로
python3 imagelist.py images
python3 detect.py --weights yolov5s.pt --conf 0.25 --img-size 1280 \
--source imagelist.txt --classes 0 --save-txt --project label_results
