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
import re
import sys

import Xlib
import Xlib.ext

from Xlib import X, display, xobject
from Xlib.error import BadWindow, CatchError


pygtk.require('2.0')


def printf(str_format, *args):
    sys.stdout.write(str_format % args)
    sys.stdout.flush()


class FilteredStdOut(object):
    """class description"""

    def __init__(self):
        self.wrapped_stdout = sys.stdout
        self.skip_next = False


    def __getattribute__(self,name):
        if name == "wrapped_stdout" or name == "write" or name == "filter" or name == "skip_next":
            return object.__getattribute__(self, name)
        else:
            return self.wrapped_stdout.__class__.__getattribute__(self.wrapped_stdout, name)


    def write(self, s):
        if self.skip_next:
            self.skip_next = False
        elif self.filter(s):
            self.wrapped_stdout.write(s)


    def filter(self, s):
        if "<class 'Xlib.protocol.request.QueryExtension'>" in s:
            self.skip_next = True

            return False
        else:
            return True


sys.stdout = FilteredStdOut()


class ViberIcons(object):

    ICON_NORMAL = """iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAACzNJREFUeNrsXU1oFFccn12C1So0qbQk
                     l2YXFDQRTC5RD9IsPVmFGEtbtFCMt0qltS0UerDioVCw1dJibyYp1NKUagTFU8mKh6CXrKC2YGHXXgwt6graWi/p+03e275MZt73fGw2fxg2xuzOzu/3/37/eZPzMiBz
                     c3MF8oKjjxzt5Oim//a435lImfu5Qo6H5KjRo5LL5eppX3suJbAHybGZgjuY4vXXKTGX6Ws5aVJyCQDeTkEeoq8FL9tSoZZzmZAx2bQEEOD3U9B3e80rsAaQcD4uMnKO
                     QYd2v0eO/RZ+O6uCuDFOjpMu3VTOIfCfUuCXujCrOOyCiJwl8O0U+Pdju9o/H3n1vx5pv6/Q25kEEV8REo6mQgABHwF11EVQrd2c9e5W73tP/n7q1W7c9X9XJb9zJZ2F
                     571Vq1d4ncXnvZWrn/GKhJz2F9Z47S+uceWaRggR5cQIIOCfMNX6J4+f+uDWbt71qjdmvdna/dR8yUpCShchp7CpyyfF0mrgkk7GSgB1OaO6mQ1A//XaH95v1+74r1mW
                     jQMveRsGuv1XEKQpY4SEkTgJmNIpnKDd0xduejNTvzdltO0vrSPHel3L0CIhpwH+qGqWA+Avnb7q1I+nKYgVpTf6fUJck5BTBB/+/oSKq7k0erVpNV4lmL96YIuqRSAw
                     j1kTQMBHv2ZKVlghkznz+S8+CUtdtu3q8XaMbFFJU/sJCTVbAqR+Hxp/7psrXisJsqa9H78iC9Ro7pVEf5BX6Ocsgx8iiG8/EIuXyCDBcLexBZA3V0WFFlJKhS/R6u6o
                     RqygGPWfbRLtL4haBGlq/vC72xtZSY1mWw9o2wLVdFIZ2PSFWyQod/l1Q1RXBFhGBeScqfaPHrmUapp57Gd5lscXf3EmB0hTDx4fEsWDyFiQiwAffutcnK4HKR2rGUxN
                     f+NAd6OlwD5PVIlPTcz4lhuHlN7sJ7VCn7CuIyRUVAkQFl1fvvOT8YUAOBQ1TFvwOUhfXfSEoIl+b4e4hOKmzlBSpiYqfnXu2iJwPR98+7rICrCOcFhKAO33PHCd9QCc
                     fSRtCwMFYJz66Lxz7cS50EpArOCBcUk6LwjGUDCdYJzTdT+nPjyv/cUBxIFjO4Q5Mz7zNIkrcfhqnHfbrt5FLgJVO4Koy1gAK9BxQ2F1wJAIpDjAZ3+nUF0uEmQfyIh8
                     H0wOFEjBc4HUqR9nfNdZ4xIHnA/vdSWwLAk+u1UsIDL70dUYhezA+hwgN6w3AyBmpm77LjNoVcGA6bKYlNQFi7KhfAD8gqzw0pE9RLt0e+r48qKMJihYSRNZ1CffveVr
                     Of89YA084IgRJtZngNGg0AJE/h/mBRPWcT0HvxgyNmUEZZ14gPN1EIvrLK713VKQxLBOLYDnXRBIcdHJRRwQLHeW+OXLYAzoE/U+tHzzlm6rYIagqSNwOX6uT7QbiQKU
                     BSknIxEWALB5wIOuB1bgYp1YglWfKAhvjr7Ae4lWuvDRNmDAiljg5WNKUOtBAtN6kLTHQVCWYLVZRECk/5+tJr947gIM5npEPh//z2oQBHRBX0eNADFWBREBzlwQGy+x
                     EYChGpARb9AfwgEfDC3nLSjobpCtFGn2BJKCrihGFzQYSgCtgCO1yORLuKhsu4pqBPBEAXhoOYgAmCwDAgnQdiZ8djQ/KjPbeL+tFahee15F+01L9plycmvDaA4i6AJE
                     XmGg6WiBMEE84IHmgz1iRgOM0no7AgTTfHSoLbISXiT/GLYHUAjFnFEsyL8BINoZn739va/pjAi4MhRfTM7y8WBwXajVGs4FNeSBgQW0u7YAXIxNXg1tNXVjeC/IaFjC
                     zp4FHVj2vYLuhi+kbNyQZJ61oOWCbAStXxNBUOT9tVk6eN93SyzF5AHFQs3/wb4r1Gr53zuWgpYLsgWhppFB+a1pUki5mi3iAd0w0B2q6Xygx/dlrks1AQhPRe9puyDr
                     D4sSPripBFOXfXq4GwboqoBPZ4oRbOax8+v0pEwzx7zLDxMFUlWNjmOdmQEaBDoqUPLfoRjzfQaxu6CGFUyoWYFN5hElrGMa7FTygZLX9ieP/00sfU6MANWMyLYAChME
                     8yOvjQoHCXj3xLcScO/AkiCAASFzZ7pdULuezb2Gi01rxCZRAnCh0xdvSVsKxfjv72q4JHRLUbilJfmkT4iMSFZc8VVrEq7RVeXfFASwIktYpThoCdtmTWz1zLSQzDQB
                     8LeyhXe+i5mG4PtBUeK+3yGf1gXKxgTRo3G1UJ6GqCpPagRAs85I5kvnb5Jb15QEYDgg0wTwvlYkWDRJKitKUGqZIID5WlmBtjdiprRlCIi7GoQViBpw8KdY8zVxR/Nz
                     oT0+ifxNHXGLqtXyBJTTjAcqg7kAUCcws2FZvAdpLRtJwe9Sdmt1LQtY+eyKzJAAbYY1yACE5u+LuIsRxIwc27FoZNGlYDOQKOEnpPNhfikoNgsTukFZhQTEAwCIwdwo
                     IlRmTNnkRBzWoDpUFpwNnYsCBqtUiaVwiiPtfDth+uLNRhdz665e7UoaS5c6C0cqri9CsFtjfxQB+Aaha8No5yaaRxMS4EIc7emjJGjOuah+YVGw0AhZMKKej0qPTKO6
                     S3eECekk9xOC1cDybFPeTrHLFt4hc93wQ2MLzC4X6HXcnw0JkmmKhyICyoYfGqvALSTRGOMzKJuWeJeYvLKIgEpWXFBQYAXIkJJySabtcFiOJG5FuyC6DWMlSivS7NHz
                     2Rgbtoq1UjKcyMP9ySLwg1td5mUmwgs/2JSmhN3xGEdGZCLbdvYqu58oAsZFhUuaiyRBDYVLQmxwfYO3f1vrhH5N4G+HKXY/l6UE0DK5Ft0K6PWyJIgNSFf5+8FcBH2T
                     z9oqxqYetv90VC9oPNrEejJjBQs0lrolWyLQHjdxP0X5Onbo5t9RBIyJUrSsLhUyImARYTdoq1iT6US2Qto6Lu0FBdoSwh1T0t4vSDWfh8tUsVpovin4NrtmiQgokJeq
                     KAjq3kydpiCBYDviBq8DwJtmPYqNwxHtHbNUrCDpLqkLQZbSQXv1GMCyKez8lbrjQ7LMR7hnnIwAWAHysXaR32zFXRMBvmLPqCTaWV1l31DprrmttGkrczt7Dm1XAX+S
                     gD8s+gPVrYulm7fClM9+fSXV7eiTiiWKU3uopfplT9lQJaCduqKCtE0Q055sWYgd2DpBYyf10E36jAigJCjtIc0yC5TyS2ETb7gZpLKa4yxKG3drEaBLAiuM5ncjud1U
                     rgmgY7sd3MRtsCSqDL42ASYk8Fahs+FT0oCjjYx9SPGzRatFC3xIm+4Z4NcICUVKgvLN3UkurotSxy66YNJZWOuP2zh62lKdppvaCxVtJmejkb2fEHHUm3+MVezAodml
                     EtjZk5J80knB1UGJj/GxVpNU842eKdZmc2Y8Q4uQMEnrhMG4rhATbGmvxkWkmYdtH3FoPR0Ns6NzLjjKrq+SzXVmDHhofNHF8yWdjaej3KZEoC875nEDqDZFj2Ar4KRl
                     kgN+zNWHOr8/gFoEvmgHvIepVSAbcbmrrWFgBdDYJ78DLQWXwDuJAQpkTNK0VSs+IEs5ED3aFyfgUBas25ZNMprMEWCa8eyTPxzHVsoUcEwCAuiK7GlHLUNAyBb3MPs7
                     3L9fVgiS/N9XWDwyfeBmsxPwnE66GcjXtZ/N2GySxE16StUysp1Aw2tyqYOfFAFK6WZgUbtCsw9vmYCYJeTBDTXaV6kvE5AA+IGJAoA+3Crgp0qAv1P5oe1B8EtJ5d+t
                     REA9DPyQiYLhVgM/KQKu8xUuq3ID4I9kMUdfEoLHosyJZf8ySvGTUF0GP10C+jBbxAFflT1nt1XkPwEGAObH45cGp22ZAAAAAElFTkSuQmCC"""

    ICON_NOTIF  = """iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAYAAADimHc4AAAABmJLR0QAAAAAAAD5Q7t/AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH3goIDjYaFQSitAAADeRJ
                     REFUeNrtXW1wU1Uafk5TS2kLJumH6Sr0RipC40CjK1jHKl1md7ZjZ2tBZZZhZ2gdf5SFRYWRHzBVO/CDWZBx6MIPB4qzDC4oUpxKdXeYtFvdUlxJypiiUDcR1iGU0oaP
                     0lIbzv7IDRtizrnn3nxdC+9MhpJz783J+5zzvB/nPScEOhBKqQRAAlAKwAigSP4/wt7TIu1hf7sAXAbglV8uQoifUpoPwAbgcfllAzCdUppFCLkO4CwAN4Av5ZebEHIx
                     Xt+dpEjZCwDMlZW7ADoUSikIYapnHMBbAPYRQv6jawAopUZZydXyvxImlvQC+COADkII1Q0AlNLlstKfw50hHgDPE0JOpAwAmV5WA1geA2//3GU7gHWEkJGkASAr/g1Z
                     8XclaCNshJDTCQVA5vc3ALySqG/i778G/8Vrqu7JzMqAxWpWdc/NiwMYP3Ua41+5MP6VC4Heb2EoeRjpj5UGX7NnIi0/T233Kwgh7QkBgFK6AEBzPIyq1+3Dec8gRq+P
                     wfv1+SChun2anjXz0QewbP2vha4NeL7Hjf0f4fqmrUAgoHyDwYCs9WswackiGKxFol2qIoR8ElcAKKXbtI760eExeNw+eN3n4fnaB593MG6zRbJZUNdYqcwPzpO4+tIq
                     BL45rfmzDLNmYsqu7Ui3z4lpJhANlNOs1rMZHR7DqeNn8c3x73Hq+NmEUFVu4VSsblrM7//ICIY3bMTozt1x+9zM+jpkb9wAMnmy0qUPR7MJagFwqAmcfN5BdLW64XT0
                     JdTipWcYsH7vMhgMaWy6OfMdhh59RoxqVE8HA0wnOmB4aIaSYZ4a6R2lq1B+s6jyfd5BtO3u1szjauU3f/glV/lj//wXrvx2ceI6EAhgaO5TmPrpQWQ8/SRznADYDOBP
                     qmcApfQVANtEqKatuTvhIz5cCq25qN/yu9QpP0IUQACAx8KDNSKg/FIADqXAyuv2Yd/moxgdHkuqw/3qjudhum8Km3bmPpX0IMDU8zmPjjwAZoTSFmkCz9umpHynow+7
                     G9qSrnzJZmEqn46MBDk/BTL06DOgI8xA2ArgVsfSBPI5C5SUf6ipMyVftOrlMmbb8IaNiTG4gjZheMNG3hV/EQJAjnKZcur42ZQp33RfDgqmGZl+fjxdTU3xzs7dGHee
                     ZDWXUEof5AIgj36JlyJIlfIBYMnaXzHbrr60ShcJIYV+LFWaAdzRf6ipM+mcHy6/eDCXmV6IJcKNKxN9cxoBz/dc/aYxRv9zvNF/6vjZmH18i2SGRTJrujdr6iRm2439
                     H0FPwulPOqU0n3CCruWsO9+u/wD+/muaOlRWVYKKF+3IzM64RWX7Nh9VlRPi5XwGpjyQOuPLiJLzrv6XmSNKY+R7lvO8Hi3KNxbkYMXWalTWzr+l/ND7dY2VMBbkCD/r
                     /uLoaeGbFwf0pXzZI7p5cYDV+ng0CuK6nV2tbk10s2JLNZNyMrMzsHTdwtuA0QLA+KnT0KNw+hUVgGpejkdt+tgimVHXWKmoXItkRmXtfKFnFkwzRf+iX7n0CQC7XzZV
                     M8DpOKOadkSUHxJ7RTHKqkoUr7s3L3uiADA9LYL/JSXvR40sWlkurPyQVNbOV/SO7pkUPYkb6P1WlwBE6xelFJTSSZEzoJQXeKkxvhbJDMlm0dRhJXvw443x6A5HycO6
                     BCBavwghIITcEAZArd8/e36R5g4bC3JQVmVjtl8eGI7uWD9WqksAOP06GwnAXLYBvpTUTle8WMp0TfvPDU0UANyRADD53+cZTHrHF60sj/r+D33R/er02TP1CQC7X18m
                     jIJC5SWxiGSzRDXILADS8vMAg0FnBsDAqyf6PwByBBxVtCTdPG6f5nRFuBRGKbBiURAAZK1foyv9K/TnNgoq5QVgWsTZnpi14etXbiAQuBm1bdKSRboCgNOfcULIRZEl
                     SYxoTDurDdzUUF/7gejBjcFaBMMsfdgCw6yZvAq6t4Db09HGeM8Af/+1mCokulp7mTR2svM75n1Tdm3XBQAK/dgXCUBCfDgtyTsguODT1tzNbB+6cA395/zRvQ77HGTW
                     16VU+Zn1dbyyxYuhnTVpie6IzzsIrwoPanR4DDvWHBaaOa3vdjHbsjduSJ1HZDAEP58tR255bkJK9MQWhDn2O4WvfV/F4ozX7cPQhatR28jkyTCd6EiJ/k0nOpRqRb2q
                     AIh17dfj9gnbArXxxt/+7GAPxIdmYOqnB5Oq/KmfHlSqEb09dklWxxwHxGaB2uzpec8lHDvSy2zPePrJpIEgUJaYOgBEPaLZ86arfvbf//pvZlwQAsHU83nibILBAFPP
                     56qVn1QAAKCtuVuRznhZUGZEMxZA0+pDfB09NAO5/Wfi7h1l1tcht/+MKtpJGQCjw2Po+qSXe41FMsOqYR3h0vkr2N3Qxr2GTJ6MnK2bYPzis5iDNcOsmTB+8Rlytm4S
                     2ZyhDwBCHpFSjqhiiV3Ts71uH/Zu+ofiden2OTCd6IDJfQxZDa+LU5PBgKyG12FyH4PpRIfo9iT+oAj9QSl9E4xquOaGtrhutrDaLKhV2Mv1/uajmrczie4VC5cE7ZJk
                     piEIIW8CKnbIxFM8bh+6Wnu5C/CVtfPhcfs0ucBetw/vrDyIle/UcHfO3EYF+XnIyM/TZEgjJRC4iZamTixe/Yz+KCjcLeVRkbEgR7hMhWUTNi3by3VREyHHjvRi07K9
                     GBsd16cNCDfI+zYf5V5jryiGvaJY82eMjwVwZFc3dq79mBkxx0uGLlzFzrUf48iuboyPBWCx5grdl44Uis87iLbmbu5Ir1lZDn//tZhs0HnPJWxb8SEkmwVVL5cx9xVo
                     kf5zfrS+26Uq3xWeikgpAEAw5WyRcrkj/ffrFmJ3Q1vMm7q9bh+aXjkE0305mFM+AwteLBW2EZEc337AhZOd32HogqZVP3UASI8UJnTLaVtzNwqtZm7t6Iqt1TjU1Kl6
                     fSEzOwP2imJItkKMDo/B6z4Pp6MPHR/2oOPDHmRNnYSCaSbcX5yH+4vzUDDNhHvzsnHPpHT8eGMclweG0X9uCD/0DeCHvgH0nxvC9Ss3hDw9tW7oAgR3Q0YxmC5VGU1N
                     EWV2Bl7b+YJiLqirtZe7ThBpyFdsqf7JM0O7exI5qOoaK3mFaXZCiEvYCGdmZSScikaHx4R2WpZVlWDF1mrFEcaruDYW5KC2sRI1GkonRcWYzy63Dyk/EgAv64ZCqxnJ
                     EJ93UAgEi2RGbWMl6hormUCI1JjaK4rx2s4XNKU+RGafKgqSaYiyFLNjzeGkGWbRkvZwSun6xH2reOyJKpvqrGo8adZYkIPXdr7AanYRQuwsAJxgrA03LG5OqndkkcxY
                     um6hqp0zsUpo222sC1AKqZZ2QkgFKxDzxmrV40lHO9Yejut5Qkoye9501DVWat48eGvw8CnbxYuEezQ+NGGGWXSBPt70FwsIkq2Q13yZB0C7xocmVA41dSZ1X3Jmdobm
                     lDgAFPLBa+cB4NILBUVK6ECQZFGSlqXR0AxSsFtsCiKE+FkgZGZnaO5UXO3CmsNwHEj8XjCthcXWR7gD1SXrmDkDuDQ0a14R9CCO/U68Xf+B2gSYao9Ii5Q9axOmHxYA
                     7/ECl0RFjlpG6O6GNhxq6oxLGXyk8Rcto4mkaQX66VAEQA6TvexUgA16EqejDzvWBmkpXkZaq8F/gq8bPyGkRWQGcGdB2bMlupkFt41YmZZiBaKrtVcT/VhtFiUb2RLt
                     TRYAe3guWixLhckAYsfaYOygFgino0840xopAm7re4q5oIi0BPfElHhXSiTKny+rsgnNWjVp7p/SconSoPQSQqxqAZAQPOGPaQR3rD2c0kOb1Ii9ohiz5hX9hCb8/dfQ
                     1tyt2esRTBzWEkL2qAJAZBYkO0saDzEW5MAk5+pHhsdiCuwyszOwYku1kufDHP0iAEgAnOBsX0rlqYmppjfBnBH3CHuRg1sVT81N1aGtqRKLZMaiVeUiym8hhNTwLhA9
                     uljx0G6fdxAfbe9Mavo4VbYk8tQv1rhEcO3XHw8AjDIVSYppggMudLW6J9xsMBbkYNHKcjUnwNjD135jAkAGQegM6ZBn4TjgTGoeP5F0U1ZlU1uhx/R6NAOgFoRQYOR0
                     9MHpOPOzoiaLZMbs+UWwLyjWsiQqrHzVAGgBIXxWvF3/gW4Vbn3EgtnzimCRzLGkWlQpH9BQmkgIcVFKrTIIwpu7k7m4znMdC+UFE4uUi0Kr9lO9IseX7G6qXqjQVBsq
                     W3Y7b1NHvBVntVmEDLvFakZmdvBkXWN+Dkwy8FLiVvRa5JHv13JzTMW5hJA3KaUtcpywIFHfsGZlecpX4xhu5qvRUsxqJOb9AYQQl1znUgHOappWqaydrzfle+URb41V
                     +XEBIAyIUMGRHcF0tj/WZ4qeI5okaQlT/J54PTTuO2TkGVFLCDEBqNE6KyySGTWMM+OSJH55INUCMBFCauKp+LjYAAEwWmS3VZV9CJ24mwKFtyO4btuuxaPRHQBaPR41
                     B3lrlHZZ4T0IluG4CCHeVHxf3QGwdN3CyCzjHgDhP0OhtPfTG3G9K2SPlH7ZdKICcK8adzPCX99DCKnFBJZkbFMVipbLqkoiE14tE135yQJAyN2MWNR2yd4H7gKQYIny
                     ww1eOa/ivwtAEpQfUVHgB1Bzpyg/pQBkZmdg0arySOVXJMv/vpMA8EdTfpSKgpo7TfnJAqAnPMINRbkRyq/Vo48+IYRS+hzly/K7Wko8CJ67yk8tAKWUUkeY4j3y71Xe
                     8fI/bKPVDzA4zUcAAAAASUVORK5CYII="""

    INSTANCE = None


    def icon_exists(self, icon_name, icon_size=24):
        try:
            icon_info = self.git.lookup_icon(icon_name, icon_size, 0)

            return os.path.isfile(icon_info.get_filename())
        except:
            return False


    def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")

        self.git = gtk.icon_theme_get_default()

        if self.icon_exists('viber-normal') and self.icon_exists('viber-notification'):
            self.icon_type = "SYSTEM"

            self.icon_normal = "viber-normal"
            self.icon_notification = "viber-notification"
        else:
            self.icon_type = "BUILTIN"

            self.temp_icon_normal = tempfile.NamedTemporaryFile()
            self.temp_icon_notif = tempfile.NamedTemporaryFile()

            self.temp_icon_normal.write(self.ICON_NORMAL.decode('base64'))
            self.temp_icon_notif.write(self.ICON_NOTIF.decode('base64'))

            self.temp_icon_normal.flush()
            self.temp_icon_notif.flush()

            self.icon_normal = os.path.abspath(self.temp_icon_normal.name)
            self.icon_notification = os.path.abspath(self.temp_icon_notif.name)

        printf("Using %s icons\n", self.icon_type)



    @classmethod
    def Instance(cls):
        if cls.INSTANCE is None:
             cls.INSTANCE = ViberIcons()

        return cls.INSTANCE


    def get_icons(self):
        return self.icon_normal, self.icon_notification


    def clean_icons(self):
        if self.icon_type == "BUILTIN":
            self.temp_icon_normal.close()
            self.temp_icon_notif.close()


