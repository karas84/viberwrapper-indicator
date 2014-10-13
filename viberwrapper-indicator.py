#!/usr/bin/python
# -*- coding: utf-8 -*-

# Created on: 8 Oct 2014

__author__ = 'karas84'

import pygtk
import gtk
import gobject
import appindicator
import sys
import os
import threading
import time
import subprocess
import tempfile
import PIL.Image

import Xlib
import Xlib.ext

from Xlib import X, display, xobject


pygtk.require('2.0')


class ViberIcons(object):
    ICON_NORMAL = """iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJ
                    bWFnZVJlYWR5ccllPAAACzNJREFUeNrsXU1oFFccn12C1So0qbQkl2YXFDQRTC5RD9IsPVmFGEtb
                    tFCMt0qltS0UerDioVCw1dJibyYp1NKUagTFU8mKh6CXrKC2YGHXXgwt6graWi/p+03e275MZt73
                    fGw2fxg2xuzOzu/3/37/eZPzMiBzc3MF8oKjjxzt5Oim//a435lImfu5Qo6H5KjRo5LL5eppX3su
                    JbAHybGZgjuY4vXXKTGX6Ws5aVJyCQDeTkEeoq8FL9tSoZZzmZAx2bQEEOD3U9B3e80rsAaQcD4u
                    MnKOQYd2v0eO/RZ+O6uCuDFOjpMu3VTOIfCfUuCXujCrOOyCiJwl8O0U+Pdju9o/H3n1vx5pv6/Q
                    25kEEV8REo6mQgABHwF11EVQrd2c9e5W73tP/n7q1W7c9X9XJb9zJZ2F571Vq1d4ncXnvZWrn/GK
                    hJz2F9Z47S+uceWaRggR5cQIIOCfMNX6J4+f+uDWbt71qjdmvdna/dR8yUpCShchp7CpyyfF0mrg
                    kk7GSgB1OaO6mQ1A//XaH95v1+74r1mWjQMveRsGuv1XEKQpY4SEkTgJmNIpnKDd0xduejNTvzdl
                    tO0vrSPHel3L0CIhpwH+qGqWA+Avnb7q1I+nKYgVpTf6fUJck5BTBB/+/oSKq7k0erVpNV4lmL96
                    YIuqRSAwj1kTQMBHv2ZKVlghkznz+S8+CUtdtu3q8XaMbFFJU/sJCTVbAqR+Hxp/7psrXisJsqa9
                    H78iC9Ro7pVEf5BX6Ocsgx8iiG8/EIuXyCDBcLexBZA3V0WFFlJKhS/R6u6oRqygGPWfbRLtL4ha
                    BGlq/vC72xtZSY1mWw9o2wLVdFIZ2PSFWyQod/l1Q1RXBFhGBeScqfaPHrmUapp57Gd5lscXf3Em
                    B0hTDx4fEsWDyFiQiwAffutcnK4HKR2rGUxNf+NAd6OlwD5PVIlPTcz4lhuHlN7sJ7VCn7CuIyRU
                    VAkQFl1fvvOT8YUAOBQ1TFvwOUhfXfSEoIl+b4e4hOKmzlBSpiYqfnXu2iJwPR98+7rICrCOcFhK
                    AO33PHCd9QCcfSRtCwMFYJz66Lxz7cS50EpArOCBcUk6LwjGUDCdYJzTdT+nPjyv/cUBxIFjO4Q5
                    Mz7zNIkrcfhqnHfbrt5FLgJVO4Koy1gAK9BxQ2F1wJAIpDjAZ3+nUF0uEmQfyIh8H0wOFEjBc4HU
                    qR9nfNdZ4xIHnA/vdSWwLAk+u1UsIDL70dUYhezA+hwgN6w3AyBmpm77LjNoVcGA6bKYlNQFi7Kh
                    fAD8gqzw0pE9RLt0e+r48qKMJihYSRNZ1CffveVrOf89YA084IgRJtZngNGg0AJE/h/mBRPWcT0H
                    vxgyNmUEZZ14gPN1EIvrLK713VKQxLBOLYDnXRBIcdHJRRwQLHeW+OXLYAzoE/U+tHzzlm6rYIag
                    qSNwOX6uT7QbiQKUBSknIxEWALB5wIOuB1bgYp1YglWfKAhvjr7Ae4lWuvDRNmDAiljg5WNKUOtB
                    AtN6kLTHQVCWYLVZRECk/5+tJr947gIM5npEPh//z2oQBHRBX0eNADFWBREBzlwQGy+xEYChGpAR
                    b9AfwgEfDC3nLSjobpCtFGn2BJKCrihGFzQYSgCtgCO1yORLuKhsu4pqBPBEAXhoOYgAmCwDAgnQ
                    diZ8djQ/KjPbeL+tFahee15F+01L9plycmvDaA4i6AJEXmGg6WiBMEE84IHmgz1iRgOM0no7AgTT
                    fHSoLbISXiT/GLYHUAjFnFEsyL8BINoZn739va/pjAi4MhRfTM7y8WBwXajVGs4FNeSBgQW0u7YA
                    XIxNXg1tNXVjeC/IaFjCzp4FHVj2vYLuhi+kbNyQZJ61oOWCbAStXxNBUOT9tVk6eN93SyzF5AHF
                    Qs3/wb4r1Gr53zuWgpYLsgWhppFB+a1pUki5mi3iAd0w0B2q6Xygx/dlrks1AQhPRe9puyDrD4sS
                    PripBFOXfXq4GwboqoBPZ4oRbOax8+v0pEwzx7zLDxMFUlWNjmOdmQEaBDoqUPLfoRjzfQaxu6CG
                    FUyoWYFN5hElrGMa7FTygZLX9ieP/00sfU6MANWMyLYAChME8yOvjQoHCXj3xLcScO/AkiCAASFz
                    Z7pdULuezb2Gi01rxCZRAnCh0xdvSVsKxfjv72q4JHRLUbilJfmkT4iMSFZc8VVrEq7RVeXfFASw
                    IktYpThoCdtmTWz1zLSQzDQB8LeyhXe+i5mG4PtBUeK+3yGf1gXKxgTRo3G1UJ6GqCpPagRAs85I
                    5kvnb5Jb15QEYDgg0wTwvlYkWDRJKitKUGqZIID5WlmBtjdiprRlCIi7GoQViBpw8KdY8zVxR/Nz
                    oT0+ifxNHXGLqtXyBJTTjAcqg7kAUCcws2FZvAdpLRtJwe9Sdmt1LQtY+eyKzJAAbYY1yACE5u+L
                    uIsRxIwc27FoZNGlYDOQKOEnpPNhfikoNgsTukFZhQTEAwCIwdwoIlRmTNnkRBzWoDpUFpwNnYsC
                    BqtUiaVwiiPtfDth+uLNRhdz665e7UoaS5c6C0cqri9CsFtjfxQB+Aaha8No5yaaRxMS4EIc7emj
                    JGjOuah+YVGw0AhZMKKej0qPTKO6S3eECekk9xOC1cDybFPeTrHLFt4hc93wQ2MLzC4X6HXcnw0J
                    kmmKhyICyoYfGqvALSTRGOMzKJuWeJeYvLKIgEpWXFBQYAXIkJJySabtcFiOJG5FuyC6DWMlSivS
                    7NHz2Rgbtoq1UjKcyMP9ySLwg1td5mUmwgs/2JSmhN3xGEdGZCLbdvYqu58oAsZFhUuaiyRBDYVL
                    QmxwfYO3f1vrhH5N4G+HKXY/l6UE0DK5Ft0K6PWyJIgNSFf5+8FcBH2Tz9oqxqYetv90VC9oPNrE
                    ejJjBQs0lrolWyLQHjdxP0X5Onbo5t9RBIyJUrSsLhUyImARYTdoq1iT6US2Qto6Lu0FBdoSwh1T
                    0t4vSDWfh8tUsVpovin4NrtmiQgokJeqKAjq3kydpiCBYDviBq8DwJtmPYqNwxHtHbNUrCDpLqkL
                    QZbSQXv1GMCyKez8lbrjQ7LMR7hnnIwAWAHysXaR32zFXRMBvmLPqCTaWV1l31DprrmttGkrczt7
                    Dm1XAX+SgD8s+gPVrYulm7fClM9+fSXV7eiTiiWKU3uopfplT9lQJaCduqKCtE0Q055sWYgd2DpB
                    Yyf10E36jAigJCjtIc0yC5TyS2ETb7gZpLKa4yxKG3drEaBLAiuM5ncjud1UrgmgY7sd3MRtsCSq
                    DL42ASYk8Fahs+FT0oCjjYx9SPGzRatFC3xIm+4Z4NcICUVKgvLN3UkurotSxy66YNJZWOuP2zh6
                    2lKdppvaCxVtJmejkb2fEHHUm3+MVezAodmlEtjZk5J80knB1UGJj/GxVpNU842eKdZmc2Y8Q4uQ
                    MEnrhMG4rhATbGmvxkWkmYdtH3FoPR0Ns6NzLjjKrq+SzXVmDHhofNHF8yWdjaej3KZEoC875nED
                    qDZFj2Ar4KRlkgN+zNWHOr8/gFoEvmgHvIepVSAbcbmrrWFgBdDYJ78DLQWXwDuJAQpkTNK0VSs+
                    IEs5ED3aFyfgUBas25ZNMprMEWCa8eyTPxzHVsoUcEwCAuiK7GlHLUNAyBb3MPs73L9fVgiS/N9X
                    WDwyfeBmsxPwnE66GcjXtZ/N2GySxE16StUysp1Aw2tyqYOfFAFK6WZgUbtCsw9vmYCYJeTBDTXa
                    V6kvE5AA+IGJAoA+3Crgp0qAv1P5oe1B8EtJ5d+tREA9DPyQiYLhVgM/KQKu8xUuq3ID4I9kMUdf
                    EoLHosyJZf8ySvGTUF0GP10C+jBbxAFflT1nt1XkPwEGAObH45cGp22ZAAAAAElFTkSuQmCC"""

    ICON_NOTIF = """iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAABmJLR0QAAAAAAAD5Q7t/AAAACXBI
                    WXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH3goIDjYaFQSitAAADeRJREFUeNrtXW1wU1Uafk5TS2kL
                    JumH6Sr0RipC40CjK1jHKl1md7ZjZ2tBZZZhZ2gdf5SFRYWRHzBVO/CDWZBx6MIPB4qzDC4oUpxK
                    dXeYtFvdUlxJypiiUDcR1iGU0oaP0lIbzv7IDRtizrnn3nxdC+9MhpJz783J+5zzvB/nPScEOhBK
                    qQRAAlAKwAigSP4/wt7TIu1hf7sAXAbglV8uQoifUpoPwAbgcfllAzCdUppFCLkO4CwAN4Av5Zeb
                    EHIxXt+dpEjZCwDMlZW7ADoUSikIYapnHMBbAPYRQv6jawAopUZZydXyvxImlvQC+COADkII1Q0A
                    lNLlstKfw50hHgDPE0JOpAwAmV5WA1geA2//3GU7gHWEkJGkASAr/g1Z8XclaCNshJDTCQVA5vc3
                    ALySqG/i778G/8Vrqu7JzMqAxWpWdc/NiwMYP3Ua41+5MP6VC4Heb2EoeRjpj5UGX7NnIi0/T233
                    Kwgh7QkBgFK6AEBzPIyq1+3Dec8gRq+Pwfv1+SChun2anjXz0QewbP2vha4NeL7Hjf0f4fqmrUAg
                    oHyDwYCs9WswackiGKxFol2qIoR8ElcAKKXbtI760eExeNw+eN3n4fnaB593MG6zRbJZUNdYqcwP
                    zpO4+tIqBL45rfmzDLNmYsqu7Ui3z4lpJhANlNOs1rMZHR7DqeNn8c3x73Hq+NmEUFVu4VSsblrM
                    7//ICIY3bMTozt1x+9zM+jpkb9wAMnmy0qUPR7MJagFwqAmcfN5BdLW64XT0JdTipWcYsH7vMhgM
                    aWy6OfMdhh59RoxqVE8HA0wnOmB4aIaSYZ4a6R2lq1B+s6jyfd5BtO3u1szjauU3f/glV/lj//wX
                    rvx2ceI6EAhgaO5TmPrpQWQ8/SRznADYDOBPqmcApfQVANtEqKatuTvhIz5cCq25qN/yu9QpP0IU
                    QACAx8KDNSKg/FIADqXAyuv2Yd/moxgdHkuqw/3qjudhum8Km3bmPpX0IMDU8zmPjjwAZoTSFmkC
                    z9umpHynow+7G9qSrnzJZmEqn46MBDk/BTL06DOgI8xA2ArgVsfSBPI5C5SUf6ipMyVftOrlMmbb
                    8IaNiTG4gjZheMNG3hV/EQJAjnKZcur42ZQp33RfDgqmGZl+fjxdTU3xzs7dGHeeZDWXUEof5AIg
                    j36JlyJIlfIBYMnaXzHbrr60ShcJIYV+LFWaAdzRf6ipM+mcHy6/eDCXmV6IJcKNKxN9cxoBz/dc
                    /aYxRv9zvNF/6vjZmH18i2SGRTJrujdr6iRm2439H0FPwulPOqU0n3CCruWsO9+u/wD+/muaOlRW
                    VYKKF+3IzM64RWX7Nh9VlRPi5XwGpjyQOuPLiJLzrv6XmSNKY+R7lvO8Hi3KNxbkYMXWalTWzr+l
                    /ND7dY2VMBbkCD/r/uLoaeGbFwf0pXzZI7p5cYDV+ng0CuK6nV2tbk10s2JLNZNyMrMzsHTdwtuA
                    0QLA+KnT0KNw+hUVgGpejkdt+tgimVHXWKmoXItkRmXtfKFnFkwzRf+iX7n0CQC7XzZVM8DpOKOa
                    dkSUHxJ7RTHKqkoUr7s3L3uiADA9LYL/JSXvR40sWlkurPyQVNbOV/SO7pkUPYkb6P1WlwBE6xel
                    FJTSSZEzoJQXeKkxvhbJDMlm0dRhJXvw443x6A5HycO6BCBavwghIITcEAZArd8/e36R5g4bC3JQ
                    VmVjtl8eGI7uWD9WqksAOP06GwnAXLYBvpTUTle8WMp0TfvPDU0UANyRADD53+cZTHrHF60sj/r+
                    D33R/er02TP1CQC7X18mjIJC5SWxiGSzRDXILADS8vMAg0FnBsDAqyf6PwByBBxVtCTdPG6f5nRF
                    uBRGKbBiURAAZK1foyv9K/TnNgoq5QVgWsTZnpi14etXbiAQuBm1bdKSRboCgNOfcULIRZElSYxo
                    TDurDdzUUF/7gejBjcFaBMMsfdgCw6yZvAq6t4Db09HGeM8Af/+1mCokulp7mTR2svM75n1Tdm3X
                    BQAK/dgXCUBCfDgtyTsguODT1tzNbB+6cA395/zRvQ77HGTW16VU+Zn1dbyyxYuhnTVpie6IzzsI
                    rwoPanR4DDvWHBaaOa3vdjHbsjduSJ1HZDAEP58tR255bkJK9MQWhDn2O4WvfV/F4ozX7cPQhatR
                    28jkyTCd6EiJ/k0nOpRqRb2qAIh17dfj9gnbArXxxt/+7GAPxIdmYOqnB5Oq/KmfHlSqEb09dklW
                    xxwHxGaB2uzpec8lHDvSy2zPePrJpIEgUJaYOgBEPaLZ86arfvbf//pvZlwQAsHU83nibILBAFPP
                    56qVn1QAAKCtuVuRznhZUGZEMxZA0+pDfB09NAO5/Wfi7h1l1tcht/+MKtpJGQCjw2Po+qSXe41F
                    MsOqYR3h0vkr2N3Qxr2GTJ6MnK2bYPzis5iDNcOsmTB+8Rlytm4S2ZyhDwBCHpFSjqhiiV3Ts71u
                    H/Zu+ofiden2OTCd6IDJfQxZDa+LU5PBgKyG12FyH4PpRIfo9iT+oAj9QSl9E4xquOaGtrhutrDa
                    LKhV2Mv1/uajmrczie4VC5cE7ZJkpiEIIW8CKnbIxFM8bh+6Wnu5C/CVtfPhcfs0ucBetw/vrDyI
                    le/UcHfO3EYF+XnIyM/TZEgjJRC4iZamTixe/Yz+KCjcLeVRkbEgR7hMhWUTNi3by3VREyHHjvRi
                    07K9GBsd16cNCDfI+zYf5V5jryiGvaJY82eMjwVwZFc3dq79mBkxx0uGLlzFzrUf48iuboyPBWCx
                    5grdl44Uis87iLbmbu5Ir1lZDn//tZhs0HnPJWxb8SEkmwVVL5cx9xVokf5zfrS+26Uq3xWeikgp
                    AEAw5WyRcrkj/ffrFmJ3Q1vMm7q9bh+aXjkE0305mFM+AwteLBW2EZEc337AhZOd32HogqZVP3UA
                    SI8UJnTLaVtzNwqtZm7t6Iqt1TjU1Kl6fSEzOwP2imJItkKMDo/B6z4Pp6MPHR/2oOPDHmRNnYSC
                    aSbcX5yH+4vzUDDNhHvzsnHPpHT8eGMclweG0X9uCD/0DeCHvgH0nxvC9Ss3hDw9tW7oAgR3Q0Yx
                    mC5VGU1NEWV2Bl7b+YJiLqirtZe7ThBpyFdsqf7JM0O7exI5qOoaK3mFaXZCiEvYCGdmZSScikaH
                    x4R2WpZVlWDF1mrFEcaruDYW5KC2sRI1GkonRcWYzy63Dyk/EgAv64ZCqxnJEJ93UAgEi2RGbWMl
                    6hormUCI1JjaK4rx2s4XNKU+RGafKgqSaYiyFLNjzeGkGWbRkvZwSun6xH2reOyJKpvqrGo8adZY
                    kIPXdr7AanYRQuwsAJxgrA03LG5OqndkkcxYum6hqp0zsUpo222sC1AKqZZ2QkgFKxDzxmrV40lH
                    O9Yejut5Qkoye9501DVWat48eGvw8CnbxYuEezQ+NGGGWXSBPt70FwsIkq2Q13yZB0C7xocmVA41
                    dSZ1X3JmdobmlDgAFPLBa+cB4NILBUVK6ECQZFGSlqXR0AxSsFtsCiKE+FkgZGZnaO5UXO3CmsNw
                    HEj8XjCthcXWR7gD1SXrmDkDuDQ0a14R9CCO/U68Xf+B2gSYao9Ii5Q9axOmHxYA7/ECl0RFjlpG
                    6O6GNhxq6oxLGXyk8Rcto4mkaQX66VAEQA6TvexUgA16EqejDzvWBmkpXkZaq8F/gq8bPyGkRWQG
                    cGdB2bMlupkFt41YmZZiBaKrtVcT/VhtFiUb2RLtTRYAe3guWixLhckAYsfaYOygFgino0840xop
                    Am7re4q5oIi0BPfElHhXSiTKny+rsgnNWjVp7p/SconSoPQSQqxqAZAQPOGPaQR3rD2c0kOb1Ii9
                    ohiz5hX9hCb8/dfQ1tyt2esRTBzWEkL2qAJAZBYkO0saDzEW5MAk5+pHhsdiCuwyszOwYku1kufD
                    HP0iAEgAnOBsX0rlqYmppjfBnBH3CHuRg1sVT81N1aGtqRKLZMaiVeUiym8hhNTwLhA9uljx0G6f
                    dxAfbe9Mavo4VbYk8tQv1rhEcO3XHw8AjDIVSYppggMudLW6J9xsMBbkYNHKcjUnwNjD135jAkAG
                    QegM6ZBn4TjgTGoeP5F0U1ZlU1uhx/R6NAOgFoRQYOR09MHpOPOzoiaLZMbs+UWwLyjWsiQqrHzV
                    AGgBIXxWvF3/gW4Vbn3EgtnzimCRzLGkWlQpH9BQmkgIcVFKrTIIwpu7k7m4znMdC+UFE4uUi0Kr
                    9lO9IseX7G6qXqjQVBsqW3Y7b1NHvBVntVmEDLvFakZmdvBkXWN+Dkwy8FLiVvRa5JHv13JzTMW5
                    hJA3KaUtcpywIFHfsGZlecpX4xhu5qvRUsxqJOb9AYQQl1znUgHOappWqaydrzfle+URb41V+XEB
                    IAyIUMGRHcF0tj/WZ4qeI5okaQlT/J54PTTuO2TkGVFLCDEBqNE6KyySGTWMM+OSJH55INUCMBFC
                    auKp+LjYAAEwWmS3VZV9CJ24mwKFtyO4btuuxaPRHQBaPR41B3lrlHZZ4T0IluG4CCHeVHxf3QGw
                    dN3CyCzjHgDhP0OhtPfTG3G9K2SPlH7ZdKICcK8adzPCX99DCKnFBJZkbFMVipbLqkoiE14tE135
                    yQJAyN2MWNR2yd4H7gKQYInyww1eOa/ivwtAEpQfUVHgB1Bzpyg/pQBkZmdg0arySOVXJMv/vpMA
                    8EdTfpSKgpo7TfnJAqAnPMINRbkRyq/Vo48+IYRS+hzly/K7Wko8CJ67yk8tAKWUUkeY4j3y71Xe
                    8fI/bKPVDzA4zUcAAAAASUVORK5CYII="""

    INSTANCE = None


    def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")

        # do your init stuff

        self.temp_icon = tempfile.NamedTemporaryFile()
        self.temp_notif = tempfile.NamedTemporaryFile()

        self.temp_icon.write(self.ICON_NORMAL.decode('base64'))
        self.temp_notif.write(self.ICON_NOTIF.decode('base64'))

        self.temp_icon.flush()
        self.temp_notif.flush()


    @classmethod
    def Instance(cls):
        if cls.INSTANCE is None:
             cls.INSTANCE = ViberIcons()

        return cls.INSTANCE


    def get_temp_icons(self):
        icon_path = os.path.abspath(self.temp_icon.name)
        notif_path = os.path.abspath(self.temp_notif.name)

        return icon_path, notif_path


    def clean_temp_icons(self):
        self.temp_icon.close()
        self.temp_notif.close()


