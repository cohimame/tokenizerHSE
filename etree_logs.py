Python 3.3.5 (v3.3.5:62cf4e77f785, Mar  9 2014, 10:37:12) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import etree
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import etree
ImportError: No module named 'etree'
>>> import elementtree
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import elementtree
ImportError: No module named 'elementtree'
>>> import ElementTree
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import ElementTree
ImportError: No module named 'ElementTree'
>>> import xml.etree
>>> dir(xml.etree)
['__builtins__', '__cached__', '__doc__', '__file__', '__initializing__', '__loader__', '__name__', '__package__', '__path__']
>>> from xml.etree import ElementTree
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "C:/Users/student/Desktop/python-io/cw13/etree_example.py", line 4, in <module>
    tree = ElementTree.parse(infile)
  File "C:\Python33\lib\xml\etree\ElementTree.py", line 1242, in parse
    tree.parse(source, parser)
  File "C:\Python33\lib\xml\etree\ElementTree.py", line 1730, in parse
    self._root = parser._parse(source)
  File "C:\Python33\lib\encodings\cp1251.py", line 23, in decode
    return codecs.charmap_decode(input,self.errors,decoding_table)[0]
UnicodeDecodeError: 'charmap' codec can't decode byte 0x98 in position 2064: character maps to <undefined>
>>> ================================ RESTART ================================
>>> 
>>> tree
<xml.etree.ElementTree.ElementTree object at 0x02A9A210>
>>> tree[0]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tree[0]
TypeError: 'ElementTree' object does not support indexing
>>> tree.getroot()
<Element 'reviews' at 0x03493B10>
>>> x = tree.getroot()
>>> x[0]
<Element 'review' at 0x034AC7B0>
>>> x[1]
<Element 'review' at 0x034B22D0>
>>> x[2]
<Element 'review' at 0x034B2B70>
>>> len(x)
201
>>> x[-1]
<Element 'review' at 0x0394DD80>
>>> ================================ RESTART ================================
>>> 
>>> tree
<xml.etree.ElementTree.ElementTree object at 0x02D13210>
>>> tree.findall('review')
[<Element 'review' at 0x033AC7B0>, <Element 'review' at 0x033B22D0>, <Element 'review' at 0x033B2B70>, <Element 'review' at 0x033B7690>, <Element 'review' at 0x033B7F90>, <Element 'review' at 0x033BF8D0>, <Element 'review' at 0x033DB0F0>, <Element 'review' at 0x033DBD20>, <Element 'review' at 0x033E15A0>, <Element 'review' at 0x033E1DB0>, <Element 'review' at 0x033E6AE0>, <Element 'review' at 0x033ED4E0>, <Element 'review' at 0x033EDF30>, <Element 'review' at 0x033F3A50>, <Element 'review' at 0x033F92A0>, <Element 'review' at 0x033F9F00>, <Element 'review' at 0x033FFA80>, <Element 'review' at 0x03406390>, <Element 'review' at 0x03406ED0>, <Element 'review' at 0x0340B990>, <Element 'review' at 0x034116F0>, <Element 'review' at 0x0347A2D0>, <Element 'review' at 0x0347AB10>, <Element 'review' at 0x0347F630>, <Element 'review' at 0x03487120>, <Element 'review' at 0x03487870>, <Element 'review' at 0x0348C540>, <Element 'review' at 0x0348CC90>, <Element 'review' at 0x03490840>, <Element 'review' at 0x03497330>, <Element 'review' at 0x03497E70>, <Element 'review' at 0x0349C900>, <Element 'review' at 0x034A21E0>, <Element 'review' at 0x034A2C30>, <Element 'review' at 0x034A8A80>, <Element 'review' at 0x034B03F0>, <Element 'review' at 0x034B0BA0>, <Element 'review' at 0x034B4750>, <Element 'review' at 0x034B4F90>, <Element 'review' at 0x0350FB40>, <Element 'review' at 0x035156F0>, <Element 'review' at 0x0351C0F0>, <Element 'review' at 0x0351C9C0>, <Element 'review' at 0x03521420>, <Element 'review' at 0x03521E10>, <Element 'review' at 0x03527690>, <Element 'review' at 0x0352E2D0>, <Element 'review' at 0x0352EBA0>, <Element 'review' at 0x03532870>, <Element 'review' at 0x03539390>, <Element 'review' at 0x03539E10>, <Element 'review' at 0x035418A0>, <Element 'review' at 0x03547480>, <Element 'review' at 0x03547F90>, <Element 'review' at 0x03561A80>, <Element 'review' at 0x03567330>, <Element 'review' at 0x03567C30>, <Element 'review' at 0x0356B540>, <Element 'review' at 0x0356BE70>, <Element 'review' at 0x03571C00>, <Element 'review' at 0x03576570>, <Element 'review' at 0x03576F30>, <Element 'review' at 0x0357E9F0>, <Element 'review' at 0x03585300>, <Element 'review' at 0x03585B70>, <Element 'review' at 0x03589420>, <Element 'review' at 0x03589C00>, <Element 'review' at 0x0358F3F0>, <Element 'review' at 0x0358FDE0>, <Element 'review' at 0x035935A0>, <Element 'review' at 0x03593D50>, <Element 'review' at 0x0359A570>, <Element 'review' at 0x0359AEA0>, <Element 'review' at 0x03605780>, <Element 'review' at 0x03605FC0>, <Element 'review' at 0x0360B9C0>, <Element 'review' at 0x03610450>, <Element 'review' at 0x03610ED0>, <Element 'review' at 0x03616780>, <Element 'review' at 0x0361D060>, <Element 'review' at 0x0361D720>, <Element 'review' at 0x03622210>, <Element 'review' at 0x03622B40>, <Element 'review' at 0x03626660>, <Element 'review' at 0x0362D030>, <Element 'review' at 0x0362DA50>, <Element 'review' at 0x03633720>, <Element 'review' at 0x036390C0>, <Element 'review' at 0x03639C60>, <Element 'review' at 0x035BF5D0>, <Element 'review' at 0x035C50C0>, <Element 'review' at 0x035C59C0>, <Element 'review' at 0x035CB360>, <Element 'review' at 0x035CBF90>, <Element 'review' at 0x035D1A50>, <Element 'review' at 0x035D7240>, <Element 'review' at 0x035D7A80>, <Element 'review' at 0x035DC390>, <Element 'review' at 0x035DCD50>, <Element 'review' at 0x035E1B10>, <Element 'review' at 0x035E8420>, <Element 'review' at 0x035E8F90>, <Element 'review' at 0x035ED870>, <Element 'review' at 0x035F4270>, <Element 'review' at 0x035F4BD0>, <Element 'review' at 0x035F95D0>, <Element 'review' at 0x0366A150>, <Element 'review' at 0x0366ABD0>, <Element 'review' at 0x03670510>, <Element 'review' at 0x03670DE0>, <Element 'review' at 0x03676A20>, <Element 'review' at 0x0367C480>, <Element 'review' at 0x0367CFC0>, <Element 'review' at 0x03682870>, <Element 'review' at 0x03688450>, <Element 'review' at 0x03688DB0>, <Element 'review' at 0x0368D930>, <Element 'review' at 0x036944E0>, <Element 'review' at 0x03694E10>, <Element 'review' at 0x0369A7E0>, <Element 'review' at 0x036A1090>, <Element 'review' at 0x036A1E10>, <Element 'review' at 0x03708930>, <Element 'review' at 0x0370F4B0>, <Element 'review' at 0x0370FD80>, <Element 'review' at 0x03713AE0>, <Element 'review' at 0x0371B480>, <Element 'review' at 0x0371BD50>, <Element 'review' at 0x037208D0>, <Element 'review' at 0x037263C0>, <Element 'review' at 0x03726E70>, <Element 'review' at 0x0372B810>, <Element 'review' at 0x03731150>, <Element 'review' at 0x037319F0>, <Element 'review' at 0x03737390>, <Element 'review' at 0x03737DB0>, <Element 'review' at 0x0373C4B0>, <Element 'review' at 0x0373CE10>, <Element 'review' at 0x03743870>, <Element 'review' at 0x037565A0>, <Element 'review' at 0x03756F00>, <Element 'review' at 0x0375C930>, <Element 'review' at 0x037623C0>, <Element 'review' at 0x03762C90>, <Element 'review' at 0x03767570>, <Element 'review' at 0x0376D090>, <Element 'review' at 0x0376DBA0>, <Element 'review' at 0x037745D0>, <Element 'review' at 0x0377C150>, <Element 'review' at 0x0377CCF0>, <Element 'review' at 0x03782780>, <Element 'review' at 0x03782F60>, <Element 'review' at 0x03787B10>, <Element 'review' at 0x0378D660>, <Element 'review' at 0x0378DF00>, <Element 'review' at 0x037AA9C0>, <Element 'review' at 0x037B0210>, <Element 'review' at 0x037B0A20>, <Element 'review' at 0x037B5270>, <Element 'review' at 0x037B5CC0>, <Element 'review' at 0x037BA4B0>, <Element 'review' at 0x037BAC00>, <Element 'review' at 0x037C0540>, <Element 'review' at 0x037C0DB0>, <Element 'review' at 0x037C5930>, <Element 'review' at 0x037CB330>, <Element 'review' at 0x037CBBD0>, <Element 'review' at 0x037D0540>, <Element 'review' at 0x037D0E40>, <Element 'review' at 0x037D65D0>, <Element 'review' at 0x037D6CC0>, <Element 'review' at 0x037D9510>, <Element 'review' at 0x037D9E40>, <Element 'review' at 0x037DF7E0>, <Element 'review' at 0x038100F0>, <Element 'review' at 0x038107E0>, <Element 'review' at 0x03814060>, <Element 'review' at 0x03814A50>, <Element 'review' at 0x0381B480>, <Element 'review' at 0x0381BC90>, <Element 'review' at 0x03821510>, <Element 'review' at 0x03821E40>, <Element 'review' at 0x03827690>, <Element 'review' at 0x03827EA0>, <Element 'review' at 0x0382C660>, <Element 'review' at 0x0382CF60>, <Element 'review' at 0x03831870>, <Element 'review' at 0x03836180>, <Element 'review' at 0x03836960>, <Element 'review' at 0x0383D240>, <Element 'review' at 0x0383DA50>, <Element 'review' at 0x03842480>, <Element 'review' at 0x03842DE0>, <Element 'review' at 0x038488A0>, <Element 'review' at 0x0385D2A0>, <Element 'review' at 0x0385DE70>, <Element 'review' at 0x038626C0>, <Element 'review' at 0x03862DB0>, <Element 'review' at 0x03868690>, <Element 'review' at 0x0386E1E0>, <Element 'review' at 0x0386ED80>]
>>> tree.findall('reviews')
[]
>>> tree.findall('review')
[<Element 'review' at 0x033AC7B0>, <Element 'review' at 0x033B22D0>, <Element 'review' at 0x033B2B70>, <Element 'review' at 0x033B7690>, <Element 'review' at 0x033B7F90>, <Element 'review' at 0x033BF8D0>, <Element 'review' at 0x033DB0F0>, <Element 'review' at 0x033DBD20>, <Element 'review' at 0x033E15A0>, <Element 'review' at 0x033E1DB0>, <Element 'review' at 0x033E6AE0>, <Element 'review' at 0x033ED4E0>, <Element 'review' at 0x033EDF30>, <Element 'review' at 0x033F3A50>, <Element 'review' at 0x033F92A0>, <Element 'review' at 0x033F9F00>, <Element 'review' at 0x033FFA80>, <Element 'review' at 0x03406390>, <Element 'review' at 0x03406ED0>, <Element 'review' at 0x0340B990>, <Element 'review' at 0x034116F0>, <Element 'review' at 0x0347A2D0>, <Element 'review' at 0x0347AB10>, <Element 'review' at 0x0347F630>, <Element 'review' at 0x03487120>, <Element 'review' at 0x03487870>, <Element 'review' at 0x0348C540>, <Element 'review' at 0x0348CC90>, <Element 'review' at 0x03490840>, <Element 'review' at 0x03497330>, <Element 'review' at 0x03497E70>, <Element 'review' at 0x0349C900>, <Element 'review' at 0x034A21E0>, <Element 'review' at 0x034A2C30>, <Element 'review' at 0x034A8A80>, <Element 'review' at 0x034B03F0>, <Element 'review' at 0x034B0BA0>, <Element 'review' at 0x034B4750>, <Element 'review' at 0x034B4F90>, <Element 'review' at 0x0350FB40>, <Element 'review' at 0x035156F0>, <Element 'review' at 0x0351C0F0>, <Element 'review' at 0x0351C9C0>, <Element 'review' at 0x03521420>, <Element 'review' at 0x03521E10>, <Element 'review' at 0x03527690>, <Element 'review' at 0x0352E2D0>, <Element 'review' at 0x0352EBA0>, <Element 'review' at 0x03532870>, <Element 'review' at 0x03539390>, <Element 'review' at 0x03539E10>, <Element 'review' at 0x035418A0>, <Element 'review' at 0x03547480>, <Element 'review' at 0x03547F90>, <Element 'review' at 0x03561A80>, <Element 'review' at 0x03567330>, <Element 'review' at 0x03567C30>, <Element 'review' at 0x0356B540>, <Element 'review' at 0x0356BE70>, <Element 'review' at 0x03571C00>, <Element 'review' at 0x03576570>, <Element 'review' at 0x03576F30>, <Element 'review' at 0x0357E9F0>, <Element 'review' at 0x03585300>, <Element 'review' at 0x03585B70>, <Element 'review' at 0x03589420>, <Element 'review' at 0x03589C00>, <Element 'review' at 0x0358F3F0>, <Element 'review' at 0x0358FDE0>, <Element 'review' at 0x035935A0>, <Element 'review' at 0x03593D50>, <Element 'review' at 0x0359A570>, <Element 'review' at 0x0359AEA0>, <Element 'review' at 0x03605780>, <Element 'review' at 0x03605FC0>, <Element 'review' at 0x0360B9C0>, <Element 'review' at 0x03610450>, <Element 'review' at 0x03610ED0>, <Element 'review' at 0x03616780>, <Element 'review' at 0x0361D060>, <Element 'review' at 0x0361D720>, <Element 'review' at 0x03622210>, <Element 'review' at 0x03622B40>, <Element 'review' at 0x03626660>, <Element 'review' at 0x0362D030>, <Element 'review' at 0x0362DA50>, <Element 'review' at 0x03633720>, <Element 'review' at 0x036390C0>, <Element 'review' at 0x03639C60>, <Element 'review' at 0x035BF5D0>, <Element 'review' at 0x035C50C0>, <Element 'review' at 0x035C59C0>, <Element 'review' at 0x035CB360>, <Element 'review' at 0x035CBF90>, <Element 'review' at 0x035D1A50>, <Element 'review' at 0x035D7240>, <Element 'review' at 0x035D7A80>, <Element 'review' at 0x035DC390>, <Element 'review' at 0x035DCD50>, <Element 'review' at 0x035E1B10>, <Element 'review' at 0x035E8420>, <Element 'review' at 0x035E8F90>, <Element 'review' at 0x035ED870>, <Element 'review' at 0x035F4270>, <Element 'review' at 0x035F4BD0>, <Element 'review' at 0x035F95D0>, <Element 'review' at 0x0366A150>, <Element 'review' at 0x0366ABD0>, <Element 'review' at 0x03670510>, <Element 'review' at 0x03670DE0>, <Element 'review' at 0x03676A20>, <Element 'review' at 0x0367C480>, <Element 'review' at 0x0367CFC0>, <Element 'review' at 0x03682870>, <Element 'review' at 0x03688450>, <Element 'review' at 0x03688DB0>, <Element 'review' at 0x0368D930>, <Element 'review' at 0x036944E0>, <Element 'review' at 0x03694E10>, <Element 'review' at 0x0369A7E0>, <Element 'review' at 0x036A1090>, <Element 'review' at 0x036A1E10>, <Element 'review' at 0x03708930>, <Element 'review' at 0x0370F4B0>, <Element 'review' at 0x0370FD80>, <Element 'review' at 0x03713AE0>, <Element 'review' at 0x0371B480>, <Element 'review' at 0x0371BD50>, <Element 'review' at 0x037208D0>, <Element 'review' at 0x037263C0>, <Element 'review' at 0x03726E70>, <Element 'review' at 0x0372B810>, <Element 'review' at 0x03731150>, <Element 'review' at 0x037319F0>, <Element 'review' at 0x03737390>, <Element 'review' at 0x03737DB0>, <Element 'review' at 0x0373C4B0>, <Element 'review' at 0x0373CE10>, <Element 'review' at 0x03743870>, <Element 'review' at 0x037565A0>, <Element 'review' at 0x03756F00>, <Element 'review' at 0x0375C930>, <Element 'review' at 0x037623C0>, <Element 'review' at 0x03762C90>, <Element 'review' at 0x03767570>, <Element 'review' at 0x0376D090>, <Element 'review' at 0x0376DBA0>, <Element 'review' at 0x037745D0>, <Element 'review' at 0x0377C150>, <Element 'review' at 0x0377CCF0>, <Element 'review' at 0x03782780>, <Element 'review' at 0x03782F60>, <Element 'review' at 0x03787B10>, <Element 'review' at 0x0378D660>, <Element 'review' at 0x0378DF00>, <Element 'review' at 0x037AA9C0>, <Element 'review' at 0x037B0210>, <Element 'review' at 0x037B0A20>, <Element 'review' at 0x037B5270>, <Element 'review' at 0x037B5CC0>, <Element 'review' at 0x037BA4B0>, <Element 'review' at 0x037BAC00>, <Element 'review' at 0x037C0540>, <Element 'review' at 0x037C0DB0>, <Element 'review' at 0x037C5930>, <Element 'review' at 0x037CB330>, <Element 'review' at 0x037CBBD0>, <Element 'review' at 0x037D0540>, <Element 'review' at 0x037D0E40>, <Element 'review' at 0x037D65D0>, <Element 'review' at 0x037D6CC0>, <Element 'review' at 0x037D9510>, <Element 'review' at 0x037D9E40>, <Element 'review' at 0x037DF7E0>, <Element 'review' at 0x038100F0>, <Element 'review' at 0x038107E0>, <Element 'review' at 0x03814060>, <Element 'review' at 0x03814A50>, <Element 'review' at 0x0381B480>, <Element 'review' at 0x0381BC90>, <Element 'review' at 0x03821510>, <Element 'review' at 0x03821E40>, <Element 'review' at 0x03827690>, <Element 'review' at 0x03827EA0>, <Element 'review' at 0x0382C660>, <Element 'review' at 0x0382CF60>, <Element 'review' at 0x03831870>, <Element 'review' at 0x03836180>, <Element 'review' at 0x03836960>, <Element 'review' at 0x0383D240>, <Element 'review' at 0x0383DA50>, <Element 'review' at 0x03842480>, <Element 'review' at 0x03842DE0>, <Element 'review' at 0x038488A0>, <Element 'review' at 0x0385D2A0>, <Element 'review' at 0x0385DE70>, <Element 'review' at 0x038626C0>, <Element 'review' at 0x03862DB0>, <Element 'review' at 0x03868690>, <Element 'review' at 0x0386E1E0>, <Element 'review' at 0x0386ED80>]
>>> x = tree.findall('review')[0]
>>> x
<Element 'review' at 0x033AC7B0>
>>> x.findall('*')
[<Element 'meta' at 0x033AC8A0>, <Element 'scores' at 0x033ACA50>, <Element 'text' at 0x033ACB70>, <Element 'aspects' at 0x033ACBD0>, <Element 'categories' at 0x033B2180>]
>>> tree
<xml.etree.ElementTree.ElementTree object at 0x02D13210>
>>> tree.findall('//text')

Warning (from warnings module):
  File "C:/Users/student/Desktop/python-io/cw13/etree_example.py", line 1
    from xml.etree import ElementTree
