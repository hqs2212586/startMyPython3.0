import hashlib
"""
Hash一般翻译为"散列"，或音译为"哈希"。
    将任意长度的输入（也叫预映射）通过散列算法，变换为固定长度的输出，这个输出就是散列值。
    这种转换是一种压缩映射，散列值的空间通常远小于输入的空间。
    不同输入可能会散列为相同输出，因此不可能从散列值来唯一确定输入值。
Hash定义：一种将任意长度的消息压缩到某一固定长度的消息摘要的函数。
    主要用于信息安全领域中加密算法，他把一些不同长度的信息转化成杂乱的128位的编码里,叫做HASH值.也可以说，
    hash就是找到一种数据内容和数据存放地址之间的映射关系
"""
hash("hqs")  # 大量应用于各种加密算法

"""
MD5讯息摘要演算法（英语：MD5 Message-Digest Algorithm），一种被广泛使用的密码杂凑函数，
可以产生出一个128位的散列值（hash value），用于确保信息传输完整一致。MD5的前身有MD2、MD3和MD4。

MD5功能：
    输入任意长度的信息，经过处理，输出为128位的信息（数字指纹）；
    不同的输入得到的不同的结果（唯一性）

MD5算法的特点
    压缩性：任意长度的数据，算出的MD5值的长度都是固定的
    容易计算：从原数据计算出MD5值很容易
    抗修改性：对原数据进行任何改动，修改一个字节生成的MD5值区别也会很大
    强抗碰撞：已知原数据和MD5，想找到一个具有相同MD5值的数据（即伪造数据）是非常困难的。

MD5算法是否可逆？
    MD5不可逆的原因是其是一种散列函数，使用的是hash算法，在计算过程中原文的部分信息是丢失了的。

MD5用途：
    1、防止被篡改
    2、防止直接看到明文
    3、防止抵赖（数字签名）
"""
m = hashlib.md5()
m.update(b'alex')  # 传值'alex'，unicode格式不行，必须使用bytes格式
m.hexdigest()  # 输出md5值，唯一性
len(m.hexdigest())  # 输出32（字节），32*4=128位

print(hashlib.md5('admin'.encode('utf-8')).hexdigest())