import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(10_00)

    def test_alussa_rahaa_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100_000)
    
    def test_alussa_edullisia_lounaita_ei_myyty(self):
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_alussa_maukkaita_lounaita_ei_myyty(self):
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_jos_maksu_riittava_kassan_saldo_nousee_oikein(self):
        self.kassa.syo_edullisesti_kateisella(250)

        self.assertEqual(self.kassa.kassassa_rahaa, 100_240)

    def test_jos_maksu_riittava_takaisin_oikea_maara(self):
        transaktio = self.kassa.syo_edullisesti_kateisella(260)

        self.assertEqual(transaktio, 20)

    def test_jos_maksu_lapi_myydyt_lounaat_kasvaa(self):
        ennen = self.kassa.edulliset + self.kassa.maukkaat
        self.kassa.syo_edullisesti_kateisella(300)
        self.kassa.syo_maukkaasti_kateisella(500)
        jalkeen = self.kassa.edulliset + self.kassa.maukkaat

        self.assertEqual(jalkeen, ennen+2)

    def test_jos_maksu_ei_riittava_vaihtoraha_oikea_edullinen(self):
        myynti = self.kassa.syo_edullisesti_kateisella(10)

        self.assertEqual(myynti, 10)
    
    def test_jos_maksu_ei_riittava_vaihtoraha_oikea_maukas(self):
        myynti = self.kassa.syo_maukkaasti_kateisella(10)

        self.assertEqual(myynti, 10)
    
    def test_jos_maksu_ei_riita_lounaiden_myynti_ei_muutu(self):
        ennen = self.kassa.edulliset + self.kassa.maukkaat
        self.kassa.syo_edullisesti_kateisella(30)
        self.kassa.syo_maukkaasti_kateisella(50)
        jalkeen = self.kassa.edulliset + self.kassa.maukkaat

        self.assertEqual(jalkeen, ennen)


    def test_jos_maksu_ei_riita_kassa_ei_muutu(self):
        ennen = self.kassa.kassassa_rahaa
        myynti = self.kassa.syo_edullisesti_kateisella(10)

        self.assertEqual(self.kassa.kassassa_rahaa, ennen)

    def test_jos_kortilla_rahaa_veloitetaan_kortilta_edullinen(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.60 euroa")

    def test_jos_kortilla_rahaa_veloitetaan_kortilta_maukas(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")


    def test_jos_kortilla_rahaa_palautetaan_true(self):
        booli = self.kortti.ota_rahaa(240)

        self.assertEqual(booli, True)

    def test_jos_katetta_myytyjen_lounaiden_maara_kasvaa(self):
        ennen = self.kassa.edulliset + self.kassa.maukkaat
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        
        self.assertEqual(self.kassa.edulliset+self.kassa.maukkaat, ennen+2)

    def test_kortilla_ei_katetta_kortin_saldo_ei_muutu(self):
        kortti = Maksukortti(100)
        self.kassa.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(str(kortti), "Kortilla on rahaa 1.00 euroa")
    
    def test_kortilla_ei_katetta_myydyt_lounaat_ei_muutu(self):
        ennen = self.kassa.edulliset + self.kassa.maukkaat
        kortti = Maksukortti(100)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.kassa.syo_edullisesti_kortilla(kortti)

        self.assertEqual(ennen, self.kassa.edulliset + self.kassa.maukkaat)

    def test_kortilla_ei_katetta_palautetaan_false(self):
        kortti = Maksukortti(100)
        tulos = kortti.ota_rahaa(10000)

        self.assertEqual(tulos, False)

    def test_lataa_rahaa_kortille_summa_negatiivinen_kassa_ei_muutu(self):
        ennen = self.kassa.kassassa_rahaa
        self.kassa.lataa_rahaa_kortille(self.kortti, -100)

        self.assertEqual(self.kassa.kassassa_rahaa, ennen)

    def test_lataa_rahaa_kortille_kortin_saldo_nousee(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 100)

        self.assertEqual(str(self.kortti), "Kortilla on rahaa 11.00 euroa")

    def test_lataa_rahaa_kortille_kassan_saldo_muuttuu(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 100)

        self.assertEqual(self.kassa.kassassa_rahaa, 100100)
