import fitz
from app.services.utils import sha256
from app.services.database import insert_document, insert_version, insert_node
from datetime import datetime

def parse_pdf(pdf_path, doc_name, version_num):
    doc_id = insert_document(doc_name)
    ver_id = insert_version(doc_id, version_num, datetime.now().isoformat())

    doc = fitz.open(pdf_path)
    nodes = []
    parent_stack = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                text = ""
                max_size = 0
                for span in line["spans"]:
                    text += span["text"]
                    if span["size"] > max_size:
                        max_size = span["size"]

                text = text.strip()
                if not text:
                    continue

                level = 3
                if max_size > 16:
                    level = 1
                elif max_size > 12:
                    level = 2

                if level <= 2:
                    while parent_stack and parent_stack[-1]["level"] >= level:
                        parent_stack.pop()

                    parent_id = parent_stack[-1]["id"] if parent_stack else None
                    hash_val = sha256(text)
                    node_id = insert_node(ver_id, text, level, "", parent_id, hash_val)
                    parent_stack.append({"id": node_id, "level": level})
                    nodes.append({"id": node_id, "heading": text, "level": level, "parent_id": parent_id})
                else:
                    if parent_stack:
                        parent_id = parent_stack[-1]["id"]
                        hash_val = sha256(text)
                        node_id = insert_node(ver_id, "", level, text, parent_id, hash_val)
                        nodes.append({"id": node_id, "heading": "", "level": level, "body": text, "parent_id": parent_id})

    doc.close()
    return ver_id, nodes

def parse_and_store(pdf_path, doc_name, version_num):
    return parse_pdf(pdf_path, doc_name, version_num)
