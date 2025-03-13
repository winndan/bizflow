from fasthtml.common import *
from monsterui.all import *
from homepage.homepage import homepage

app, rt = fast_app(hdrs=Theme.blue.headers(daisy=True), live=True)



# 🏠 Frontend Routes
@rt("/")
def home():
    return homepage()


if __name__ == "__main__":
    serve()