class XTools(object):
    """class description"""

    INSTANCE = None


    def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")

        # do your init stuff

        self.display = display.Display()
        self.root = self.display.screen().root


    @classmethod
    def Instance(cls):
        if cls.INSTANCE is None:
             cls.INSTANCE = XTools()

        return cls.INSTANCE


    def get_root(self):
        return self.root


    def get_display(self):
        return self.display


    def get_mouse_location(self):
        data = self.root.query_pointer()._data
        return data["root_x"], data["root_y"]


    @staticmethod
    def translate_coordinates(window, src_window, src_x, src_y):
        data = window.translate_coords(src_window, src_x, src_y)._data
        return data['x'], data['y']


    def get_input_state(self):
        data = self.root.query_pointer()._data
        return data['mask']


    def mousebutton(self, window, button=1, is_press=True):
        XButtons = {
            1: X.Button1,
            2: X.Button2,
            3: X.Button3,
            4: X.Button4,
            5: X.Button5
        }

        XButtonMasks = {
            1: X.Button1MotionMask,
            2: X.Button2MotionMask,
            3: X.Button3MotionMask,
            4: X.Button4MotionMask,
            5: X.Button5MotionMask
        }

        XEvent = {
            True: Xlib.protocol.event.ButtonPress,
            False: Xlib.protocol.event.ButtonRelease
        }

        root_x, root_y = self.get_mouse_location()
        state = self.get_input_state()
        x, y = self.translate_coordinates(window, self.root, root_x, root_y)

        if not is_press:
            state |= XButtonMasks[button]


        XEventFunction = XEvent[is_press]
        mouse_event = XEventFunction(detail=XButtons[button],
                                     root=self.root, root_x=root_x, root_y=root_y,
                                     window=window, event_x=x, event_y=y,
                                     same_screen=1, state=state,
                                     time=X.CurrentTime, child=0)

        window.send_event(event=mouse_event, event_mask=X.ButtonPressMask, propagate=1)


    def mouse_up(self, window, button):
        self.mousebutton(window, button, is_press=False)


    def mouse_down(self, window, button):
        self.mousebutton(window, button, is_press=True)