FutureWarning: This search is broken in 1.3 and earlier, and will be fixed in a future version.  If you rely on the current behaviour, change it to './/text'
[<Element 'text' at 0x033ACB70>, <Element 'text' at 0x033B25D0>, <Element 'text' at 0x033B2E70>, <Element 'text' at 0x033B7990>, <Element 'text' at 0x033BF300>, <Element 'text' at 0x033BFC30>, <Element 'text' at 0x033DB3F0>, <Element 'text' at 0x033E1060>, <Element 'text' at 0x033E18A0>, <Element 'text' at 0x033E60F0>, <Element 'text' at 0x033E6DE0>, <Element 'text' at 0x033ED7E0>, <Element 'text' at 0x033F3270>, <Element 'text' at 0x033F3D50>, <Element 'text' at 0x033F95A0>, <Element 'text' at 0x033FF240>, <Element 'text' at 0x033FFD80>, <Element 'text' at 0x03406690>, <Element 'text' at 0x0340B240>, <Element 'text' at 0x0340BC90>, <Element 'text' at 0x034119F0>, <Element 'text' at 0x0347A600>, <Element 'text' at 0x0347AE10>, <Element 'text' at 0x0347F930>, <Element 'text' at 0x03487420>, <Element 'text' at 0x03487B40>, <Element 'text' at 0x0348C840>, <Element 'text' at 0x0348CF90>, <Element 'text' at 0x03490B40>, <Element 'text' at 0x03497630>, <Element 'text' at 0x0349C1B0>, <Element 'text' at 0x0349CC00>, <Element 'text' at 0x034A24E0>, <Element 'text' at 0x034A2F30>, <Element 'text' at 0x034A8DB0>, <Element 'text' at 0x034B06F0>, <Element 'text' at 0x034B0EA0>, <Element 'text' at 0x034B4A50>, <Element 'text' at 0x0350F2D0>, <Element 'text' at 0x0350FE70>, <Element 'text' at 0x035159F0>, <Element 'text' at 0x0351C3F0>, <Element 'text' at 0x0351CCC0>, <Element 'text' at 0x03521720>, <Element 'text' at 0x03527150>, <Element 'text' at 0x03527990>, <Element 'text' at 0x0352E5D0>, <Element 'text' at 0x0352EEA0>, <Element 'text' at 0x03532B70>, <Element 'text' at 0x03539690>, <Element 'text' at 0x03541150>, <Element 'text' at 0x03541BA0>, <Element 'text' at 0x03547780>, <Element 'text' at 0x03561300>, <Element 'text' at 0x03561DB0>, <Element 'text' at 0x03567630>, <Element 'text' at 0x03567F30>, <Element 'text' at 0x0356B870>, <Element 'text' at 0x035711E0>, <Element 'text' at 0x03571F00>, <Element 'text' at 0x035768A0>, <Element 'text' at 0x0357E270>, <Element 'text' at 0x0357ED20>, <Element 'text' at 0x03585600>, <Element 'text' at 0x03585E70>, <Element 'text' at 0x03589750>, <Element 'text' at 0x03589F00>, <Element 'text' at 0x0358F6F0>, <Element 'text' at 0x03593120>, <Element 'text' at 0x035938A0>, <Element 'text' at 0x0359A090>, <Element 'text' at 0x0359A870>, <Element 'text' at 0x036051E0>, <Element 'text' at 0x03605A80>, <Element 'text' at 0x0360B300>, <Element 'text' at 0x0360BCC0>, <Element 'text' at 0x03610750>, <Element 'text' at 0x03616210>, <Element 'text' at 0x03616A80>, <Element 'text' at 0x0361D360>, <Element 'text' at 0x0361DA50>, <Element 'text' at 0x03622510>, <Element 'text' at 0x03622E40>, <Element 'text' at 0x03626960>, <Element 'text' at 0x0362D330>, <Element 'text' at 0x0362DD50>, <Element 'text' at 0x03633A20>, <Element 'text' at 0x036393C0>, <Element 'text' at 0x03639F60>, <Element 'text' at 0x035BF8D0>, <Element 'text' at 0x035C53C0>, <Element 'text' at 0x035C5CC0>, <Element 'text' at 0x035CB660>, <Element 'text' at 0x035D12D0>, <Element 'text' at 0x035D1D50>, <Element 'text' at 0x035D7540>, <Element 'text' at 0x035D7D80>, <Element 'text' at 0x035DC690>, <Element 'text' at 0x035E1090>, <Element 'text' at 0x035E1E10>, <Element 'text' at 0x035E8720>, <Element 'text' at 0x035ED330>, <Element 'text' at 0x035EDBA0>, <Element 'text' at 0x035F45A0>, <Element 'text' at 0x035F4ED0>, <Element 'text' at 0x035F98D0>, <Element 'text' at 0x0366A450>, <Element 'text' at 0x0366AED0>, <Element 'text' at 0x03670840>, <Element 'text' at 0x03676120>, <Element 'text' at 0x03676D20>, <Element 'text' at 0x0367C780>, <Element 'text' at 0x03682300>, <Element 'text' at 0x03682B70>, <Element 'text' at 0x03688750>, <Element 'text' at 0x0368D0F0>, <Element 'text' at 0x0368DC30>, <Element 'text' at 0x036947E0>, <Element 'text' at 0x0369A150>, <Element 'text' at 0x0369AAE0>, <Element 'text' at 0x036A1390>, <Element 'text' at 0x03708150>, <Element 'text' at 0x03708C30>, <Element 'text' at 0x0370F7B0>, <Element 'text' at 0x037130C0>, <Element 'text' at 0x03713DE0>, <Element 'text' at 0x0371B780>, <Element 'text' at 0x03720090>, <Element 'text' at 0x03720BD0>, <Element 'text' at 0x037266F0>, <Element 'text' at 0x0372B1B0>, <Element 'text' at 0x0372BB10>, <Element 'text' at 0x03731450>, <Element 'text' at 0x03731CF0>, <Element 'text' at 0x03737690>, <Element 'text' at 0x0373C0F0>, <Element 'text' at 0x0373C7B0>, <Element 'text' at 0x03743150>, <Element 'text' at 0x03743B70>, <Element 'text' at 0x037568A0>, <Element 'text' at 0x0375C240>, <Element 'text' at 0x0375CC30>, <Element 'text' at 0x037626C0>, <Element 'text' at 0x03762F90>, <Element 'text' at 0x03767870>, <Element 'text' at 0x0376D390>, <Element 'text' at 0x0376DEA0>, <Element 'text' at 0x03774900>, <Element 'text' at 0x0377C450>, <Element 'text' at 0x03782030>, <Element 'text' at 0x03782A80>, <Element 'text' at 0x037872D0>, <Element 'text' at 0x03787E10>, <Element 'text' at 0x0378D960>, <Element 'text' at 0x037AA240>, <Element 'text' at 0x037AACC0>, <Element 'text' at 0x037B0510>, <Element 'text' at 0x037B0D20>, <Element 'text' at 0x037B5570>, <Element 'text' at 0x037B5FC0>, <Element 'text' at 0x037BA7B0>, <Element 'text' at 0x037BAF00>, <Element 'text' at 0x037C0840>, <Element 'text' at 0x037C50F0>, <Element 'text' at 0x037C5C30>, <Element 'text' at 0x037CB630>, <Element 'text' at 0x037CBED0>, <Element 'text' at 0x037D0870>, <Element 'text' at 0x037D6180>, <Element 'text' at 0x037D68D0>, <Element 'text' at 0x037D9030>, <Element 'text' at 0x037D9810>, <Element 'text' at 0x037DF180>, <Element 'text' at 0x037DFAE0>, <Element 'text' at 0x038103F0>, <Element 'text' at 0x03810AE0>, <Element 'text' at 0x03814360>, <Element 'text' at 0x03814D50>, <Element 'text' at 0x0381B780>, <Element 'text' at 0x0381BF90>, <Element 'text' at 0x03821810>, <Element 'text' at 0x03827180>, <Element 'text' at 0x03827990>, <Element 'text' at 0x0382C1E0>, <Element 'text' at 0x0382C960>, <Element 'text' at 0x038312A0>, <Element 'text' at 0x03831B70>, <Element 'text' at 0x03836480>, <Element 'text' at 0x03836C60>, <Element 'text' at 0x0383D540>, <Element 'text' at 0x0383DD50>, <Element 'text' at 0x03842780>, <Element 'text' at 0x03848120>, <Element 'text' at 0x03848BA0>, <Element 'text' at 0x0385D5A0>, <Element 'text' at 0x038621B0>, <Element 'text' at 0x038629C0>, <Element 'text' at 0x038680F0>, <Element 'text' at 0x03868990>, <Element 'text' at 0x0386E510>, <Element 'text' at 0x038730C0>]
>>> tree.findall('text')
[]
>>> tree.findall('*//text')
[<Element 'text' at 0x033ACB70>, <Element 'text' at 0x033B25D0>, <Element 'text' at 0x033B2E70>, <Element 'text' at 0x033B7990>, <Element 'text' at 0x033BF300>, <Element 'text' at 0x033BFC30>, <Element 'text' at 0x033DB3F0>, <Element 'text' at 0x033E1060>, <Element 'text' at 0x033E18A0>, <Element 'text' at 0x033E60F0>, <Element 'text' at 0x033E6DE0>, <Element 'text' at 0x033ED7E0>, <Element 'text' at 0x033F3270>, <Element 'text' at 0x033F3D50>, <Element 'text' at 0x033F95A0>, <Element 'text' at 0x033FF240>, <Element 'text' at 0x033FFD80>, <Element 'text' at 0x03406690>, <Element 'text' at 0x0340B240>, <Element 'text' at 0x0340BC90>, <Element 'text' at 0x034119F0>, <Element 'text' at 0x0347A600>, <Element 'text' at 0x0347AE10>, <Element 'text' at 0x0347F930>, <Element 'text' at 0x03487420>, <Element 'text' at 0x03487B40>, <Element 'text' at 0x0348C840>, <Element 'text' at 0x0348CF90>, <Element 'text' at 0x03490B40>, <Element 'text' at 0x03497630>, <Element 'text' at 0x0349C1B0>, <Element 'text' at 0x0349CC00>, <Element 'text' at 0x034A24E0>, <Element 'text' at 0x034A2F30>, <Element 'text' at 0x034A8DB0>, <Element 'text' at 0x034B06F0>, <Element 'text' at 0x034B0EA0>, <Element 'text' at 0x034B4A50>, <Element 'text' at 0x0350F2D0>, <Element 'text' at 0x0350FE70>, <Element 'text' at 0x035159F0>, <Element 'text' at 0x0351C3F0>, <Element 'text' at 0x0351CCC0>, <Element 'text' at 0x03521720>, <Element 'text' at 0x03527150>, <Element 'text' at 0x03527990>, <Element 'text' at 0x0352E5D0>, <Element 'text' at 0x0352EEA0>, <Element 'text' at 0x03532B70>, <Element 'text' at 0x03539690>, <Element 'text' at 0x03541150>, <Element 'text' at 0x03541BA0>, <Element 'text' at 0x03547780>, <Element 'text' at 0x03561300>, <Element 'text' at 0x03561DB0>, <Element 'text' at 0x03567630>, <Element 'text' at 0x03567F30>, <Element 'text' at 0x0356B870>, <Element 'text' at 0x035711E0>, <Element 'text' at 0x03571F00>, <Element 'text' at 0x035768A0>, <Element 'text' at 0x0357E270>, <Element 'text' at 0x0357ED20>, <Element 'text' at 0x03585600>, <Element 'text' at 0x03585E70>, <Element 'text' at 0x03589750>, <Element 'text' at 0x03589F00>, <Element 'text' at 0x0358F6F0>, <Element 'text' at 0x03593120>, <Element 'text' at 0x035938A0>, <Element 'text' at 0x0359A090>, <Element 'text' at 0x0359A870>, <Element 'text' at 0x036051E0>, <Element 'text' at 0x03605A80>, <Element 'text' at 0x0360B300>, <Element 'text' at 0x0360BCC0>, <Element 'text' at 0x03610750>, <Element 'text' at 0x03616210>, <Element 'text' at 0x03616A80>, <Element 'text' at 0x0361D360>, <Element 'text' at 0x0361DA50>, <Element 'text' at 0x03622510>, <Element 'text' at 0x03622E40>, <Element 'text' at 0x03626960>, <Element 'text' at 0x0362D330>, <Element 'text' at 0x0362DD50>, <Element 'text' at 0x03633A20>, <Element 'text' at 0x036393C0>, <Element 'text' at 0x03639F60>, <Element 'text' at 0x035BF8D0>, <Element 'text' at 0x035C53C0>, <Element 'text' at 0x035C5CC0>, <Element 'text' at 0x035CB660>, <Element 'text' at 0x035D12D0>, <Element 'text' at 0x035D1D50>, <Element 'text' at 0x035D7540>, <Element 'text' at 0x035D7D80>, <Element 'text' at 0x035DC690>, <Element 'text' at 0x035E1090>, <Element 'text' at 0x035E1E10>, <Element 'text' at 0x035E8720>, <Element 'text' at 0x035ED330>, <Element 'text' at 0x035EDBA0>, <Element 'text' at 0x035F45A0>, <Element 'text' at 0x035F4ED0>, <Element 'text' at 0x035F98D0>, <Element 'text' at 0x0366A450>, <Element 'text' at 0x0366AED0>, <Element 'text' at 0x03670840>, <Element 'text' at 0x03676120>, <Element 'text' at 0x03676D20>, <Element 'text' at 0x0367C780>, <Element 'text' at 0x03682300>, <Element 'text' at 0x03682B70>, <Element 'text' at 0x03688750>, <Element 'text' at 0x0368D0F0>, <Element 'text' at 0x0368DC30>, <Element 'text' at 0x036947E0>, <Element 'text' at 0x0369A150>, <Element 'text' at 0x0369AAE0>, <Element 'text' at 0x036A1390>, <Element 'text' at 0x03708150>, <Element 'text' at 0x03708C30>, <Element 'text' at 0x0370F7B0>, <Element 'text' at 0x037130C0>, <Element 'text' at 0x03713DE0>, <Element 'text' at 0x0371B780>, <Element 'text' at 0x03720090>, <Element 'text' at 0x03720BD0>, <Element 'text' at 0x037266F0>, <Element 'text' at 0x0372B1B0>, <Element 'text' at 0x0372BB10>, <Element 'text' at 0x03731450>, <Element 'text' at 0x03731CF0>, <Element 'text' at 0x03737690>, <Element 'text' at 0x0373C0F0>, <Element 'text' at 0x0373C7B0>, <Element 'text' at 0x03743150>, <Element 'text' at 0x03743B70>, <Element 'text' at 0x037568A0>, <Element 'text' at 0x0375C240>, <Element 'text' at 0x0375CC30>, <Element 'text' at 0x037626C0>, <Element 'text' at 0x03762F90>, <Element 'text' at 0x03767870>, <Element 'text' at 0x0376D390>, <Element 'text' at 0x0376DEA0>, <Element 'text' at 0x03774900>, <Element 'text' at 0x0377C450>, <Element 'text' at 0x03782030>, <Element 'text' at 0x03782A80>, <Element 'text' at 0x037872D0>, <Element 'text' at 0x03787E10>, <Element 'text' at 0x0378D960>, <Element 'text' at 0x037AA240>, <Element 'text' at 0x037AACC0>, <Element 'text' at 0x037B0510>, <Element 'text' at 0x037B0D20>, <Element 'text' at 0x037B5570>, <Element 'text' at 0x037B5FC0>, <Element 'text' at 0x037BA7B0>, <Element 'text' at 0x037BAF00>, <Element 'text' at 0x037C0840>, <Element 'text' at 0x037C50F0>, <Element 'text' at 0x037C5C30>, <Element 'text' at 0x037CB630>, <Element 'text' at 0x037CBED0>, <Element 'text' at 0x037D0870>, <Element 'text' at 0x037D6180>, <Element 'text' at 0x037D68D0>, <Element 'text' at 0x037D9030>, <Element 'text' at 0x037D9810>, <Element 'text' at 0x037DF180>, <Element 'text' at 0x037DFAE0>, <Element 'text' at 0x038103F0>, <Element 'text' at 0x03810AE0>, <Element 'text' at 0x03814360>, <Element 'text' at 0x03814D50>, <Element 'text' at 0x0381B780>, <Element 'text' at 0x0381BF90>, <Element 'text' at 0x03821810>, <Element 'text' at 0x03827180>, <Element 'text' at 0x03827990>, <Element 'text' at 0x0382C1E0>, <Element 'text' at 0x0382C960>, <Element 'text' at 0x038312A0>, <Element 'text' at 0x03831B70>, <Element 'text' at 0x03836480>, <Element 'text' at 0x03836C60>, <Element 'text' at 0x0383D540>, <Element 'text' at 0x0383DD50>, <Element 'text' at 0x03842780>, <Element 'text' at 0x03848120>, <Element 'text' at 0x03848BA0>, <Element 'text' at 0x0385D5A0>, <Element 'text' at 0x038621B0>, <Element 'text' at 0x038629C0>, <Element 'text' at 0x038680F0>, <Element 'text' at 0x03868990>, <Element 'text' at 0x0386E510>, <Element 'text' at 0x038730C0>]
>>> x = tree.findall('*//text')[0]
>>> x
<Element 'text' at 0x033ACB70>
>>> dict(x)
{}
>>> x = tree.findall('*//meta')[0]
>>> dict(x)
{}
>>> x = tree.findall('*//aspect')[100]
>>> dict(x)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    dict(x)
TypeError: element indices must be integers
>>> x.keys()
['type', 'category', 'from', 'sentiment', 'to', 'mark', 'term']
>>> x['type']
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    x['type']
TypeError: element indices must be integers
>>> x = tree.findall('*//aspect')[100]
>>> x['type']
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    x['type']
TypeError: element indices must be integers
>>> x.keys()
['type', 'category', 'from', 'sentiment', 'to', 'mark', 'term']
>>> x.get('cetegory')
>>> x.get('type')
'implicit'
>>> x.get('category')
'Service'
>>> tree.findall('.//*[@category=Service]')
Traceback (most recent call last):
  File "C:\Python33\lib\xml\etree\ElementPath.py", line 254, in iterfind
    selector = _cache[cache_key]
KeyError: ('.//*[@category=Service]', None)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    tree.findall('.//*[@category=Service]')
  File "C:\Python33\lib\xml\etree\ElementTree.py", line 757, in findall
    return self._root.findall(path, namespaces)
  File "C:\Python33\lib\xml\etree\ElementPath.py", line 295, in findall
    return list(iterfind(elem, path, namespaces))
  File "C:\Python33\lib\xml\etree\ElementPath.py", line 265, in iterfind
    selector.append(ops[token[0]](next, token))
  File "C:\Python33\lib\xml\etree\ElementPath.py", line 224, in prepare_predicate
    raise SyntaxError("invalid predicate")
  File "<string>", line None
