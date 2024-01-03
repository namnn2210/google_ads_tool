from seleniumbase import Driver
import time

if __name__ == '__main__':
    driver = Driver(uc=True, headless=False)
    url_login = 'https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fads.google.com%2Fnav%2Flogin%3Fdst%3D%2Faw%2Fbilling%2Fsettings%3Focid%253D997744739%2526euid%253D644410729%2526__u%253D7075053921%2526uscid%253D997744739%2526__c%253D3548678411%2526authuser%253D0%2526fbclid%253DIwAR3jGW6Bki8L7OA-u6kLEr1Csdt0orwxKyirABn9Ab6OjpyZoAruLM6Rtr0%26pli%3D1%26a%3D1&faa=1&ifkv=ASKXGp1uL64n6aHIlA3cRf3XMydCgTVsavxs3JvuyN4CyBz9aiGC96eFWdA_p3lZ0y7hXBUuOKyo&rip=1&sacu=1&service=adwords&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1175388492%3A1704265390249159&theme=glif'
    driver.get(url_login)
    driver.type('#identifierId', 'feuer.personius31ym@gmail.com')
    driver.click('#identifierNext')
    time.sleep(2)
    driver.type('name=Passwd', 'jngqkqvq1e')
    driver.click('#passwordNext')
    time.sleep(5)
    driver.click('button[aria-label="New Google Ads Account"]')
    time.sleep(5)
    driver.click('button[class="start-button"]')
