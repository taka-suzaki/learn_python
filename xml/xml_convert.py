import xmltodict
import dicttoxml
import json

xml = """<?xml version="1.0" encoding="UTF-8" ?>
<foods>
  <food>
    <name value="i" kind="primary">イチゴ</name>
    <color>赤</color>
  </food>

  <food>
    <name>バナナ</name>
    <color>黄</color>
  </food>
</foods>
"""

# XMLから辞書に変換
dict_xml = xmltodict.parse(xml)
print(json.dumps(dict_xml, indent=2, ensure_ascii=False))

# 辞書からXMLに変換
# attr_type：属性に型名を付ける
# root：rootの要素を付与する
xml = dicttoxml.dicttoxml(dict_xml, attr_type=False, root=False)
print(xml.decode('utf-8'))