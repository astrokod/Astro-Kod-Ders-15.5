from .node import Node
from json import dumps


# Ağaç sınıfı
class Tree:
    # Constructor metodu. root value değerini zorunlu alır
    def __init__(self, rootVale):
        # Gelen değer ile bir nod oluştur ve self.root değişkenine ata
        self.root = Node(rootVale)

    # Bu objeyi ekrana yazdığımızda çıkacak değer
    def __str__(self):
        # Nodlar ve alt nodları iç içe göster
        return dumps(self.root.show())

    # Tree'ye bir nod ekle
    def add(self, val):
        # Root nod'a bir nod ekle
        self.root.add(val)

    # Tree'nin içindeki değerleri sırala
    def sort(self):
        # Root nod'un içindeki değerleri sırala
        return self.root.sort()

    # Tree içinde arama yap
    def search(self, val):
        # Root nod içinde arama yap
        return isinstance(self.root.search(val), Node)