class XTools(object):
    """class description"""

    INSTANCE = None

    def __init__(self):
        if self.INSTANCE is not None:
            raise ValueError("An instantiation already exists!")

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


    def create_window_from_id(self, window_id):
        return self.display.create_resource_object('window', window_id)


    def get_client_list(self):
        return self.root.get_full_property(self.display.intern_atom('_NET_CLIENT_LIST'), Xlib.X.AnyPropertyType).value


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


    def get_window_by_class_name(self, class_name):
        XTools.Instance().get_display().sync()
        window = None

        for win in self.root.query_tree().children:
            try:
                window_wm_class = win.get_wm_class()
                if window_wm_class is not None:
                    if class_name in window_wm_class[0] or class_name in window_wm_class[1]:
                        window = self.display.create_resource_object('window', win.id)
                        break
            except BadWindow:
                printf("Error getting window's WM_CLASS of window 0x%08x\n", win.id)
                pass

        return window


    def get_client_by_class_name(self, class_name):
        XTools.Instance().get_display().sync()
        window = None

        for win_id in self.get_client_list():
            try:
                win = self.create_window_from_id(win_id)
                wclass = win.get_wm_class()
                if wclass is not None and (class_name in wclass[0] or class_name in wclass[1]):
                    window = win
                    break
            except BadWindow:
                printf("Error getting client's WM_CLASS of window 0x%08x\n", win_id)
                pass

        return window


