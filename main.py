import tkinter as tk
from morseTranslator import MorseTranslator

def updateText(textVar):
    text = textVar.get()
    translatedText = MorseTranslator.translate(text)
    resultVar.set(translatedText)


# Interface
app = tk.Tk()
app.title('Morse Translator')

width, height = app.winfo_screenwidth(), app.winfo_screenheight()
L, H = width / 3, height / 2
X, Y = (width - L) / 2, (height - H) / 2
app.geometry('%dx%d%+d%+d' % (L,H,X,Y))

textVar = tk.StringVar(app, value='Entrez votre texte')
textVar.trace("w", lambda name, index, mode, textVar=textVar: updateText(textVar))
entry = tk.Entry(app, textvariable=textVar)

resultVar = tk.StringVar(app, value='')
result = tk.Label(app, textvariable=resultVar)

entry.pack()
result.pack()
app.mainloop()
