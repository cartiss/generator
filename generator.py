import hashlib

class Md5Generator():

    def __init__(self, file):
        self.file = file

    def hesh_generator(self):
        with open(self.file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            i = 0

            while i < len(lines):
                line = hashlib.md5(lines[i].encode('utf-8'))
                i += 1
                yield line



if __name__ == '__main__':
    generator = Md5Generator('countries.json')
    for line in generator.hesh_generator():
        print(line.digest())