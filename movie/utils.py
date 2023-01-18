import os


# создание path для сохранения файлов в папку media
def get_file_path_poster(instance, filename):
    # получаем расширение файла
    ext = filename.split('.')[-1]
    # получаем имя файла
    filename = f"{instance.title}.{ext}"
    # возвращаем путь к файлу
    return os.path.join('movies/poster/', filename)


def get_file_path_video(instance, filename):
    # получаем расширение файла
    ext = filename.split('.')[-1]
    # получаем имя файла
    filename = f"{instance.title}.{ext}"
    # возвращаем путь к файлу
    return os.path.join('movies/video/', filename)