class XWindow(object):
    """class description"""

    class WindowIsNone(Exception):
        """class description"""

        def __init__(self):
            super(XWindow.WindowIsNone, self).__init__("Window is None")


    def __init__(self, window):
        if window is None:
            raise XWindow.WindowIsNone

        self.XTools = XTools.Instance()
        self.window = window


    def click(self, button=1):
        self.XTools.mouse_down(self.window, button)
        self.XTools.mouse_up(self.window, button)


    def double_click(self, button=1):
        self.click(button)
        self.click(button)


    def close(self):
        _NET_CLOSE_WINDOW = self.XTools.get_display().intern_atom("_NET_CLOSE_WINDOW")

        close_message = Xlib.protocol.event.ClientMessage(window=self.window, client_type=_NET_CLOSE_WINDOW, data=(32,[0,0,0,0,0]))
        mask = (X.SubstructureRedirectMask | X.SubstructureNotifyMask)

        self.XTools.Instance().get_root().send_event(close_message, event_mask=mask)
        self.XTools.get_display().flush()


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


    def next_event(self, instance=None, atom=None):
        ev = None
        while ev is None:
            ev = self.window.display.next_event()

            if atom is not None:
                ev = ev if hasattr(ev, 'atom') and ev.atom == atom else None

            if instance is not None:
                ev = ev if isinstance(ev, instance) else None

        return ev


