import os
from PIL import Image, ImageSequence


def generate_img_h(path):
    total_size = 0
    file_count = 0
    files = os.listdir(path)
    f = open('img.h', 'w')
    f.write('#include <pgmspace.h>\n')
    f.write('typedef struct image{\n')
    f.write('    int width;\n')
    f.write('    int height;\n')
    f.write('    uint16_t pixels[];\n')
    f.write('}image;\n\n')
    for file in files:
        if file.endswith('.jpg') or file.endswith('.png'):
            file_count += 1
            img = Image.open(os.path.join(path, file))
            width, height = img.size
            pixels = img.load()
            name = file.split('.')[0]
            print(f'{name}: {width}x{height} pixels')
            total_size += width * height * 2
            f.write(f'const image {name} = {{\n')
            f.write(f'    {width},\n')
            f.write(f'    {height},\n')
            f.write(f'    {{\n\t\t')
            for y in range(height):
                for x in range(width):
                    if x % 16 == 0 and x != 0:
                        f.write('\n\t\t')
                    r, g, b = pixels[x, y]
                    color = (b & 0xf8) << 8 | (g & 0xfc) << 3 | r >> 3
                    f.write(f'0x{color:06x}, ')
                f.write('\n\t\t')
            f.write('}};\n\n\n')
            total_size /= 1024
    f.close()
    print(f'Total size: {total_size} KB')
    print(f'File count: {file_count}')

if __name__ == '__main__':
    generate_img_h("image")
