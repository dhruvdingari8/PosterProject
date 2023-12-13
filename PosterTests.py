import unittest
import Poster as p
import Textbox as tb
import Track as tr
import Title as ttl



class JSONReaderTests(unittest.TestCase):
    def test_error(self):
        with self.assertRaises(FileNotFoundError):
            p.JSONReader.readJSON(p.JSONReader(), "randy.json")
            print("Test 1 failed")
        print("Test 1 passed")

    def test_readJSON(self):
        posters = p.JSONReader.readJSON(p.JSONReader(), "input.json")
        assert posters[0].title.text == ttl.Title("DARK BLOOD").text
        assert posters[0].artist.text == tb.Textbox("ENHYPEN", (50, 1500), 48).text
        assert posters[0].tot_len.text == tb.Textbox("18:13", (50, 1500), 66).text
        assert posters[0].tracklist[0].text == tr.Track({"title" : "Fate",
                                                         "length": "2:31"}, (50, 1500)).text
        assert posters[0].info.text == tb.Textbox("Belift Lab, K-Pop | Hip-Hop, May 22, 2023", (50, 1500), 66).text
        assert posters[0].cover == "AlbumCovers/DARKBLOOD.jpg"
        assert posters[0].cover_colors == ["#cfcfcf", "#262c38", "#0e0e0e"]
        assert posters[0].spotify_code == "SpotifyCodes/DARKBLOOD.jpeg"

        print("Test 1 passed")

class TrackTests(unittest.TestCase):

    def test_Track(self):
        track = tr.Track({"title" : "Fate", "length" : "2:31"}, (50, 1500))
        assert track.text == "Fate - 2:31"
        assert track.posn == (50, 1500)
        assert track.size == 66
        print("Test 1 passed")

if __name__ == '__main__':
    unittest.main()
