import easyocr

reader = easyocr.Reader(['en']) # specify the language  

print("Ready!")
while True:
    file = input()

    result = reader.readtext(file)

    for (bbox, text, prob) in result:
        print(f'Text: {text}, Probability: {prob}')
