import unittest
import sys
import requests
import json
import subprocess
import time

# Use double backslashes or a raw string for the path
sys.path.append('C:\\Users\\Igor\\Desktop\\projects\\personal\\company_fetcher_api\\app')
import caches.get_company_names as gcn

class FilterTests(unittest.TestCase):
    def test_filter(self):
        pass    

    # normalize string test
    def test_normalize_strings(self):
        self.assertEqual(gcn.normalize_strings(["Ubisoft-entertainment"]), ["ubisoft entertainment"])
        pass
    
    # remove_duplicates test
    def remove_duplicates(self):
        self.assertEqual(gcn.remove_duplicates(["Ubisoft-entertainment", "ubisoft entertainment", "Ubisoft Enternainment"]), ["ubisoft entertainment"])
        pass
    
    # get_keywords test
    def get_keywords(self):
        self.assertEqual(gcn.get_keywords(["ubisoft entertainment"]), ["ubisoft entertainment", "ubisoft", "entertainment"])
        pass
    
class TestFlaskServer(unittest.TestCase):
    base_url = 'http://127.0.0.1:5000'  # Update with your server URL
    
    @classmethod
    def setUpClass(cls):
        # Start the Flask server in a subprocess
        cls.server_process = subprocess.Popen(['python', 'C:\\Users\\Igor\\Desktop\\projects\\personal\\company_fetcher_api\\app\\flask_app.py'])
        time.sleep(2)  # Give some time for the server to start

    @classmethod
    def tearDownClass(cls):
        # Stop the Flask server process after tests are done
        cls.server_process.terminate()
    
    def test_root_endpoint(self):
        response = requests.get(f'{self.base_url}/')
        self.assertEqual(response.status_code, 200)
        pass

    def test_getjobs_endpoint(self):
        params = {
            "location": "ca",
            "keywords_include": "Python, Developer"
        }
        response = requests.get(f'{self.base_url}/getjobs', params=params)
        self.assertEqual(response.status_code, 200)
        # Add further assertions based on the expected response format/content
        pass

if __name__ == '__main__':
    unittest.main()