class XWindow(object):
    """class description"""

    def __init__(self, window):
        self.XTools = XTools.Instance()
        self.window = window


    def click(self, button=1):
        self.XTools.mouse_down(self.window, button)
        self.XTools.mouse_up(self.window, button)


    def double_click(self, button=1):
        self.click(button)
        self.click(button)


    def hide(self):
        Xlib.protocol.request.UnmapWindow(display=self.XTools.get_display().display, window=self.window.id)
        self.XTools.get_display().sync()


    def show(self):
        Xlib.protocol.request.MapWindow(display=self.XTools.get_display().display, window=self.window.id)
        self.XTools.get_display().sync()


    def move(self, x, y):
        win = xobject.drawable.Window(self.XTools.get_display().display, self.window.id)
        w_geom = self.window.get_geometry()._data
        win.configure(x=x, y=y, width=w_geom['width'], height=w_geom['height'])
        win.change_attributes(win_gravity=X.NorthWestGravity, bit_gravity=X.StaticGravity)
        self.XTools.get_display().sync()


    def read_image(self, width, height, save_to=None):
        pixmp = self.window.get_image(0, 0, width, height, Xlib.X.ZPixmap, 0xFFFFFFFF)
        rgbim = PIL.Image.frombytes("RGB", (width, height), pixmp.data, "raw", "BGRX")

        if save_to is not None:
            rgbim.save(save_to)

        return rgbim


