
from setuptools import setup



setup(
	name='jxcrawl', 				# 这是安装到 python 目录后的文件名，仅仅是文件名或目录名，不是包名，无法对这个名称进行 import；但如果用 twine upload dist/* 到了 pypi.org 的话，则此处是 pip install 要用到的包名，然后安装到 python 的 lib 之后，依然是文件名，无法用 import 引入。下面那个 packages 参数所指向的包名，才是可以 import 的。
	version='1.01',
	author='xjxfly',
	license='BSD',
	#zip_safe = False, 				# 这个参数为 False ，使得安装到目标位置后是平坦的目录文件形式，而非 .egg 形式
	install_requires = [
		'requests>=1',
		'selenium>=1',
		'beautifulsoup4>=1',
		'jxbase>=2.20'
		'cnstock>=1'
		], 	# 这是本包要用到的依赖包
	packages=['jxcrawl'], 			# 这是实际待安装的包名，即是个内含 __init__.py 的目录名，可以当作未来的包名引用，如 import pandas as pd 等，这里注意，子包必须带上父包前缀才能被找到安装，如 jxcrawl.sina 会被找到，但只写 sina 不会被找到，虽然他也是包名
	package_data = {'':['*.*']} 	# 表示安装时将上述 packages 指定的每个包下的所有文件都带过去安装。如果没有这句，那只安装所有 py 文件。'' 表示所有上述指定的包，['*.*']表示该包下的所有文件
	)