SyntaxError: invalid predicate
>>> tree.findall('.//*[@category="Service"]')
[<Element 'aspect' at 0x033ACC90>, <Element 'aspect' at 0x033ACCC0>, <Element 'aspect' at 0x033ACCF0>, <Element 'aspect' at 0x033ACD20>, <Element 'aspect' at 0x033ACDE0>, <Element 'aspect' at 0x033ACE70>, <Element 'aspect' at 0x033ACEA0>, <Element 'aspect' at 0x033ACED0>, <Element 'aspect' at 0x033B20F0>, <Element 'aspect' at 0x033B26F0>, <Element 'aspect' at 0x033B2720>, <Element 'aspect' at 0x033B28D0>, <Element 'aspect' at 0x033B2900>, <Element 'aspect' at 0x033B2F60>, <Element 'aspect' at 0x033B2FC0>, <Element 'aspect' at 0x033B7030>, <Element 'aspect' at 0x033B7060>, <Element 'aspect' at 0x033B7090>, <Element 'aspect' at 0x033B70C0>, <Element 'aspect' at 0x033B70F0>, <Element 'aspect' at 0x033B7120>, <Element 'aspect' at 0x033B7150>, <Element 'aspect' at 0x033B7180>, <Element 'aspect' at 0x033B7240>, <Element 'aspect' at 0x033B7270>, <Element 'aspect' at 0x033B72A0>, <Element 'aspect' at 0x033B7AB0>, <Element 'aspect' at 0x033B7AE0>, <Element 'aspect' at 0x033B7B10>, <Element 'aspect' at 0x033B7B40>, <Element 'aspect' at 0x033B7BA0>, <Element 'aspect' at 0x033B7BD0>, <Element 'aspect' at 0x033B7C00>, <Element 'aspect' at 0x033B7C30>, <Element 'aspect' at 0x033B7C60>, <Element 'aspect' at 0x033B7C90>, <Element 'aspect' at 0x033B7CC0>, <Element 'aspect' at 0x033BF3C0>, <Element 'aspect' at 0x033BF4E0>, <Element 'aspect' at 0x033BF510>, <Element 'aspect' at 0x033BF540>, <Element 'aspect' at 0x033BF5A0>, <Element 'aspect' at 0x033BF5D0>, <Element 'aspect' at 0x033BF6C0>, <Element 'aspect' at 0x033BF6F0>, <Element 'aspect' at 0x0339A6F0>, <Element 'aspect' at 0x0339A720>, <Element 'aspect' at 0x0339A7B0>, <Element 'aspect' at 0x0339A750>, <Element 'aspect' at 0x0339A660>, <Element 'aspect' at 0x0339A600>, <Element 'aspect' at 0x0339A540>, <Element 'aspect' at 0x0339A510>, <Element 'aspect' at 0x033BFE70>, <Element 'aspect' at 0x033DB5A0>, <Element 'aspect' at 0x033DB5D0>, <Element 'aspect' at 0x033DB600>, <Element 'aspect' at 0x033DB750>, <Element 'aspect' at 0x033DB780>, <Element 'aspect' at 0x033DB7B0>, <Element 'aspect' at 0x033DB7E0>, <Element 'aspect' at 0x033DB810>, <Element 'aspect' at 0x033DB840>, <Element 'aspect' at 0x033DBA50>, <Element 'aspect' at 0x033DBA80>, <Element 'aspect' at 0x033E12D0>, <Element 'aspect' at 0x033E1300>, <Element 'aspect' at 0x033E1330>, <Element 'aspect' at 0x033E1360>, <Element 'aspect' at 0x033E1390>, <Element 'aspect' at 0x033E13C0>, <Element 'aspect' at 0x033E1960>, <Element 'aspect' at 0x033E1990>, <Element 'aspect' at 0x033E19C0>, <Element 'aspect' at 0x033E19F0>, <Element 'aspect' at 0x033E1A20>, <Element 'aspect' at 0x033E1AE0>, <Element 'aspect' at 0x033E1B40>, <Element 'aspect' at 0x033E62A0>, <Element 'aspect' at 0x033E62D0>, <Element 'aspect' at 0x033E6300>, <Element 'aspect' at 0x033E6330>, <Element 'aspect' at 0x033E6360>, <Element 'aspect' at 0x033E6390>, <Element 'aspect' at 0x033E63C0>, <Element 'aspect' at 0x033E63F0>, <Element 'aspect' at 0x033E6480>, <Element 'aspect' at 0x033E65A0>, <Element 'aspect' at 0x033E65D0>, <Element 'aspect' at 0x033E6810>, <Element 'aspect' at 0x033E68A0>, <Element 'aspect' at 0x033E6EA0>, <Element 'aspect' at 0x033ED120>, <Element 'aspect' at 0x033ED150>, <Element 'aspect' at 0x033ED180>, <Element 'aspect' at 0x033ED1B0>, <Element 'aspect' at 0x033ED1E0>, <Element 'aspect' at 0x033ED210>, <Element 'aspect' at 0x033ED240>, <Element 'aspect' at 0x033ED2D0>, <Element 'aspect' at 0x033ED8D0>, <Element 'aspect' at 0x033ED900>, <Element 'aspect' at 0x033ED9F0>, <Element 'aspect' at 0x033EDA20>, <Element 'aspect' at 0x033EDD20>, <Element 'aspect' at 0x033F36F0>, <Element 'aspect' at 0x033F3720>, <Element 'aspect' at 0x033F3750>, <Element 'aspect' at 0x033F37B0>, <Element 'aspect' at 0x033F3DE0>, <Element 'aspect' at 0x033F3E40>, <Element 'aspect' at 0x033F3E70>, <Element 'aspect' at 0x033F3EA0>, <Element 'aspect' at 0x033F3ED0>, <Element 'aspect' at 0x033F3F00>, <Element 'aspect' at 0x033F3F30>, <Element 'aspect' at 0x033F3F60>, <Element 'aspect' at 0x033F3F90>, <Element 'aspect' at 0x033F90C0>, <Element 'aspect' at 0x033F9750>, <Element 'aspect' at 0x033F9780>, <Element 'aspect' at 0x033F97E0>, <Element 'aspect' at 0x033F9840>, <Element 'aspect' at 0x033F98A0>, <Element 'aspect' at 0x033FF390>, <Element 'aspect' at 0x033FF3C0>, <Element 'aspect' at 0x033FF3F0>, <Element 'aspect' at 0x033FF420>, <Element 'aspect' at 0x033FF450>, <Element 'aspect' at 0x033FFE70>, <Element 'aspect' at 0x033FFEA0>, <Element 'aspect' at 0x033FFF00>, <Element 'aspect' at 0x033FFF60>, <Element 'aspect' at 0x03406030>, <Element 'aspect' at 0x03406090>, <Element 'aspect' at 0x03406120>, <Element 'aspect' at 0x034061B0>, <Element 'aspect' at 0x03406A50>, <Element 'aspect' at 0x03406A80>, <Element 'aspect' at 0x03406BD0>, <Element 'aspect' at 0x03406C00>, <Element 'aspect' at 0x03406C30>, <Element 'aspect' at 0x03406C60>, <Element 'aspect' at 0x03406C90>, <Element 'aspect' at 0x0340B300>, <Element 'aspect' at 0x0340B450>, <Element 'aspect' at 0x0340B720>, <Element 'aspect' at 0x0340B750>, <Element 'aspect' at 0x0340B780>, <Element 'aspect' at 0x0340BDB0>, <Element 'aspect' at 0x0340BDE0>, <Element 'aspect' at 0x0340BE10>, <Element 'aspect' at 0x0340BE40>, <Element 'aspect' at 0x0340BE70>, <Element 'aspect' at 0x0340BF00>, <Element 'aspect' at 0x0340BFC0>, <Element 'aspect' at 0x03411030>, <Element 'aspect' at 0x03411090>, <Element 'aspect' at 0x034110C0>, <Element 'aspect' at 0x034112D0>, <Element 'aspect' at 0x03411300>, <Element 'aspect' at 0x03411330>, <Element 'aspect' at 0x03411360>, <Element 'aspect' at 0x03411390>, <Element 'aspect' at 0x034113C0>, <Element 'aspect' at 0x034113F0>, <Element 'aspect' at 0x03411420>, <Element 'aspect' at 0x03411450>, <Element 'aspect' at 0x03411510>, <Element 'aspect' at 0x03411BA0>, <Element 'aspect' at 0x0347A6C0>, <Element 'aspect' at 0x0347A8D0>, <Element 'aspect' at 0x0347A900>, <Element 'aspect' at 0x0347A930>, <Element 'aspect' at 0x0347F1E0>, <Element 'aspect' at 0x0347F210>, <Element 'aspect' at 0x0347F3C0>, <Element 'aspect' at 0x0347F3F0>, <Element 'aspect' at 0x0347FA20>, <Element 'aspect' at 0x0347FA50>, <Element 'aspect' at 0x0347FA80>, <Element 'aspect' at 0x0347FAB0>, <Element 'aspect' at 0x0347FB10>, <Element 'aspect' at 0x0347FB70>, <Element 'aspect' at 0x0347FC00>, <Element 'aspect' at 0x0347FC90>, <Element 'aspect' at 0x0347FCC0>, <Element 'aspect' at 0x0347FCF0>, <Element 'aspect' at 0x0347FD20>, <Element 'aspect' at 0x0347FD50>, <Element 'aspect' at 0x0347FDB0>, <Element 'aspect' at 0x0347FE10>, <Element 'aspect' at 0x034874E0>, <Element 'aspect' at 0x034875A0>, <Element 'aspect' at 0x03487600>, <Element 'aspect' at 0x03487DE0>, <Element 'aspect' at 0x03487E10>, <Element 'aspect' at 0x03487F90>, <Element 'aspect' at 0x0348C060>, <Element 'aspect' at 0x0348C180>, <Element 'aspect' at 0x0348C240>, <Element 'aspect' at 0x0348C990>, <Element 'aspect' at 0x034900C0>, <Element 'aspect' at 0x034900F0>, <Element 'aspect' at 0x034904B0>, <Element 'aspect' at 0x034904E0>, <Element 'aspect' at 0x03490510>, <Element 'aspect' at 0x03490540>, <Element 'aspect' at 0x03490570>, <Element 'aspect' at 0x034905A0>, <Element 'aspect' at 0x034905D0>, <Element 'aspect' at 0x03490630>, <Element 'aspect' at 0x03490660>, <Element 'aspect' at 0x03490C00>, <Element 'aspect' at 0x03490C30>, <Element 'aspect' at 0x03490C60>, <Element 'aspect' at 0x03490C90>, <Element 'aspect' at 0x03490FC0>, <Element 'aspect' at 0x03497030>, <Element 'aspect' at 0x034970C0>, <Element 'aspect' at 0x034970F0>, <Element 'aspect' at 0x03497120>, <Element 'aspect' at 0x03497150>, <Element 'aspect' at 0x03497AB0>, <Element 'aspect' at 0x03497AE0>, <Element 'aspect' at 0x03497B10>, <Element 'aspect' at 0x03497B40>, <Element 'aspect' at 0x03497BA0>, <Element 'aspect' at 0x03497BD0>, <Element 'aspect' at 0x03497C00>, <Element 'aspect' at 0x03497C60>, <Element 'aspect' at 0x03497C90>, <Element 'aspect' at 0x0349C240>, <Element 'aspect' at 0x0349C300>, <Element 'aspect' at 0x0349C4E0>, <Element 'aspect' at 0x0349C510>, <Element 'aspect' at 0x0349C540>, <Element 'aspect' at 0x0349C6F0>, <Element 'aspect' at 0x0349C720>, <Element 'aspect' at 0x0349CF60>, <Element 'aspect' at 0x0349CF90>, <Element 'aspect' at 0x0349CFC0>, <Element 'aspect' at 0x034A26C0>, <Element 'aspect' at 0x034A2810>, <Element 'aspect' at 0x034A2840>, <Element 'aspect' at 0x034A2870>, <Element 'aspect' at 0x034A28A0>, <Element 'aspect' at 0x034A2960>, <Element 'aspect' at 0x034A2A50>, <Element 'aspect' at 0x034A8090>, <Element 'aspect' at 0x034A8330>, <Element 'aspect' at 0x034A8360>, <Element 'aspect' at 0x034A8390>, <Element 'aspect' at 0x034A83C0>, <Element 'aspect' at 0x034A83F0>, <Element 'aspect' at 0x034A8420>, <Element 'aspect' at 0x034A8570>, <Element 'aspect' at 0x034A85A0>, <Element 'aspect' at 0x034A8690>, <Element 'aspect' at 0x034A86C0>, <Element 'aspect' at 0x034A8780>, <Element 'aspect' at 0x034A87B0>, <Element 'aspect' at 0x034A87E0>, <Element 'aspect' at 0x034A8810>, <Element 'aspect' at 0x034A8F90>, <Element 'aspect' at 0x034A8FC0>, <Element 'aspect' at 0x034B0840>, <Element 'aspect' at 0x034B0870>, <Element 'aspect' at 0x034B08A0>, <Element 'aspect' at 0x034B08D0>, <Element 'aspect' at 0x034B0990>, <Element 'aspect' at 0x034B40C0>, <Element 'aspect' at 0x034B4180>, <Element 'aspect' at 0x034B41B0>, <Element 'aspect' at 0x034B4210>, <Element 'aspect' at 0x034B4450>, <Element 'aspect' at 0x034B44B0>, <Element 'aspect' at 0x034B4510>, <Element 'aspect' at 0x034B4540>, <Element 'aspect' at 0x034B4570>, <Element 'aspect' at 0x034B4C60>, <Element 'aspect' at 0x0350F420>, <Element 'aspect' at 0x0350F450>, <Element 'aspect' at 0x0350F480>, <Element 'aspect' at 0x0350F4B0>, <Element 'aspect' at 0x0350F4E0>, <Element 'aspect' at 0x0350F570>, <Element 'aspect' at 0x0350F870>, <Element 'aspect' at 0x03515030>, <Element 'aspect' at 0x03515060>, <Element 'aspect' at 0x035152A0>, <Element 'aspect' at 0x035152D0>, <Element 'aspect' at 0x03515300>, <Element 'aspect' at 0x035154B0>, <Element 'aspect' at 0x035154E0>, <Element 'aspect' at 0x03515510>, <Element 'aspect' at 0x03515B10>, <Element 'aspect' at 0x03515B40>, <Element 'aspect' at 0x03515DB0>, <Element 'aspect' at 0x03515DE0>, <Element 'aspect' at 0x03515ED0>, <Element 'aspect' at 0x0351C510>, <Element 'aspect' at 0x0351C5A0>, <Element 'aspect' at 0x0351C5D0>, <Element 'aspect' at 0x0351C600>, <Element 'aspect' at 0x0351C630>, <Element 'aspect' at 0x0351CDB0>, <Element 'aspect' at 0x0351CDE0>, <Element 'aspect' at 0x0351CE10>, <Element 'aspect' at 0x0351CE40>, <Element 'aspect' at 0x0351CE70>, <Element 'aspect' at 0x0351CEA0>, <Element 'aspect' at 0x0351CED0>, <Element 'aspect' at 0x0351CF00>, <Element 'aspect' at 0x0351CF60>, <Element 'aspect' at 0x0351CF90>, <Element 'aspect' at 0x035211E0>, <Element 'aspect' at 0x035217E0>, <Element 'aspect' at 0x035219F0>, <Element 'aspect' at 0x03521A20>, <Element 'aspect' at 0x03521A50>, <Element 'aspect' at 0x03521A80>, <Element 'aspect' at 0x03527210>, <Element 'aspect' at 0x03527240>, <Element 'aspect' at 0x03527270>, <Element 'aspect' at 0x03527AB0>, <Element 'aspect' at 0x03527B40>, <Element 'aspect' at 0x03527B70>, <Element 'aspect' at 0x03527BA0>, <Element 'aspect' at 0x03527BD0>, <Element 'aspect' at 0x03527C60>, <Element 'aspect' at 0x03527CF0>, <Element 'aspect' at 0x03527D20>, <Element 'aspect' at 0x03527D50>, <Element 'aspect' at 0x03527D80>, <Element 'aspect' at 0x0352E0C0>, <Element 'aspect' at 0x0352E840>, <Element 'aspect' at 0x0352E870>, <Element 'aspect' at 0x0352E8A0>, <Element 'aspect' at 0x0352E8D0>, <Element 'aspect' at 0x0352E900>, <Element 'aspect' at 0x0352E960>, <Element 'aspect' at 0x0352E990>, <Element 'aspect' at 0x0352EFC0>, <Element 'aspect' at 0x03532030>, <Element 'aspect' at 0x03532060>, <Element 'aspect' at 0x03532090>, <Element 'aspect' at 0x03532690>, <Element 'aspect' at 0x03532D80>, <Element 'aspect' at 0x03532DB0>, <Element 'aspect' at 0x03532DE0>, <Element 'aspect' at 0x03532E10>, <Element 'aspect' at 0x03532F30>, <Element 'aspect' at 0x03539030>, <Element 'aspect' at 0x03539060>, <Element 'aspect' at 0x035390C0>, <Element 'aspect' at 0x035390F0>, <Element 'aspect' at 0x03539120>, <Element 'aspect' at 0x03539150>, <Element 'aspect' at 0x03539180>, <Element 'aspect' at 0x035397E0>, <Element 'aspect' at 0x03539810>, <Element 'aspect' at 0x03539840>, <Element 'aspect' at 0x03539870>, <Element 'aspect' at 0x035398A0>, <Element 'aspect' at 0x035398D0>, <Element 'aspect' at 0x03539900>, <Element 'aspect' at 0x03539B40>, <Element 'aspect' at 0x03539C30>, <Element 'aspect' at 0x03541510>, <Element 'aspect' at 0x03541540>, <Element 'aspect' at 0x03541570>, <Element 'aspect' at 0x03541C30>, <Element 'aspect' at 0x03541E10>, <Element 'aspect' at 0x03541E40>, <Element 'aspect' at 0x03541E70>, <Element 'aspect' at 0x03541F60>, <Element 'aspect' at 0x035471B0>, <Element 'aspect' at 0x035471E0>, <Element 'aspect' at 0x03547210>, <Element 'aspect' at 0x03547870>, <Element 'aspect' at 0x035478A0>, <Element 'aspect' at 0x03547900>, <Element 'aspect' at 0x035479F0>, <Element 'aspect' at 0x03547A20>, <Element 'aspect' at 0x03547AE0>, <Element 'aspect' at 0x03547B40>, <Element 'aspect' at 0x03547B70>, <Element 'aspect' at 0x03547BA0>, <Element 'aspect' at 0x03547BD0>, <Element 'aspect' at 0x03547C30>, <Element 'aspect' at 0x03547C60>, <Element 'aspect' at 0x03547D50>, <Element 'aspect' at 0x03547D80>, <Element 'aspect' at 0x035615A0>, <Element 'aspect' at 0x035615D0>, <Element 'aspect' at 0x03561600>, <Element 'aspect' at 0x03561630>, <Element 'aspect' at 0x03561660>, <Element 'aspect' at 0x03561720>, <Element 'aspect' at 0x03561FC0>, <Element 'aspect' at 0x03567030>, <Element 'aspect' at 0x03567060>, <Element 'aspect' at 0x03567090>, <Element 'aspect' at 0x035676F0>, <Element 'aspect' at 0x03567720>, <Element 'aspect' at 0x03567750>, <Element 'aspect' at 0x035677B0>, <Element 'aspect' at 0x035677E0>, <Element 'aspect' at 0x03567810>, <Element 'aspect' at 0x035678A0>, <Element 'aspect' at 0x035678D0>, <Element 'aspect' at 0x03567990>, <Element 'aspect' at 0x03567A20>, <Element 'aspect' at 0x03567A50>, <Element 'aspect' at 0x0356B210>, <Element 'aspect' at 0x0356B240>, <Element 'aspect' at 0x0356B930>, <Element 'aspect' at 0x0356B960>, <Element 'aspect' at 0x0356B9F0>, <Element 'aspect' at 0x0356BAE0>, <Element 'aspect' at 0x0356BB70>, <Element 'aspect' at 0x0356BBD0>, <Element 'aspect' at 0x0356BC00>, <Element 'aspect' at 0x035712D0>, <Element 'aspect' at 0x03571300>, <Element 'aspect' at 0x03571330>, <Element 'aspect' at 0x03571360>, <Element 'aspect' at 0x03571390>, <Element 'aspect' at 0x035713C0>, <Element 'aspect' at 0x035718A0>, <Element 'aspect' at 0x03571F90>, <Element 'aspect' at 0x03571FC0>, <Element 'aspect' at 0x03576060>, <Element 'aspect' at 0x03576090>, <Element 'aspect' at 0x035760F0>, <Element 'aspect' at 0x035761B0>, <Element 'aspect' at 0x035761E0>, <Element 'aspect' at 0x03576210>, <Element 'aspect' at 0x03576240>, <Element 'aspect' at 0x03576270>, <Element 'aspect' at 0x035762A0>, <Element 'aspect' at 0x035762D0>, <Element 'aspect' at 0x03576300>, <Element 'aspect' at 0x03576390>, <Element 'aspect' at 0x035769F0>, <Element 'aspect' at 0x03576A20>, <Element 'aspect' at 0x03576B70>, <Element 'aspect' at 0x0357E420>, <Element 'aspect' at 0x0357E510>, <Element 'aspect' at 0x0357E690>, <Element 'aspect' at 0x0357E6C0>, <Element 'aspect' at 0x0357E780>, <Element 'aspect' at 0x0357EE10>, <Element 'aspect' at 0x0357EE40>, <Element 'aspect' at 0x0357EE70>, <Element 'aspect' at 0x0357EEA0>, <Element 'aspect' at 0x03585060>, <Element 'aspect' at 0x035856C0>, <Element 'aspect' at 0x035856F0>, <Element 'aspect' at 0x03585720>, <Element 'aspect' at 0x035858A0>, <Element 'aspect' at 0x03585F30>, <Element 'aspect' at 0x03585F60>, <Element 'aspect' at 0x03585F90>, <Element 'aspect' at 0x03585FC0>, <Element 'aspect' at 0x03589120>, <Element 'aspect' at 0x03589930>, <Element 'aspect' at 0x03589960>, <Element 'aspect' at 0x03589990>, <Element 'aspect' at 0x0358F030>, <Element 'aspect' at 0x0358F060>, <Element 'aspect' at 0x0358F090>, <Element 'aspect' at 0x0358F7B0>, <Element 'aspect' at 0x0358F7E0>, <Element 'aspect' at 0x0358F810>, <Element 'aspect' at 0x0358F840>, <Element 'aspect' at 0x0358F870>, <Element 'aspect' at 0x0358F8A0>, <Element 'aspect' at 0x0358F8D0>, <Element 'aspect' at 0x0358F900>, <Element 'aspect' at 0x0358FB10>, <Element 'aspect' at 0x0358FBA0>, <Element 'aspect' at 0x0358FC00>, <Element 'aspect' at 0x03593210>, <Element 'aspect' at 0x03593240>, <Element 'aspect' at 0x03593270>, <Element 'aspect' at 0x035939C0>, <Element 'aspect' at 0x035939F0>, <Element 'aspect' at 0x03593A20>, <Element 'aspect' at 0x03593A50>, <Element 'aspect' at 0x0359A150>, <Element 'aspect' at 0x0359A1E0>, <Element 'aspect' at 0x0359A240>, <Element 'aspect' at 0x0359A270>, <Element 'aspect' at 0x0359A2A0>, <Element 'aspect' at 0x0359A2D0>, <Element 'aspect' at 0x0359A990>, <Element 'aspect' at 0x0359A9C0>, <Element 'aspect' at 0x0359A9F0>, <Element 'aspect' at 0x0359AA20>, <Element 'aspect' at 0x0359AA50>, <Element 'aspect' at 0x0359AA80>, <Element 'aspect' at 0x03605450>, <Element 'aspect' at 0x03605480>, <Element 'aspect' at 0x036054B0>, <Element 'aspect' at 0x03605C30>, <Element 'aspect' at 0x03605C60>, <Element 'aspect' at 0x03605C90>, <Element 'aspect' at 0x03605CF0>, <Element 'aspect' at 0x03605D20>, <Element 'aspect' at 0x03605D50>, <Element 'aspect' at 0x03605D80>, <Element 'aspect' at 0x0360B3F0>, <Element 'aspect' at 0x0360B4E0>, <Element 'aspect' at 0x0360B510>, <Element 'aspect' at 0x0360B540>, <Element 'aspect' at 0x0360B570>, <Element 'aspect' at 0x0360B5A0>, <Element 'aspect' at 0x0360B5D0>, <Element 'aspect' at 0x0360B600>, <Element 'aspect' at 0x0360B630>, <Element 'aspect' at 0x0360B660>, <Element 'aspect' at 0x0360B690>, <Element 'aspect' at 0x0360B6C0>, <Element 'aspect' at 0x0360B6F0>, <Element 'aspect' at 0x0360B720>, <Element 'aspect' at 0x0360B750>, <Element 'aspect' at 0x0360B780>, <Element 'aspect' at 0x0360B7E0>, <Element 'aspect' at 0x0360BED0>, <Element 'aspect' at 0x0360BF90>, <Element 'aspect' at 0x0360BFC0>, <Element 'aspect' at 0x03610030>, <Element 'aspect' at 0x036100C0>, <Element 'aspect' at 0x03610120>, <Element 'aspect' at 0x03610870>, <Element 'aspect' at 0x03610960>, <Element 'aspect' at 0x03610990>, <Element 'aspect' at 0x03610A50>, <Element 'aspect' at 0x03610AB0>, <Element 'aspect' at 0x03610AE0>, <Element 'aspect' at 0x03610B10>, <Element 'aspect' at 0x03610B40>, <Element 'aspect' at 0x03616330>, <Element 'aspect' at 0x03616360>, <Element 'aspect' at 0x03616390>, <Element 'aspect' at 0x036163C0>, <Element 'aspect' at 0x036163F0>, <Element 'aspect' at 0x03616420>, <Element 'aspect' at 0x03616450>, <Element 'aspect' at 0x03616480>, <Element 'aspect' at 0x03616BA0>, <Element 'aspect' at 0x03616BD0>, <Element 'aspect' at 0x03616C00>, <Element 'aspect' at 0x03616C30>, <Element 'aspect' at 0x0361D420>, <Element 'aspect' at 0x0361D540>, <Element 'aspect' at 0x0361DDE0>, <Element 'aspect' at 0x0361DE40>, <Element 'aspect' at 0x0361DE70>, <Element 'aspect' at 0x0361DF60>, <Element 'aspect' at 0x0361DF90>, <Element 'aspect' at 0x036225D0>, <Element 'aspect' at 0x03622600>, <Element 'aspect' at 0x03622630>, <Element 'aspect' at 0x03622660>, <Element 'aspect' at 0x03622780>, <Element 'aspect' at 0x036227B0>, <Element 'aspect' at 0x036227E0>, <Element 'aspect' at 0x03622810>, <Element 'aspect' at 0x03622840>, <Element 'aspect' at 0x036228D0>, <Element 'aspect' at 0x03622900>, <Element 'aspect' at 0x03626180>, <Element 'aspect' at 0x03626330>, <Element 'aspect' at 0x036263F0>, <Element 'aspect' at 0x03626420>, <Element 'aspect' at 0x03626450>, <Element 'aspect' at 0x03626480>, <Element 'aspect' at 0x03626A50>, <Element 'aspect' at 0x03626A80>, <Element 'aspect' at 0x03626AB0>, <Element 'aspect' at 0x03626AE0>, <Element 'aspect' at 0x03626B10>, <Element 'aspect' at 0x0362D420>, <Element 'aspect' at 0x0362D450>, <Element 'aspect' at 0x0362D480>, <Element 'aspect' at 0x0362D4B0>, <Element 'aspect' at 0x0362D4E0>, <Element 'aspect' at 0x0362D7E0>, <Element 'aspect' at 0x0362DF60>, <Element 'aspect' at 0x03633270>, <Element 'aspect' at 0x036332A0>, <Element 'aspect' at 0x036332D0>, <Element 'aspect' at 0x03633300>, <Element 'aspect' at 0x03633360>, <Element 'aspect' at 0x03633390>, <Element 'aspect' at 0x036333C0>, <Element 'aspect' at 0x036333F0>, <Element 'aspect' at 0x03633420>, <Element 'aspect' at 0x03633450>, <Element 'aspect' at 0x03633480>, <Element 'aspect' at 0x036334B0>, <Element 'aspect' at 0x036334E0>, <Element 'aspect' at 0x03633C00>, <Element 'aspect' at 0x03633C30>, <Element 'aspect' at 0x03633C60>, <Element 'aspect' at 0x03633C90>, <Element 'aspect' at 0x03633CC0>, <Element 'aspect' at 0x03633CF0>, <Element 'aspect' at 0x03633D20>, <Element 'aspect' at 0x03633D50>, <Element 'aspect' at 0x03633D80>, <Element 'aspect' at 0x03633DB0>, <Element 'aspect' at 0x03633DE0>, <Element 'aspect' at 0x03633E10>, <Element 'aspect' at 0x036394B0>, <Element 'aspect' at 0x036394E0>, <Element 'aspect' at 0x03639510>, <Element 'aspect' at 0x03639540>, <Element 'aspect' at 0x03639570>, <Element 'aspect' at 0x036395A0>, <Element 'aspect' at 0x036395D0>, <Element 'aspect' at 0x03639600>, <Element 'aspect' at 0x03639630>, <Element 'aspect' at 0x03639660>, <Element 'aspect' at 0x03639690>, <Element 'aspect' at 0x036396C0>, <Element 'aspect' at 0x03639750>, <Element 'aspect' at 0x03639780>, <Element 'aspect' at 0x036397B0>, <Element 'aspect' at 0x03639840>, <Element 'aspect' at 0x03639870>, <Element 'aspect' at 0x036398A0>, <Element 'aspect' at 0x036398D0>, <Element 'aspect' at 0x035BF060>, <Element 'aspect' at 0x035BF090>, <Element 'aspect' at 0x035BF0C0>, <Element 'aspect' at 0x035BF120>, <Element 'aspect' at 0x035BF150>, <Element 'aspect' at 0x035BF180>, <Element 'aspect' at 0x035BF1E0>, <Element 'aspect' at 0x035BF210>, <Element 'aspect' at 0x035BF240>, <Element 'aspect' at 0x035BF270>, <Element 'aspect' at 0x035BF2A0>, <Element 'aspect' at 0x035BF2D0>, <Element 'aspect' at 0x035BF300>, <Element 'aspect' at 0x035BF330>, <Element 'aspect' at 0x035BF3F0>, <Element 'aspect' at 0x035BF990>, <Element 'aspect' at 0x035BF9C0>, <Element 'aspect' at 0x035BF9F0>, <Element 'aspect' at 0x035BFA50>, <Element 'aspect' at 0x035BFB70>, <Element 'aspect' at 0x035BFBA0>, <Element 'aspect' at 0x035BFC00>, <Element 'aspect' at 0x035BFC30>, <Element 'aspect' at 0x035BFD80>, <Element 'aspect' at 0x035BFDB0>, <Element 'aspect' at 0x035BFDE0>, <Element 'aspect' at 0x035BFE10>, <Element 'aspect' at 0x035BFE70>, <Element 'aspect' at 0x035C55A0>, <Element 'aspect' at 0x035C55D0>, <Element 'aspect' at 0x035C5600>, <Element 'aspect' at 0x035C5630>, <Element 'aspect' at 0x035C5660>, <Element 'aspect' at 0x035C5D50>, <Element 'aspect' at 0x035C5DB0>, <Element 'aspect' at 0x035C5DE0>, <Element 'aspect' at 0x035CB0F0>, <Element 'aspect' at 0x035CB120>, <Element 'aspect' at 0x035CB150>, <Element 'aspect' at 0x035CB840>, <Element 'aspect' at 0x035CB870>, <Element 'aspect' at 0x035CB8A0>, <Element 'aspect' at 0x035CB8D0>, <Element 'aspect' at 0x035CB900>, <Element 'aspect' at 0x035CB930>, <Element 'aspect' at 0x035CBA50>, <Element 'aspect' at 0x035CBC90>, <Element 'aspect' at 0x035CBCC0>, <Element 'aspect' at 0x035CBCF0>, <Element 'aspect' at 0x035CBD20>, <Element 'aspect' at 0x035CBD50>, <Element 'aspect' at 0x035D1540>, <Element 'aspect' at 0x035D1870>, <Element 'aspect' at 0x035D7600>, <Element 'aspect' at 0x035D7660>, <Element 'aspect' at 0x035D7690>, <Element 'aspect' at 0x035D76C0>, <Element 'aspect' at 0x035D76F0>, <Element 'aspect' at 0x035D7720>, <Element 'aspect' at 0x035D77E0>, <Element 'aspect' at 0x035D7810>, <Element 'aspect' at 0x035D7E40>, <Element 'aspect' at 0x035D7E70>, <Element 'aspect' at 0x035D7ED0>, <Element 'aspect' at 0x035DC0F0>, <Element 'aspect' at 0x035DC750>, <Element 'aspect' at 0x035E1150>, <Element 'aspect' at 0x035E11B0>, <Element 'aspect' at 0x035E11E0>, <Element 'aspect' at 0x035E1210>, <Element 'aspect' at 0x035E1240>, <Element 'aspect' at 0x035E1420>, <Element 'aspect' at 0x035E14B0>, <Element 'aspect' at 0x035E15A0>, <Element 'aspect' at 0x035E15D0>, <Element 'aspect' at 0x035E1630>, <Element 'aspect' at 0x035E16C0>, <Element 'aspect' at 0x035E18D0>, <Element 'aspect' at 0x035E1ED0>, <Element 'aspect' at 0x035E87B0>, <Element 'aspect' at 0x035E88D0>, <Element 'aspect' at 0x035E8930>, <Element 'aspect' at 0x035E8960>, <Element 'aspect' at 0x035E8990>, <Element 'aspect' at 0x035E8AE0>, <Element 'aspect' at 0x035E8D50>, <Element 'aspect' at 0x035ED540>, <Element 'aspect' at 0x035ED570>, <Element 'aspect' at 0x035ED5A0>, <Element 'aspect' at 0x035ED690>, <Element 'aspect' at 0x035EDDE0>, <Element 'aspect' at 0x035EDE10>, <Element 'aspect' at 0x035EDE40>, <Element 'aspect' at 0x035EDE70>, <Element 'aspect' at 0x035EDFC0>, <Element 'aspect' at 0x035F4030>, <Element 'aspect' at 0x035F4060>, <Element 'aspect' at 0x035F46C0>, <Element 'aspect' at 0x035F46F0>, <Element 'aspect' at 0x035F4810>, <Element 'aspect' at 0x035F4840>, <Element 'aspect' at 0x035F9030>, <Element 'aspect' at 0x035F9060>, <Element 'aspect' at 0x035F9090>, <Element 'aspect' at 0x035F9120>, <Element 'aspect' at 0x035F9150>, <Element 'aspect' at 0x035F9180>, <Element 'aspect' at 0x035F91B0>, <Element 'aspect' at 0x035F9210>, <Element 'aspect' at 0x035F9270>, <Element 'aspect' at 0x035F92A0>, <Element 'aspect' at 0x035F92D0>, <Element 'aspect' at 0x035F9330>, <Element 'aspect' at 0x035F9C60>, <Element 'aspect' at 0x035F9C90>, <Element 'aspect' at 0x035F9CC0>, <Element 'aspect' at 0x035F9CF0>, <Element 'aspect' at 0x035F9D20>, <Element 'aspect' at 0x035F9DB0>, <Element 'aspect' at 0x035F9F00>, <Element 'aspect' at 0x0366A540>, <Element 'aspect' at 0x0366A570>, <Element 'aspect' at 0x0366A5A0>, <Element 'aspect' at 0x0366A5D0>, <Element 'aspect' at 0x0366A660>, <Element 'aspect' at 0x0366A6C0>, <Element 'aspect' at 0x0366A6F0>, <Element 'aspect' at 0x0366A8D0>, <Element 'aspect' at 0x0366A900>, <Element 'aspect' at 0x0366A930>, <Element 'aspect' at 0x0366A960>, <Element 'aspect' at 0x036701B0>, <Element 'aspect' at 0x036701E0>, <Element 'aspect' at 0x03670210>, <Element 'aspect' at 0x03670270>, <Element 'aspect' at 0x036702D0>, <Element 'aspect' at 0x03670960>, <Element 'aspect' at 0x03670990>, <Element 'aspect' at 0x036709C0>, <Element 'aspect' at 0x03676240>, <Element 'aspect' at 0x03676270>, <Element 'aspect' at 0x036762A0>, <Element 'aspect' at 0x03676690>, <Element 'aspect' at 0x036766C0>, <Element 'aspect' at 0x03676720>, <Element 'aspect' at 0x03676750>, <Element 'aspect' at 0x03676810>, <Element 'aspect' at 0x03676EA0>, <Element 'aspect' at 0x03676F00>, <Element 'aspect' at 0x0367CCC0>, <Element 'aspect' at 0x0367CCF0>, <Element 'aspect' at 0x0367CD20>, <Element 'aspect' at 0x0367CD50>, <Element 'aspect' at 0x0367CD80>, <Element 'aspect' at 0x0367CDB0>, <Element 'aspect' at 0x0367CDE0>, <Element 'aspect' at 0x036825A0>, <Element 'aspect' at 0x036825D0>, <Element 'aspect' at 0x03682600>, <Element 'aspect' at 0x03682D50>, <Element 'aspect' at 0x03682D80>, <Element 'aspect' at 0x03682DB0>, <Element 'aspect' at 0x03682DE0>, <Element 'aspect' at 0x03682E10>, <Element 'aspect' at 0x03688810>, <Element 'aspect' at 0x03688840>, <Element 'aspect' at 0x03688870>, <Element 'aspect' at 0x036888A0>, <Element 'aspect' at 0x036888D0>, <Element 'aspect' at 0x03688900>, <Element 'aspect' at 0x03688960>, <Element 'aspect' at 0x03688990>, <Element 'aspect' at 0x03688A20>, <Element 'aspect' at 0x03688A50>, <Element 'aspect' at 0x03688B10>, <Element 'aspect' at 0x03688B40>, <Element 'aspect' at 0x03688B70>, <Element 'aspect' at 0x0368D480>, <Element 'aspect' at 0x0368D4B0>, <Element 'aspect' at 0x0368D4E0>, <Element 'aspect' at 0x0368D510>, <Element 'aspect' at 0x0368D5A0>, <Element 'aspect' at 0x0368D660>, <Element 'aspect' at 0x0368D6C0>, <Element 'aspect' at 0x0368DEA0>, <Element 'aspect' at 0x0368DED0>, <Element 'aspect' at 0x03694240>, <Element 'aspect' at 0x03694270>, <Element 'aspect' at 0x036948A0>, <Element 'aspect' at 0x036948D0>, <Element 'aspect' at 0x03694900>, <Element 'aspect' at 0x0369A300>, <Element 'aspect' at 0x0369A330>, <Element 'aspect' at 0x0369A3C0>, <Element 'aspect' at 0x0369A3F0>, <Element 'aspect' at 0x0369A420>, <Element 'aspect' at 0x0369AC90>, <Element 'aspect' at 0x0369ACC0>, <Element 'aspect' at 0x0369ACF0>, <Element 'aspect' at 0x0369AE40>, <Element 'aspect' at 0x036A1480>, <Element 'aspect' at 0x036A14B0>, <Element 'aspect' at 0x036A14E0>, <Element 'aspect' at 0x036A1510>, <Element 'aspect' at 0x036A1540>, <Element 'aspect' at 0x036A1A80>, <Element 'aspect' at 0x036A1AB0>, <Element 'aspect' at 0x036A1BA0>, <Element 'aspect' at 0x036A1BD0>, <Element 'aspect' at 0x03708630>, <Element 'aspect' at 0x037086C0>, <Element 'aspect' at 0x03708CF0>, <Element 'aspect' at 0x03708D20>, <Element 'aspect' at 0x03708D80>, <Element 'aspect' at 0x03708DB0>, <Element 'aspect' at 0x03708DE0>, <Element 'aspect' at 0x03708F00>, <Element 'aspect' at 0x0370F2D0>, <Element 'aspect' at 0x0370F8D0>, <Element 'aspect' at 0x0370F900>, <Element 'aspect' at 0x0370F930>, <Element 'aspect' at 0x0370F960>, <Element 'aspect' at 0x0370F990>, <Element 'aspect' at 0x0370F9F0>, <Element 'aspect' at 0x0370FAE0>, <Element 'aspect' at 0x0370FBA0>, <Element 'aspect' at 0x03713510>, <Element 'aspect' at 0x03713F90>, <Element 'aspect' at 0x03713FC0>, <Element 'aspect' at 0x0371B030>, <Element 'aspect' at 0x0371B090>, <Element 'aspect' at 0x0371B8D0>, <Element 'aspect' at 0x0371B900>, <Element 'aspect' at 0x0371B930>, <Element 'aspect' at 0x0371BB70>, <Element 'aspect' at 0x03720150>, <Element 'aspect' at 0x03720180>, <Element 'aspect' at 0x037201B0>, <Element 'aspect' at 0x037201E0>, <Element 'aspect' at 0x03720210>, <Element 'aspect' at 0x03720240>, <Element 'aspect' at 0x03720270>, <Element 'aspect' at 0x037202A0>, <Element 'aspect' at 0x037202D0>, <Element 'aspect' at 0x037203F0>, <Element 'aspect' at 0x037204E0>, <Element 'aspect' at 0x03720C90>, <Element 'aspect' at 0x03720D20>, <Element 'aspect' at 0x03720D80>, <Element 'aspect' at 0x03720DB0>, <Element 'aspect' at 0x03720DE0>, <Element 'aspect' at 0x03720E10>, <Element 'aspect' at 0x03720F00>, <Element 'aspect' at 0x03726030>, <Element 'aspect' at 0x03726060>, <Element 'aspect' at 0x037267E0>, <Element 'aspect' at 0x03726A20>, <Element 'aspect' at 0x03726A50>, <Element 'aspect' at 0x03726AE0>, <Element 'aspect' at 0x03726B10>, <Element 'aspect' at 0x03726BA0>, <Element 'aspect' at 0x03726C00>, <Element 'aspect' at 0x03726C30>, <Element 'aspect' at 0x03726C60>, <Element 'aspect' at 0x0372B3F0>, <Element 'aspect' at 0x0372B420>, <Element 'aspect' at 0x0372B450>, <Element 'aspect' at 0x0372B480>, <Element 'aspect' at 0x0372B4B0>, <Element 'aspect' at 0x0372B540>, <Element 'aspect' at 0x0372B570>, <Element 'aspect' at 0x0372BD80>, <Element 'aspect' at 0x0372BDB0>, <Element 'aspect' at 0x0372BDE0>, <Element 'aspect' at 0x0372BE10>, <Element 'aspect' at 0x0372BE40>, <Element 'aspect' at 0x0372BE70>, <Element 'aspect' at 0x03731750>, <Element 'aspect' at 0x037317B0>, <Element 'aspect' at 0x03731F90>, <Element 'aspect' at 0x03731FC0>, <Element 'aspect' at 0x03737030>, <Element 'aspect' at 0x03737090>, <Element 'aspect' at 0x037370C0>, <Element 'aspect' at 0x037370F0>, <Element 'aspect' at 0x037371B0>, <Element 'aspect' at 0x037377E0>, <Element 'aspect' at 0x03737810>, <Element 'aspect' at 0x03737840>, <Element 'aspect' at 0x03737870>, <Element 'aspect' at 0x037378A0>, <Element 'aspect' at 0x0373C210>, <Element 'aspect' at 0x0373C240>, <Element 'aspect' at 0x0373C270>, <Element 'aspect' at 0x0373C870>, <Element 'aspect' at 0x0373C8A0>, <Element 'aspect' at 0x0373C900>, <Element 'aspect' at 0x0373C9F0>, <Element 'aspect' at 0x0373CA20>, <Element 'aspect' at 0x0373CB70>, <Element 'aspect' at 0x0373CBA0>, <Element 'aspect' at 0x0373CBD0>, <Element 'aspect' at 0x0373CC00>, <Element 'aspect' at 0x0373CC30>, <Element 'aspect' at 0x03743240>, <Element 'aspect' at 0x037432D0>, <Element 'aspect' at 0x03743300>, <Element 'aspect' at 0x03743420>, <Element 'aspect' at 0x03743510>, <Element 'aspect' at 0x03743540>, <Element 'aspect' at 0x03743600>, <Element 'aspect' at 0x03743630>, <Element 'aspect' at 0x03743EA0>, <Element 'aspect' at 0x03743F90>, <Element 'aspect' at 0x03756030>, <Element 'aspect' at 0x03756060>, <Element 'aspect' at 0x03756090>, <Element 'aspect' at 0x037560C0>, <Element 'aspect' at 0x03756960>, <Element 'aspect' at 0x03756990>, <Element 'aspect' at 0x037569C0>, <Element 'aspect' at 0x03756CF0>, <Element 'aspect' at 0x0375C390>, <Element 'aspect' at 0x0375C3C0>, <Element 'aspect' at 0x0375C5A0>, <Element 'aspect' at 0x03762090>, <Element 'aspect' at 0x037627B0>, <Element 'aspect' at 0x03762810>, <Element 'aspect' at 0x037628A0>, <Element 'aspect' at 0x03762990>, <Element 'aspect' at 0x03767240>, <Element 'aspect' at 0x03767960>, <Element 'aspect' at 0x03767AB0>, <Element 'aspect' at 0x03767AE0>, <Element 'aspect' at 0x03767B10>, <Element 'aspect' at 0x03767B40>, <Element 'aspect' at 0x03767B70>, <Element 'aspect' at 0x03767BD0>, <Element 'aspect' at 0x03767D20>, <Element 'aspect' at 0x03767D50>, <Element 'aspect' at 0x03767D80>, <Element 'aspect' at 0x03767DB0>, <Element 'aspect' at 0x03767DE0>, <Element 'aspect' at 0x03767E40>, <Element 'aspect' at 0x03767E70>, <Element 'aspect' at 0x0376D420>, <Element 'aspect' at 0x0376D450>, <Element 'aspect' at 0x0376D480>, <Element 'aspect' at 0x0376D4B0>, <Element 'aspect' at 0x0376D4E0>, <Element 'aspect' at 0x0376D510>, <Element 'aspect' at 0x0376D7B0>, <Element 'aspect' at 0x0376D840>, <Element 'aspect' at 0x0376DF90>, <Element 'aspect' at 0x03774210>, <Element 'aspect' at 0x03774240>, <Element 'aspect' at 0x037742A0>, <Element 'aspect' at 0x037749C0>, <Element 'aspect' at 0x037749F0>, <Element 'aspect' at 0x03774A20>, <Element 'aspect' at 0x03774A80>, <Element 'aspect' at 0x03774AB0>, <Element 'aspect' at 0x03774AE0>, <Element 'aspect' at 0x03774B10>, <Element 'aspect' at 0x03774B40>, <Element 'aspect' at 0x03774B70>, <Element 'aspect' at 0x03774BD0>, <Element 'aspect' at 0x03774F30>, <Element 'aspect' at 0x0377C510>, <Element 'aspect' at 0x0377C900>, <Element 'aspect' at 0x0377C930>, <Element 'aspect' at 0x0377C9C0>, <Element 'aspect' at 0x0377CA50>, <Element 'aspect' at 0x0377CA80>, <Element 'aspect' at 0x0377CAB0>, <Element 'aspect' at 0x0377CAE0>, <Element 'aspect' at 0x037820F0>, <Element 'aspect' at 0x03782120>, <Element 'aspect' at 0x03782270>, <Element 'aspect' at 0x037822A0>, <Element 'aspect' at 0x03782390>, <Element 'aspect' at 0x03782420>, <Element 'aspect' at 0x03782450>, <Element 'aspect' at 0x03782540>, <Element 'aspect' at 0x03782570>, <Element 'aspect' at 0x03782B70>, <Element 'aspect' at 0x03782BA0>, <Element 'aspect' at 0x03782BD0>, <Element 'aspect' at 0x03782C00>, <Element 'aspect' at 0x03782C30>, <Element 'aspect' at 0x03787540>, <Element 'aspect' at 0x03787570>, <Element 'aspect' at 0x037875D0>, <Element 'aspect' at 0x03787ED0>, <Element 'aspect' at 0x03787F00>, <Element 'aspect' at 0x03787F30>, <Element 'aspect' at 0x0378D270>, <Element 'aspect' at 0x0378D2D0>, <Element 'aspect' at 0x0378DA20>, <Element 'aspect' at 0x0378DAB0>, <Element 'aspect' at 0x0378DAE0>, <Element 'aspect' at 0x0378DB10>, <Element 'aspect' at 0x037AA360>, <Element 'aspect' at 0x037AA4E0>, <Element 'aspect' at 0x037AA510>, <Element 'aspect' at 0x037AA570>, <Element 'aspect' at 0x037AA5A0>, <Element 'aspect' at 0x037AA600>, <Element 'aspect' at 0x037AA630>, <Element 'aspect' at 0x037AA660>, <Element 'aspect' at 0x037AA690>, <Element 'aspect' at 0x037AA6C0>, <Element 'aspect' at 0x037AA6F0>, <Element 'aspect' at 0x037AA720>, <Element 'aspect' at 0x037AA750>, <Element 'aspect' at 0x037AA780>, <Element 'aspect' at 0x037AA7B0>, <Element 'aspect' at 0x037AAD50>, <Element 'aspect' at 0x037AAD80>, <Element 'aspect' at 0x037AADB0>, <Element 'aspect' at 0x037AADE0>, <Element 'aspect' at 0x037AAE10>, <Element 'aspect' at 0x037AAE40>, <Element 'aspect' at 0x037AAE70>, <Element 'aspect' at 0x037AAEA0>, <Element 'aspect' at 0x037AAED0>, <Element 'aspect' at 0x037AAF00>, <Element 'aspect' at 0x037AAF30>, <Element 'aspect' at 0x037B0660>, <Element 'aspect' at 0x037B0690>, <Element 'aspect' at 0x037B06C0>, <Element 'aspect' at 0x037B06F0>, <Element 'aspect' at 0x037B0720>, <Element 'aspect' at 0x037B0810>, <Element 'aspect' at 0x037B0840>, <Element 'aspect' at 0x037B0DE0>, <Element 'aspect' at 0x037B0E10>, <Element 'aspect' at 0x037B0E70>, <Element 'aspect' at 0x037B0EA0>, <Element 'aspect' at 0x037B0ED0>, <Element 'aspect' at 0x037B0F30>, <Element 'aspect' at 0x037B0F60>, <Element 'aspect' at 0x037B5600>, <Element 'aspect' at 0x037B5930>, <Element 'aspect' at 0x037B5960>, <Element 'aspect' at 0x037BA090>, <Element 'aspect' at 0x037BA0C0>, <Element 'aspect' at 0x037BA0F0>, <Element 'aspect' at 0x037BA120>, <Element 'aspect' at 0x037BA150>, <Element 'aspect' at 0x037BA180>, <Element 'aspect' at 0x037BA1B0>, <Element 'aspect' at 0x037BA1E0>, <Element 'aspect' at 0x037BA210>, <Element 'aspect' at 0x037BA2A0>, <Element 'aspect' at 0x037BA2D0>, <Element 'aspect' at 0x037BA8D0>, <Element 'aspect' at 0x037BA900>, <Element 'aspect' at 0x037BA930>, <Element 'aspect' at 0x037BA960>, <Element 'aspect' at 0x037C0060>, <Element 'aspect' at 0x037C0120>, <Element 'aspect' at 0x037C0150>, <Element 'aspect' at 0x037C0180>, <Element 'aspect' at 0x037C01B0>, <Element 'aspect' at 0x037C01E0>, <Element 'aspect' at 0x037C0210>, <Element 'aspect' at 0x037C0930>, <Element 'aspect' at 0x037C0960>, <Element 'aspect' at 0x037C0990>, <Element 'aspect' at 0x037C09C0>, <Element 'aspect' at 0x037C09F0>, <Element 'aspect' at 0x037C54B0>, <Element 'aspect' at 0x037C54E0>, <Element 'aspect' at 0x037C5510>, <Element 'aspect' at 0x037C5540>, <Element 'aspect' at 0x037C5570>, <Element 'aspect' at 0x037C5630>, <Element 'aspect' at 0x037C5660>, <Element 'aspect' at 0x037C5690>, <Element 'aspect' at 0x037C5750>, <Element 'aspect' at 0x037C5CF0>, <Element 'aspect' at 0x037C5D20>, <Element 'aspect' at 0x037C5D50>, <Element 'aspect' at 0x037C5D80>, <Element 'aspect' at 0x037C5E70>, <Element 'aspect' at 0x037C5EA0>, <Element 'aspect' at 0x037C5ED0>, <Element 'aspect' at 0x037C5F00>, <Element 'aspect' at 0x037C5F30>, <Element 'aspect' at 0x037C5F60>, <Element 'aspect' at 0x037CB090>, <Element 'aspect' at 0x037CB6C0>, <Element 'aspect' at 0x037CB780>, <Element 'aspect' at 0x037CB7B0>, <Element 'aspect' at 0x037CB7E0>, <Element 'aspect' at 0x037CB810>, <Element 'aspect' at 0x037CB840>, <Element 'aspect' at 0x037CB8A0>, <Element 'aspect' at 0x037CB900>, <Element 'aspect' at 0x037CB930>, <Element 'aspect' at 0x037CB960>, <Element 'aspect' at 0x037CB990>, <Element 'aspect' at 0x037CB9C0>, <Element 'aspect' at 0x037CBF60>, <Element 'aspect' at 0x037CBF90>, <Element 'aspect' at 0x037CBFC0>, <Element 'aspect' at 0x037D0030>, <Element 'aspect' at 0x037D02A0>, <Element 'aspect' at 0x037D02D0>, <Element 'aspect' at 0x037D0300>, <Element 'aspect' at 0x037D0330>, <Element 'aspect' at 0x037D0360>, <Element 'aspect' at 0x037D0930>, <Element 'aspect' at 0x037D0960>, <Element 'aspect' at 0x037D0A20>, <Element 'aspect' at 0x037D0A80>, <Element 'aspect' at 0x037D0B40>, <Element 'aspect' at 0x037D0BD0>, <Element 'aspect' at 0x037D62A0>, <Element 'aspect' at 0x037D63C0>, <Element 'aspect' at 0x037D6A20>, <Element 'aspect' at 0x037D6A80>, <Element 'aspect' at 0x037D6AB0>, <Element 'aspect' at 0x037D6AE0>, <Element 'aspect' at 0x037D9240>, <Element 'aspect' at 0x037D9270>, <Element 'aspect' at 0x037D92A0>, <Element 'aspect' at 0x037D9300>, <Element 'aspect' at 0x037D9330>, <Element 'aspect' at 0x037D98A0>, <Element 'aspect' at 0x037D9930>, <Element 'aspect' at 0x037D9AE0>, <Element 'aspect' at 0x037DF210>, <Element 'aspect' at 0x037DF240>, <Element 'aspect' at 0x037DF270>, <Element 'aspect' at 0x037DF2A0>, <Element 'aspect' at 0x037DF2D0>, <Element 'aspect' at 0x037DF300>, <Element 'aspect' at 0x037DF330>, <Element 'aspect' at 0x037DF390>, <Element 'aspect' at 0x037DFBA0>, <Element 'aspect' at 0x037DFBD0>, <Element 'aspect' at 0x037DFC00>, <Element 'aspect' at 0x037DFC30>, <Element 'aspect' at 0x037DFC60>, <Element 'aspect' at 0x037DFC90>, <Element 'aspect' at 0x037DFCC0>, <Element 'aspect' at 0x037DFCF0>, <Element 'aspect' at 0x03810480>, <Element 'aspect' at 0x038104B0>, <Element 'aspect' at 0x038104E0>, <Element 'aspect' at 0x03810510>, <Element 'aspect' at 0x03810540>, <Element 'aspect' at 0x03810600>, <Element 'aspect' at 0x03810DB0>, <Element 'aspect' at 0x03810DE0>, <Element 'aspect' at 0x03810E10>, <Element 'aspect' at 0x03814630>, <Element 'aspect' at 0x03814660>, <Element 'aspect' at 0x03814690>, <Element 'aspect' at 0x038146C0>, <Element 'aspect' at 0x038146F0>, <Element 'aspect' at 0x03814750>, <Element 'aspect' at 0x03814780>, <Element 'aspect' at 0x03814810>, <Element 'aspect' at 0x03814840>, <Element 'aspect' at 0x03814870>, <Element 'aspect' at 0x03814DE0>, <Element 'aspect' at 0x03814E10>, <Element 'aspect' at 0x03814E40>, <Element 'aspect' at 0x03814E70>, <Element 'aspect' at 0x03814EA0>, <Element 'aspect' at 0x03814F90>, <Element 'aspect' at 0x0381B0F0>, <Element 'aspect' at 0x0381B120>, <Element 'aspect' at 0x0381B210>, <Element 'aspect' at 0x0381B240>, <Element 'aspect' at 0x0381B870>, <Element 'aspect' at 0x0381B8D0>, <Element 'aspect' at 0x0381B900>, <Element 'aspect' at 0x0381B960>, <Element 'aspect' at 0x0381B9F0>, <Element 'aspect' at 0x03821270>, <Element 'aspect' at 0x038212A0>, <Element 'aspect' at 0x038212D0>, <Element 'aspect' at 0x03821300>, <Element 'aspect' at 0x03821330>, <Element 'aspect' at 0x038218D0>, <Element 'aspect' at 0x03821900>, <Element 'aspect' at 0x03821930>, <Element 'aspect' at 0x03821AB0>, <Element 'aspect' at 0x03821BA0>, <Element 'aspect' at 0x03821C30>, <Element 'aspect' at 0x03821C60>, <Element 'aspect' at 0x038272A0>, <Element 'aspect' at 0x03827390>, <Element 'aspect' at 0x038273C0>, <Element 'aspect' at 0x038274B0>, <Element 'aspect' at 0x03827A50>, <Element 'aspect' at 0x03827A80>, <Element 'aspect' at 0x03827AB0>, <Element 'aspect' at 0x0382C270>, <Element 'aspect' at 0x0382C2A0>, <Element 'aspect' at 0x0382C2D0>, <Element 'aspect' at 0x0382C360>, <Element 'aspect' at 0x0382C390>, <Element 'aspect' at 0x0382C3C0>, <Element 'aspect' at 0x0382CB10>, <Element 'aspect' at 0x0382CB40>, <Element 'aspect' at 0x0382CCF0>, <Element 'aspect' at 0x038313C0>, <Element 'aspect' at 0x038313F0>, <Element 'aspect' at 0x03831420>, <Element 'aspect' at 0x03831450>, <Element 'aspect' at 0x03831630>, <Element 'aspect' at 0x03831660>, <Element 'aspect' at 0x03831C30>, <Element 'aspect' at 0x03831DE0>, <Element 'aspect' at 0x03831E10>, <Element 'aspect' at 0x03831E40>, <Element 'aspect' at 0x03831E70>, <Element 'aspect' at 0x03831EA0>, <Element 'aspect' at 0x03831F60>, <Element 'aspect' at 0x03836660>, <Element 'aspect' at 0x03836690>, <Element 'aspect' at 0x038366C0>, <Element 'aspect' at 0x038366F0>, <Element 'aspect' at 0x03836F00>, <Element 'aspect' at 0x03836F30>, <Element 'aspect' at 0x03836F60>, <Element 'aspect' at 0x03836F90>, <Element 'aspect' at 0x03836FC0>, <Element 'aspect' at 0x0383D030>, <Element 'aspect' at 0x0383D060>, <Element 'aspect' at 0x0383D6F0>, <Element 'aspect' at 0x038420C0>, <Element 'aspect' at 0x03842150>, <Element 'aspect' at 0x03842240>, <Element 'aspect' at 0x03842270>, <Element 'aspect' at 0x03842900>, <Element 'aspect' at 0x03842930>, <Element 'aspect' at 0x03842AE0>, <Element 'aspect' at 0x03842B10>, <Element 'aspect' at 0x03842B40>, <Element 'aspect' at 0x03842B70>, <Element 'aspect' at 0x03842BA0>, <Element 'aspect' at 0x03848330>, <Element 'aspect' at 0x03848360>, <Element 'aspect' at 0x03848390>, <Element 'aspect' at 0x038483C0>, <Element 'aspect' at 0x038483F0>, <Element 'aspect' at 0x03848420>, <Element 'aspect' at 0x03848450>, <Element 'aspect' at 0x03848480>, <Element 'aspect' at 0x038484B0>, <Element 'aspect' at 0x038484E0>, <Element 'aspect' at 0x03848510>, <Element 'aspect' at 0x038486C0>, <Element 'aspect' at 0x03848C30>, <Element 'aspect' at 0x03848F90>, <Element 'aspect' at 0x0385D030>, <Element 'aspect' at 0x0385D060>, <Element 'aspect' at 0x0385D090>, <Element 'aspect' at 0x0385D720>, <Element 'aspect' at 0x0385D750>, <Element 'aspect' at 0x0385D7B0>, <Element 'aspect' at 0x0385D840>, <Element 'aspect' at 0x0385D870>, <Element 'aspect' at 0x0385DC90>, <Element 'aspect' at 0x03862360>, <Element 'aspect' at 0x03862390>, <Element 'aspect' at 0x038623F0>, <Element 'aspect' at 0x038624E0>, <Element 'aspect' at 0x03862AE0>, <Element 'aspect' at 0x038681B0>, <Element 'aspect' at 0x038683C0>, <Element 'aspect' at 0x038683F0>, <Element 'aspect' at 0x03868420>, <Element 'aspect' at 0x03868450>, <Element 'aspect' at 0x03868AB0>, <Element 'aspect' at 0x03868AE0>, <Element 'aspect' at 0x03868B10>, <Element 'aspect' at 0x03868B40>, <Element 'aspect' at 0x03868B70>, <Element 'aspect' at 0x03868BA0>, <Element 'aspect' at 0x03868BD0>, <Element 'aspect' at 0x03868C90>, <Element 'aspect' at 0x03868CC0>, <Element 'aspect' at 0x0386E630>, <Element 'aspect' at 0x0386EAB0>, <Element 'aspect' at 0x0386EAE0>, <Element 'aspect' at 0x0386EB10>, <Element 'aspect' at 0x0386EB40>, <Element 'aspect' at 0x03873180>, <Element 'aspect' at 0x038731B0>, <Element 'aspect' at 0x038731E0>, <Element 'aspect' at 0x03873210>, <Element 'aspect' at 0x03873510>]
tree.findall('.//*[@category="Service"]')
>>> tree.findall('.//*[@category="Service"][@type="implicit"]')
[<Element 'aspect' at 0x033B7270>, <Element 'aspect' at 0x033B72A0>, <Element 'aspect' at 0x033B7AB0>, <Element 'aspect' at 0x033B7AE0>, <Element 'aspect' at 0x033B7B40>, <Element 'aspect' at 0x033B7C00>, <Element 'aspect' at 0x033B7C90>, <Element 'aspect' at 0x033BF5A0>, <Element 'aspect' at 0x033BF6C0>, <Element 'aspect' at 0x0339A600>, <Element 'aspect' at 0x0339A540>, <Element 'aspect' at 0x033DB750>, <Element 'aspect' at 0x033DB7B0>, <Element 'aspect' at 0x033DB810>, <Element 'aspect' at 0x033E1300>, <Element 'aspect' at 0x033E19F0>, <Element 'aspect' at 0x033E6330>, <Element 'aspect' at 0x033E6390>, <Element 'aspect' at 0x033ED120>, <Element 'aspect' at 0x033ED1E0>, <Element 'aspect' at 0x033ED210>, <Element 'aspect' at 0x033ED9F0>, <Element 'aspect' at 0x033F3720>, <Element 'aspect' at 0x033FF3F0>, <Element 'aspect' at 0x033FF420>, <Element 'aspect' at 0x03406A80>, <Element 'aspect' at 0x03406C00>, <Element 'aspect' at 0x03406C30>, <Element 'aspect' at 0x0340BE10>, <Element 'aspect' at 0x03487E10>, <Element 'aspect' at 0x03490540>, <Element 'aspect' at 0x03490570>, <Element 'aspect' at 0x03497BA0>, <Element 'aspect' at 0x0349C4E0>, <Element 'aspect' at 0x034A2870>, <Element 'aspect' at 0x034A28A0>, <Element 'aspect' at 0x034A2960>, <Element 'aspect' at 0x034A8330>, <Element 'aspect' at 0x034A8360>, <Element 'aspect' at 0x034A83F0>, <Element 'aspect' at 0x034A87B0>, <Element 'aspect' at 0x034A87E0>, <Element 'aspect' at 0x034A8810>, <Element 'aspect' at 0x034A8F90>, <Element 'aspect' at 0x034B0870>, <Element 'aspect' at 0x034B41B0>, <Element 'aspect' at 0x0350F450>, <Element 'aspect' at 0x0350F480>, <Element 'aspect' at 0x03515060>, <Element 'aspect' at 0x035152A0>, <Element 'aspect' at 0x035152D0>, <Element 'aspect' at 0x035154B0>, <Element 'aspect' at 0x035154E0>, <Element 'aspect' at 0x03515DB0>, <Element 'aspect' at 0x03515ED0>, <Element 'aspect' at 0x03527D50>, <Element 'aspect' at 0x0352E8D0>, <Element 'aspect' at 0x0352E900>, <Element 'aspect' at 0x03532030>, <Element 'aspect' at 0x03532060>, <Element 'aspect' at 0x03532D80>, <Element 'aspect' at 0x03532DB0>, <Element 'aspect' at 0x03532F30>, <Element 'aspect' at 0x03539870>, <Element 'aspect' at 0x035398D0>, <Element 'aspect' at 0x035471E0>, <Element 'aspect' at 0x03547210>, <Element 'aspect' at 0x03547870>, <Element 'aspect' at 0x03561630>, <Element 'aspect' at 0x03561660>, <Element 'aspect' at 0x0356B210>, <Element 'aspect' at 0x03571F90>, <Element 'aspect' at 0x035856F0>, <Element 'aspect' at 0x03585720>, <Element 'aspect' at 0x03585FC0>, <Element 'aspect' at 0x03589990>, <Element 'aspect' at 0x0358F8A0>, <Element 'aspect' at 0x0358F900>, <Element 'aspect' at 0x0359AA50>, <Element 'aspect' at 0x03605450>, <Element 'aspect' at 0x03605D50>, <Element 'aspect' at 0x03605D80>, <Element 'aspect' at 0x0360B570>, <Element 'aspect' at 0x0360B660>, <Element 'aspect' at 0x0360B6F0>, <Element 'aspect' at 0x0360B750>, <Element 'aspect' at 0x03610AB0>, <Element 'aspect' at 0x03610B10>, <Element 'aspect' at 0x03616360>, <Element 'aspect' at 0x03616420>, <Element 'aspect' at 0x03616480>, <Element 'aspect' at 0x03616C00>, <Element 'aspect' at 0x03616C30>, <Element 'aspect' at 0x0361DE40>, <Element 'aspect' at 0x03622810>, <Element 'aspect' at 0x03622900>, <Element 'aspect' at 0x03626330>, <Element 'aspect' at 0x03626450>, <Element 'aspect' at 0x03626480>, <Element 'aspect' at 0x03626A80>, <Element 'aspect' at 0x0362D4B0>, <Element 'aspect' at 0x0362D4E0>, <Element 'aspect' at 0x036332D0>, <Element 'aspect' at 0x03633360>, <Element 'aspect' at 0x03633390>, <Element 'aspect' at 0x036333F0>, <Element 'aspect' at 0x03633450>, <Element 'aspect' at 0x03633C00>, <Element 'aspect' at 0x03633CC0>, <Element 'aspect' at 0x03633CF0>, <Element 'aspect' at 0x03633D50>, <Element 'aspect' at 0x03633DB0>, <Element 'aspect' at 0x036394B0>, <Element 'aspect' at 0x03639510>, <Element 'aspect' at 0x036396C0>, <Element 'aspect' at 0x03639750>, <Element 'aspect' at 0x03639870>, <Element 'aspect' at 0x036398D0>, <Element 'aspect' at 0x035BF090>, <Element 'aspect' at 0x035BF0C0>, <Element 'aspect' at 0x035BF120>, <Element 'aspect' at 0x035BF330>, <Element 'aspect' at 0x035BFC00>, <Element 'aspect' at 0x035BFDB0>, <Element 'aspect' at 0x035CB870>, <Element 'aspect' at 0x035CBD50>, <Element 'aspect' at 0x035D77E0>, <Element 'aspect' at 0x035D7ED0>, <Element 'aspect' at 0x035E87B0>, <Element 'aspect' at 0x035E8960>, <Element 'aspect' at 0x035ED570>, <Element 'aspect' at 0x035ED5A0>, <Element 'aspect' at 0x035EDDE0>, <Element 'aspect' at 0x035F9C90>, <Element 'aspect' at 0x0366A5A0>, <Element 'aspect' at 0x0366A930>, <Element 'aspect' at 0x03670210>, <Element 'aspect' at 0x03670990>, <Element 'aspect' at 0x036709C0>, <Element 'aspect' at 0x03676240>, <Element 'aspect' at 0x03676270>, <Element 'aspect' at 0x03676690>, <Element 'aspect' at 0x0367CD50>, <Element 'aspect' at 0x0367CDB0>, <Element 'aspect' at 0x0367CDE0>, <Element 'aspect' at 0x03682DE0>, <Element 'aspect' at 0x03688840>, <Element 'aspect' at 0x03688870>, <Element 'aspect' at 0x03688A50>, <Element 'aspect' at 0x0368DEA0>, <Element 'aspect' at 0x0369A3F0>, <Element 'aspect' at 0x0369ACC0>, <Element 'aspect' at 0x0369ACF0>, <Element 'aspect' at 0x0369AE40>, <Element 'aspect' at 0x036A1540>, <Element 'aspect' at 0x036A1BD0>, <Element 'aspect' at 0x03708D80>, <Element 'aspect' at 0x0371B900>, <Element 'aspect' at 0x03720180>, <Element 'aspect' at 0x03720240>, <Element 'aspect' at 0x0372BDE0>, <Element 'aspect' at 0x0372BE10>, <Element 'aspect' at 0x03731F90>, <Element 'aspect' at 0x037377E0>, <Element 'aspect' at 0x0373C210>, <Element 'aspect' at 0x0373C240>, <Element 'aspect' at 0x0373C9F0>, <Element 'aspect' at 0x0373CBA0>, <Element 'aspect' at 0x0373CBD0>, <Element 'aspect' at 0x03756060>, <Element 'aspect' at 0x03756990>, <Element 'aspect' at 0x03767E40>, <Element 'aspect' at 0x037749F0>, <Element 'aspect' at 0x03774A80>, <Element 'aspect' at 0x03774B10>, <Element 'aspect' at 0x03774B40>, <Element 'aspect' at 0x0377C900>, <Element 'aspect' at 0x0377CA80>, <Element 'aspect' at 0x0377CAB0>, <Element 'aspect' at 0x03782120>, <Element 'aspect' at 0x03782420>, <Element 'aspect' at 0x03782450>, <Element 'aspect' at 0x03782BA0>, <Element 'aspect' at 0x0378DAB0>, <Element 'aspect' at 0x0378DAE0>, <Element 'aspect' at 0x037AA750>, <Element 'aspect' at 0x037AA780>, <Element 'aspect' at 0x037B0660>, <Element 'aspect' at 0x037BA180>, <Element 'aspect' at 0x037C5EA0>, <Element 'aspect' at 0x037C5F30>, <Element 'aspect' at 0x037CB930>, <Element 'aspect' at 0x037CBF60>, <Element 'aspect' at 0x037CBF90>, <Element 'aspect' at 0x037D0360>, <Element 'aspect' at 0x037D9240>, <Element 'aspect' at 0x037DF270>, <Element 'aspect' at 0x037DF2A0>, <Element 'aspect' at 0x037DF330>, <Element 'aspect' at 0x037DFCC0>, <Element 'aspect' at 0x037DFCF0>, <Element 'aspect' at 0x03814870>, <Element 'aspect' at 0x03814EA0>, <Element 'aspect' at 0x03814F90>, <Element 'aspect' at 0x03827390>, <Element 'aspect' at 0x03827A80>, <Element 'aspect' at 0x0382C2A0>, <Element 'aspect' at 0x0382C2D0>, <Element 'aspect' at 0x0382C390>, <Element 'aspect' at 0x03836690>, <Element 'aspect' at 0x038366C0>, <Element 'aspect' at 0x03836FC0>, <Element 'aspect' at 0x0383D060>, <Element 'aspect' at 0x03842B70>, <Element 'aspect' at 0x03842BA0>, <Element 'aspect' at 0x03848390>, <Element 'aspect' at 0x038483C0>, <Element 'aspect' at 0x038484B0>, <Element 'aspect' at 0x038484E0>, <Element 'aspect' at 0x03848510>, <Element 'aspect' at 0x0385D840>, <Element 'aspect' at 0x03868C90>, <Element 'aspect' at 0x0386EAE0>, <Element 'aspect' at 0x0386EB10>]
>>> tree.findall('..//aspect[@category="Service"][@type="implicit"]')
[]
>>> tree.findall('.//aspect[@category="Service"][@type="implicit"]')
[<Element 'aspect' at 0x033B7270>, <Element 'aspect' at 0x033B72A0>, <Element 'aspect' at 0x033B7AB0>, <Element 'aspect' at 0x033B7AE0>, <Element 'aspect' at 0x033B7B40>, <Element 'aspect' at 0x033B7C00>, <Element 'aspect' at 0x033B7C90>, <Element 'aspect' at 0x033BF5A0>, <Element 'aspect' at 0x033BF6C0>, <Element 'aspect' at 0x0339A600>, <Element 'aspect' at 0x0339A540>, <Element 'aspect' at 0x033DB750>, <Element 'aspect' at 0x033DB7B0>, <Element 'aspect' at 0x033DB810>, <Element 'aspect' at 0x033E1300>, <Element 'aspect' at 0x033E19F0>, <Element 'aspect' at 0x033E6330>, <Element 'aspect' at 0x033E6390>, <Element 'aspect' at 0x033ED120>, <Element 'aspect' at 0x033ED1E0>, <Element 'aspect' at 0x033ED210>, <Element 'aspect' at 0x033ED9F0>, <Element 'aspect' at 0x033F3720>, <Element 'aspect' at 0x033FF3F0>, <Element 'aspect' at 0x033FF420>, <Element 'aspect' at 0x03406A80>, <Element 'aspect' at 0x03406C00>, <Element 'aspect' at 0x03406C30>, <Element 'aspect' at 0x0340BE10>, <Element 'aspect' at 0x03487E10>, <Element 'aspect' at 0x03490540>, <Element 'aspect' at 0x03490570>, <Element 'aspect' at 0x03497BA0>, <Element 'aspect' at 0x0349C4E0>, <Element 'aspect' at 0x034A2870>, <Element 'aspect' at 0x034A28A0>, <Element 'aspect' at 0x034A2960>, <Element 'aspect' at 0x034A8330>, <Element 'aspect' at 0x034A8360>, <Element 'aspect' at 0x034A83F0>, <Element 'aspect' at 0x034A87B0>, <Element 'aspect' at 0x034A87E0>, <Element 'aspect' at 0x034A8810>, <Element 'aspect' at 0x034A8F90>, <Element 'aspect' at 0x034B0870>, <Element 'aspect' at 0x034B41B0>, <Element 'aspect' at 0x0350F450>, <Element 'aspect' at 0x0350F480>, <Element 'aspect' at 0x03515060>, <Element 'aspect' at 0x035152A0>, <Element 'aspect' at 0x035152D0>, <Element 'aspect' at 0x035154B0>, <Element 'aspect' at 0x035154E0>, <Element 'aspect' at 0x03515DB0>, <Element 'aspect' at 0x03515ED0>, <Element 'aspect' at 0x03527D50>, <Element 'aspect' at 0x0352E8D0>, <Element 'aspect' at 0x0352E900>, <Element 'aspect' at 0x03532030>, <Element 'aspect' at 0x03532060>, <Element 'aspect' at 0x03532D80>, <Element 'aspect' at 0x03532DB0>, <Element 'aspect' at 0x03532F30>, <Element 'aspect' at 0x03539870>, <Element 'aspect' at 0x035398D0>, <Element 'aspect' at 0x035471E0>, <Element 'aspect' at 0x03547210>, <Element 'aspect' at 0x03547870>, <Element 'aspect' at 0x03561630>, <Element 'aspect' at 0x03561660>, <Element 'aspect' at 0x0356B210>, <Element 'aspect' at 0x03571F90>, <Element 'aspect' at 0x035856F0>, <Element 'aspect' at 0x03585720>, <Element 'aspect' at 0x03585FC0>, <Element 'aspect' at 0x03589990>, <Element 'aspect' at 0x0358F8A0>, <Element 'aspect' at 0x0358F900>, <Element 'aspect' at 0x0359AA50>, <Element 'aspect' at 0x03605450>, <Element 'aspect' at 0x03605D50>, <Element 'aspect' at 0x03605D80>, <Element 'aspect' at 0x0360B570>, <Element 'aspect' at 0x0360B660>, <Element 'aspect' at 0x0360B6F0>, <Element 'aspect' at 0x0360B750>, <Element 'aspect' at 0x03610AB0>, <Element 'aspect' at 0x03610B10>, <Element 'aspect' at 0x03616360>, <Element 'aspect' at 0x03616420>, <Element 'aspect' at 0x03616480>, <Element 'aspect' at 0x03616C00>, <Element 'aspect' at 0x03616C30>, <Element 'aspect' at 0x0361DE40>, <Element 'aspect' at 0x03622810>, <Element 'aspect' at 0x03622900>, <Element 'aspect' at 0x03626330>, <Element 'aspect' at 0x03626450>, <Element 'aspect' at 0x03626480>, <Element 'aspect' at 0x03626A80>, <Element 'aspect' at 0x0362D4B0>, <Element 'aspect' at 0x0362D4E0>, <Element 'aspect' at 0x036332D0>, <Element 'aspect' at 0x03633360>, <Element 'aspect' at 0x03633390>, <Element 'aspect' at 0x036333F0>, <Element 'aspect' at 0x03633450>, <Element 'aspect' at 0x03633C00>, <Element 'aspect' at 0x03633CC0>, <Element 'aspect' at 0x03633CF0>, <Element 'aspect' at 0x03633D50>, <Element 'aspect' at 0x03633DB0>, <Element 'aspect' at 0x036394B0>, <Element 'aspect' at 0x03639510>, <Element 'aspect' at 0x036396C0>, <Element 'aspect' at 0x03639750>, <Element 'aspect' at 0x03639870>, <Element 'aspect' at 0x036398D0>, <Element 'aspect' at 0x035BF090>, <Element 'aspect' at 0x035BF0C0>, <Element 'aspect' at 0x035BF120>, <Element 'aspect' at 0x035BF330>, <Element 'aspect' at 0x035BFC00>, <Element 'aspect' at 0x035BFDB0>, <Element 'aspect' at 0x035CB870>, <Element 'aspect' at 0x035CBD50>, <Element 'aspect' at 0x035D77E0>, <Element 'aspect' at 0x035D7ED0>, <Element 'aspect' at 0x035E87B0>, <Element 'aspect' at 0x035E8960>, <Element 'aspect' at 0x035ED570>, <Element 'aspect' at 0x035ED5A0>, <Element 'aspect' at 0x035EDDE0>, <Element 'aspect' at 0x035F9C90>, <Element 'aspect' at 0x0366A5A0>, <Element 'aspect' at 0x0366A930>, <Element 'aspect' at 0x03670210>, <Element 'aspect' at 0x03670990>, <Element 'aspect' at 0x036709C0>, <Element 'aspect' at 0x03676240>, <Element 'aspect' at 0x03676270>, <Element 'aspect' at 0x03676690>, <Element 'aspect' at 0x0367CD50>, <Element 'aspect' at 0x0367CDB0>, <Element 'aspect' at 0x0367CDE0>, <Element 'aspect' at 0x03682DE0>, <Element 'aspect' at 0x03688840>, <Element 'aspect' at 0x03688870>, <Element 'aspect' at 0x03688A50>, <Element 'aspect' at 0x0368DEA0>, <Element 'aspect' at 0x0369A3F0>, <Element 'aspect' at 0x0369ACC0>, <Element 'aspect' at 0x0369ACF0>, <Element 'aspect' at 0x0369AE40>, <Element 'aspect' at 0x036A1540>, <Element 'aspect' at 0x036A1BD0>, <Element 'aspect' at 0x03708D80>, <Element 'aspect' at 0x0371B900>, <Element 'aspect' at 0x03720180>, <Element 'aspect' at 0x03720240>, <Element 'aspect' at 0x0372BDE0>, <Element 'aspect' at 0x0372BE10>, <Element 'aspect' at 0x03731F90>, <Element 'aspect' at 0x037377E0>, <Element 'aspect' at 0x0373C210>, <Element 'aspect' at 0x0373C240>, <Element 'aspect' at 0x0373C9F0>, <Element 'aspect' at 0x0373CBA0>, <Element 'aspect' at 0x0373CBD0>, <Element 'aspect' at 0x03756060>, <Element 'aspect' at 0x03756990>, <Element 'aspect' at 0x03767E40>, <Element 'aspect' at 0x037749F0>, <Element 'aspect' at 0x03774A80>, <Element 'aspect' at 0x03774B10>, <Element 'aspect' at 0x03774B40>, <Element 'aspect' at 0x0377C900>, <Element 'aspect' at 0x0377CA80>, <Element 'aspect' at 0x0377CAB0>, <Element 'aspect' at 0x03782120>, <Element 'aspect' at 0x03782420>, <Element 'aspect' at 0x03782450>, <Element 'aspect' at 0x03782BA0>, <Element 'aspect' at 0x0378DAB0>, <Element 'aspect' at 0x0378DAE0>, <Element 'aspect' at 0x037AA750>, <Element 'aspect' at 0x037AA780>, <Element 'aspect' at 0x037B0660>, <Element 'aspect' at 0x037BA180>, <Element 'aspect' at 0x037C5EA0>, <Element 'aspect' at 0x037C5F30>, <Element 'aspect' at 0x037CB930>, <Element 'aspect' at 0x037CBF60>, <Element 'aspect' at 0x037CBF90>, <Element 'aspect' at 0x037D0360>, <Element 'aspect' at 0x037D9240>, <Element 'aspect' at 0x037DF270>, <Element 'aspect' at 0x037DF2A0>, <Element 'aspect' at 0x037DF330>, <Element 'aspect' at 0x037DFCC0>, <Element 'aspect' at 0x037DFCF0>, <Element 'aspect' at 0x03814870>, <Element 'aspect' at 0x03814EA0>, <Element 'aspect' at 0x03814F90>, <Element 'aspect' at 0x03827390>, <Element 'aspect' at 0x03827A80>, <Element 'aspect' at 0x0382C2A0>, <Element 'aspect' at 0x0382C2D0>, <Element 'aspect' at 0x0382C390>, <Element 'aspect' at 0x03836690>, <Element 'aspect' at 0x038366C0>, <Element 'aspect' at 0x03836FC0>, <Element 'aspect' at 0x0383D060>, <Element 'aspect' at 0x03842B70>, <Element 'aspect' at 0x03842BA0>, <Element 'aspect' at 0x03848390>, <Element 'aspect' at 0x038483C0>, <Element 'aspect' at 0x038484B0>, <Element 'aspect' at 0x038484E0>, <Element 'aspect' at 0x03848510>, <Element 'aspect' at 0x0385D840>, <Element 'aspect' at 0x03868C90>, <Element 'aspect' at 0x0386EAE0>, <Element 'aspect' at 0x0386EB10>]
>>> tree.findall('.//aspect[@category="Service"][@type="implicit"]/..')
[<Element 'aspects' at 0x033B2ED0>, <Element 'aspects' at 0x033B79F0>, <Element 'aspects' at 0x033BF360>, <Element 'aspects' at 0x0339A7E0>, <Element 'aspects' at 0x033DB450>, <Element 'aspects' at 0x033E10C0>, <Element 'aspects' at 0x033E1900>, <Element 'aspects' at 0x033E6150>, <Element 'aspects' at 0x033E6E40>, <Element 'aspects' at 0x033ED840>, <Element 'aspects' at 0x033F32D0>, <Element 'aspects' at 0x033FF2A0>, <Element 'aspects' at 0x034066F0>, <Element 'aspects' at 0x0340BCF0>, <Element 'aspects' at 0x03487BA0>, <Element 'aspects' at 0x03490030>, <Element 'aspects' at 0x03497690>, <Element 'aspects' at 0x0349C210>, <Element 'aspects' at 0x034A2540>, <Element 'aspects' at 0x034A2F90>, <Element 'aspects' at 0x034A8E10>, <Element 'aspects' at 0x034B0750>, <Element 'aspects' at 0x034B0F00>, <Element 'aspects' at 0x0350F330>, <Element 'aspects' at 0x0350FED0>, <Element 'aspects' at 0x03515A50>, <Element 'aspects' at 0x035279F0>, <Element 'aspects' at 0x0352E630>, <Element 'aspects' at 0x0352EF00>, <Element 'aspects' at 0x03532BD0>, <Element 'aspects' at 0x035396F0>, <Element 'aspects' at 0x03541C00>, <Element 'aspects' at 0x035477E0>, <Element 'aspects' at 0x03561360>, <Element 'aspects' at 0x03567F90>, <Element 'aspects' at 0x03571F60>, <Element 'aspects' at 0x03585660>, <Element 'aspects' at 0x03585ED0>, <Element 'aspects' at 0x035897B0>, <Element 'aspects' at 0x0358F750>, <Element 'aspects' at 0x0359A8D0>, <Element 'aspects' at 0x03605240>, <Element 'aspects' at 0x03605AE0>, <Element 'aspects' at 0x0360B360>, <Element 'aspects' at 0x036107B0>, <Element 'aspects' at 0x03616270>, <Element 'aspects' at 0x03616AE0>, <Element 'aspects' at 0x0361DAB0>, <Element 'aspects' at 0x03622570>, <Element 'aspects' at 0x03622EA0>, <Element 'aspects' at 0x036269C0>, <Element 'aspects' at 0x0362D390>, <Element 'aspects' at 0x0362DDB0>, <Element 'aspects' at 0x03633A80>, <Element 'aspects' at 0x03639420>, <Element 'aspects' at 0x03639FC0>, <Element 'aspects' at 0x035BF930>, <Element 'aspects' at 0x035CB6C0>, <Element 'aspects' at 0x035D75A0>, <Element 'aspects' at 0x035D7DE0>, <Element 'aspects' at 0x035E8780>, <Element 'aspects' at 0x035ED390>, <Element 'aspects' at 0x035EDC00>, <Element 'aspects' at 0x035F9930>, <Element 'aspects' at 0x0366A4B0>, <Element 'aspects' at 0x0366AF30>, <Element 'aspects' at 0x036708A0>, <Element 'aspects' at 0x03676180>, <Element 'aspects' at 0x0367C7E0>, <Element 'aspects' at 0x03682BD0>, <Element 'aspects' at 0x036887B0>, <Element 'aspects' at 0x0368DC90>, <Element 'aspects' at 0x0369A1E0>, <Element 'aspects' at 0x0369AB40>, <Element 'aspects' at 0x036A13F0>, <Element 'aspects' at 0x03708C90>, <Element 'aspects' at 0x0371B7E0>, <Element 'aspects' at 0x037200F0>, <Element 'aspects' at 0x0372BB70>, <Element 'aspects' at 0x03731D50>, <Element 'aspects' at 0x037376F0>, <Element 'aspects' at 0x0373C150>, <Element 'aspects' at 0x0373C810>, <Element 'aspects' at 0x03743BD0>, <Element 'aspects' at 0x03756900>, <Element 'aspects' at 0x03767900>, <Element 'aspects' at 0x03774960>, <Element 'aspects' at 0x0377C4B0>, <Element 'aspects' at 0x03782090>, <Element 'aspects' at 0x03782AE0>, <Element 'aspects' at 0x0378D9C0>, <Element 'aspects' at 0x037AA2A0>, <Element 'aspects' at 0x037B0570>, <Element 'aspects' at 0x037BA060>, <Element 'aspects' at 0x037C5C90>, <Element 'aspects' at 0x037CB690>, <Element 'aspects' at 0x037CBF30>, <Element 'aspects' at 0x037D9090>, <Element 'aspects' at 0x037DF1E0>, <Element 'aspects' at 0x037DFB40>, <Element 'aspects' at 0x038143C0>, <Element 'aspects' at 0x03814DB0>, <Element 'aspects' at 0x038271E0>, <Element 'aspects' at 0x038279F0>, <Element 'aspects' at 0x0382C240>, <Element 'aspects' at 0x038364E0>, <Element 'aspects' at 0x03836CC0>, <Element 'aspects' at 0x038427E0>, <Element 'aspects' at 0x03848180>, <Element 'aspects' at 0x0385D600>, <Element 'aspects' at 0x038689F0>, <Element 'aspects' at 0x0386E570>]
>>> tree.findall('.//aspect[@category="Service"][@type="implicit"]/../..')
[<Element 'review' at 0x033B2B70>, <Element 'review' at 0x033B7690>, <Element 'review' at 0x033B7F90>, <Element 'review' at 0x033BF8D0>, <Element 'review' at 0x033DB0F0>, <Element 'review' at 0x033DBD20>, <Element 'review' at 0x033E15A0>, <Element 'review' at 0x033E1DB0>, <Element 'review' at 0x033E6AE0>, <Element 'review' at 0x033ED4E0>, <Element 'review' at 0x033EDF30>, <Element 'review' at 0x033F9F00>, <Element 'review' at 0x03406390>, <Element 'review' at 0x0340B990>, <Element 'review' at 0x03487870>, <Element 'review' at 0x0348CC90>, <Element 'review' at 0x03497330>, <Element 'review' at 0x03497E70>, <Element 'review' at 0x034A21E0>, <Element 'review' at 0x034A2C30>, <Element 'review' at 0x034A8A80>, <Element 'review' at 0x034B03F0>, <Element 'review' at 0x034B0BA0>, <Element 'review' at 0x034B4F90>, <Element 'review' at 0x0350FB40>, <Element 'review' at 0x035156F0>, <Element 'review' at 0x03527690>, <Element 'review' at 0x0352E2D0>, <Element 'review' at 0x0352EBA0>, <Element 'review' at 0x03532870>, <Element 'review' at 0x03539390>, <Element 'review' at 0x035418A0>, <Element 'review' at 0x03547480>, <Element 'review' at 0x03547F90>, <Element 'review' at 0x03567C30>, <Element 'review' at 0x03571C00>, <Element 'review' at 0x03585300>, <Element 'review' at 0x03585B70>, <Element 'review' at 0x03589420>, <Element 'review' at 0x0358F3F0>, <Element 'review' at 0x0359A570>, <Element 'review' at 0x0359AEA0>, <Element 'review' at 0x03605780>, <Element 'review' at 0x03605FC0>, <Element 'review' at 0x03610450>, <Element 'review' at 0x03610ED0>, <Element 'review' at 0x03616780>, <Element 'review' at 0x0361D720>, <Element 'review' at 0x03622210>, <Element 'review' at 0x03622B40>, <Element 'review' at 0x03626660>, <Element 'review' at 0x0362D030>, <Element 'review' at 0x0362DA50>, <Element 'review' at 0x03633720>, <Element 'review' at 0x036390C0>, <Element 'review' at 0x03639C60>, <Element 'review' at 0x035BF5D0>, <Element 'review' at 0x035CB360>, <Element 'review' at 0x035D7240>, <Element 'review' at 0x035D7A80>, <Element 'review' at 0x035E8420>, <Element 'review' at 0x035E8F90>, <Element 'review' at 0x035ED870>, <Element 'review' at 0x035F95D0>, <Element 'review' at 0x0366A150>, <Element 'review' at 0x0366ABD0>, <Element 'review' at 0x03670510>, <Element 'review' at 0x03670DE0>, <Element 'review' at 0x0367C480>, <Element 'review' at 0x03682870>, <Element 'review' at 0x03688450>, <Element 'review' at 0x0368D930>, <Element 'review' at 0x03694E10>, <Element 'review' at 0x0369A7E0>, <Element 'review' at 0x036A1090>, <Element 'review' at 0x03708930>, <Element 'review' at 0x0371B480>, <Element 'review' at 0x0371BD50>, <Element 'review' at 0x0372B810>, <Element 'review' at 0x037319F0>, <Element 'review' at 0x03737390>, <Element 'review' at 0x03737DB0>, <Element 'review' at 0x0373C4B0>, <Element 'review' at 0x03743870>, <Element 'review' at 0x037565A0>, <Element 'review' at 0x03767570>, <Element 'review' at 0x037745D0>, <Element 'review' at 0x0377C150>, <Element 'review' at 0x0377CCF0>, <Element 'review' at 0x03782780>, <Element 'review' at 0x0378D660>, <Element 'review' at 0x0378DF00>, <Element 'review' at 0x037B0210>, <Element 'review' at 0x037B5CC0>, <Element 'review' at 0x037C5930>, <Element 'review' at 0x037CB330>, <Element 'review' at 0x037CBBD0>, <Element 'review' at 0x037D6CC0>, <Element 'review' at 0x037D9E40>, <Element 'review' at 0x037DF7E0>, <Element 'review' at 0x03814060>, <Element 'review' at 0x03814A50>, <Element 'review' at 0x03821E40>, <Element 'review' at 0x03827690>, <Element 'review' at 0x03827EA0>, <Element 'review' at 0x03836180>, <Element 'review' at 0x03836960>, <Element 'review' at 0x03842480>, <Element 'review' at 0x03842DE0>, <Element 'review' at 0x0385D2A0>, <Element 'review' at 0x03868690>, <Element 'review' at 0x0386E1E0>]
>>> tree.findall('.//aspect[@category="Service"][@type="implicit"]/../../text')
[<Element 'text' at 0x033B2E70>, <Element 'text' at 0x033B7990>, <Element 'text' at 0x033BF300>, <Element 'text' at 0x033BFC30>, <Element 'text' at 0x033DB3F0>, <Element 'text' at 0x033E1060>, <Element 'text' at 0x033E18A0>, <Element 'text' at 0x033E60F0>, <Element 'text' at 0x033E6DE0>, <Element 'text' at 0x033ED7E0>, <Element 'text' at 0x033F3270>, <Element 'text' at 0x033FF240>, <Element 'text' at 0x03406690>, <Element 'text' at 0x0340BC90>, <Element 'text' at 0x03487B40>, <Element 'text' at 0x0348CF90>, <Element 'text' at 0x03497630>, <Element 'text' at 0x0349C1B0>, <Element 'text' at 0x034A24E0>, <Element 'text' at 0x034A2F30>, <Element 'text' at 0x034A8DB0>, <Element 'text' at 0x034B06F0>, <Element 'text' at 0x034B0EA0>, <Element 'text' at 0x0350F2D0>, <Element 'text' at 0x0350FE70>, <Element 'text' at 0x035159F0>, <Element 'text' at 0x03527990>, <Element 'text' at 0x0352E5D0>, <Element 'text' at 0x0352EEA0>, <Element 'text' at 0x03532B70>, <Element 'text' at 0x03539690>, <Element 'text' at 0x03541BA0>, <Element 'text' at 0x03547780>, <Element 'text' at 0x03561300>, <Element 'text' at 0x03567F30>, <Element 'text' at 0x03571F00>, <Element 'text' at 0x03585600>, <Element 'text' at 0x03585E70>, <Element 'text' at 0x03589750>, <Element 'text' at 0x0358F6F0>, <Element 'text' at 0x0359A870>, <Element 'text' at 0x036051E0>, <Element 'text' at 0x03605A80>, <Element 'text' at 0x0360B300>, <Element 'text' at 0x03610750>, <Element 'text' at 0x03616210>, <Element 'text' at 0x03616A80>, <Element 'text' at 0x0361DA50>, <Element 'text' at 0x03622510>, <Element 'text' at 0x03622E40>, <Element 'text' at 0x03626960>, <Element 'text' at 0x0362D330>, <Element 'text' at 0x0362DD50>, <Element 'text' at 0x03633A20>, <Element 'text' at 0x036393C0>, <Element 'text' at 0x03639F60>, <Element 'text' at 0x035BF8D0>, <Element 'text' at 0x035CB660>, <Element 'text' at 0x035D7540>, <Element 'text' at 0x035D7D80>, <Element 'text' at 0x035E8720>, <Element 'text' at 0x035ED330>, <Element 'text' at 0x035EDBA0>, <Element 'text' at 0x035F98D0>, <Element 'text' at 0x0366A450>, <Element 'text' at 0x0366AED0>, <Element 'text' at 0x03670840>, <Element 'text' at 0x03676120>, <Element 'text' at 0x0367C780>, <Element 'text' at 0x03682B70>, <Element 'text' at 0x03688750>, <Element 'text' at 0x0368DC30>, <Element 'text' at 0x0369A150>, <Element 'text' at 0x0369AAE0>, <Element 'text' at 0x036A1390>, <Element 'text' at 0x03708C30>, <Element 'text' at 0x0371B780>, <Element 'text' at 0x03720090>, <Element 'text' at 0x0372BB10>, <Element 'text' at 0x03731CF0>, <Element 'text' at 0x03737690>, <Element 'text' at 0x0373C0F0>, <Element 'text' at 0x0373C7B0>, <Element 'text' at 0x03743B70>, <Element 'text' at 0x037568A0>, <Element 'text' at 0x03767870>, <Element 'text' at 0x03774900>, <Element 'text' at 0x0377C450>, <Element 'text' at 0x03782030>, <Element 'text' at 0x03782A80>, <Element 'text' at 0x0378D960>, <Element 'text' at 0x037AA240>, <Element 'text' at 0x037B0510>, <Element 'text' at 0x037B5FC0>, <Element 'text' at 0x037C5C30>, <Element 'text' at 0x037CB630>, <Element 'text' at 0x037CBED0>, <Element 'text' at 0x037D9030>, <Element 'text' at 0x037DF180>, <Element 'text' at 0x037DFAE0>, <Element 'text' at 0x03814360>, <Element 'text' at 0x03814D50>, <Element 'text' at 0x03827180>, <Element 'text' at 0x03827990>, <Element 'text' at 0x0382C1E0>, <Element 'text' at 0x03836480>, <Element 'text' at 0x03836C60>, <Element 'text' at 0x03842780>, <Element 'text' at 0x03848120>, <Element 'text' at 0x0385D5A0>, <Element 'text' at 0x03868990>, <Element 'text' at 0x0386E510>]
>>> result = tree.findall('.//aspect[@category="Service"][@type="implicit"]/../../text')
>>> type(result)
<class 'list'>
>>> result[0]
<Element 'text' at 0x033B2E70>
>>> result[0].text
'Для встречи с друзьями было выбрано данное заведение в основном благодаря отзывам. Ну во-первых, хочется отметить одно маленькое разочарование, которое меня охватило сразу же: интерьер. Я действительно ожидала увидеть нечто большее. Не буду нудно расписывать что и как не так. Просто осталось чувство, что столь интересную задумку gangster bar-а не до конца смогли реализовать. Черно-белые плакаты, кирпичные стены... Во-вторых: Встреча гостей в ресторане- отсутствовала, мы стояли ждали...оглядывались, пару официантов делали свои дела... Не дождавшись хоть какого-то внимания в наш адрес, подошли к ближайшей девушке-официанту, и попросили посадить нас за столик, заказанный ранее. Провели. Усадили. Дальше было лучше. Заказ принимали быстро, еду приносили тоже достаточно быстро, убирали пустые тарелки, бокалы вовремя. Сама еда-названия соответствуют выбранному стилю заведения. Хотя на деле, ничего особенного и не предлагают. Персонал улыбчивый, приветливый. Сырная тарелка оставляет желать лучшего-для любителей сыра ее ну просто ОЧЕНЬ мало:) Салат цезарь-тарелка капусты, и три тонюсеньких (0,3см) ломтика курицы, сухарики, соус. Из блюд больше ничего нареканий не вызвало. В итоге, хочу сделать вывод: соотношение цена-качество выдержано. Отличное место для большой компании.'
>>> for elem in tree.findall('.//aspect[@category="Service"][@type="implicit"]/../../text'):
	print elem.text[:50]
	
