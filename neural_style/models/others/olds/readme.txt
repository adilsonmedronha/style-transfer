
# o treino foi feito com a mesma configuração que o repo forkado

# 2 epocas
# batch size = 4
# img-size = 256x256
# seed = 42 (random seed for training)
# content-weight = 1e5 (w for content-loss)
# style-weight = 1e10 (w for style-loss)
# lr = 1e-3


# candy
python neural_style.py train --dataset ../dataset/ --style-image images/imgs_used_to_train/candy.jpg --save-model-dir saved_models/using_coco2017/candy --epochs 2 --cuda 1            

# mosaic
python neural_style.py train --dataset ../dataset/ --style-image images/imgs_used_to_train/mosaic.jpg --save-model-dir saved_models/using_coco2017/mosaic --epochs 2 --cuda 1      

# rain-princess
python neural_style.py train --dataset ../dataset/ --style-image images/imgs_used_to_train/rain-princess.jpg --save-model-dir saved_models/using_coco2017/rain-princess --epochs 2 --cuda 1        

# udnie
python neural_style.py train --dataset ../dataset/ --style-image images/imgs_used_to_train/udnie.jpg --save-model-dir saved_models/using_coco2017/udnie --epochs 2 --cuda 1      

# militar
python neural_style.py train --dataset ../dataset/ --style-image images/imgs_used_to_train/militar.png --save-model-dir saved_models/using_coco2017/militar --epochs 1 --cuda 1      

# militar_melhorado
python neural_style.py train --dataset ../dataset/ --style-image images/imgs_used_to_train/militar_2.png --save-model-dir saved_models/using_coco2017/2epocas/militar_2/  --epochs 2 --cuda 1 

# esferas
python neural_style.py train --dataset ../dataset/ --style-image images/imgs_used_to_train/Galatea_das_esferas.jpg --save-model-dir saved_models/using_coco2017/2epocas/esferas/  --epochs 2 --cuda 1 

# cs
python neural_style.py train --dataset ../dataset/ --style-image images/imgs_used_to_train/cs.jpg --save-model-dir saved_models/using_coco2017/2epocas_batchsize-4/cs/ --epochs 2 --cuda 1      
