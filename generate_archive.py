import os
import glob

# ==================== 配置区域 ====================
LOCAL_NOVELS_DIR = "novels"
WEB_NOVELS_PATH = ""
TEMPLATE_PATH = "templates/archive_template.html"
OUTPUT_PATH = "archive.html"


# ================================================

def main():
    # 1. 获取所有PDF文件，并按文件名排序
    # 注意：这里依然扫描本地目录
    novel_files = sorted(glob.glob(os.path.join(LOCAL_NOVELS_DIR, "*.pdf")))
    
    table_rows = []
    for file_path in novel_files:
        # 获取本地文件名（带novels/）
        local_file_name = os.path.basename(file_path)
        
        # ！！！核心修改：构建网站上的文件路径 ！！！
        # 如果WEB_NOVELS_PATH为空，则链接就是文件名本身。
        # 例如：'d20 - 01~07.pdf'
        web_file_path = os.path.join(WEB_NOVELS_PATH, local_file_name).replace('\\', '/')
        
        display_name = local_file_name.replace('.pdf', '')
        
        # 构建一行的HTML代码：href 使用网站路径 web_file_path
        row_html = f"""
        <tr>
            <td><strong>《{display_name}》</strong></td>
            <td><a href="{web_file_path}" class="chapter-link">阅读全文</a></td>
            <td>PDF</td>
        </tr>
        """
        table_rows.append(row_html)
    
    # 3. 读取模板文件
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template_content = f.read()
        
    final_html = template_content.replace('<!-- TABLE_ROWS -->', '\n'.join(table_rows))
        
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(final_html)
        
    print(f"✅ 成功生成！已输出至: {OUTPUT_PATH}")
    print(f"📊 共处理了 {len(novel_files)} 个小说文件。")
    print(f"🌐 生成的链接已适配网站根目录路径。")
    
if __name__ == '__main__':
    main()