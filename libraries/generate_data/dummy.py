import hashlib
import random
import numpy as np


class HashAndSelection:
    # Function to generate a random SHA256 hash
    def generate_sha256_hash(self):
        # Open the file in write mode
        with open("hashes.txt", "w") as f:
            # Generate 10,000 rows
            for _ in range(10000):
                hash_value = hashlib.sha256(str(random.random()).encode('utf-8')).hexdigest()
                bool_value = random.choice([0, 1])  # Random 0 or 1
                f.write(f"('{hash_value}', {bool_value}),\n")

        print("File 'hashes.txt' with 10,000 rows has been generated.")


class MatrixFileAnalysis:
    def __init__(self):
        pass

    def matrix(self):
        with open("matrix.txt", "w") as f:
            # generate 10 000 rows
            for _ in range(10000):
                nparray = np.ndarray((1,10))
                for val in nparray:

