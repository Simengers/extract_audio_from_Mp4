import os
from moviepy.editor import VideoFileClip

def extract_audio(input_file, output_file):
    try:
        # 加载视频文件
        video = VideoFileClip(input_file)
        
        # 提取音频
        audio = video.audio
        
        # 将音频保存为MP3文件
        audio.write_audiofile(output_file)
        
        # 关闭视频文件
        video.close()
        
        print(f"音频已成功提取并保存为 {output_file}")
    except Exception as e:
        print(f"提取音频时发生错误: {str(e)}")

def main():
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 输入文件路径
    input_file = input("请输入MP4文件的路径（或拖拽文件到此处）: ").strip('"')
    
    # 如果输入的是相对路径，转换为绝对路径
    if not os.path.isabs(input_file):
        input_file = os.path.join(current_dir, input_file)
    
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print("输入文件不存在，请检查路径是否正确。")
        return
    
    # 生成输出文件路径（与输入文件同目录，但扩展名改为.mp3）
    output_file = os.path.splitext(input_file)[0] + ".mp3"
    
    # 提取音频
    extract_audio(input_file, output_file)

if __name__ == "__main__":
    main()
