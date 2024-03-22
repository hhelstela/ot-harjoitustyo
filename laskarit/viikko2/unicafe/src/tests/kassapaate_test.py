import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_luodun_kassapaatteen_rahamaara_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_luodun_kassapaatteen_edulliset_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_luodun_kassapaatteen_maukkaat_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kateis_osto_kun_raha_riittaa(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100640)
    
    def test_kateis_osto_kun_raha_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_korttiosto_toimii_edullisella(self):
        edullisesti = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(edullisesti, True)
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.6)
    
    def test_korttiosto_toimii_maukkailla(self):
        maukkaasti = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(maukkaasti, True)
        self.assertEqual(self.maksukortti.saldo_euroina(), 6)
    
    def test_korttiostot_kasvattavat_myytyjen_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_korttiostot_toimivat_oikein_kun_raha_ei_riita(self):
        maksukortti = Maksukortti(10)
        edullisesti = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        maukkaasti = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(edullisesti, False)
        self.assertEqual(maukkaasti, False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(maksukortti.saldo, 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kortille_rahan_lataaminen_toimii_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo, 2000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_kortille_rahan_lataaminen_kun_summa_on_negatiivinen(self):
        lataus = self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(lataus, None)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kassassa_rahaa_euroina(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)