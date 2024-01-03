from seleniumbase import Driver
import time

if __name__ == '__main__':
    driver = Driver(uc=True, headless=False)
    url_login = 'https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fads.google.com%2Fnav%2Flogin%3Fdst%3D%2Faw%2Fbilling%2Fsettings%3Focid%253D997744739%2526euid%253D644410729%2526__u%253D7075053921%2526uscid%253D997744739%2526__c%253D3548678411%2526authuser%253D0%2526fbclid%253DIwAR3jGW6Bki8L7OA-u6kLEr1Csdt0orwxKyirABn9Ab6OjpyZoAruLM6Rtr0%26pli%3D1%26a%3D1&faa=1&ifkv=ASKXGp1uL64n6aHIlA3cRf3XMydCgTVsavxs3JvuyN4CyBz9aiGC96eFWdA_p3lZ0y7hXBUuOKyo&rip=1&sacu=1&service=adwords&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1175388492%3A1704265390249159&theme=glif'
    driver.get(url_login)
    driver.type('#identifierId', 'stanzak.cristiangzvr8a1@gmail.com')
    driver.click('#identifierNext')
    time.sleep(2)
    driver.type('name=Passwd', 'xkhskbqjo3sr')
    driver.click('#passwordNext')
    time.sleep(5)
    div_selector = f"div:contains('Name and address')"
    driver.click(div_selector)
    driver.click('input[name="ORGANIZATION"]')
    driver.type('name=ORGANIZATION', 'NTP TECHNOLOGY COMPANY LIMITED')
    driver.type('name=RECIPIENT', 'NTP TECHNOLOGY COMPANY LIMITED')
    driver.type('name=ADDRESS_LINE_1', 'Số 17 ngách 35, ngõ 135 phố Đội Cấn, Phường Ngọc Hà, Quận Ba Đình, Thành phố Hà Nội, Việt Nam')
    driver.type('name=LOCALITY', 'Hanoi')
    driver.type('name=POSTAL_CODE', '100000')
