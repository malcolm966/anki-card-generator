# anki-card-generator

## Version1(Claude Project Version)

### Tech
- python
- uv 包管理
- flask

### Purpose

使用claude, 进行下面流程:
- 新建一个Claude project, 
    - 里面放有:
        - User的背景介绍. 
        - User熟悉的日语单词. 
        - User熟悉的日语表现语法 
- User将在此项目中询问Claude问题. Claude将使用User提供的上述资料, 生成适切的答案.让用户知道如何使用已知的语言知识, 回答该问题.

### To do list

1. 使用Anki 插件(export cards/notes from browser with metadata to csv or xlsx) 将Anki已数值的单词转为csv, 并且上传到google sheet,进行正则替换,删除不用的列, 并正则替换,只保留单词部分.
2. 新建Grammar.md, 录入毎日のんびり日本語教師的语法
    - 使用爬虫,抓取毎日のんびり日本語教師的语法条目,导入SQLite 数据库
    - 文法, 单词词汇 分类.
3. 调整合适的提示语
4. 使用BQ卡组中的问题, 询问Claude
5. 复制答案, 并生成语音
6. 使用 DK course 列出, 工作中场景
7. 使用6的场景, 询问Claude




        ┌──────────────┐
        │ 原始 grammar │  ← SQLite / PostgreSQL
        │ (结构化数据)│
        └──────┬───────┘
               │ id
               ▼
        ┌──────────────┐
        │ 向量索引 FAISS│  ← 只存 embedding + id
        │ (语义空间)  │
        └──────┬───────┘
               │ search
               ▼
        用户问题 → 向量 → Top-k ids → 回表 → LLM