class ViberIconPoller(threading.Thread):
    """class description"""

    def __init__(self, xviber_window):
        super(ViberIconPoller, self).__init__()
        self.viber_window = xviber_window


    def run(self):
        self.poll_viber_icon()


    def poll_viber_icon(self):
        vi = ViberIcons.Instance()
        temp_icon, temp_notif = vi.get_temp_icons()

        notified = False
        while True:
            time.sleep(1)
            n = self.is_notified()

            if n and not notified:
                notified = True
                ind.set_icon(temp_notif)
            elif not n and notified:
                notified = False
                ind.set_icon(temp_icon)


    def is_notified(self):
        viber_img = self.viber_window.read_image(22, 22)
        r, g, b = viber_img.getpixel((17, 4))

        if r >= 200 and g <= 50 and b <= 50:
            return True

        return False


class NoViberWindowFound(Exception):
        """class description"""

        def __init__(self):
            super(NoViberWindowFound, self).__init__("No Viber Window Found")


class ViberWindow(XWindow):
    """class description"""

    @staticmethod
    def get_viber_window():
        children = XTools.Instance().get_root().query_tree().children

        found_viber_window = None
        for window in children:
            try:
                w_class = window.get_wm_class()
                if w_class is not None:
                    if "viber" in w_class[0].lower() or "viber" in w_class[1].lower():
                        geom = window.get_geometry()._data
                        if geom['width'] == 22 and geom['height'] == 22:
                            found_viber_window = window
            except:
                pass

        return found_viber_window


    @staticmethod
    def poll_viber_window():
        found_viber_window = ViberWindow.get_viber_window()

        poll_second_count = 10
        while poll_second_count > 0:
            if found_viber_window is not None:
                break

            time.sleep(1)
            poll_second_count -= 1

            found_viber_window = ViberWindow.get_viber_window()

        return found_viber_window


    def __init__(self):
        super(ViberWindow, self).__init__(ViberWindow.poll_viber_window())

        if self.window is None:
            raise NoViberWindowFound

        self.move(-128, -128)


    def open(self, widget, data=None):
        self.double_click(button=1)


    def quit(self, widget, data=None):
        gtk.main_quit()
        os.system('pkill -9 Viber')



