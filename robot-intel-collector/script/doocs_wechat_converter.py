import sys
import os
import time

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("Please install playwright: pip install playwright")
    sys.exit(1)

def convert_md_to_wechat_html(md_path, output_html_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    print("Starting Playwright browser...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(permissions=["clipboard-read", "clipboard-write"])
        page = context.new_page()
        
        print(f"Opening https://md.doocs.org/ ...")
        page.goto("https://md.doocs.org/")
        try:
            page.wait_for_selector("#wx-box, .wx-box, #output", timeout=15000)
        except Exception as e:
            print("Warning: Could not strictly wait for selector. Proceeding anyway.")
        time.sleep(3)
        
        print("Configuring DOOCS custom theme (衬线, 经典蓝...)...")
        try:
            # 尝试点击“样式”菜单打开右侧或浮窗的配置面板
            style_btn = page.get_by_text("样式", exact=True)
            if style_btn.count() > 0 and not page.get_by_text("衬线", exact=True).is_visible():
                style_btn.first.click()
                time.sleep(1)

            # 通过 JS 查找对应的配置选项并点击，这比定位复杂的嵌套 DOM 更稳健
            page.evaluate("""() => {
                const targetSettings = {
                    "主题": "经典",
                    "字体": "衬线",
                    "字号": "推荐",
                    "主题色": "经典蓝",
                    "图注格式": "只显示 alt",
                    "Mac 代码块": "开启",
                    "代码块行号": "关闭",
                    "微信外链转底部引用": "关闭",
                    "段落首行缩进": "关闭"
                };

                for (const [section, option] of Object.entries(targetSettings)) {
                    // 找到所有的纯文本标签
                    const elements = Array.from(document.querySelectorAll('*'));
                    const label = elements.find(el => el.textContent.trim() === section && el.children.length === 0);
                    
                    if (label) {
                        // 往上找几层共同的父级容器
                        let container = label;
                        for(let i=0; i<4; i++) {
                            if(container.parentElement) container = container.parentElement;
                        }
                        
                        // 在这个父级容器内找对应的选项按钮
                        const btns = Array.from(container.querySelectorAll('*'));
                        const targetBtn = btns.find(el => el.textContent.trim() === option && el.children.length === 0);
                        if (targetBtn) {
                            targetBtn.click();
                        }
                    }
                }
            }""")
            time.sleep(1)
            
            # 点击页面其它地方以关闭弹出的面板
            page.mouse.click(10, 200)
            time.sleep(0.5)
        except Exception as e:
            print("Warning: Could not configure custom DOOCS styles.", e)
        
        print("Injecting Markdown content...")
        
        try:
            page.evaluate(
                "async (text) => await navigator.clipboard.writeText(text)", 
                md_content
            )
            
            editor_selectors = ['.CodeMirror', '.monaco-editor', '.CodeMirror-scroll', '.bytemd-editor', 'textarea']
            clicked = False
            for sel in editor_selectors:
                if page.locator(sel).count() > 0:
                    page.locator(sel).first.click()
                    clicked = True
                    break
                    
            if not clicked:
                page.mouse.click(200, 300)
            
            page.keyboard.down('Control')
            page.keyboard.press('a')
            page.keyboard.up('Control')
            page.keyboard.press('Backspace')
            
            page.keyboard.down('Control')
            page.keyboard.press('v')
            page.keyboard.up('Control')
            
        except Exception as e:
            print(f"Warning during paste: {e}")
            
        # 等待页面渲染出 wx-box 并准备好样式
        print("Waiting 3 seconds for rendering and theme initialization...")
        time.sleep(3)
        
        # 很多在线渲染工具会将主题样式注入到全局或动态创建的 <style> 标签里
        # 这里除了拿到 #wx-box 以外，还会执行复制页面的全局 style 逻辑，保证样式跟网站一样
        rendered_html = page.evaluate("""() => { 
            const box = document.getElementById('wx-box') || document.querySelector('.wx-box') || document.getElementById('output');
            if (!box) return '';
            
            // 抓取可能影响该块的页内 style 标签（主要是 DOOCS 注入的主题 CSS）
            let styles = '';
            document.querySelectorAll('style').forEach(s => {
                // DOOCS 会把一些关键排版写在带有特殊标识或内联的 style 标签里
                // 修改：提取所有没有 type 限制或跟排版有关的全局 style
                if (s.innerText.includes('#wx-box') || s.innerText.includes('.wx-box') || s.innerText.includes('#output') || s.innerText.includes('font-family') || s.innerText.includes('.h1')) {
                    styles += s.outerHTML;
                }
            });
            
            return styles + box.outerHTML; 
        }""")
        
        if not rendered_html or len(rendered_html) < 100:
            print("Warning: Extracted HTML is empty or very short. The paste might have failed.")
        
        # 核心修复 2：在生成的本地页面植入 Clipboard API 复制按钮，避免 Ctrl+A 污染剪贴板格式
        full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<title>微信公众号排版预览</title>
<style>
  body {{
    background-color: #f5f5f5;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  }}
  .action-bar {{
    position: sticky;
    top: 0;
    background: #fff;
    padding: 15px 30px;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    z-index: 100;
    display: flex;
    align-items: center;
    gap: 15px;
  }}
  .copy-btn {{
    background-color: #07c160;
    color: white;
    border: none;
    padding: 10px 24px;
    font-size: 16px;
    font-weight: bold;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.2s;
  }}
  .copy-btn:hover {{
    background-color: #06ad56;
  }}
  .preview-container {{
    background-color: #fff;
    padding: 20px 40px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    max-width: 600px;
    width: 100%;
    box-sizing: border-box;
  }}
  .hint {{
    color: #666;
    font-size: 14px;
  }}
</style>
</head>
<body>
  <div class="action-bar">
    <button id="copyBtn" class="copy-btn">🚀 一键复制到微信</button>
    <span class="hint">请点击此按钮复制（不要手动Ctrl+A，会导致格式错乱）</span>
  </div>

  <div class="preview-container" id="previewContainer">
    {rendered_html}
  </div>

  <script>
    document.getElementById('copyBtn').addEventListener('click', async function() {{
      const contentElement = document.getElementById('wx-box') || document.querySelector('.wx-box') || document.getElementById('output');
      if (!contentElement) {{
          alert("找不到渲染内容！可能提取失败。");
          return;
      }}
      
      // 非常关键：这里不仅要把 contentElement.outerHTML 放进去
      // 如果有挂载的全局 <style> 标签（Doocs 很喜欢把微信的类名样式写在这里），也需要带进剪贴板里
      let htmlToCopy = '';
      document.querySelectorAll('style').forEach(s => {{
         if (s.innerText.includes('wx-box') || s.innerText.includes('.h1') || s.innerText.includes('output')) {{ htmlToCopy += s.outerHTML; }}
      }});
      htmlToCopy += contentElement.outerHTML;
      
      const text = contentElement.innerText;
      
      try {{
        // 使用 ClipboardItem 强行只写入纯正的富文本格式，规避浏览器自动附加的无关样式
        const clipboardItem = new ClipboardItem({{
          'text/html': new Blob([htmlToCopy], {{ type: 'text/html' }}),
          'text/plain': new Blob([text], {{ type: 'text/plain' }})
        }});
        await navigator.clipboard.write([clipboardItem]);
        
        const btn = document.getElementById('copyBtn');
        const originalText = btn.innerText;
        btn.innerText = "✅ 复制成功！去粘贴吧";
        btn.style.backgroundColor = "#ff9800";
        setTimeout(() => {{
            btn.innerText = originalText;
            btn.style.backgroundColor = "#07c160";
        }}, 3000);
        
      }} catch (err) {{
        console.error('Clipboard API failed', err);
        // 兼容性降级方案
        const selection = window.getSelection();
        const range = document.createRange();
        range.selectNodeContents(contentElement);
        // 如果有 fallback，我们最好创建一个临时隐藏容器包含 style 和 body
        const tempDiv = document.createElement('div');
        tempDiv.innerHTML = htmlToCopy;
        document.body.appendChild(tempDiv);
        range.selectNodeContents(tempDiv);
        selection.removeAllRanges();
        selection.addRange(range);
        
        try {{
            document.execCommand('copy');
            alert("已使用降级方案复制成功！");
        }} catch (e) {{
            alert("复制失败，您的浏览器不支持此操作。");
        }}
        selection.removeAllRanges();
        document.body.removeChild(tempDiv);
      }}
    }});
  </script>
</body>
</html>"""
        
        with open(output_html_path, 'w', encoding='utf-8') as f:
            f.write(full_html)
        print(f"Successfully saved WeChat HTML to: {output_html_path}")
            
        browser.close()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python doocs_wechat_converter.py <input.md> <output.html>")
        sys.exit(1)
        
    md_file = sys.argv[1]
    html_file = sys.argv[2]
    
    if not os.path.exists(md_file):
        print(f"Error: Markdown file '{md_file}' not found.")
        sys.exit(1)
        
    convert_md_to_wechat_html(md_file, html_file)