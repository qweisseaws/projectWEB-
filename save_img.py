import requests
import asyncio


async def save_function_main(images, which_img):
    which_img_true = int(which_img) - 1
    url_img = requests.get(images[which_img_true])
    img_optoin = open(str(which_img) + '.jpg', 'wb')
    img_optoin.write(url_img.content)
    img_optoin.close()

    return True