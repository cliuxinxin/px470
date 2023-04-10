import os
import shutil
import tempfile
from pathlib import Path
from pydub import AudioSegment
from paddlespeech.cli.asr.infer import ASRExecutor
from paddlespeech.cli.text.infer import TextExecutor
import streamlit as st

def convert_mp3_to_wav(mp3_file, wav_file):
    audio = AudioSegment.from_mp3(mp3_file)
    audio = audio.set_frame_rate(16000).set_sample_width(2).set_channels(1)
    audio.export(wav_file, format="wav")

def transcribe_audio(wav_file):
    asr = ASRExecutor()
    result = asr(wav_file)
    return result

def add_punctuation(text):
    text_punc = TextExecutor()
    result = text_punc(text)
    return result

def process_audio_file(input_file, output_folder):
    output_file = os.path.join(output_folder, f"{Path(input_file).stem}.txt")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as wav_file:
        convert_mp3_to_wav(input_file, wav_file.name)
        result_text = transcribe_audio(wav_file.name)
        result_text_with_punctuation = add_punctuation(result_text)

    return result_text_with_punctuation

st.title("中文语音识别")
st.write("请手动输入包含 MP3 格式录音文件的文件夹路径，以及输出识别结果的文件夹路径。")

input_folder = st.text_input("输入文件夹路径：")
output_folder = st.text_input("输出文件夹路径：")

if st.button("加载文件"):
    if os.path.isdir(input_folder) and os.path.isdir(output_folder):
        audio_files = [file for file in os.listdir(input_folder) if file.lower().endswith(".mp3")]
        audio_file_index = 0
        if audio_files:
            st.session_state.audio_files = audio_files
            st.session_state.audio_file_index = audio_file_index
            st.success(f"成功加载 {len(audio_files)} 个 MP3 文件。")
        else:
            st.warning("输入文件夹中没有找到 MP3 文件。")
    else:
        st.error("请确保输入的路径是有效的文件夹。")

if "audio_files" in st.session_state and st.session_state.audio_files:
    audio_file = st.session_state.audio_files[st.session_state.audio_file_index]
    st.write(f"当前文件：{audio_file}")

    input_file = os.path.join(input_folder, audio_file)
    result_text = process_audio_file(input_file, output_folder)
    result_text = st.text_area("识别结果：", value=result_text, height=200)

    if st.button("保存结果并处理下一个文件"):
        output_file = os.path.join(output_folder, f"{Path(audio_file).stem}.txt")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result_text)

        shutil.move(input_file, os.path.join(output_folder, audio_file))
        st.session_state.audio_file_index += 1

        if st.session_state.audio_file_index < len(st.session_state.audio_files):
            audio_file = st.session_state.audio_files[st.session_state.audio_file_index]
            st.write(f"当前文件：{audio_file}")
        else:
            st.success("所有文件已处理完成！")
            del st.session_state.audio_files
            del st.session_state.audio_file_index
