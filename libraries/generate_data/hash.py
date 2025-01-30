from hashlib import sha256


class Hash:
    """
    Renders different types of hashes
    """
    def __init__(self, /,hash_type='sha256') -> None:
        self.hash_type = hash_type

    def sha256(self, input_data) -> str:
        return sha256(str(input_data).encode('utf-8')).hexdigest()