SyntaxError: invalid syntax
>>> for elem in tree.findall('.//aspect[@category="Service"][@type="implicit"]/../../text'):
	print(elem.text[:50])

	
Для встречи с друзьями было выбрано данное заведен
Хочу поделиться своим впечатлением от посещения ре
Добрый день! Были вчера с друзьями в этом кафе! Оч
Отметили с мужем годовщину свадьбы 6 ноября в этом
Впервые побывала в этом пабе совсем недавно и могу
Ребята, вы - лучшие! Недавно были небольшой дружно
Зашла в ресторан первое впечатление отличное, но п
Мы посетили этот замечательный ресторанчик поздним
Были вчера компанией 6 человек в "Суп-вино". Столи
В прошлую субботу посетили с друзьями это заведени
Добрый день! Мы с молодым человеком любим открыват
Была в этом заведении 10.09.2008, заехали с мужем 
Буквально на днях отмечали с мужем наш небольшой ю
В эту субботу решили с друзьями куда ни будь сходи
Были в этом заведении впервые, компанией из 4-х че
Привет. Отмечала в этом ресторане свой День Рожден
Сегодня обедали в Фартуке вдвоем с мужем. На сайте
Добрый день, Праздновали День Рождение в середине 
Здравствуйте! 12.08.2014 мы отмечали нашу свадьбу 
Отмечали свадьбу 15 марта. Ах-Ах!!! Замечательный 
Добрый день! Первый раз пишу отзыв о ресторане, на
Прекрасный ресторан! Уютная обстановка и атмосфера
Праздновали день рождения,все понравилось, удалось
Добрый день! Недавно праздновали свадьбу в банкетн
Никогда серьезно не относился к данному заведению,
Н Начну из далека)) года 1,5-2 назад заходила в "д
Сегодня мы всей семьей посетили ресторан Марчеллис
Добрый день! Ходил с девушкой 22.12- ей очень понр
Отличное заведение! Посещаю эту место с самого отк
Праздновали свадьбу в этом ресторане 7 августа 201
В один из недавних, совсем не по-весеннему холодны
Вы помните мультик про мышонка повара, живущего в 
Решил отметить в этом заведении свой ДР в компании
Субботним вечером зашли компанией в кафе Dolce Ita
Нам понравилось абсолютно все!!!Очень хороший рест
Давно здесь не был, хотя близко от меня. На мой вз
Были на мой день рождения в этом ресторане! Мне вс
Заезжали поужинать с подругой пару недель назад. С
Являюсь постоянным гостем данного кафе. Недавно в 
17 июня отмечали в Санторини свадьбу - обслуживани
Посетили данное заведение по случаю юбилея моего п
Хочу оставить свой отзыв об этом замечательном каф
Несколько раз посещали с друзьями данный ресторан!
мы посетили ресторан 10 марта. впечатления осталис
Праздновали свадьбу в этом ресторане! Свадьба была
Были в этом ресторане в апреле месяце. Остались хо
Была в этом ресторане только однажды, но с удоволь
Зашли в ресторан в выходной день случайно. Посовет
06.09.2013 были на ужине в ресторане Пури. Выбирал
Всем добрый день! Вчера отдыхали с компанией 9 чел
При входе в ресторан вас встречают необычный интер
Вчера отмечали юбилей, очередную годовщину нашей с
Мы отмечали 19.04 свадьбу в этом ресторане, гостей
Первый раз посетили с друзьями этот уютный рестора
Первое посещение Дачи было в рамках поиска рестора
Бывала раньше в этом заведении и всегда замечала,ч
Были 1 февраля. Я второй раз, подруга - первый. Пр
Был в ресторане пару недель назад с девушкой. Обст
Здравствуйте, Я отмечала свой день рожденья в этом
Были с мужем в выходные. Очень много народу, но ст
Вывод напишу сразу: дружелюбно, вкусно и приятно. 
Примерно месяц назад посетили это заведение, т. к.
Всем хорошего дня! 9 августа у нас с мужем был 10т
Выбрали это место для начала празднования с коллек
Я редко пишу отрицательные отзывы, но в данном слу
Очень долго выбирали ресторан на Новогодний карпор
Недавно отмечали в Санам день рождения. Безумно по
Были уже не один раз, нравится! Приятное и очень у
Ходили с молодым человеком в пятницу, 25 ноября. К
После прогулки решили с подругой зайти-перекусить,
Сегодня с подругой посетил данное заведение! очень
Я недавно переехала в Пушкин.Абсолютно не было вре
Сегодня отмечали день рождения небольшой компанией
Замечательный ресторан, ходили туда уже два раза, 
Встретились с подругами пообщаться, выпить пива. С
Да, это что-то, даже не могу сказать как, но поста
31 июля отмечали нашу свадьбу в ресторане Анданте.
Посетил данный ресторан в начале сентября в компан
Ходим в этот ресторанчик не так часто, только когд
из всех посещенных мной ресторанов китайской кухни
Очень хочется поделится своим мнением! Мы с друзья
Почитал отзывы на этом сайте и решил посетить заве
Мы пришли с мужем в "Небо" приблизительно в 19:00 
Отличное место, с отличной кухней. Читал много отз
Удивлена наличием негативных отзывов о данном заве
Посетили этот ресторан 25,08,12. После посещения ж
На прошлой недели удалось таки сходить в этот рест
Первый раз зашла случайно, хотелось кофе попить...
Были в этом ресторане два раза. В первый раз работ
Вчера впервые побывали у вас на Комендантском 2. О
Хороший ресторан с неплохим обслуживанием. Были в 
До недавнего времени регулярно с коллегами посещал
Кухня супер, спасибо поварам, интерьер приятный, х
Ужасный персонал на Невском пр-те 22, особенно есл
Заходили в субботу в 5 вечера в начале декабря. Ра
Мой молодой человек как-то заказывал столик на 8 м
Недавно с подругой ужинали у Вас. Давно смотрели п
Отмечали день рождения, компанией из 8 человек. В 
Отмечали свадьбу друга. Приехали вечером, шел дожд
Хороший свежий ресторан, обслуживание понравилось,
Все не собраться было написать отзыв об этом прекр
Бронировали столик в прошлые выходные (30.08.14), 
Здравствуйте! 23.12.2013г.Провели корпоратив в рес
На днях я таки посетила Террасу, в которой не была
Были сегодня первый раз! Все очень понравилось. И 
Юбилей это тот повод, когда хочется собраться толь
Вчера были в ресторане "Небо", что могу сказать, р
Иногда захожу в это местечко выпить пива с друзьям
Семейное торжество отмечали в Амадеусе 30 мая . На
Готовясь идти с любимой в этот ресторан, что бы вс
Не так давно были в Жан-Жаке с подругой, вот решил
Была пару раз в пабе, очень понравилось. Вкусное п
>>> for elem in tree.findall('.//aspect[@category="Service"][@type="implicit"]/../../text'):
	print(elem.text[:50])

	
