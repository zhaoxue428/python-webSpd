## Disclaimer

- 爬取 xxx

### Basic: vscode

#### 1.Setup BeautifulSoup4 model

    /opt/homebrew/bin/python3 -m pip install beautifulsoup4

- 如果 mac 是由 Homebrew 管理的，可能它会限制使用 pip3 全局安装 python 包的能力。为了防止与 HomeBrew 管理的系统包发生冲突

  - 使用虚拟环境，允许为不同的项目安装不同版本的包，且不会影响到系统中的其他 python 项目
    - /opt/homebrew/bin/python3 -m venv ~/venvs/myproject
  - 激活虚拟环境
    - source ~/venvs/myproject/bin/activate
  - 查看虚拟环境 list
    - ls ~/venvs
  - 安装 beautifulsoup4
    - python3 -m pip install beautifulsoup4

#### 2. 安装 requests python 库

    pip install requests

#### 3. 安装 lxml 库（高效的 XML 和 HTML 解析库）

    pip install lxml

#### 4. 运行 main.py

    python main.py
