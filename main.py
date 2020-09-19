# binaryTree paketinden Tree sınıfını içe aktar
from binaryTree import Tree
# Rastgele ve Zaman hesabı için metodlar içe aktar
from random import randint
from time import time

# 200000 adet [0, 2000000) arasında veri oluştur
data = [randint(0, 2000000) for _ in range(200000)]

# Binary Tree'yi oluştur
tree = Tree(data[0])
for val in data[1:]:
    tree.add(val)

# Şimdiki zamanı al
start_tree = time()
# Binary tree içinde var olmayan bir değer ara
tree.search(-1)
# Şimdiki zamanı al
end_tree = time()
# Geeçn süreyi hesapla
print(end_tree - start_tree)

# Şimdiki zamanı al
start_list = time()
# Liste içinde var olmayan bir değer ara
-1 in data
# Şimdiki zamanı al
end_list = time()
# Geeçn süreyi hesapla
print(end_list - start_list)
