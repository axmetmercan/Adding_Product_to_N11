from N11 import N11
import termcolor


user = N11("User Name", "User Password")

Baslik = "Product Name"
AltBaslik ="Second Product Title"
StokAdi = "Stock Name"
Fiyat = "50"


user.addProduct(Baslik, AltBaslik, StokAdi, "999", "Diğer", Fiyat, "55")
#user.setProduct()
