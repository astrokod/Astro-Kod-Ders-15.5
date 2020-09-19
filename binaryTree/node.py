# Nod sınıfını oluştur
class Node:
    # Constructor metod. Zorunlu olarak değer alır
    def __init__(self, value):
        # Değeri self.value' değişkenine ata
        self.value = value
        # Bu nodun solu ve sağında birer boş eleman oluştr
        self.left = None
        self.right = None

    # Bütün nodlar iç içe return et
    def show(self):
        # Recursive olarak tüm nodları bir dict olarak return eder
        # Anlatması çok zor. Videoya bakın
        left = None
        if self.left is not None:
            left = self.left.show()

        right = None
        if self.right is not None:
            right = self.right.show()

        return {"Value": self.value, "LEFT": left, "RIGHT": right}

    def add(self, val):
        # Recursive olarak bir nod ekler
        # Anlatması çok zor. Videoya bakın
        if self.value > val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.add(val)
        elif self.value < val:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.add(val)

    def sort(self):
        # Recursive olarak tüm nodları sıralar
        # Anlatması çok zor. Videoya bakın
        data = []
        if self.left is not None:
            data.extend(self.left.sort())

        data.append(self.value)

        if self.right is not None:
            data.extend(self.right.sort())

        return data

    def search(self, val):
        # Recursive olarak bir nodun var olup olmadığını söyler
        # Anlatması çok zor. Videoya bakın
        if self.value == val:
            return self
        elif self.value > val and self.left is not None:
            return self.left.search(val)
        elif self.value < val and self.right is not None:
            return self.right.search(val)



