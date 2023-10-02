import os
import subprocess

# 假设Grobid已经安装并运行在本地端口8070上
grobid_url = "http://localhost:8070/api/processFulltextDocument"

pdf_folder = "/您的PDF文件夹的路径"
output_folder = "/用于保存Grobid输出的文件夹路径"

# 遍历PDF文件
for pdf_file in os.listdir(pdf_folder):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_folder, pdf_file)

        # 使用curl发送POST请求到Grobid
        subprocess.run(["curl", "-v", "-H", "Content-Type: application/pdf", "--data-binary",
                        "@{}".format(pdf_path), grobid_url, "-o", os.path.join(output_folder, pdf_file + ".xml")])
