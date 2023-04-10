# 中文语音识别与转写工具

本项目使用 PaddleSpeech 和 Streamlit 开发了一个中文语音识别与转写工具，可以将包含 MP3 格式录音文件的文件夹中的所有音频文件转换为文字，并添加标点符号。用户可以实时查看和编辑转写结果，然后将结果保存为文本文件。

## 功能

- 将 MP3 格式的音频文件转换为 WAV 格式
- 使用 PaddleSpeech 识别音频文件中的语音内容
- 对识别结果添加标点符号
- 通过 Streamlit 实现交互式界面，方便用户查看和编辑转写结果
- 将处理过的音频文件及其对应的转写结果保存到指定的输出文件夹

## 安装

1. 克隆本仓库到本地：

```
git clone https://github.com/cliuxinxin/px470.git
```

2. 进入项目文件夹：
```
cd px470
```


3. 创建一个虚拟环境：
```
python3 -m venv venv
```

4. 激活虚拟环境：

- macOS/Linux:

  ```
  source venv/bin/activate
  ```

- Windows:

  ```
  .\venv\Scripts\activate
  ```

5. 安装依赖：

```
pip install -r requirements.txt
```

## 使用

1. 激活虚拟环境（如果尚未激活）：

- macOS/Linux:

  ```
  source venv/bin/activate
  ```

- Windows:

  ```
  .\venv\Scripts\activate
  ```

2. 启动 Streamlit 应用：

```
streamlit run app.py
```

3. 在浏览器中打开 [http://localhost:8501](http://localhost:8501) 以访问应用界面。

4. 按照提示，输入包含 MP3 格式录音文件的文件夹路径和输出识别结果的文件夹路径。

5. 单击 "加载文件" 按钮以加载音频文件。

6. 逐个查看和编辑转写结果。

7. 单击 "保存结果并处理下一个文件" 按钮以将结果保存为文本文件，并将处理过的音频文件及其对应的转写结果移动到输出文件夹。

8. 当所有文件处理完成后，关闭应用。

## 许可证

本项目采用 [MIT 许可证](LICENSE)。