import sys
import platform

print("=" * 50)
print(f"Python 完整版本信息：\n{sys.version}")
print(f"版本号：{platform.python_version()}")
print(f"解释器类型：{platform.python_implementation()}")
print(f"解释器路径：{sys.executable}")
print(f"主/次版本：{sys.version_info.major}.{sys.version_info.minor}")
print("=" * 50)