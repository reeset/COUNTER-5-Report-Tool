from cryptography.fernet import Fernet
from os.path import exists
import shutil
import os


class EncryptUtils:
    KEYFILE_PATH = "./all_data/vendor_manager/loCakey.txt"
    TMP_COPY_FILE = "./all_data/vendor_manager/tmp_file.dat"

    def __init__(self):
        super().__init__()

    def is_encrypted(self):
        if not exists(self.KEYFILE_PATH):
            return False
        else:
            return True

    def new_key(self):
        obey = Fernet.generate_key()
        with open(self.KEYFILE_PATH, 'wb') as pkwy:
            pkwy.write(obey)

    def load_key(self):
        if not exists(self.KEYFILE_PATH):
            self.new_key()

        with open(self.KEYFILE_PATH, 'rb') as pkwy:
            key = pkwy.read()
        return key

    def decrypt_buffer_stream(self, encrypted_buffer):
        crypt = Fernet(self.load_key())

        buffer = crypt.decrypt(encrypted_buffer)
        return buffer

    def encrypt_buffer_stream(self, buffer):
        crypt = Fernet(self.load_key())

        encrypted_buffer = crypt.encrypt(buffer)
        return encrypted_buffer

    def encrypt_file(self, source_file):

        tmp_file = self.TMP_COPY_FILE
        shutil.copyfile(source_file, tmp_file)

        with open(tmp_file, 'rb') as handle:
            buffer = handle.read()

        encrypted_buffer = self.encrypt_buffer_stream(buffer)

        with open(source_file, 'wb') as encrypted_handle:
            encrypted_handle.write(encrypted_buffer)

        os.remove(tmp_file)

