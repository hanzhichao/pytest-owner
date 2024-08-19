# pytest-owner
![Languate - Python](https://img.shields.io/badge/language-python-blue.svg)
![PyPI - License](https://img.shields.io/pypi/l/pytest-owner)
![PyPI](https://img.shields.io/pypi/v/pytest-owner)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pytest-owner)

为用例增加归属人owner标记，运行用例时可以使用--owner指定用例归属人运行。

## 安装方法
```shell
pip install pytest-owner
```
## 使用方式
```python
# filename: test_pytest_owner.py
@pytest.mark.owner('hzc')
def test_a():
    pass
    
@pytest.mark.owner('superhin')
def test_b():
    pass
```
使用以下命令指定归属人运行，支持指定多个归属人
```shell
pytest test_pytest_owner.py --owner=hzc --owner=superhin
```
另外，该插件提供了额外的名为owner的Fixture函数，以共获取当前指定的owner列表。
