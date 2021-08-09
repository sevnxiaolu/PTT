# PTT pictuer to table 将图片中表格直接转换为excel
## 整个功能基于百度AI图像识别接口
### 百度AI文字识别链接 https://ai.baidu.com/ai-doc/OCR/1k3h7y3db
### 请求方式HTTP方法：post     
### 请求URL: https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic
### 请求参数详情
| 参数 | 类型 |
| :-----: | :-----: |
| image | string |
| url | string |
| pdf_file | string |
| pdf_file_num | string |
| language_type | string |
| detect_direction | string |
| paragraph | string |
| probability | string |
### 返回参数详情
| 参数 | 类型 |
| :-----: | :-----: |
| log_id | uint64 |
| direction | int32 |
| words_result | array[] |
| words_result_num | uint32 |
| + words | array[] |
| paragraphs_result | array[] |
| words_result_idx | array[] |
| + probability | object |
| pdf_file_size | string |
## 注意事项
**百度AI提供有一定免费额度需要去申请获取access token**



