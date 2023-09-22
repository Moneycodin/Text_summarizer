import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__="0.0.0"

REPO_NAME = "Text_summarizer"
AUTHOR_USER_NAME = "Moneycodin"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "manmeetroorkee@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    
)