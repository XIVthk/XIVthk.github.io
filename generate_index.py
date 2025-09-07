#!/usr/bin/env python3
import os
import json
from jinja2 import Template


def generate_index():
    """
    读取 metadata.json，生成按系列分组的 index.html 主页
    """
    # 1. 读取元数据文件
    with open('metadata.json', 'r', encoding='utf-8') as f:
        metadata = json.load(f)
    
    # 2. 按系列 (series) 进行分组
    series_dict = {}
    for item in metadata['novels']:
        series_name = item['series']
        if series_name not in series_dict:
            series_dict[series_name] = []
        # 为每个作品添加完整的网页链接路径
        item['href'] = os.path.join('novels', item['file_name']).replace('\\', '/')
        series_dict[series_name].append(item)
    
    # 3. 读取主页模板文件
    with open('templates/index_template.html', 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    # 4. 渲染模板（将数据填充进去）
    template = Template(template_content)
    html_output = template.render(series_dict=series_dict)
    
    # 5. 将渲染结果写入 index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_output)
    
    print("✅ index.html 已成功生成！")
    print(f"📋 共处理了 {len(metadata['novels'])} 部作品，分为 {len(series_dict)} 个系列。")


if __name__ == '__main__':
    generate_index()