Для встречи с друзьями было выбрано данное заведен
Хочу поделиться своим впечатлением от посещения ре
Добрый день! Были вчера с друзьями в этом кафе! Оч
Отметили с мужем годовщину свадьбы 6 ноября в этом
Впервые побывала в этом пабе совсем недавно и могу
Ребята, вы - лучшие! Недавно были небольшой дружно
Зашла в ресторан первое впечатление отличное, но п
Мы посетили этот замечательный ресторанчик поздним
Были вчера компанией 6 человек в "Суп-вино". Столи
В прошлую субботу посетили с друзьями это заведени
Добрый день! Мы с молодым человеком любим открыват
Была в этом заведении 10.09.2008, заехали с мужем 
Буквально на днях отмечали с мужем наш небольшой ю
В эту субботу решили с друзьями куда ни будь сходи
Были в этом заведении впервые, компанией из 4-х че
Привет. Отмечала в этом ресторане свой День Рожден
Сегодня обедали в Фартуке вдвоем с мужем. На сайте
Добрый день, Праздновали День Рождение в середине 
Здравствуйте! 12.08.2014 мы отмечали нашу свадьбу 
Отмечали свадьбу 15 марта. Ах-Ах!!! Замечательный 
Добрый день! Первый раз пишу отзыв о ресторане, на
Прекрасный ресторан! Уютная обстановка и атмосфера
Праздновали день рождения,все понравилось, удалось
Добрый день! Недавно праздновали свадьбу в банкетн
Никогда серьезно не относился к данному заведению,
Н Начну из далека)) года 1,5-2 назад заходила в "д
Сегодня мы всей семьей посетили ресторан Марчеллис
Добрый день! Ходил с девушкой 22.12- ей очень понр
Отличное заведение! Посещаю эту место с самого отк
Праздновали свадьбу в этом ресторане 7 августа 201
В один из недавних, совсем не по-весеннему холодны
Вы помните мультик про мышонка повара, живущего в 
Решил отметить в этом заведении свой ДР в компании
Субботним вечером зашли компанией в кафе Dolce Ita
Нам понравилось абсолютно все!!!Очень хороший рест
Давно здесь не был, хотя близко от меня. На мой вз
Были на мой день рождения в этом ресторане! Мне вс
Заезжали поужинать с подругой пару недель назад. С
Являюсь постоянным гостем данного кафе. Недавно в 
17 июня отмечали в Санторини свадьбу - обслуживани
Посетили данное заведение по случаю юбилея моего п
Хочу оставить свой отзыв об этом замечательном каф
Несколько раз посещали с друзьями данный ресторан!
мы посетили ресторан 10 марта. впечатления осталис
Праздновали свадьбу в этом ресторане! Свадьба была
Были в этом ресторане в апреле месяце. Остались хо
Была в этом ресторане только однажды, но с удоволь
Зашли в ресторан в выходной день случайно. Посовет
06.09.2013 были на ужине в ресторане Пури. Выбирал
Всем добрый день! Вчера отдыхали с компанией 9 чел
При входе в ресторан вас встречают необычный интер
Вчера отмечали юбилей, очередную годовщину нашей с
Мы отмечали 19.04 свадьбу в этом ресторане, гостей
Первый раз посетили с друзьями этот уютный рестора
Первое посещение Дачи было в рамках поиска рестора
Бывала раньше в этом заведении и всегда замечала,ч
Были 1 февраля. Я второй раз, подруга - первый. Пр
Был в ресторане пару недель назад с девушкой. Обст
Здравствуйте, Я отмечала свой день рожденья в этом
Были с мужем в выходные. Очень много народу, но ст
Вывод напишу сразу: дружелюбно, вкусно и приятно. 
Примерно месяц назад посетили это заведение, т. к.
Всем хорошего дня! 9 августа у нас с мужем был 10т
Выбрали это место для начала празднования с коллек
Я редко пишу отрицательные отзывы, но в данном слу
Очень долго выбирали ресторан на Новогодний карпор
Недавно отмечали в Санам день рождения. Безумно по
Были уже не один раз, нравится! Приятное и очень у
Ходили с молодым человеком в пятницу, 25 ноября. К
После прогулки решили с подругой зайти-перекусить,
Сегодня с подругой посетил данное заведение! очень
Я недавно переехала в Пушкин.Абсолютно не было вре
Сегодня отмечали день рождения небольшой компанией
Замечательный ресторан, ходили туда уже два раза, 
Встретились с подругами пообщаться, выпить пива. С
Да, это что-то, даже не могу сказать как, но поста
31 июля отмечали нашу свадьбу в ресторане Анданте.
Посетил данный ресторан в начале сентября в компан
Ходим в этот ресторанчик не так часто, только когд
из всех посещенных мной ресторанов китайской кухни
Очень хочется поделится своим мнением! Мы с друзья
Почитал отзывы на этом сайте и решил посетить заве
Мы пришли с мужем в "Небо" приблизительно в 19:00 
Отличное место, с отличной кухней. Читал много отз
Удивлена наличием негативных отзывов о данном заве
Посетили этот ресторан 25,08,12. После посещения ж
На прошлой недели удалось таки сходить в этот рест
Первый раз зашла случайно, хотелось кофе попить...
Были в этом ресторане два раза. В первый раз работ
Вчера впервые побывали у вас на Комендантском 2. О
Хороший ресторан с неплохим обслуживанием. Были в 
До недавнего времени регулярно с коллегами посещал
Кухня супер, спасибо поварам, интерьер приятный, х
Ужасный персонал на Невском пр-те 22, особенно есл
Заходили в субботу в 5 вечера в начале декабря. Ра
Мой молодой человек как-то заказывал столик на 8 м
Недавно с подругой ужинали у Вас. Давно смотрели п
Отмечали день рождения, компанией из 8 человек. В 
Отмечали свадьбу друга. Приехали вечером, шел дожд
Хороший свежий ресторан, обслуживание понравилось,
Все не собраться было написать отзыв об этом прекр
Бронировали столик в прошлые выходные (30.08.14), 
Здравствуйте! 23.12.2013г.Провели корпоратив в рес
На днях я таки посетила Террасу, в которой не была
Были сегодня первый раз! Все очень понравилось. И 
Юбилей это тот повод, когда хочется собраться толь
Вчера были в ресторане "Небо", что могу сказать, р
Иногда захожу в это местечко выпить пива с друзьям
Семейное торжество отмечали в Амадеусе 30 мая . На
Готовясь идти с любимой в этот ресторан, что бы вс
Не так давно были в Жан-Жаке с подругой, вот решил
Была пару раз в пабе, очень понравилось. Вкусное п
>>> for review in tree.findall('.//review'):
	print(review.text[:50])

	

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                

                
>>> for review in tree.findall('.//review'):
	print(''.join(review.itertext())[:50])

	

                
                        13 маршр

                
                        Веселый 

                
                        Моб Джой

                
                        Крапива


                
                        Советско

                
                        Дитай
  

                
                        ПАБ № 1


                
                        Сытинъ
 

                
                        Люмьер
 

                
                        Квартира

                
                        Суп Вино

                
                        Пенабар


                
                        Парк Джу

                
                        Одеяло
 

                
                        Хан Гун


                
                        Фёст оф 

                
                        Семейный

                
                        MACARENA

                
                        Кошкин д

                
                        Amsterda

                
                        Лоза
   

                
                        Гости
  

                
                        Day & Ni

                
                        Царский 

                
                        Буль-вар

                
                        Общество

                
                        Марчелли

                
                        Свельто


                
                        Лесная Р

                
                        Фартук
 

                
                        Кэт
    

                
                        Набережн

                
                        Фаворит


                
                        Repin Lo

                
                        Омлет
  

                
                        Панорама

                
                        Первое, 

                
                        Улица ра

                
                        Кабинет-

                
                        Город
  

                
                        Дали
   

                
                        Мама Ром

                
                        Аппетит


                
                        Соль ФаС

                
                        Гоголь
 

                
                        Марчелли

                
                        DachA
  

                
                        Roll & R

                
                        У Горчак

                
                        Amarena


                
                        Радио Ир

                
                        Серафино

                
                        Глобусба

                
                        Итали
  

                
                        Моджо
  

                
                        El'Grang

                
                        Ани
    

                
                        Scalini


                
                        Диана
  

                
                        Две пало

                
                        Тбилисо


                
                        Нагасаки

                
                        Дитай
  

                
                        Bona Cap

                
                        Бричмула

                
                        Мосты
  

                
                        Жюль Вер

                
                        Санторин

                
                        Беллини


                
                        Достоевс

                
                        Buddha B

                
                        Бали
   

                
                        Выборг
 

                
                        Квадрат


                
                        Паулайне

                
                        Баррель


                
                        Via Dell

                
                        Толстый 

                
                        Буль-вар

                
                        Буль-вар

                
                        Мама Ром

                
                        Пури
   

                
                        Моцарелл

                
                        Валхалл


                
                        Аджабсан

                
                        Bravo-La

                
                        Градъ Пе

                
                        DachA
  

                
                        Длинный 

                
                        Кастом
 

                
                        Чаплин H

                
                        Таверна 

                
                        Джун Го


                
                        Моб Джой

                
                        Глори Па

                
                        Старый П

                
                        Карл и Ф

                
                        Roll & R

                
                        Полента


                
                        Невский,

                
                        Е.Д.А. и

                
                        Тепло
  

                
                        Tiramisu

                
                        Олива
  

                
                        Наследие

                
                        22.13
  

                
                        Билл-Хук

                
                        Кон-Коро

                
                        Санам
  

                
                        Munhell


                
                        MACARENA

                
                        Roll & R

                
                        Мидзуки


                
                        Da Alber

                
                        Арт фонд

                
                        Гроссенш

                
                        Белый Кр

                
                        Sardina


                
                        Карелия


                
                        Пекорино

                
                        Фогги Дь

                
                        Дуглас
 

                
                        Культ. Л

                
                        Любимый


                
                        Про-суши

                
                        Длинный 

                
                        Анданте


                
                        Ti Amo
 

                
                        Манилов


                
                        Tefsi
  

                
                        Палермо


                
                        Roll & R

                
                        Буратино

                
                        Тан Жен


                
                        Гостиная

                
                        Пиросман

                
                        Небо
   

                
                        Карл и Ф

                
                        Старый Б

                
                        Спорт Па

                
                        Ресттаун

                
                        Чаплин-Х

                
                        Apteka
 

                
                        Омар Хай

                
                        Марчелли

                
                        Мамалыга

                
                        Кафе Ита

                
                        Ферма
  

                
                        Штрудель

                
                        Sardina


                
                        Bona Cap

                
                        Самса
  

                
                        MASSIMO 

                
                        Оттолина

                
                        Гренадер

                
                        Плюшкин


                
                        Тан Жен


                
                        13 маршр

                
                        Сабантуй

                
                        Две пало

                
                        Шабу-Шаб

                
                        Хутор Во

                
                        Да Винчи

                
                        Траттори

                
                        Фартук
 

                
                        Фиделио


                
                        Рыба - Р

                
                        Волна
  

                
                        Мисо
   

                
                        Атриум
 

                
                        Корчма
 

                
                        VinoGrad

                
                        Лисья но

                
                        0,75
   

                
                        Penabar


                
                        Баден-Ба

                
                        Сытинъ
 

                
                        Meat Lin

                
                        Кирочный

                
                        Bongiorn

                
                        Солнечна

                
                        Le Glamo

                
                        Терраса


                
                        Молли О'

                
                        Duplex
 

                
                        Georgia 

                
                        Паберти


                
                        Mon Peti

                
                        Небо
   

                
                        Санторин

                
                        Bravo-La

                
                        Ягер Хау

                
                        Амадеус


                
                        Ля Багет

                
                        Джун Го


                
                        Муви паб

                
                        Качели
 

                
                        Бегемот


                
                        Жан-Жак 

                
                        Dickens 

                
                        Паулайне
