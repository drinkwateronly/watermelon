from PIL import Image, ImageDraw
import openpyxl


def MakeCircleImage(image):
    circle_image = Image.new("RGBA", image.size)
    draw = ImageDraw.Draw(circle_image)
    draw.ellipse([(0, 0), image.size], fill=(255, 255, 255))
    result = Image.new("RGBA", image.size)
    result.paste(image, mask=circle_image)
    return result


def ChangeImageShape(image, width):
    result = image.resize((width, width))
    return result


if __name__ == '__main__':
    wb = openpyxl.load_workbook('./info.xlsx')
    sheet = wb.active

    for row in range(1, 12):
        imageDir = str(sheet[f'B{row}'].value)
        imageFileName = sheet[f'C{row}'].value
        print(sheet[f'D{row}'].value)
        imageSize = int(sheet[f'D{row}'].value.split('x')[0])

        index = row
        image = Image.open(f"./original2/{index}.jpg")
        image = ChangeImageShape(image, imageSize)
        image = MakeCircleImage(image)
        image.save(f'../res/raw-assets/{imageDir}/{imageFileName}')
