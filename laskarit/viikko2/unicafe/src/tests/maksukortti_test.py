import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)


    def test_alussa_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_rahan_lataaminen_kasvattaa_oikein(self):
        self.maksukortti.lataa_rahaa(100)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 11.00 euroa")

    def test_saldo_vahenee_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(250)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.50 euroa")

    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        kortti = Maksukortti(1)
        kortti.ota_rahaa(100)

        self.assertEqual(str(kortti), "Kortilla on rahaa 0.01 euroa")

    def test_metodi_palauttaa_true_jos_saldoa_tarpeeksi(self):
        tulos = self.maksukortti.ota_rahaa(10)

        self.assertEqual(tulos, True)
    
    def test_metodi_palauttaa_false_jos_saldo_ei_riita(self):
        tulos = self.maksukortti.ota_rahaa(200000)

        self.assertEqual(tulos, False)

