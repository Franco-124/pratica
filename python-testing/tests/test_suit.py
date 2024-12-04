import unittest

from test_banckaccount import BankAccountTests
def Banck_account_suite():
    suite  = unittest.TestSuite()

    suite.addTest(BankAccountTests(" test_deposit"))
    suite.addTest(BankAccountTests("test_withdraw"))
    
    return suite
if __name__=="__main__":
    runner = unittest.TextTestRunner()
    runner.run(Banck_account_suite())