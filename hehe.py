from guizero import App,TextBox,Combo,Slider,Drawing

def draw_meme():
    meme.clear()
    meme.image(0,0,"KLlook.png")
    meme.text(20,8.5,toptext.value,
            color=color.value,
            font=font.value,
            size=slider.value)
    meme.text(20,50,bottomtext.value,
            color.value,
            font.value,
            size=slider.value)

app = App(title="guizero")
toptext = TextBox(app,"top text",command=draw_meme)
bottomtext = TextBox(app,"bottom text",command=draw_meme)
color = Combo(app,
    options=["black","white","red","green","blue","orange","maroon","dark red","brown","firebrick"],
    command=draw_meme,
    selected="blue")

font = Combo(app,
    options=["Times new roman","Arial","Verada","Courier","Agency FB","Algerian","Calibri","Cambria"],
    command=draw_meme)

slider = Slider(app,
            start=20,
            end = 40,
            command=draw_meme)

meme = Drawing(app,width="fill",height="fill")
draw_meme()
app.display()