class ViberIconPoller(threading.Thread):
    """class description"""

    def __init__(self, xviber_window):
        super(ViberIconPoller, self).__init__()
        self.viber_window = xviber_window
        self.setDaemon(True)


    def run(self):
        self.poll_viber_icon()


    def poll_viber_icon(self):
        vi = ViberIcons.Instance()
        icon_norml, icon_notif = vi.get_icons()

        notified = False
        while True:
            try:
                time.sleep(1)
                n = self.is_notified()
            except:
                n = False

            if n and not notified:
                notified = True
                # ind.set_icon(icon_notif)
                ind.set_status(appindicator.STATUS_ATTENTION)
            elif not n and notified:
                notified = False
                # ind.set_icon(icon_norml)
                ind.set_status(appindicator.STATUS_ACTIVE)


    def is_notified(self):
        viber_img = self.viber_window.read_image(22, 22)
        r, g, b = viber_img.getpixel((17, 4))

        if r >= 200 and g <= 50 and b <= 50:
            return True

        return False


class ViberChatWindow(XWindow):
    """class description"""

    @staticmethod
    def get_viber_chat():
        window = None

        windowIDs = XTools.Instance().get_client_list()
        for windowID in windowIDs:
            window = XTools.Instance().create_window_from_id(windowID)
            wclass = window.get_wm_class()

            if wclass is None:
                continue

            if "Viber" in wclass[0] or "Viber" in wclass[1]:
                break

        return window


    def __init__(self):
        super(ViberChatWindow, self).__init__(ViberChatWindow.get_viber_chat())


