from guizero import *
app = App()


def size_slide():
    Slider(app,
            start=20,
            end=40,
            )
size_slide()
picture = Picture(app,image= "KLlook.png")


app.display()