import lucene
import os
from lxml import etree
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import IndexWriter, IndexWriterConfig
from org.apache.lucene.document import Document, Field, FieldType
from org.apache.lucene.store import MMapDirectory
from java.nio.file import Paths

lucene.initVM()

indexDir = MMapDirectory(Paths.get("/用于存储索引的文件夹路径"))
config = IndexWriterConfig(StandardAnalyzer())
writer = IndexWriter(indexDir, config)

# 解析XML文件
def parse_xml(xml_path):
    tree = etree.parse(xml_path)
    return tree

# 来自Grobid的包含元数据的XML文件
xml_folder = "/Grobid输出的XML文件夹路径"
# 使用的是 lxml 库来解析 XML
tree = parse_xml(xml_folder)

# 提取标题
def extract_title(tree):
    title = tree.findtext("title")
    return title

# 提取作者列表
def extract_authors(tree):
    authors = [author.text for author in tree.xpath("//authors/author")]
    return authors

# 提取日期
def extract_date(tree):
    date = tree.findtext("date")
    return date

# 提取机构
def extract_affiliation(tree):
    affiliation = tree.findtext("affiliation")
    return affiliation

# 提取地址
def extract_address(tree):
    address = tree.findtext("address")
    return address

# 提取全文
def extract_fulltext(tree):
    fulltext = tree.findtext("fulltext")
    return fulltext

for xml_file in os.listdir(xml_folder):
    if xml_file.endswith(".xml"):
        xml_path = os.path.join(xml_folder, xml_file)

        # 从XML中提取元数据
        # 请自行编写代码以从XML中提取title, authors, date, affiliation, address, fulltext等信息
        title = extract_title(xml_path)
        authors = extract_authors(xml_path)
        date = extract_date(xml_path)
        affiliation = extract_affiliation(xml_path)
        address = extract_address(xml_path)
        fulltext = extract_fulltext(xml_path)

        # 创建Lucene文档并添加字段
        doc = Document()
        doc.add(Field("title", title, FieldType))
        doc.add(Field("authors", authors, FieldType))
        doc.add(Field("date", date, FieldType))
        doc.add(Field("affiliation", affiliation, FieldType))
        doc.add(Field("address", address, FieldType))
        doc.add(Field("fulltext", fulltext, FieldType))

        writer.addDocument(doc)

writer.close()