>>> for review in tree.findall('.//review'):
	print(review.keys())

	
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
['id']
>>> for review in tree.findall('.//review'):
	if review.findall('*') != []:
		pass

	
>>> for review in tree.findall('.//review'):
	if review.findall('.//aspect[@sentiment="positive"][@type="implicit"]') != []:
		print(review.findall('.//text')[0].text[:50])

		
День 8-го марта прошёл, можно и итоги подвести. Ре
Отмечали в этом ресторане день рождение на первом 
Для встречи с друзьями было выбрано данное заведен
Хочу поделиться своим впечатлением от посещения ре
Добрый день! Были вчера с друзьями в этом кафе! Оч
Отметили с мужем годовщину свадьбы 6 ноября в этом
Впервые побывала в этом пабе совсем недавно и могу
Ребята, вы - лучшие! Недавно были небольшой дружно
Зашла в ресторан первое впечатление отличное, но п
Мы посетили этот замечательный ресторанчик поздним
Были вчера компанией 6 человек в "Суп-вино". Столи
В прошлую субботу посетили с друзьями это заведени
Добрый день! Мы с молодым человеком любим открыват
Добрый вечер! Начну сразу, мне ужасно не понравило
Добрый день! Недавно (22 ноября) посещали этот рес
Была в этом заведении 10.09.2008, заехали с мужем 
Буквально на днях отмечали с мужем наш небольшой ю
В эту субботу решили с друзьями куда ни будь сходи
Отличное кафе!!!! Отмечала в нем свой день рождени
В эти выходные отмечала день рождения в этом ресто
На днях, в командировку, приезжали коллеги по рабо
Не могу не рассказать, как прошел банкет на мою св
Были в этом заведении впервые, компанией из 4-х че
была там последний раз где то месяц назад в часа 4
Привет. Отмечала в этом ресторане свой День Рожден
Мы проводили торжество в марте 2014 года в рестора
Сегодня обедали в Фартуке вдвоем с мужем. На сайте
Добрый день, Праздновали День Рождение в середине 
Очень просторно и светло, интерьер в моем любимом 
Здравствуйте! 12.08.2014 мы отмечали нашу свадьбу 
Отмечали свадьбу 15 марта. Ах-Ах!!! Замечательный 
Добрый день! Первый раз пишу отзыв о ресторане, на
Прекрасный ресторан! Уютная обстановка и атмосфера
Праздновали день рождения,все понравилось, удалось
Последний раз был в этом ресторане несколько лет н
Добрый день! Недавно праздновали свадьбу в банкетн
Никогда серьезно не относился к данному заведению,
Н Начну из далека)) года 1,5-2 назад заходила в "д
Была в трёх разных ресторанах Мама Рома. Кухня рад
Зашли в"аппетит" случайно.Не смотря на то,что был 
Один из моих любимых ресторанов. С самого открытия
Отмечали в этом ресторане день рождение в субботу 
Сегодня мы всей семьей посетили ресторан Марчеллис
Добрый день! Ходил с девушкой 22.12- ей очень понр
Отличное заведение! Посещаю эту место с самого отк
Праздновали свадьбу в этом ресторане 7 августа 201
В один из недавних, совсем не по-весеннему холодны
Никогда не писал отзывы, но тут - просто обязан! И
Вы помните мультик про мышонка повара, живущего в 
Решил отметить в этом заведении свой ДР в компании
Субботним вечером зашли компанией в кафе Dolce Ita
На 2ом этаже была раза два. Красивый интерьер - си
Нам понравилось абсолютно все!!!Очень хороший рест
Мы были в этом ресторане 2 раза. Обслуживанием оче
Небольшой и уютный ресторан. При входе нас встрети
Давно здесь не был, хотя близко от меня. На мой вз
Ресторан очень хороший!!! С ним у меня связано оче
Являемся постоянными посетителями данного заведени
Давно хотела посетить этот ресторан, т.к. очень лю
Были на мой день рождения в этом ресторане! Мне вс
Заезжали поужинать с подругой пару недель назад. С
Являюсь постоянным гостем данного кафе. Недавно в 
17 июня отмечали в Санторини свадьбу - обслуживани
Привет всем!Мы из Москвы,посетили на выходные Пите
Красиво. Вкусно. Обслуживание "на уровне". Вот на 
Посетили данное заведение по случаю юбилея моего п
Хочу оставить свой отзыв об этом замечательном каф
Несколько раз посещали с друзьями данный ресторан!
мы посетили ресторан 10 марта. впечатления осталис
Впервые посетила это замечательное место! С первых
Праздновали свадьбу в этом ресторане! Свадьба была
Были в этом ресторане в апреле месяце. Остались хо
Была в этом ресторане только однажды, но с удоволь
Зашли в ресторан в выходной день случайно. Посовет
06.09.2013 были на ужине в ресторане Пури. Выбирал
Всем добрый день! Вчера отдыхали с компанией 9 чел
При входе в ресторан вас встречают необычный интер
Вчера отмечали юбилей, очередную годовщину нашей с
Мы отмечали 19.04 свадьбу в этом ресторане, гостей
Первый раз посетили с друзьями этот уютный рестора
Первое посещение Дачи было в рамках поиска рестора
Бывала раньше в этом заведении и всегда замечала,ч
Были 1 февраля. Я второй раз, подруга - первый. Пр
Приятное заведение. Действительно много места, как
Был в ресторане пару недель назад с девушкой. Обст
Отличный паб!!!!!! Я решила устроить мужу сюрприз,
Здравствуйте, Я отмечала свой день рожденья в этом
Всем доброго дня! Зашел посмотреть телефон заведен
Сегодня случайно попали в этот ресторан. В общем п
Я была здесь с подругой пока один раз. Пришли вече
Вывод напишу сразу: дружелюбно, вкусно и приятно. 
Примерно месяц назад посетили это заведение, т. к.
Всем хорошего дня! 9 августа у нас с мужем был 10т
Недавно посетила данный ресторан,я согласна со мно
Выбрали это место для начала празднования с коллек
Я редко пишу отрицательные отзывы, но в данном слу
Очень долго выбирали ресторан на Новогодний карпор
Недавно отмечали в Санам день рождения. Безумно по
Были уже не один раз, нравится! Приятное и очень у
Праздновала в этом ресторане свой Др, праздник был
Ходили с молодым человеком в пятницу, 25 ноября. К
На день рождения моей девушки, мы решили сходить в
После прогулки решили с подругой зайти-перекусить,
Сегодня с подругой посетил данное заведение! очень
В пятницу 8 числа с друзьями проходили мимо рестор
Я недавно переехала в Пушкин.Абсолютно не было вре
Приятный итальянский ресторанчик без претензий. Из
Сегодня отмечали день рождения небольшой компанией
Замечательный ресторан, ходили туда уже два раза, 
Встретились с подругами пообщаться, выпить пива. С
В Дугласе оказались случайно, друзья отмечали день
Да, это что-то, даже не могу сказать как, но поста
Меня не обманули мои друзья! Как было сказано: "Са
Я как-то увидела, что на месте не безызвестного ма
31 июля отмечали нашу свадьбу в ресторане Анданте.
Посетил данный ресторан в начале сентября в компан
Ходим в этот ресторанчик не так часто, только когд
из всех посещенных мной ресторанов китайской кухни
Очень хочется поделится своим мнением! Мы с друзья
Почитал отзывы на этом сайте и решил посетить заве
Мы пришли с мужем в "Небо" приблизительно в 19:00 
Очень испортился ресторан за последний год, цены в
Отличное место, с отличной кухней. Читал много отз
Удивлена наличием негативных отзывов о данном заве
Отмечали с мужем годовщину свадьбы на первом этаже
Ну вот посетила Чаплин-холл, поделюсь впечатлениям
Место очень интересное. Просто сходить стоит. Но..
Зашли в кафе с подругой по рекомендации родителей,
Посетили этот ресторан 25,08,12. После посещения ж
решили этот день рождения отметить семьей-я,жена и
На прошлой недели удалось таки сходить в этот рест
Первый раз зашла случайно, хотелось кофе попить...
Были в этом ресторане два раза. В первый раз работ
Вчера впервые побывали у вас на Комендантском 2. О
Первое свидание с молодым человеком решили провест
Хороший ресторан с неплохим обслуживанием. Были в 
Очень не понравилось обслуживание! Были вчера вече
Как то посещали данное заведение с женой и друзьям
Были с мужем, хотели отметить дату знакомства, НО!
Ужасный персонал на Невском пр-те 22, особенно есл
Посещала это заведение раз пять. Возвращаться туда
Заходили в субботу в 5 вечера в начале декабря. Ра
Недавно с подругой ужинали у Вас. Давно смотрели п
Отмечали день рождения, компанией из 8 человек. В 
Приятно когда тебя встречают улыбкой аж с "парковк
Отмечали свадьбу друга. Приехали вечером, шел дожд
Хороший свежий ресторан, обслуживание понравилось,
Хочу написать своё впечатление о Бадене. Живём в О
Все не собраться было написать отзыв об этом прекр
Бронировали столик в прошлые выходные (30.08.14), 
Отмечали свадьбу в ресторане «Кирочный Двор». Хоте
Всем добрый день! Банкетный зал открылся недавно, 
Была на днях в этом ресторане, приехали в пятницу 
Здравствуйте! 23.12.2013г.Провели корпоратив в рес
На днях я таки посетила Террасу, в которой не была
Были сегодня первый раз! Все очень понравилось. И 
Хочется поделиться со всеми пользователями сайта о
18 октября отмечал день рожденья в Паберти. Заказы
Юбилей это тот повод, когда хочется собраться толь
Вчера были в ресторане "Небо", что могу сказать, р
Праздновали здесь юбилей подруги. Довольны очень! 
Хочу выразить огромную благодарность ресторану Бра
Иногда захожу в это местечко выпить пива с друзьям
Семейное торжество отмечали в Амадеусе 30 мая . На
Очень странно, заказав столик в кафе, прийти, а та
Готовясь идти с любимой в этот ресторан, что бы вс
Неделю назад зашли посмотреть на новое заведение. 
Не так давно были в Жан-Жаке с подругой, вот решил
Была пару раз в пабе, очень понравилось. Вкусное п
В целом, мне и моим друзьям очень нравится этот ре
>>> for review in tree.findall('.//review'):
	if review.findall('.//aspect[@sentiment="positive"][@type="implicit"]') != []:
		print(review.findall('.//text')[0].text[:51])

		
