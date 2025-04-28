from pathlib import Path
import re

target_directory = Path(r"F:\ani-rss\bangumi\彻夜之歌\Season 1")

def rename_files(directory):
    for file_path in directory.iterdir():  # 遍历目标目录
        if file_path.is_file() and "Yofukashi no Uta" in file_path.name:
            # 使用正则表达式提取集数信息
            episode_match = re.search(r'\s(\d+)\s', file_path.name)
            if episode_match:
                episode_number = episode_match.group(1)
                new_file_name = f"[XKsub&LoliHouse] Yofukashi no Uta S01E{episode_number} [WebRip 1080p HEVC-10bit AAC ASSx2].mkv"
                new_file_path = file_path.with_name(new_file_name)
                file_path.rename(new_file_path)
                print(f"Renamed {file_path.name} to {new_file_name}")

if __name__ == "__main__":
    rename_files(target_directory)