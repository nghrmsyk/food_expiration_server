from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
import numpy as np
import json

def get_labels():
    """ラベル名を取得"""
    #ラベル読み込み
    with open("config/label_name.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        labels = [data[str(i)] for i in range(len(data))]
        return labels

def get_net():
    #パラメータファイル設定
    cfg = get_cfg()
    cfg.merge_from_file("config/config.yaml")
    cfg.MODEL.WEIGHTS = "config/model.pth"
    cfg.MODEL.DEVICE = "cpu"
    labels = get_labels()
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = len(labels)

    predictor = DefaultPredictor(cfg)
    return predictor, labels

def detect(image, predictor):
    image = np.array(image)[:, :, ::-1]
    outputs = predictor(image)

    boxes = outputs["instances"].pred_boxes.tensor
    scores = outputs["instances"].scores
    classes = outputs["instances"].pred_classes

    selected_box = [{
        "box": box.int().tolist(),
        "score": float(score),
        "label": int(label)
    }for box, score, label in zip(boxes, scores, classes)]

    return selected_box