День 8-го марта прошёл, можно и итоги подвести. Реш
Отмечали в этом ресторане день рождение на первом э
Для встречи с друзьями было выбрано данное заведени
Хочу поделиться своим впечатлением от посещения рес
Добрый день! Были вчера с друзьями в этом кафе! Оче
Отметили с мужем годовщину свадьбы 6 ноября в этом 
Впервые побывала в этом пабе совсем недавно и могу 
Ребята, вы - лучшие! Недавно были небольшой дружной
Зашла в ресторан первое впечатление отличное, но пр
Мы посетили этот замечательный ресторанчик поздним 
Были вчера компанией 6 человек в "Суп-вино". Столик
В прошлую субботу посетили с друзьями это заведение
Добрый день! Мы с молодым человеком любим открывать
Добрый вечер! Начну сразу, мне ужасно не понравилос
Добрый день! Недавно (22 ноября) посещали этот рест
Была в этом заведении 10.09.2008, заехали с мужем п
Буквально на днях отмечали с мужем наш небольшой юб
В эту субботу решили с друзьями куда ни будь сходит
Отличное кафе!!!! Отмечала в нем свой день рождения
В эти выходные отмечала день рождения в этом рестор
На днях, в командировку, приезжали коллеги по работ
Не могу не рассказать, как прошел банкет на мою сва
Были в этом заведении впервые, компанией из 4-х чел
была там последний раз где то месяц назад в часа 4!
Привет. Отмечала в этом ресторане свой День Рождени
Мы проводили торжество в марте 2014 года в ресторан
Сегодня обедали в Фартуке вдвоем с мужем. На сайте 
Добрый день, Праздновали День Рождение в середине н
Очень просторно и светло, интерьер в моем любимом с
Здравствуйте! 12.08.2014 мы отмечали нашу свадьбу в
Отмечали свадьбу 15 марта. Ах-Ах!!! Замечательный р
Добрый день! Первый раз пишу отзыв о ресторане, нас
Прекрасный ресторан! Уютная обстановка и атмосфера,
Праздновали день рождения,все понравилось, удалось 
Последний раз был в этом ресторане несколько лет на
Добрый день! Недавно праздновали свадьбу в банкетно
Никогда серьезно не относился к данному заведению, 
Н Начну из далека)) года 1,5-2 назад заходила в "да
Была в трёх разных ресторанах Мама Рома. Кухня раду
Зашли в"аппетит" случайно.Не смотря на то,что был б
Один из моих любимых ресторанов. С самого открытия 
Отмечали в этом ресторане день рождение в субботу в
Сегодня мы всей семьей посетили ресторан Марчеллис.
Добрый день! Ходил с девушкой 22.12- ей очень понра
Отличное заведение! Посещаю эту место с самого откр
Праздновали свадьбу в этом ресторане 7 августа 2014
В один из недавних, совсем не по-весеннему холодных
Никогда не писал отзывы, но тут - просто обязан! Ис
Вы помните мультик про мышонка повара, живущего в П
Решил отметить в этом заведении свой ДР в компании 
Субботним вечером зашли компанией в кафе Dolce Ital
На 2ом этаже была раза два. Красивый интерьер - сид
Нам понравилось абсолютно все!!!Очень хороший ресто
Мы были в этом ресторане 2 раза. Обслуживанием очен
Небольшой и уютный ресторан. При входе нас встретил
Давно здесь не был, хотя близко от меня. На мой взг
Ресторан очень хороший!!! С ним у меня связано очен
Являемся постоянными посетителями данного заведения
Давно хотела посетить этот ресторан, т.к. очень люб
Были на мой день рождения в этом ресторане! Мне все
Заезжали поужинать с подругой пару недель назад. Ст
Являюсь постоянным гостем данного кафе. Недавно в н
17 июня отмечали в Санторини свадьбу - обслуживание
Привет всем!Мы из Москвы,посетили на выходные Питер
Красиво. Вкусно. Обслуживание "на уровне". Вот на э
Посетили данное заведение по случаю юбилея моего па
Хочу оставить свой отзыв об этом замечательном кафе
Несколько раз посещали с друзьями данный ресторан! 
мы посетили ресторан 10 марта. впечатления остались
Впервые посетила это замечательное место! С первых 
Праздновали свадьбу в этом ресторане! Свадьба была 
Были в этом ресторане в апреле месяце. Остались хор
Была в этом ресторане только однажды, но с удовольс
Зашли в ресторан в выходной день случайно. Посовето
06.09.2013 были на ужине в ресторане Пури. Выбирали
Всем добрый день! Вчера отдыхали с компанией 9 чело
При входе в ресторан вас встречают необычный интерь
Вчера отмечали юбилей, очередную годовщину нашей св
Мы отмечали 19.04 свадьбу в этом ресторане, гостей 
Первый раз посетили с друзьями этот уютный ресторан
Первое посещение Дачи было в рамках поиска ресторан
Бывала раньше в этом заведении и всегда замечала,чт
Были 1 февраля. Я второй раз, подруга - первый. При
Приятное заведение. Действительно много места, как 
Был в ресторане пару недель назад с девушкой. Обста
Отличный паб!!!!!! Я решила устроить мужу сюрприз, 
Здравствуйте, Я отмечала свой день рожденья в этом 
Всем доброго дня! Зашел посмотреть телефон заведени
Сегодня случайно попали в этот ресторан. В общем пр
Я была здесь с подругой пока один раз. Пришли вечер
Вывод напишу сразу: дружелюбно, вкусно и приятно. В
Примерно месяц назад посетили это заведение, т. к. 
Всем хорошего дня! 9 августа у нас с мужем был 10ти
Недавно посетила данный ресторан,я согласна со мног
Выбрали это место для начала празднования с коллект
Я редко пишу отрицательные отзывы, но в данном случ
Очень долго выбирали ресторан на Новогодний карпора
Недавно отмечали в Санам день рождения. Безумно пон
Были уже не один раз, нравится! Приятное и очень ую
Праздновала в этом ресторане свой Др, праздник был 
Ходили с молодым человеком в пятницу, 25 ноября. Ку
На день рождения моей девушки, мы решили сходить в 
После прогулки решили с подругой зайти-перекусить, 
Сегодня с подругой посетил данное заведение! очень 
В пятницу 8 числа с друзьями проходили мимо рестора
Я недавно переехала в Пушкин.Абсолютно не было врем
Приятный итальянский ресторанчик без претензий. Из 
Сегодня отмечали день рождения небольшой компанией 
Замечательный ресторан, ходили туда уже два раза, о
Встретились с подругами пообщаться, выпить пива. Ст
В Дугласе оказались случайно, друзья отмечали день 
Да, это что-то, даже не могу сказать как, но постар
Меня не обманули мои друзья! Как было сказано: "Сам
Я как-то увидела, что на месте не безызвестного маг
31 июля отмечали нашу свадьбу в ресторане Анданте. 
Посетил данный ресторан в начале сентября в компани
Ходим в этот ресторанчик не так часто, только когда
из всех посещенных мной ресторанов китайской кухни 
Очень хочется поделится своим мнением! Мы с друзьям
Почитал отзывы на этом сайте и решил посетить завед
Мы пришли с мужем в "Небо" приблизительно в 19:00 9
Очень испортился ресторан за последний год, цены вы
Отличное место, с отличной кухней. Читал много отзы
Удивлена наличием негативных отзывов о данном завед
Отмечали с мужем годовщину свадьбы на первом этаже 
Ну вот посетила Чаплин-холл, поделюсь впечатлениями
Место очень интересное. Просто сходить стоит. Но...
Зашли в кафе с подругой по рекомендации родителей, 
Посетили этот ресторан 25,08,12. После посещения же
решили этот день рождения отметить семьей-я,жена и 
На прошлой недели удалось таки сходить в этот ресто
Первый раз зашла случайно, хотелось кофе попить...С
Были в этом ресторане два раза. В первый раз работа
Вчера впервые побывали у вас на Комендантском 2. Оч
Первое свидание с молодым человеком решили провести
Хороший ресторан с неплохим обслуживанием. Были в н
Очень не понравилось обслуживание! Были вчера вечер
Как то посещали данное заведение с женой и друзьями
Были с мужем, хотели отметить дату знакомства, НО! 
Ужасный персонал на Невском пр-те 22, особенно если
Посещала это заведение раз пять. Возвращаться туда 
Заходили в субботу в 5 вечера в начале декабря. Раз
Недавно с подругой ужинали у Вас. Давно смотрели пр
Отмечали день рождения, компанией из 8 человек. В о
Приятно когда тебя встречают улыбкой аж с "парковки
Отмечали свадьбу друга. Приехали вечером, шел дождь
Хороший свежий ресторан, обслуживание понравилось, 
Хочу написать своё впечатление о Бадене. Живём в Оз
Все не собраться было написать отзыв об этом прекра
Бронировали столик в прошлые выходные (30.08.14), н
Отмечали свадьбу в ресторане «Кирочный Двор». Хотел
Всем добрый день! Банкетный зал открылся недавно, и
Была на днях в этом ресторане, приехали в пятницу в
Здравствуйте! 23.12.2013г.Провели корпоратив в рест
На днях я таки посетила Террасу, в которой не была 
Были сегодня первый раз! Все очень понравилось. И м
Хочется поделиться со всеми пользователями сайта от
18 октября отмечал день рожденья в Паберти. Заказыв
Юбилей это тот повод, когда хочется собраться тольк
Вчера были в ресторане "Небо", что могу сказать, ра
Праздновали здесь юбилей подруги. Довольны очень! В
Хочу выразить огромную благодарность ресторану Брав
Иногда захожу в это местечко выпить пива с друзьями
Семейное торжество отмечали в Амадеусе 30 мая . Нак
Очень странно, заказав столик в кафе, прийти, а там
Готовясь идти с любимой в этот ресторан, что бы вст
Неделю назад зашли посмотреть на новое заведение. С
Не так давно были в Жан-Жаке с подругой, вот решила
Была пару раз в пабе, очень понравилось. Вкусное пи
В целом, мне и моим друзьям очень нравится этот рес
>>> for review in tree.findall('.//review'):
	if review.findall('.//aspect[@sentiment="positive"][@type="implicit"]') != []:
		print(review.findall('.//text')[0].text[:51])

		
