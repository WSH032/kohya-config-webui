# kohya-config-webui
A WebUI for making config files used by kohya_sd_script
![9@`$94}$U~DCAQCEA }20AX](https://user-images.githubusercontent.com/126865849/232077304-cb04f8c4-e815-4de8-a5ec-e9116413c5e2.png)

## 现在我们有什么？
目前，我为4月14日版本的kohya-lora-dreambooth训练中较为常用、实用的训练参数（除了aug增强参数），使用gradio和toml库，编写了一个交互式的WebUI生成工具，可以在带有python环境的windows和Colab环境中快速部署。

使用本项目，你可以快速指定训练参数，并生成config_file.toml和sample_prompt.txt。

除秋叶一键整合包所具有的参数外，目前还添加了DyLoRa训练参数、分层训练参数

## 使用方法

### （一）Colab版本：

[![](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=5c5c5c&color=0f80c1&label=%20&style=flat)](https://colab.research.google.com/github/WSH032/kohya-config-webui/blob/main/kohya_train_webui.ipynb)

### （二）AUTOMATIC1111/stable-diffusion-webui插件：

`https://github.com/WSH032/kohya-config-webui.git`

将这个仓库连接复制到SD-WebUi的`扩展`->`从网址安装`界面下载即可

### （三）直接下载：

运行以下代码，或直接从github上下载zip并解压（直接下载将无法使用[update.bat](update.bat)），
```Shell
git clone https://github.com/WSH032/kohya-config-webui.git
```
运行目录下的[install_webui.ps1](install_webui.ps1)在虚拟环境中安装gradio和toml,或者
```Python
pip install  gradio>=3.24.1
pip install  toml>=0.10.2
```
运行[run_webui.ps1](run_webui.ps1)，或者
```Python
python .\module\kohya_config_webui.py
```


## Todo
- [x] 增加上一次参数保存功能
- [ ] 增加dataset_config.toml生成功能


## 其他部分展示
![0S2_@5B6638VJ 4%Y@TQDXK](https://user-images.githubusercontent.com/126865849/232079134-15154ccf-06ac-45a0-984f-244a6e8983f3.png)

![7$K@5833YHY(8T1 `3RE03L](https://user-images.githubusercontent.com/126865849/232079434-d471da6e-9e1d-457b-b635-4c37a838bf15.png)
