from common import ParameterStore
import unittest

class test(unittest.TestCase):
    #arrange
    ps = ParameterStore()
    
    def testInt(self):
        self.ps.set("int1", 123)
        self.ps.set("int2", 0)
        
        value1 = self.ps.get("int1")
        value2 = self.ps.get("int2")
        
        self.assertEqual(value1,123)
        self.assertEqual(value2,0)
        
    def testFloat(self):
        self.ps.set("float1", 1.23)
        self.ps.set("float2", 1.0)
        
        value1 = self.ps.get("float1")
        value2 = self.ps.get("float2")
        
        self.assertEqual(value1, 1.23)
        self.assertEqual(value2, 1.0)
    
    def testString(self):
        self.ps.set("str1","str1")
        self.ps.set("str2","s")
        self.ps.set("str3","")
        
        value1 = self.ps.get("str1")
        value2 = self.ps.get("str2")
        value3 = self.ps.get("str3")
        
        self.assertEqual(value1, "str1")
        self.assertEqual(value2, "s")
        self.assertEqual(value3, "")

    def testBool(self):
        # act
        self.ps.set("bool1", True )
        self.ps.set("bool2", False)
        
        value1 = self.ps.get("bool1")
        value2 = self.ps.get("bool2")
        #assert
        self.assertEqual(value1, True)
        self.assertEqual(value2,False)
        
    def testManyBool(self):
        values1 = {"mBool1": True, "mBool2": False}
        keys = ["mBool1","mBool2"]
        
        self.ps.mset(values1)
        result1 = self.ps.mget(keys)
        
        self.assertEqual(result1, values1)
        
    def testManyInt(self):
        values1 = {"mInt1": 123, "mInt2": 1, "mInt3": 0}
        keys = ["mInt1", "mInt2", "mInt3"]
        
        self.ps.mset(values1)
        result1 = self.ps.mget(keys)
        
        self.assertEqual(result1, values1)
        
    def testManyStr(self):
        values1 = {"mStr1": "str1", "mStr2": "s", "mStr3": ""}
        keys = ["mStr1", "mStr2", "mStr3"]
        
        self.ps.mset(values1)
        result1 = self.ps.mget(keys)
        
        self.assertEqual(result1, values1)
        
    def testManyFloat(self):
        values1 = {"mFloat1": 1.23, "mFloat2": 1.0}
        keys = ["mFloat1", "mFloat2"]
        
        self.ps.mset(values1)
        result1 = self.ps.mget(keys)
        
        self.assertEqual(result1, values1)
        
    def testMix(self):
        values1 = {"mix1": "str1", "mix2": 234, "mix3": True, "mix4": 12.3}
        keys = ["mix1", "mix2", "mix3", "mix4"]
        
        self.ps.mset(values1)
        result1 = self.ps.mget(keys)
        
        self.assertEqual(result1, values1)
        
if __name__ == "__main__":
    unittest.main()