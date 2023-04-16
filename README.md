# kohya-config-webui
A WebUI for making config files used by kohya_sd_script
![9@`$94}$U~DCAQCEA }20AX](https://user-images.githubusercontent.com/126865849/232077304-cb04f8c4-e815-4de8-a5ec-e9116413c5e2.png)

## 现在我们有什么？
目前，我为4月14日版本的kohya-lora-dreambooth训练中较为常用、实用的训练参数（除了aug增强参数），编写了一个交互式的WebUI生成工具，可以在带有python环境的windows和Colab环境中快速部署。

使用本项目，你可以快速指定训练参数，并生成config_file.toml和sample_prompt.txt。

除秋叶一键整合包所具有的参数外，目前还添加了DyLoRa训练参数、分层训练参数

**目前只提供了Colab试用版本，稍后更新本地部署版本**

[![](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=5c5c5c&color=0f80c1&label=%20&style=flat)](https://colab.research.google.com/github/WSH032/kohya-config-webui/blob/main/kohya_train_webui.ipynb)
    
## Todo
- [x] 增加上一次参数保存功能
- [ ] 增加dataset_config.toml生成功能


## 其他部分展示
![0S2_@5B6638VJ 4%Y@TQDXK](https://user-images.githubusercontent.com/126865849/232079134-15154ccf-06ac-45a0-984f-244a6e8983f3.png)

![7$K@5833YHY(8T1 `3RE03L](https://user-images.githubusercontent.com/126865849/232079434-d471da6e-9e1d-457b-b635-4c37a838bf15.png)
