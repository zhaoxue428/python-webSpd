# main.py

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
    python3 main.py

# main3.py --还没完事，可能因为 chrome 版本太新了，和下载的 WebDriver 版本不一致导，导致 error “Unable to obtain driver for chrome”

## Disclaimer

- 爬取 url 视频的字幕

## fix questions

first

- 做了什么：python3 main3.py
- error:ModuleNotFoundError: No module named 'requests'
- 代码：import requests
- 解决方法：python3 -m pip install requests
  用 python 的包管理器 pip 来安装 requests 库

second

- 做了什么：python3 -m pip install requests
- error: externally-managed-environment 外部的管理环境
- 代码：无
- 分析： python 的包管理器 pip 收到了限制，以防止干扰系统级别的包管理器，如 Homebrew
- 解决方法：使用虚拟环境 （创建一个虚拟环境可以使你在隔离的环境中安装和管理 python 库，不受外部包管理器的影响）
  使用虚拟环境的优点：虚拟环境是管理 Python 项目依赖的最佳实践，可以避免多个项目之间的依赖冲突

  # 创建虚拟环境

  python3 -m venv myvenv

  # 激活虚拟环境（MacOS/Linux）

  source myvenv/bin/activate

  # 激活虚拟环境（Windows）

  myvenv\Scripts\activate

  # 安装 requests

  pip install requests

third

- 做了什么：python3 main3.py
- error:抓去的字幕有问题，
- 分析：寻找原因，发现 url 并不是拥有字幕的视频的 url；流媒体服务通常会使用多种技术来保护其内容
- 解决方法：
  pip install selenium --使用像 Selenium 这样的工具来模拟真实用户的行为
  下载对应的 WebDriver --chrome://settings/help 来查看版本信息。 https://googlechromelabs.github.io/chrome-for-testing/#stable

other

- 做了什么：`git filter-repo --invert-paths --path-glob 'chrome-mac-arm64/**'
` --因为 git push 的时候发现.git 占用空间爆了 150M，所以调查具体哪些占用内容那么多,找到了具体的大文件尝试移除，即用到了这个命令行，但是执行的时候出了 error
- error:
  Aborting: Refusing to destructively overwrite repo history since
  this does not look like a fresh clone.
  (you have unstaged changes)
  Please operate on a fresh clone instead. If you want to proceed
  anyway, use --force.
- 分析：unstaged changes -> 本地修改了，但是还没提交, 所以需要提交； fresh clone ->目前不是一个新的克隆，需要克隆一个新的仓库
- 解决方法：
  git add . ; git commit
