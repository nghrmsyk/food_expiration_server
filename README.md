# food_expiration_server
Fast API Server

## 準備
### Google Cloud Vision API
Google Cloud のサーバを用意して　Vision APIを有効化してください。

### OpenAI API
OpenAIへ登録してAPIを有効化してください。

### api keyとモデルのパラメータファイル 
app/configディレクトに次のファイルを用意してください。
- google-api-key.json : google cloudのapi key
- openai-api-key.txt : OpenAIのapi key
- model.pth: 物体検出モデルの学習済みの重み(detectron2のfaster_rcnn_X_101_32x8d_FPN_3x)

### config.yaml
物体検出モデルの設定変更する場合はconfig.yamlを変更してください。
https://detectron2.readthedocs.io/en/latest/modules/config.html

