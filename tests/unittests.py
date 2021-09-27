import unittest
from webserver import webserver

class webserver_tests(unittest.TestCase):

    def test_request_no_parameters(self):
        request = 'GET / HTTP/1.1 Host: localhost Connection: keep-alive Cache-Control: max-age=0 sec-ch-ua: "Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93" sec-ch-ua-mobile: ?0 sec-ch-ua-platform: "Windows" Upgrade-Insecure-Requests: 1 User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 Sec-Fetch-Site: none Sec-Fetch-Mode: navigate Sec-Fetch-User: ?1 Sec-Fetch-Dest: document Accept-Encoding: gzip, deflate, br Accept-Language: en,uk-UA;q=0.9,uk;q=0.8,en-US;q=0.7'
        res = webserver.parse_request(request)
        self.assertEqual(res, "/")

    def test_request_index_html(self):
        request = 'GET /index.html HTTP/1.1 Host: localhost Connection: keep-alive sec-ch-ua: "Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93" sec-ch-ua-mobile: ?0 sec-ch-ua-platform: "Windows" Upgrade-Insecure-Requests: 1User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9Sec-Fetch-Site: noneSec-Fetch-Mode: navigateSec-Fetch-User: ?1Sec-Fetch-Dest: documentAccept-Encoding: gzip, deflate, brAccept-Language: en,uk-UA;q=0.9,uk;q=0.8,en-US;q=0.7'
        res = webserver.parse_request(request)
        self.assertEqual(res, "/index.html")

    def test_request_github_png(self):
        request = 'GET /github.png HTTP/1.1Host: localhostConnection: keep-alivesec-ch-ua: "Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"sec-ch-ua-mobile: ?0sec-ch-ua-platform: "Windows"Upgrade-Insecure-Requests: 1User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9Sec-Fetch-Site: noneSec-Fetch-Mode: navigateSec-Fetch-User: ?1Sec-Fetch-Dest: documentAccept-Encoding: gzip, deflate, brAccept-Language: en,uk-UA;q=0.9,uk;q=0.8,en-US;q=0.7'
        res = webserver.parse_request(request)
        self.assertEqual(res, "/github.png")

    def test_request_background2_jpg(self):
        request = 'GET /background2.jpg HTTP/1.1Host: localhostConnection: keep-alivesec-ch-ua: "Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"sec-ch-ua-mobile: ?0sec-ch-ua-platform: "Windows"Upgrade-Insecure-Requests: 1User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9Sec-Fetch-Site: noneSec-Fetch-Mode: navigateSec-Fetch-User: ?1Sec-Fetch-Dest: documentAccept-Encoding: gzip, deflate, brAccept-Language: en,uk-UA;q=0.9,uk;q=0.8,en-US;q=0.7'
        res = webserver.parse_request(request)
        self.assertEqual(res, "/background2.jpg")

if __name__ == "__main__":
    unittest.main()
