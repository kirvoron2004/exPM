import matplotlib.pyplot as plt
import codecs
from laba13_ import func1, func2, func3

fileObj1 = codecs.open("voina_i_mir.txt", "r", "utf_8_sig")
text1 = fileObj1.read()
fileObj1.close()

fileObj2 = codecs.open("1grams.txt", "r", "utf_8_sig")
text2 = fileObj2.read()
fileObj2.close()

func1(text1)
func2(text2)
func3(text1, text2)