class ViberLauncher(threading.Thread):
    """class description"""

    def __init__(self, viber_path="/opt/viber/Viber"):
        super(ViberLauncher, self).__init__()
        self.viber_path = viber_path


    def run(self):
        sp_viber = subprocess.Popen([self.viber_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        sp_viber.wait()

        gtk.main_quit()


if __name__ == "__main__":

    viber_launcher = ViberLauncher()
    viber_launcher.start()

    viber_icons = ViberIcons.Instance()
    temp_icon_path, temp_notif_path = viber_icons.get_temp_icons()

    try:
        viber_window = ViberWindow()

        ind = appindicator.Indicator("Viber Indicator", "", appindicator.CATEGORY_APPLICATION_STATUS)
        ind.set_status(appindicator.STATUS_ACTIVE)
        ind.set_icon(temp_icon_path)

        menu = gtk.Menu()

        item_open = gtk.MenuItem("Open Viber")
        item_open.connect("activate", viber_window.open)
        item_open.show()
        menu.append(item_open)

        sep = gtk.SeparatorMenuItem()
        sep.show()
        menu.append(sep)

        item_exit = gtk.MenuItem("Exit")
        item_exit.connect("activate", viber_window.quit)
        item_exit.show()
        menu.append(item_exit)

        menu.show()
        ind.set_menu(menu)

        t_vipoller = ViberIconPoller(viber_window)
        t_vipoller.setDaemon(True)
        t_vipoller.start()

        gobject.threads_init()
        gtk.main()

    except NoViberWindowFound:

        os.system('pkill -9 Viber')
        sys.exit(-1)

    finally:

        viber_icons.clean_temp_icons()
        sys.exit(0)
