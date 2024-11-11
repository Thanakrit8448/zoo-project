import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def testecp_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def testecp_notyetborn_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-3), 'Invalid')

    def testecp_young_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(19), 100)

    def testecp_workingage_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(45), 150)

    def testecp_old_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(87), 100)

    # BVA

    def testbva_notyetborn_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), 'Invalid')

    def testbva_child_ticket_price1(self):
        self.assertEqual(self.zoo.get_ticket_price(1), 50)
    
    def testbva_child_ticket_price2(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def testbva_young_ticket_price1(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)

    def testbva_young_ticket_price2(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def testecp_workingage_ticket_price1(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def testecp_workingage_ticket_price1(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def testecp_old_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

    


    


    



    
if __name__ == '__main__':
    unittest.main()