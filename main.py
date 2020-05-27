import hashlib

def hash_generator(file_path):
    data_file = open(file_path, 'r')
    while True:
        try:
            yield hashlib.md5(next(data_file).encode()).hexdigest()
        except StopIteration:
            data_file.close()
            break


if __name__ == '__main__':
    for item in hash_generator('countries.json'):
        print(item)