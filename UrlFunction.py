global chapter
global paragraph
global type
import asyncio

async def get_url(predmet, number_of_task, number_of_class, paragraph=False, type=False, chapter=False):
    if predmet == 'algebra':
        if number_of_class == '7':
            url = f'https://gdz.ru/class-{number_of_class}/{predmet}/makarichev-18/{number_of_task}/'
        if number_of_class == '9':
            url = f'https://gdz.ru/class-{number_of_class}/{predmet}/makarichev-14/task-{number_of_task}/'
        if number_of_class == '8':
            url = f'https://gdz.ru/class-{number_of_class}/{predmet}/makarychev-8/{number_of_task}-nom/'
        print(url)
    if predmet == 'biologiya':
        if number_of_class == '9':
            url = f'https://gdz.ru/class-{number_of_class}/{predmet}/pasechenik/{number_of_task}-item/'
        if number_of_class == '8':
            url = f'https://gdz.ru/class-{number_of_class}/{predmet}/kolesov-mash/{number_of_task}-item/'
        if number_of_class == '7':
            url = f'https://gdz.ru/class-{number_of_class}/{predmet}/latiushin/{number_of_task}-item/'
    if predmet == 'russkii_yazik':
        if number_of_class == '9':
            url = f'https://gdz.ru/class-{number_of_class}/{predmet}/barhudarov-kruchkov-9/{number_of_task}-nom/'
        if number_of_class == '8':
            url = f'https://gdz.ru/class-{number_of_class}/{predmet}/barhudarov-8/{number_of_task}-nom/'
        if number_of_class == '7':
            url = f'https://gdz.ru/class-{number_of_class}/{predmet}/baranova/{number_of_task}-nom/'
        print(url)
    if predmet == 'himiya':
        if number_of_class == '9':
            if 'вопросы' in type.lower():
                type = '1'
                url = f'https://gdz.ru/class-{number_of_class}/{predmet}/rudzitis-feldman/{paragraph}-item-{type}-{number_of_task}/'
            if 'подумай' in type.lower():
                type = '2'
                url = f'https://gdz.ru/class-{number_of_class}/{predmet}/rudzitis-feldman/{paragraph}-item-{type}-{number_of_task}/'
            if 'тестовые' in type.lower():
                type = '3'
                url = f'https://gdz.ru/class-{number_of_class}/{predmet}/rudzitis-feldman/{paragraph}-item-{type}-{number_of_task}/'
            print(url)
        if number_of_class == '8':
            url = f'https://gdz.ru/class-{number_of_class}/{predmet}/rudzitis-feldman/{number_of_task}-item/'
    if predmet == 'geometria':
        url = f'https://gdz.ru/class-7/{predmet}/atanasyan-7-9/{chapter}-chapter-{number_of_task}/'
        print(url)
    if predmet == 'english':
        if number_of_class == '7':
            url = f'https://gdz.ru/class-{number_of_class}/{predmet}/reshebnik-angliyskiy-v-fokuse-vaulina-yu-e/{number_of_task}-s/'
        if number_of_class == '9':
            url = f'https://gdz.ru/class-{number_of_class}/{predmet}/reshebnik-spotlight-{number_of_class}-vaulina-yu-e/{number_of_task}-s/'
        if number_of_class == '8':
            url = f'https://gdz.ru/class-{number_of_class}/{predmet}/reshebnik-spotlight-8-angliyskiy-v-fokuse-vaulina-yu-e/{number_of_task}-s/'
        print(url)
    if predmet == 'literatura':
        if number_of_class == '9':
            url = f"https://gdz.ru/class-{number_of_class}/literatura/korovina/{chapter}-prt-{number_of_task}/"
        if number_of_class == '8':
            url = f"https://gdz.ru/class-{number_of_class}/literatura/korovina/{chapter}-prt-{number_of_task}/"
        if number_of_class == '7':
            url = f"https://gdz.ru/class-{number_of_class}/literatura/korovina/{chapter}-prt-{number_of_task}/"
        print(url)
    return url