class NoViberWindowFound(Exception):
        """class description"""

        def __init__(self):
            super(NoViberWindowFound, self).__init__("No Viber Window Found")


class CompizNotFound(Exception):

    def __init__(self):
        super(CompizNotFound, self).__init__()


class ViberAlreadyRunning(Exception):

    def __init__(self):
        super(ViberAlreadyRunning, self).__init__()


class ViberWindow(XWindow):
    """class description"""

    @staticmethod
    def external_find_viber():
        r = subprocess.Popen(["xwininfo", "-root", "-children"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ou, er = map(lambda s: s.strip(), r.communicate())

        if len(ou) > 0 and len(er) == 0:
            ou = [i for i in ou.split('\n') if "ViberPC" in i and "+0+0" in i]

            if len(ou) == 0:
                return None

            try:
                viber_window_id = int(re.match(r"^ *(0x[^ ]+) .*$", ou[0]).groups()[0], base=16)
            except:
                return None

            return XTools.Instance().create_window_from_id(viber_window_id)
        else:
            return None


    def find_viber(self):
        while self.viber_window is None:
            if self.w_compiz.next_event():
                self.viber_window = XTools.Instance().get_window_by_class_name('ViberPC')


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
                        if geom['x'] == 0 and geom['y'] == 0 and geom['width'] <= 64 and geom['height'] <= 64:
                            found_viber_window = window
            except:
                pass

        return found_viber_window


    def poll_viber_window(self, external=False):
        if external:
            printf(" (EXTERNAL)\n")
            finder_fn = ViberWindow.external_find_viber
        else:
            printf(" (INTERNAL)\n")
            finder_fn = ViberWindow.get_viber_window

        found_viber_window = finder_fn()

        poll_second_count = 10
        while poll_second_count > 0:
            if found_viber_window is not None:
                break

            time.sleep(1)
            poll_second_count -= 1

            found_viber_window = finder_fn()

        self.viber_window = found_viber_window


    def __init__(self, close_chat=False, use_old=False, use_external=False):
        self.viber_window = None
        self.viber_launcher = ViberLauncher()

        try:
            if use_old:
                raise CompizNotFound()

            try:
                self.w_compiz = XWindow(XTools.Instance().get_window_by_class_name('compiz'))
            except XWindow.WindowIsNone:
                raise CompizNotFound()

            printf("Using NEW detection method\n")

            XTools.Instance().get_root().change_attributes(event_mask=X.SubstructureNotifyMask)
            self.w_compiz.window.change_attributes(event_mask=X.SubstructureNotifyMask)

            self.thread = threading.Thread(target=self.find_viber)
        except CompizNotFound:
            printf("Using OLD detection method")

            self.thread = threading.Thread(target=self.poll_viber_window, kwargs={"external": use_old and use_external})

        self.thread.setDaemon(True)
        self.thread.start()

        self.viber_launcher.start()

        self.thread.join()

        super(ViberWindow, self).__init__(self.viber_window)

        if self.window is None:
            raise NoViberWindowFound

        self.move(-128, -128)

        printf("Viber Found")

        if close_chat:
            self.chat_window = ViberChatWindow()
            self.chat_window.close()


    def open(self, widget, data=None):
        self.double_click(button=1)


    def quit(self, widget, data=None):
        os.system('pkill -9 Viber')


class ProcessFinder(object):
    """class description"""

    def __init__(self, process_path):
        self.process_path = process_path.strip().replace('\t', ' ')
        self.re = re.compile(r".* " + re.escape(self.process_path) + r"$")

        self._found = None


    def _find_process(self):
        self._found = False

        ret = subprocess.Popen(['ps', '-aux'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out_stream, err_stream = ret.communicate()

        for line in out_stream.split('\n'):
            if self.re.match(line):
                self._found = True


    def find(self):
        finder_t = threading.Thread(target=self._find_process)
        finder_t.setDaemon(True)
        finder_t.start()
        finder_t.join()

        process_found = self._found
        self._found = None

        return process_found


class ViberLauncher(threading.Thread):
    """class description"""

    def __init__(self, viber_path="/opt/viber/Viber"):
        super(ViberLauncher, self).__init__()
        self.viber_path = viber_path
        self.setDaemon(True)


    def start(self):
        viber_finder = ProcessFinder(self.viber_path)

        if viber_finder.find():
            raise ViberAlreadyRunning()
        else:
            super(ViberLauncher, self).start()


    def run(self):
        try:
            printf("Launching Viber (%s) ... ", self.viber_path)
            p_viber = subprocess.Popen([self.viber_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            printf("OK\n")

            p_viber.wait()

            printf("Viber process terminated. Quitting...\n")
        except OSError as ose:

            printf("Error starting Viber. Operating System reported: '%s'\n", ose.strerror)

            os.system('pkill -9 Viber')
            ViberIcons.Instance().clean_icons()
            os._exit(-1)

        except Exception as ex:

            printf("Error starting Viber because of exception '%s: %s'\n", ex.__class__.__name__, ex.args[0])

            os.system('pkill -9 Viber')
            ViberIcons.Instance().clean_icons()
            os._exit(-1)


        try: gtk.main_quit()
        except: pass


if __name__ == "__main__":
    viber_icons = ViberIcons.Instance()
    icon_normal, icon_notification = viber_icons.get_icons()

    try:
        arg_close_chat = "--close-chat"               in sys.argv
        arg_use_old    = "--use-old-detection-method" in sys.argv
        arg_use_ext    = "--use-external-detector"    in sys.argv

        viber_window = ViberWindow(close_chat=arg_close_chat, use_old=arg_use_old, use_external=arg_use_ext)

        ind = appindicator.Indicator("Viber Indicator", "", appindicator.CATEGORY_APPLICATION_STATUS)
        ind.set_status(appindicator.STATUS_ACTIVE)
        ind.set_icon(icon_normal)
        ind.set_attention_icon(icon_notification)

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

    except ViberAlreadyRunning:

        sys.stdout.write("Viber Already Running!\n")
        sys.stdout.flush()

    except Exception as e:

        printf("Exiting because of exception '%s: %s'\n", e.__class__.__name__, e.args[0])

        os.system('pkill -9 Viber')
        viber_icons.clean_icons()
        os._exit(-1)

    finally:

        viber_icons.clean_icons()
        os._exit(0)