День 8-го марта прошёл, можно и итоги подвести. Реш
Отмечали в этом ресторане день рождение на первом э
Для встречи с друзьями было выбрано данное заведени
Хочу поделиться своим впечатлением от посещения рес
Добрый день! Были вчера с друзьями в этом кафе! Оче
Отметили с мужем годовщину свадьбы 6 ноября в этом 
Впервые побывала в этом пабе совсем недавно и могу 
Ребята, вы - лучшие! Недавно были небольшой дружной
Зашла в ресторан первое впечатление отличное, но пр
Мы посетили этот замечательный ресторанчик поздним 
Были вчера компанией 6 человек в "Суп-вино". Столик
В прошлую субботу посетили с друзьями это заведение
Добрый день! Мы с молодым человеком любим открывать
Добрый вечер! Начну сразу, мне ужасно не понравилос
Добрый день! Недавно (22 ноября) посещали этот рест
Была в этом заведении 10.09.2008, заехали с мужем п
Буквально на днях отмечали с мужем наш небольшой юб
В эту субботу решили с друзьями куда ни будь сходит
Отличное кафе!!!! Отмечала в нем свой день рождения
В эти выходные отмечала день рождения в этом рестор
На днях, в командировку, приезжали коллеги по работ
Не могу не рассказать, как прошел банкет на мою сва
Были в этом заведении впервые, компанией из 4-х чел
была там последний раз где то месяц назад в часа 4!
Привет. Отмечала в этом ресторане свой День Рождени
Мы проводили торжество в марте 2014 года в ресторан
Сегодня обедали в Фартуке вдвоем с мужем. На сайте 
Добрый день, Праздновали День Рождение в середине н
Очень просторно и светло, интерьер в моем любимом с
Здравствуйте! 12.08.2014 мы отмечали нашу свадьбу в
Отмечали свадьбу 15 марта. Ах-Ах!!! Замечательный р
Добрый день! Первый раз пишу отзыв о ресторане, нас
Прекрасный ресторан! Уютная обстановка и атмосфера,
Праздновали день рождения,все понравилось, удалось 
Последний раз был в этом ресторане несколько лет на
Добрый день! Недавно праздновали свадьбу в банкетно
Никогда серьезно не относился к данному заведению, 
Н Начну из далека)) года 1,5-2 назад заходила в "да
Была в трёх разных ресторанах Мама Рома. Кухня раду
Зашли в"аппетит" случайно.Не смотря на то,что был б
Один из моих любимых ресторанов. С самого открытия 
Отмечали в этом ресторане день рождение в субботу в
Сегодня мы всей семьей посетили ресторан Марчеллис.
Добрый день! Ходил с девушкой 22.12- ей очень понра
Отличное заведение! Посещаю эту место с самого откр
Праздновали свадьбу в этом ресторане 7 августа 2014
В один из недавних, совсем не по-весеннему холодных
Никогда не писал отзывы, но тут - просто обязан! Ис
Вы помните мультик про мышонка повара, живущего в П
Решил отметить в этом заведении свой ДР в компании 
Субботним вечером зашли компанией в кафе Dolce Ital
На 2ом этаже была раза два. Красивый интерьер - сид
Нам понравилось абсолютно все!!!Очень хороший ресто
Мы были в этом ресторане 2 раза. Обслуживанием очен
Небольшой и уютный ресторан. При входе нас встретил
Давно здесь не был, хотя близко от меня. На мой взг
Ресторан очень хороший!!! С ним у меня связано очен
Являемся постоянными посетителями данного заведения
Давно хотела посетить этот ресторан, т.к. очень люб
Были на мой день рождения в этом ресторане! Мне все
Заезжали поужинать с подругой пару недель назад. Ст
Являюсь постоянным гостем данного кафе. Недавно в н
17 июня отмечали в Санторини свадьбу - обслуживание
Привет всем!Мы из Москвы,посетили на выходные Питер
Красиво. Вкусно. Обслуживание "на уровне". Вот на э
Посетили данное заведение по случаю юбилея моего па
Хочу оставить свой отзыв об этом замечательном кафе
Несколько раз посещали с друзьями данный ресторан! 
мы посетили ресторан 10 марта. впечатления остались
Впервые посетила это замечательное место! С первых 
Праздновали свадьбу в этом ресторане! Свадьба была 
Были в этом ресторане в апреле месяце. Остались хор
Была в этом ресторане только однажды, но с удовольс
Зашли в ресторан в выходной день случайно. Посовето
06.09.2013 были на ужине в ресторане Пури. Выбирали
Всем добрый день! Вчера отдыхали с компанией 9 чело
При входе в ресторан вас встречают необычный интерь
Вчера отмечали юбилей, очередную годовщину нашей св
Мы отмечали 19.04 свадьбу в этом ресторане, гостей 
Первый раз посетили с друзьями этот уютный ресторан
Первое посещение Дачи было в рамках поиска ресторан
Бывала раньше в этом заведении и всегда замечала,чт
Были 1 февраля. Я второй раз, подруга - первый. При
Приятное заведение. Действительно много места, как 
Был в ресторане пару недель назад с девушкой. Обста
Отличный паб!!!!!! Я решила устроить мужу сюрприз, 
Здравствуйте, Я отмечала свой день рожденья в этом 
Всем доброго дня! Зашел посмотреть телефон заведени
Сегодня случайно попали в этот ресторан. В общем пр
Я была здесь с подругой пока один раз. Пришли вечер
Вывод напишу сразу: дружелюбно, вкусно и приятно. В
Примерно месяц назад посетили это заведение, т. к. 
Всем хорошего дня! 9 августа у нас с мужем был 10ти
Недавно посетила данный ресторан,я согласна со мног
Выбрали это место для начала празднования с коллект
Я редко пишу отрицательные отзывы, но в данном случ
Очень долго выбирали ресторан на Новогодний карпора
Недавно отмечали в Санам день рождения. Безумно пон
Были уже не один раз, нравится! Приятное и очень ую
Праздновала в этом ресторане свой Др, праздник был 
Ходили с молодым человеком в пятницу, 25 ноября. Ку
На день рождения моей девушки, мы решили сходить в 
После прогулки решили с подругой зайти-перекусить, 
Сегодня с подругой посетил данное заведение! очень 
В пятницу 8 числа с друзьями проходили мимо рестора
Я недавно переехала в Пушкин.Абсолютно не было врем
Приятный итальянский ресторанчик без претензий. Из 
Сегодня отмечали день рождения небольшой компанией 
Замечательный ресторан, ходили туда уже два раза, о
Встретились с подругами пообщаться, выпить пива. Ст
В Дугласе оказались случайно, друзья отмечали день 
Да, это что-то, даже не могу сказать как, но постар
Меня не обманули мои друзья! Как было сказано: "Сам
Я как-то увидела, что на месте не безызвестного маг
31 июля отмечали нашу свадьбу в ресторане Анданте. 
Посетил данный ресторан в начале сентября в компани
Ходим в этот ресторанчик не так часто, только когда
из всех посещенных мной ресторанов китайской кухни 
Очень хочется поделится своим мнением! Мы с друзьям
Почитал отзывы на этом сайте и решил посетить завед
Мы пришли с мужем в "Небо" приблизительно в 19:00 9
Очень испортился ресторан за последний год, цены вы
Отличное место, с отличной кухней. Читал много отзы
Удивлена наличием негативных отзывов о данном завед
Отмечали с мужем годовщину свадьбы на первом этаже 
Ну вот посетила Чаплин-холл, поделюсь впечатлениями
Место очень интересное. Просто сходить стоит. Но...
Зашли в кафе с подругой по рекомендации родителей, 
Посетили этот ресторан 25,08,12. После посещения же
решили этот день рождения отметить семьей-я,жена и 
На прошлой недели удалось таки сходить в этот ресто
Первый раз зашла случайно, хотелось кофе попить...С
Были в этом ресторане два раза. В первый раз работа
Вчера впервые побывали у вас на Комендантском 2. Оч
Первое свидание с молодым человеком решили провести
Хороший ресторан с неплохим обслуживанием. Были в н
Очень не понравилось обслуживание! Были вчера вечер
Как то посещали данное заведение с женой и друзьями
Были с мужем, хотели отметить дату знакомства, НО! 
Ужасный персонал на Невском пр-те 22, особенно если
Посещала это заведение раз пять. Возвращаться туда 
Заходили в субботу в 5 вечера в начале декабря. Раз
Недавно с подругой ужинали у Вас. Давно смотрели пр
Отмечали день рождения, компанией из 8 человек. В о
Приятно когда тебя встречают улыбкой аж с "парковки
Отмечали свадьбу друга. Приехали вечером, шел дождь
Хороший свежий ресторан, обслуживание понравилось, 
Хочу написать своё впечатление о Бадене. Живём в Оз
Все не собраться было написать отзыв об этом прекра
Бронировали столик в прошлые выходные (30.08.14), н
Отмечали свадьбу в ресторане «Кирочный Двор». Хотел
Всем добрый день! Банкетный зал открылся недавно, и
Была на днях в этом ресторане, приехали в пятницу в
Здравствуйте! 23.12.2013г.Провели корпоратив в рест
На днях я таки посетила Террасу, в которой не была 
Были сегодня первый раз! Все очень понравилось. И м
Хочется поделиться со всеми пользователями сайта от
18 октября отмечал день рожденья в Паберти. Заказыв
Юбилей это тот повод, когда хочется собраться тольк
Вчера были в ресторане "Небо", что могу сказать, ра
Праздновали здесь юбилей подруги. Довольны очень! В
Хочу выразить огромную благодарность ресторану Брав
Иногда захожу в это местечко выпить пива с друзьями
Семейное торжество отмечали в Амадеусе 30 мая . Нак
Очень странно, заказав столик в кафе, прийти, а там
Готовясь идти с любимой в этот ресторан, что бы вст
Неделю назад зашли посмотреть на новое заведение. С
Не так давно были в Жан-Жаке с подругой, вот решила
Была пару раз в пабе, очень понравилось. Вкусное пи
В целом, мне и моим друзьям очень нравится этот рес
>>> 
