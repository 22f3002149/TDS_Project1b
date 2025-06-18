import google.generativeai as genai

def get_image_description(image_path):
    genai.configure(api_key='AIzaSyC5YkGur9cSxFSBotVm1q5JTYO-bpnNGGY')

    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([
        {'text': 'What is in this image?'},
        {'inline_data': {'mime_type': 'image/webp', 'data': image_data}}
    ])
    print(response)

get_image_description('ImgData/02.webp')