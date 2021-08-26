class cipher:
    def __init__(self):
        pass

    def set_word(self, word):
        self.word=word
        print(self.word)

    def set_shift(self, shift):
        self.shift=int(shift)
        print(self.shift)

    def encode(self):
        self.encoded =""
        for i in self.word:
            self.encoded=self.encoded+chr((ord(i.upper())+self.shift - 65) % 26 + 65)
        self.display("encoded")
    
    def display(self, param):
        if(param=="encoded"):
            print(self.encoded)
        else:
            print(self.decoded)

    def decode(self):
        self.decoded=""
        for i in self.word:
            self.decoded = self.decoded + chr((ord(i.upper())-(self.shift) - 65) % 26 + 65)
        self.display("decoded")


#while(1):
cipher_obj=cipher()
while(1):
    cipher_obj.set_word(str(input("Give word")))
    cipher_obj.set_shift(input("Give shift"))
    encode_or_decode=input("encode(1) or decode(2)")
    if(encode_or_decode == "1" or encode_or_decode.lower() == "encode"):
        cipher_obj.encode()
        print("cipher word",cipher_obj.word)
    else:
        cipher_obj.decode()
