import string

def sort(d):
    d = list(d.items())
    while True:
        for i in range(len(d)-1):
            if d[i][-1] > d[i+1][-1]:
                d[i], d[i+1] = d[i+1], d[i]
        cnt = 0
        for j in range(len(d)-1):
            if d[j][-1] <= d[j+1][-1]:
                cnt += 1
        if cnt == len(d)-1:
            break
    return d

cipher = "".lower()

class FrequencyAnalysis:
    def __init__(self):
        self.freq_eng = {'a': 0.0817, 'b': 0.0150, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270, 'f': 0.0223,
               'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015, 'k': 0.0077, 'l': 0.0403,
               'm': 0.0241, 'n': 0.0675, 'o': 0.0751, 'p': 0.0193, 'q': 0.0010, 'r': 0.0599,
               's': 0.0633, 't': 0.0906, 'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015,
               'y': 0.0197, 'z': 0.0007}
        self.freq_cipher, self.mapping, self.key = {}, {}, {}
        self.letters = string.ascii_lowercase

    def count_freq(self):
        for i in self.letters:
            if i not in self.freq_cipher:
                self.freq_cipher[i] = round(cipher.count(i)/len("".join(cipher.split())), 4)
    
    def map_cipher(self):
        for i in self.letters:
            map = {}
            for j in self.letters:
                map[j] = round(abs(self.freq_cipher[i] - self.freq_eng[j]), 4)
            self.mapping[i] = sort(map)
        return self.mapping 
    
    def create_initial_key(self):
        for i in self.mapping:
            for letter, diff in self.mapping[i]:
                if letter in self.letters:
                    self.key[i] = letter
                    self.letters = self.letters.replace(letter, '')
                    break

    def manual_set(self, ct, k):
        self.key[ct] = k
    
    def get_key(self):
        return self.key

    def decryption(self, c):
        decrypted = ''
        for i in c:
            if i in self.key:
                decrypted += self.key[i]
            else:
                decrypted += i
        return decrypted

if __name__ == '__main__':
    
    obj = FrequencyAnalysis()
    obj.count_freq()
    obj.map_cipher()
    obj.create_initial_key()
    
    print(f'{cipher}\n')
    print(f'{obj.decryption(cipher)}')
