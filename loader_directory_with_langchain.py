from langchain_community.document_loaders import DirectoryLoader
import os
def langchain_load_files():
    test_local_repo_path = os.path.join(PROJECT_DIRECTORY, "test_repo")
    loader = DirectoryLoader(test_local_repo_path, glob="**/*.md")
    docs = loader.load()
    print(f"total docs: {len(docs)}")
    # 将docs保存在PROJECT_DIRECTORY下新建目录output
    output_directory = os.path.join(PROJECT_DIRECTORY, "output")
    os.makedirs(output_directory, exist_ok=True)

    # 保存每个doc，文件名用文件原来的名字，格式修改为txt
    for doc in docs:
        # 为了避免文件名重复，用doc.metadata['source']作为文件名，后缀改为txt, / 改为_
        # 将绝对路径转换为相对路径，并使用相对路径作为文件名，后缀改为txt, / 改为_
        relative_path = os.path.relpath(doc.metadata['source'], start="test_repo")
        relative_filename = relative_path.replace('/', '_')
        original_filename = os.path.splitext(os.path.basename(doc.metadata['source']))[0]
        original_filename = relative_filename + "_" + original_filename
        file_path = os.path.join(output_directory, f"{original_filename}.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(doc.page_content)
            
        print(f"Saved {original_filename}.txt")
        
        
        print(docs[0].json)
        print(docs[0].page_content[0:])

        print(docs[1].page_content[0:])
