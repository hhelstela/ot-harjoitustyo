import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_rahan_lisaaminen_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(100)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 9.00 euroa")

    def test_saldo_ei_muutu_jos_ei_riita(self):
        self.maksukortti.ota_rahaa(2000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
        
    def test_rahan_otto_palautusarvot(self):
        toimii = self.maksukortti.ota_rahaa(500)
        eitoimi = self.maksukortti.ota_rahaa(2000)
        
        self.assertEqual(toimii, True)
        self.assertEqual(eitoimi, False)
        