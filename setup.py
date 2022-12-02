import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "sfode",
    version = "0.0.1",
    author = "Xiaodu Hu",
    author_email= "xiaodu.hu@outlook.com",
    description = "String Function of Ordinary Defferential Equations transformation.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    keywords = ['python', 'ode', 'string', 'function'],
    license = "MIT",
    # url = "",
    classifiers = [
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS"
    ],
    package_dir={'':'src'},
    # py_modules=["_cpp", "_py"],
    packages = setuptools.find_packages('src'),
)

# python setup.py sdist bdist