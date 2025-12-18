#!/usr/bin/env python3
"""
文档翻译辅助工具
- 合并：将多个 MD 文件合并为一个，方便上传翻译
- 还原：将翻译后的文件按标记拆分还原

用法：
  python doc_translate.py merge <源目录> <输出文件>
  python doc_translate.py split <翻译后文件> <目标目录>

示例：
  # 合并中文文档
  python doc_translate.py merge i18n/zh/documents all_docs_zh.md
  
  # 翻译后还原到英文目录
  python doc_translate.py split all_docs_en.md i18n/en/documents
"""

import os
import sys
from pathlib import Path

SEPARATOR = "<!-- ===== FILE: {} ===== -->"

def merge(src_dir: str, output_file: str):
    """合并目录下所有 MD 文件"""
    src_path = Path(src_dir)
    files = sorted(src_path.rglob("*.md"))
    
    with open(output_file, "w", encoding="utf-8") as out:
        for f in files:
            rel_path = f.relative_to(src_path)
            out.write(SEPARATOR.format(rel_path) + "\n\n")
            out.write(f.read_text(encoding="utf-8"))
            out.write("\n\n")
    
    print(f"✅ 合并完成: {len(files)} 个文件 -> {output_file}")

def split(input_file: str, dest_dir: str):
    """按标记拆分还原为多个文件"""
    dest_path = Path(dest_dir)
    content = Path(input_file).read_text(encoding="utf-8")
    
    parts = content.split("<!-- ===== FILE: ")
    count = 0
    
    for part in parts[1:]:  # 跳过第一个空部分
        if " ===== -->" not in part:
            continue
        
        header, body = part.split(" ===== -->", 1)
        rel_path = header.strip()
        file_path = dest_path / rel_path
        
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(body.strip() + "\n", encoding="utf-8")
        count += 1
    
    print(f"✅ 还原完成: {input_file} -> {count} 个文件")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "merge":
        merge(sys.argv[2], sys.argv[3])
    elif cmd == "split":
        split(sys.argv[2], sys.argv[3])
    else:
        print(f"未知命令: {cmd}")
        sys.exit(1)
