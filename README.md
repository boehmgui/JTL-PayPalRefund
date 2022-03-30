# PayPal Erstattungen

Dieses Skript erstattet einen per Paypal bezahlten Betrag ganz oder teilweise.

Es implementiert den "Refund captured payment" Teil der Payments API von PayPal, welche hier beschrieben ist:
https://developer.paypal.com/api/payments/v2/#captures_refund

# Vorbereitungen

Das Skript kann entweder direkt als Python Skript, oder als Windows .exe, die im Releasebereich dieses
Repositories zur Verfügung steht, ausgeführt werden.

## Benötigte Dateien

Folgende Dateien werden benötigt und müssen auf der lokalen HD in einem gemeinsamen Verzeichnis abgelegt werden:

- pp_refund.py (nur wenn man das Skript direkt als Python-Skript ausführen möchte)
- requirements.txt (nur wenn man das Skript direkt als Python-Skript ausführen möchte)
- pp_refund.exe (aus dem Releasebereich)
- config.yaml

## Konfigurationsdateien

### Zugangsdaten

- Generieren der Zugansgdaten für PayPals REST API gemäß Beschreibung: https://developer.paypal.com/api/rest/#link-getcredentials

Die so erstellten Zugangsdaten dann in folgende zu erstellende Dateien eingetragen.

**Wichtig**: .env.* Dateien müssen im gleichen Verueichnis wie das Skript (.py oder .exe) liegen.

- PayPals Live System: ```.env.production```
- PayPals Sandbox: ```.env.sanbox```

Beispiel

```
# API Zugangsdaten wie hier beschrieben generieren
# https://developer.paypal.com/api/rest/#link-getcredentials
Client_ID=AaNSfvjN3aV3rTaEd2d0n51foIzhbmnlkrmuw3zk0oqFEFjWQ72jp0Jy3EzSuev5LCoyzYyxbl9ikmPOo
Secret=EGnt5uUA1TB0Mw43yWPtrgsGcUghgn76fd9DId5i_kgdSYJ8Ef1qQ0Zxti00U4v7mTvqFIwKuuhkmPK9m-
```

### config.yaml

Diese Datei enthält die URLs zur PayPal API (Live und Sandbox). Zum Testen kann man hin und her wechseln indem man
die Variable ```LiveModus``` von ```True``` auf ```False``` ändert.
Weitere Änderung sollte man nicht durchführen

```
# Soll die Live API oder Sandbox AP benutzt werden?
# True -> Live API
# False -> Sandbox
LiveModus: True

# nur auf Anforderung ändern
Debug: True

# PayPal API Dokumentation:
# https://developer.paypal.com/api/payments/v2/#captures_refund
SandBoxAPI:
  BaseUrl: 'https://api-m.sandbox.paypal.com'
  EndPoint_Token: '/v1/oauth2/token'
  EndPoint_Payments: '/v2/payments/captures/{capture_id}/refund'

LiveAPI:
  BaseUrl: 'https://api-m.paypal.com'
  EndPoint_Token: '/v1/oauth2/token'
  EndPoint_Payments: '/v2/payments/captures/{capture_id}/refund'

```

## benötigte Python Module (nicht notwendig, wenn Windows .exe verwendet wird)

Installieren der Python Module

```
pip install -r requirements.txt
```

## Skriptstart

### Aufruf als Windows .exe

```
pp_refund.exe -p capture_id=<pp Transaktionscode> amount= <Betrag> currency_code=EUR invoice_id=>Rechnungs-/Auftragsnummer> note_to_payer=<"Erstattugnsgrund">
```

### Aufruf als Python Skript

```
python3 pp_refund.py -p capture_id=<pp Transaktionscode> amount= <Betrag> currency_code=EUR invoice_id=>Rechnungs-/Auftragsnummer> note_to_payer=<"Erstattugnsgrund">
```

## Kommandozeilen Parameter:

Mandatory:

- ```capture_id```: Transaktionscode der Transaktion welche erstattet werden soll. E.g. 2AB57058X62543450

Optional:

- ```amount```: Betrag der erstattet werden soll. Wenn nicht angegeben, wird der gesamte Betrag erstattet. **Achtung**: Betrag muss mit Dezimalpunkt geschrieben werden, e.g. 99.25 - (manadatory, wenn currency_code angegeben ist)
- ```currency_code```: [Währungscode](https://developer.paypal.com/docs/integration/direct/rest/currency-codes/) (mandatory, wenn amount angegeben ist)
- ```invoice_id```: Referenz, zB Rechnungs oder Auftragsnummer. **Achtung**: muss eindeutig sein (optional)
- ```note_to_payer```: Erstattungsgrund - Text in "" einschliessen wenn Leerzeichen enthalten (optional)

## Logs

Das Skript schreibt für jede Erstattung eine Logdatei

- Erfolgreiche Erstattung:
  \<skript-dir>/logs/<capture_id>.txt

```YAML
Method: get_token
url=https://api-m.sandbox.paypal.com/v1/oauth2/token
headers={'Content-Type': 'application/x-www-form-urlencoded'}
payload=grant_type=client_credentials
http status code: 200 - OK

Method: refund_transaction
capture_id: 0242518980917994X
url=https://api-m.sandbox.paypal.com/v2/payments/captures/0242518980917994X/refund
payload={}
http status code: 201 - Created
```

- Fehlgeschlagene Erstattung:
  \<skript-dir>/failed-refunds/<capture_id>.txt

```YAML
Errormessage: 404 Client Error: Not Found for url: https://api-m.paypal.com/v2/payments/captures/0242518980917994X/refund

Method: get_token
  url=https://api-m.paypal.com/v1/oauth2/token
headers={'Content-Type': 'application/x-www-form-urlencoded'}
  payload=grant_type=client_credentials
http status code: 200 - OK

Method: refund_transaction
capture_id: 0242518980917994X
  url=https://api-m.paypal.com/v2/payments/captures/0242518980917994X/refund
  payload={}
http status code: 404 - Not Found

  full debug data

  refund request failed
debug_id: e12e60044068d
details:
  - description: Specified resource ID does not exist. Please check the resource ID
      and try again.
    field: capture_id
    issue: INVALID_RESOURCE_ID
    location: path
    value: 0242518980917994X
links:
  - href: https://developer.paypal.com/docs/api/payments/v2/#error-INVALID_RESOURCE_ID
    rel: information_link
message: The specified resource does not exist.
name: RESOURCE_NOT_FOUND
```

**Achtung**: Das Skript betreibt kein "house keeping". Es sollten also von Zeit zu Zeit alte Logs gelöscht werden

#Famous last words...

Copyright 2022, Guido Boehm
All Rights Reserved.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
