# -*- coding: utf-8 -*-
"""
Project: PayPalRefund
Filename: Currencies.py
Description

list of currencies currently in circulation

taken from https://www.currency-iso.org/iso_index/iso_tables/iso_tables_a1.htm


"""

__author__ = "Guido Boehm"
__filename__ = "Currencies.py"
__credits__ = [""]
__license__ = ""
__version__ = "0.0.1"
__maintainer__ = "Guido Boehm"
__email__ = "olb@family-boehm.de"
__status__ = "Prototype"
__copyright__ = """
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
"""

from enum import Enum


class Currencies(Enum):
    AFN = (object(), 'Afghani')
    DZD = (object(), 'Algerian Dinar')
    ARS = (object(), 'Argentine Peso')
    AMD = (object(), 'Armenian Dram')
    AWG = (object(), 'Aruban Guilder')
    AUD = (object(), 'Australian Dollar')
    AZN = (object(), 'Azerbaijanian Manat')
    BSD = (object(), 'Bahamian Dollar')
    BHD = (object(), 'Bahraini Dinar')
    THB = (object(), 'Baht')
    PAB = (object(), 'Balboa')
    BBD = (object(), 'Barbados Dollar')
    BYR = (object(), 'Belarussian Ruble')
    BZD = (object(), 'Belize Dollar')
    BMD = (object(), 'Bermudian Dollar')
    VEF = (object(), 'Bolivar Fuerte')
    BOB = (object(), 'Boliviano')
    BRL = (object(), 'Brazilian Real')
    BND = (object(), 'Brunei Dollar')
    BGN = (object(), 'Bulgarian Lev')
    BIF = (object(), 'Burundi Franc')
    CAD = (object(), 'Canadian Dollar')
    CVE = (object(), 'Cape Verde Escudo')
    KYD = (object(), 'Cayman Islands Dollar')
    GHS = (object(), 'Cedi')
    CLP = (object(), 'Chilean Peso')
    COP = (object(), 'Colombian Peso')
    KMF = (object(), 'Comoro Franc')
    CDF = (object(), 'Congolese Franc')
    BAM = (object(), 'Convertible Mark')
    NIO = (object(), 'Cordoba Oro')
    CRC = (object(), 'Costa Rican Colon')
    HRK = (object(), 'Croatian Kuna')
    CUP = (object(), 'Cuban Peso')
    CZK = (object(), 'Czech Koruna')
    GMD = (object(), 'Dalasi')
    DKK = (object(), 'Danish Krone')
    MKD = (object(), 'Denar')
    DJF = (object(), 'Djibouti Franc')
    STD = (object(), 'Dobra')
    DOP = (object(), 'Dominican Peso')
    VND = (object(), 'Dong')
    XCD = (object(), 'East Caribbean Dollar')
    EGP = (object(), 'Egyptian Pound')
    SVC = (object(), 'El Salvador Colon')
    ETB = (object(), 'Ethiopian Birr')
    EUR = (object(), 'Euro')
    FKP = (object(), 'Falkland Islands Pound')
    FJD = (object(), 'Fiji Dollar')
    HUF = (object(), 'Forint')
    GIP = (object(), 'Gibraltar Pound')
    XAU = (object(), 'Gold')
    HTG = (object(), 'Gourde')
    PYG = (object(), 'Guarani')
    GNF = (object(), 'Guinea Franc')
    GYD = (object(), 'Guyana Dollar')
    HKD = (object(), 'Hong Kong Dollar')
    UAH = (object(), 'Hryvnia')
    ISK = (object(), 'Iceland Krona')
    INR = (object(), 'Indian Rupee')
    IRR = (object(), 'Iranian Rial')
    IQD = (object(), 'Iraqi Dinar')
    JMD = (object(), 'Jamaican Dollar')
    JOD = (object(), 'Jordanian Dinar')
    KES = (object(), 'Kenyan Shilling')
    PGK = (object(), 'Kina')
    LAK = (object(), 'Kip')
    KWD = (object(), 'Kuwaiti Dinar')
    MWK = (object(), 'Kwacha')
    AOA = (object(), 'Kwanza')
    MMK = (object(), 'Kyat')
    GEL = (object(), 'Lari')
    LVL = (object(), 'Latvian Lats')
    LBP = (object(), 'Lebanese Pound')
    ALL = (object(), 'Lek')
    HNL = (object(), 'Lempira')
    SLL = (object(), 'Leone')
    RON = (object(), 'Leu')
    LRD = (object(), 'Liberian Dollar')
    LYD = (object(), 'Libyan Dinar')
    SZL = (object(), 'Lilangeni')
    LTL = (object(), 'Lithuanian Litas')
    LSL = (object(), 'Loti')
    MGA = (object(), 'Malagasy Ariary')
    MYR = (object(), 'Malaysian Ringgit')
    MUR = (object(), 'Mauritius Rupee')
    MZN = (object(), 'Metical')
    MXN = (object(), 'Mexican Peso')
    MDL = (object(), 'Moldovan Leu')
    MAD = (object(), 'Moroccan Dirham')
    BOV = (object(), 'Mvdol')
    NGN = (object(), 'Naira')
    ERN = (object(), 'Nakfa')
    NAD = (object(), 'Namibia Dollar')
    NPR = (object(), 'Nepalese Rupee')
    ANG = (object(), 'Netherlands Antillean Guilder')
    ILS = (object(), 'New Israeli Sheqel')
    TMT = (object(), 'New Manat')
    TWD = (object(), 'New Taiwan Dollar')
    NZD = (object(), 'New Zealand Dollar')
    BTN = (object(), 'Ngultrum')
    KPW = (object(), 'North Korean Won')
    NOK = (object(), 'Norwegian Krone')
    PEN = (object(), 'Nuevo Sol')
    MRO = (object(), 'Ouguiya')
    PKR = (object(), 'Pakistan Rupee')
    XPD = (object(), 'Palladium')
    MOP = (object(), 'Pataca')
    TOP = (object(), 'Pa’anga')
    CUC = (object(), 'Peso Convertible')
    UYU = (object(), 'Peso Uruguayo')
    PHP = (object(), 'Philippine Peso')
    XPT = (object(), 'Platinum')
    GBP = (object(), 'Pound Sterling')
    BWP = (object(), 'Pula')
    QAR = (object(), 'Qatari Rial')
    GTQ = (object(), 'Quetzal')
    OMR = (object(), 'Rial Omani')
    KHR = (object(), 'Riel')
    MVR = (object(), 'Rufiyaa')
    IDR = (object(), 'Rupiah')
    RUB = (object(), 'Russian Ruble')
    RWF = (object(), 'Rwanda Franc')
    SHP = (object(), 'Saint Helena Pound')
    SAR = (object(), 'Saudi Riyal')
    RSD = (object(), 'Serbian Dinar')
    SCR = (object(), 'Seychelles Rupee')
    XAG = (object(), 'Silver')
    SGD = (object(), 'Singapore Dollar')
    SBD = (object(), 'Solomon Islands Dollar')
    KGS = (object(), 'Som')
    SOS = (object(), 'Somali Shilling')
    TJS = (object(), 'Somoni')
    ZAR = (object(), 'South African Rand')
    LKR = (object(), 'Sri Lanka Rupee')
    XSU = (object(), 'Sucre')
    SDG = (object(), 'Sudanese Pound')
    SRD = (object(), 'Surinam Dollar')
    SEK = (object(), 'Swedish Krona')
    CHF = (object(), 'Swiss Franc')
    SYP = (object(), 'Syrian Pound')
    BDT = (object(), 'Taka')
    WST = (object(), 'Tala')
    TZS = (object(), 'Tanzanian Shilling')
    KZT = (object(), 'Tenge')
    TTD = (object(), 'Trinidad and Tobago Dollar')
    MNT = (object(), 'Tugrik')
    TND = (object(), 'Tunisian Dinar')
    TRY = (object(), 'Turkish Lira')
    AED = (object(), 'UAE Dirham')
    USD = (object(), 'US Dollar')
    UGX = (object(), 'Uganda Shilling')
    COU = (object(), 'Unidad de Valor Real')
    CLF = (object(), 'Unidades de fomento')
    UYI = (object(), 'Uruguay Peso en Unidades Indexadas (URUIURUI)')
    UZS = (object(), 'Uzbekistan Sum')
    VUV = (object(), 'Vatu')
    KRW = (object(), 'Won')
    YER = (object(), 'Yemeni Rial')
    JPY = (object(), 'Yen')
    CNY = (object(), 'Yuan Renminbi')
    ZMK = (object(), 'Zambian Kwacha')
    ZWL = (object(), 'Zimbabwe Dollar')
    PLN = (object(), 'Zloty')

    def __new__(cls, member_value, member_phrase):
        member = object.__new__(cls)

        # set up instance attributes
        member.currency_name = member_phrase
        return member
