
code = []
code.append("import unittest")
path = "chapter_maker.py"
test_path = "test_chapter_maker.py"

# go through a file with pathway
f = open(path, 'r+')
for line in f.readlines():
    if "class" in line:
        line = line.replace("(", "Test(unittest.TestCase")
        code.append(line.replace("\n", ""))
    elif "def" in line:
        line = line.replace("def ", "def test_")
        code.append(line.replace("\n", ""))
        code.append("        self.assertEqual(True, True)\n")
f.close()

code.append("if __name__ == '__main__':")
code.append("    unittest.main()")

with open(test_path, 'w') as f:
    for item in code:
        f.write("%s\n" % item)

#python -m unittest test_module1 test_module2
#python -m unittest test_module.TestClass
#python -m unittest test_module.TestClass.test_method