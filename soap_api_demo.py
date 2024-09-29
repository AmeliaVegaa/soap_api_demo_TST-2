import requests
import xml.etree.ElementTree as ET

# Meminta input dari pengguna
arg1 = input("Masukkan angka pertama (pembilang): ")
arg2 = input("Masukkan angka kedua (penyebut): ")

# URL API SOAP
url = 'https://www.crcind.com/csp/samples/SOAP.Demo.cls'

# Body XML untuk request SOAP (method DivideInteger) dengan input dari pengguna
soap_request = f"""<?xml version="1.0"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org">
   <soapenv:Header/>
   <soapenv:Body>
      <tem:DivideInteger>
         <tem:Arg1>{arg1}</tem:Arg1>  <!-- Angka pembilang dari user -->
         <tem:Arg2>{arg2}</tem:Arg2>  <!-- Angka penyebut dari user -->
      </tem:DivideInteger>
   </soapenv:Body>
</soapenv:Envelope>
"""

# Headers untuk SOAP request
headers = {
    'Content-Type': 'text/xml; charset=utf-8',
    'SOAPAction': 'http://tempuri.org/SOAP.Demo.DivideInteger'
}

# Kirim request ke API
response = requests.post(url, data=soap_request, headers=headers)

# Cek status kode HTTP
print("HTTP Status Code:", response.status_code)

# Cek response text jika statusnya 200 OK
if response.status_code == 200:
    print("Response:", response.text)

    # Parsing XML response dengan namespace
    namespaces = {'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/', 'tem': 'http://tempuri.org'}
    root = ET.fromstring(response.text)
    
    # Ambil nilai dari elemen yang berisi hasil pembagian
    result = root.find('.//tem:DivideIntegerResult', namespaces)
    
    if result is not None:
        print(f"Hasil pembagian {arg1} / {arg2}:", result.text)
    else:
        print("Tidak dapat menemukan hasil pembagian di response.")
else:
    print("Error:", response.text)
