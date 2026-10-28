class Dictionary:
    def __init__(self) -> None:
        self.capacity = 8
        self.load_factor = 2 / 3
        self.length = 0
        self.table = [None] * self.capacity

    def __setitem__(self, key, value) -> None:
        index = hash(key) % self.capacity

        if self.table[index] is None:
            self.table[index] = []

        for node in self.table[index]:
            if node["key"] == key:
                node["value"] = value
                return

        self.table[index].append({
            "key": key,
            "hash": hash(key),
            "value": value,
        })

        self.length += 1

    def __getitem__(self, key):
        index = hash(key) % self.capacity

        if self.table[index] is None:
            raise KeyError(f"Key {key} is not found")

        for node in self.table[index]:
            if node["key"] == key:
                return node["value"]

        raise KeyError(f"Key {key} is not found")

    def __len__(self) -> int:
        return self.length
