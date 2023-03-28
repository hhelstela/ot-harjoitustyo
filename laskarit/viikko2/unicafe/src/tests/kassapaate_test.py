import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
    
    def test_luotu_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_syo_edullisesti_kateisella(self):
        ok = self.kassa.syo_edullisesti_kateisella(500)

        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(ok, 260)
    
    def test_syo_edullisesti_kateisella_ei_riita(self):
        eiok = self.kassa.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(eiok, 200)

    def test_syo_maukkaasti_kateisella(self):
        ok = self.kassa.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(ok, 100)
    
    def test_syo_maukkaasti_kateisella_ei_riita(self):
        eiok = self.kassa.syo_maukkaasti_kateisella(200)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(eiok, 200)


    def test_syo_edullisesti_kortilla(self):
        kortti = Maksukortti(1000)
        osto = self.kassa.syo_edullisesti_kortilla(kortti)

        self.assertEqual(osto, True)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo, 760)

    def test_syo_edullisesti_kortilla_ei_riita(self):
        kortti = Maksukortti(0)
        osto = self.kassa.syo_edullisesti_kortilla(kortti)

        self.assertEqual(osto, False)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo, 0)
    
    def test_syo_maukkaasti_kortilla(self):
        kortti = Maksukortti(1000)
        osto = self.kassa.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(osto, True)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo, 600)

    def test_syo_maukkaasti_kortilla_ei_riita(self):
        kortti = Maksukortti(0)
        osto = self.kassa.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(osto, False)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo, 0)
    
    def test_lataa_rahaa_kortille(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti, 100)

        self.assertEqual(self.kassa.kassassa_rahaa, 100100)
        self.assertEqual(kortti.saldo, 100)
    
    def test_lataa_rahaa_kortille_negatiivinen(self):
        kortti = Maksukortti(0)
        self.kassa.lataa_rahaa_kortille(kortti, -100)

        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(kortti.saldo, 0)