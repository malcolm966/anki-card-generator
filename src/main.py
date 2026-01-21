import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from db_util import create_grammar_table, insert_grammar
from log_util import get_logger


logger = get_logger("grammar_import")

def extract_urls_from_index(html_path: str) -> list[dict]:
    """
    从index-example.html中读取含有<span class="n[1-5]color">行中a标签的url
    返回包含url和级别信息的字典列表
    """
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r'<span class="n([1-5])color">.*?</span>.*?<a href="([^"]+)"[^>]*>([^<]+)</a>'
    matches = re.findall(pattern, content)

    results = []
    for level, url, title in matches:
        results.append({
            "level": f"N{level}",
            "url": url,
            "title": title.strip(),
        })

    return results


def fetch_article_thumb(url: str) -> dict | None:
    wanted = {"接続", "意味", "解説", "例文"}
    eng = {"接続":"usage", "意味":"meaning", "解説":"explanation", "例文":"sentences"}
    """
    获取url的html内容，提取figure class="p-articleThumb"的内容
    返回figure元素的完整HTML或图片URL
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        result = {}

        for h3 in soup.find_all("h3"):
            title = h3.get_text(strip=True)
            if title not in wanted:
                continue

            ps = []
            for sib in h3.find_next_siblings():
                if sib.name == "h3":
                    break
                if sib.name == "p":
                    ps.append(sib.get_text(strip=True))

                result[eng[title]] = "\n".join(ps)
        # figure = soup.find("figure", class_="p-articleThumb")

        # if figure:
        #     img = figure.find("img")
        #     if img and img.get("src"):
        #         return img.get("src")
        return result
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def main():
    index_path = Path(__file__).parent.parent / "resources" / "index-example.html"
    create_grammar_table()
    print("正在解析 index-example.html...")
    grammar_items_raw = extract_urls_from_index(str(index_path))
    print(f"找到 {len(grammar_items_raw)} 个语法条目\n")
    grammar_items = dict()
    for i in grammar_items_raw:
        title = i['title'].strip()
        url  = i["url"]
        if title not in grammar_items and url:
            grammar_items[i["title"]] = dict()
            grammar_items[i["title"]]['url'] = i["url"]
            grammar_items[i["title"]]['level'] = i['level']
            
    print(f"找到 {len(grammar_items)} 个语法条目\n")
    for idx, title in enumerate(grammar_items):
        level = grammar_items[title]["level"]
        # print(f"当前语法点是:{title}, 对应级别是 {level}")

        grammar = fetch_article_thumb(grammar_items[title]["url"])
        if grammar:
            # print(f"当前语法点是:{title}    Grammar Content: {grammar}")
            try:
                insert_grammar(title=title,
                        usage=grammar['usage'],
                        meaning=grammar['meaning'],
                        explanation=grammar['explanation'],
                        sentences=grammar['sentences'],
                        level=level)
            except Exception as e:
                logger.exception(
            f"插入语法失败 | title={title} | url={grammar_items[title]["url"]}"
        )

if __name__ == "__main__":
    main()
