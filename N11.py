from selenium import webdriver
import termcolor
import time


class N11:
    def __init__(self, userName: object, userPassword: object) -> object:

        self.userName = userName
        self.userPassword = userPassword

        self.driver = webdriver.Chrome(executable_path="driver/chromedriver")
        self.driver.maximize_window()
        self.driver.get("https://so.n11.com/")
        time.sleep(3)
        self.driver.find_element_by_id("j_username").send_keys(self.userName)
        self.driver.find_element_by_id("j_password").send_keys(self.userPassword)
        self.driver.find_element_by_id("j_id45_j_id_2f").click()

    def addProduct(self, title, smallTitle, stocCode, stocQuantity, producer, price, discountRate):
        print("Ürün Ekleme Sayfası Açılıyor....\n" +
              "********************************")

        self.title = title
        self.smallTitle = smallTitle
        self.stocCode = stocCode
        self.stocQuantity = stocQuantity
        self.producer = producer
        self.price = price
        self.discountRate = discountRate

        self.driver.get("https://so.n11.com/selleroffice/product/createProduct")
        termcolor.cprint("Lütfen Ürün Eklemek İstediğiniz Kategori Adını Yazınız: ", "green")
        #category = input()
        category = "tül perde"

        time.sleep(5)
        self.driver.find_element_by_id("categorySearch").send_keys(category)
        time.sleep(3)
        self.driver.find_element_by_css_selector("#searchCategoryButton > span").click()
        time.sleep(3)
        ### Dikkat Burası Değişim İsteyebilir / Kategori Seçim Alanı
        self.driver.find_element_by_xpath("/html/body/div[3]/form/div[2]/div/div/div[2]/div/div/div[3]/div[2]/div[2]/div/div[1]/table/tbody/tr/td/input").click()
        time.sleep(2)
        ###  Dikkat Burası Değişim İsteyebilir / Kategori Seçim Alanı
        self.driver.find_element_by_xpath("/html/body/div[3]/form/div[2]/div/div/div[2]/div/div/div[3]/div[2]/div[3]/div/table/tbody/tr/td[3]/button/span").click()
        time.sleep(5)

        # Ürün Adı
        self.driver.find_element_by_id("title").send_keys(self.title)
        self.driver.find_element_by_id("subTitle").send_keys(self.smallTitle)
        self.driver.find_element_by_id('sellerCode').send_keys(self.stocCode)
        self.driver.find_element_by_id("selectOneMenuBrand_label").click()
        self.driver.find_element_by_xpath("//*[@id='selectOneMenuBrand_panel']/div/ul/li[512]").click()
        # Beraber Satışa Uygun
        self.driver.find_element_by_css_selector(
            "#bundle > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default").click()
        # Yerli Üretim
        self.driver.find_element_by_css_selector(
            "#domestic > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default").click()
        # Kargo Süresi
        self.driver.find_element_by_css_selector(
            "#productPreparationType > tbody > tr > td:nth-child(11) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-radiobutton-relative.ui-state-default").click()

        ## Fiyat Bilgileri Dolduruluyor İndirim Varsa Giriyor.
        self.driver.find_element_by_id("price").clear()
        self.driver.find_element_by_id("price").send_keys("0")
        self.driver.find_element_by_id("priceDecimal").clear()
        self.driver.find_element_by_id("priceDecimal").send_keys('02')
        self.driver.find_element_by_id("stock").send_keys(self.stocQuantity)

        self.addTulCurtain()

        if int(self.discountRate) > int("0"):
            self.createDiscount()


    def setProduct(self):
        self.driver.get("https://so.n11.com/selleroffice/product/products")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='idDataTable_paginator_bottom']/select").click()
        self.driver.find_element_by_xpath("//*[@id='idDataTable_paginator_bottom']/select/option[4]").click()
        time.sleep(20)
        self.driver.find_element_by_id("idDataTable:27:j_id_7x").click()
        time.sleep(45)
        self.driver.find_element_by_css_selector("#tabView\:optionalAttributeValueSelectorTable\:0\:j_id_ix > span.ui-button-text").click()
        time.sleep(15)
        self.driver.find_element_by_id("tabView:customTextOptionsTable:0:j_id_hz").click()
        time.sleep(5)
        self.driver.find_element_by_css_selector("#tabView\:optionalValuetable\:j_id_ka > div > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default").click()
        time.sleep(3)
        self.driver.find_element_by_css_selector("#tabView\:j_id_k7 > span.ui-button-text").click()
        time.sleep(15)

        self.addTulCurtain()



    ### İndirim Yapma Ekranını Oransal Yüzde Verir
    def createDiscount(self):
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#sale > tbody > tr > td:nth-child(3) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-radiobutton-relative.ui-state-default").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector(
            "#saleType > tbody > tr > td:nth-child(3) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-radiobutton-relative.ui-state-default").click()
        time.sleep(5)
        self.driver.find_element_by_id("saleRatioAmount").clear()
        self.driver.find_element_by_id("saleRatioAmount").send_keys(self.discountRate)

    # Yüzdesel Şekilde Çalışacak
    def updatePrice(self):
        print("Fiyat Güncelleme Sayfası Açılıyor...\n" +
              "************************************")

    def addKruvaze(self):
        pass

    def addCurtain(self):
        pass

    def addMechanicCurtain(self):
        pass

    ## Başlangıç ve Bitiş Eni ni İnput Alıcak
    def addTulCurtain(self):
        # En Ekleme Oluştur
        self.driver.find_element_by_css_selector("#addOtherOption > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default").click()
        time.sleep(3)
        self.driver.find_element_by_id("customOptionalValue").send_keys("En")
        self.driver.find_element_by_xpath("/html/body/div[3]/form/div[2]/div/div/div[2]/div/div/div[3]/div/div[8]/div[2]/div/span/div[1]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/button/span").click()
        time.sleep(5)
        # self.driver.find_element_by_css_selector("#addOtherOption > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default").click()
        time.sleep(2)

        self.driver.find_element_by_id("customOptionalValue").send_keys("Pile")
        self.driver.find_element_by_xpath("/html/body/div[3]/form/div[2]/div/div/div[2]/div/div/div[3]/div/div[8]/div[2]/div/span/div[1]/table/tbody/tr[3]/td/table/tbody/tr/td[2]/button/span").click()
        time.sleep(5)
        self.driver.find_element_by_css_selector("#j_id362_j_id_gt > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default").click()
        time.sleep(2)
        self.driver.find_element_by_id("customTextOption").send_keys("Boy(Max:260cm)")
        self.driver.find_element_by_xpath("/html/body/div[3]/form/div[2]/div/div/div[2]/div/div/div[3]/div/div[8]/div[2]/div/span/div[1]/span/table/tbody/tr[3]/td/button/span").click()
        """
        self.initialWidth = initialWidth
        self.lastWidth = lastWidth
        """

        termcolor.cprint("Başlangıc Enini Cm Olarak Giriniz: ", "blue")
        self.initialWidth = input()
        termcolor.cprint("Bitiş Enini Cm Olarak Giriniz: ", "blue")
        self.lastWidth = input()

        self.addingWidth(self.initialWidth, self.lastWidth)
        self.addingPile()

        #Creating The Variants
        self.driver.find_element_by_xpath("/html/body/div[3]/form/div[2]/div/div/div[2]/div/div/div[3]/div/div[8]/div[2]/div/span/div[3]/div/button/span").click()
        time.sleep(13)


        #Fazlalıkları Siler
        for delete in ["2","3","4"]:
            self.driver.find_element_by_css_selector("#optionalValuetable_data > tr:nth-child({}) > td.ui-selection-column > div > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default".format(delete)).click()
        #Seçilen Varyantları Siler
        self.driver.find_element_by_xpath("/html/body/div[3]/form/div[2]/div/div/div[2]/div/div/div[3]/div/div[8]/div[2]/div/span/div[4]/div[2]/div/span/div[1]/div/table/tbody/tr/td[2]/button/span[2]").click()
        time.sleep(10)

        self.calculteTulPrice()




    ######### Tül Perde Fiyatı Hesaplar #######
    def calculteTulPrice(self):
        initialwidth = int(self.initialWidth)
        lastwidth = int(self.lastWidth)

        quantitySku = (((lastwidth - initialwidth)/10)+1)*4
        initialSku = "1"
        lastSku = int(quantitySku)

        while int(initialSku) <= lastSku:
            for pile in [1, 2, 2.5, 3]:
                self.driver.find_element_by_id("optionalValuetable:{}:skuCurrencyAmount".format(initialSku)).clear()

                if pile != 3:
                    price = (((initialwidth/100)*pile)+20/100)*int(self.price)
                    price = int(price)
                    price = str(price)
                    self.driver.find_element_by_id("optionalValuetable:{}:skuCurrencyAmount".format(initialSku)).send_keys(price)

                    initialSku = int(initialSku)
                    initialSku += 1
                    initialSku = str(initialSku)

                elif pile == 3:
                    price = (initialwidth/100)*pile*int(self.price)
                    price = int(price)
                    price = str(price)



                    self.driver.find_element_by_id("optionalValuetable:{}:skuCurrencyAmount".format(str(initialSku))).send_keys(price)

                    initialSku = int(initialSku)
                    initialSku += 1
                    initialSku = str(initialSku)

            initialwidth += 10







    def addingWidth(self, initialWidth, lastWidth ):
        self.driver.find_element_by_id('optionalAttributeValueSelectorTable:0:optionalValue').send_keys("Numune Talep Et(10 Cm)")
        self.driver.find_element_by_xpath("/html/body/div[3]/form/div[2]/div/div/div[2]/div/div/div[3]/div/div[8]/div[2]/div/span/div[2]/div/div/table/tbody/tr/td[1]/table/tbody/tr[1]/td/div/table/tbody/tr/td[3]/div/button/span").click()
        time.sleep(1.5)
        while int(lastWidth) >= int(initialWidth):
            self.driver.find_element_by_id("optionalAttributeValueSelectorTable:0:optionalValue").send_keys(initialWidth)
            self.driver.find_element_by_xpath("/html/body/div[3]/form/div[2]/div/div/div[2]/div/div/div[3]/div/div[8]/div[2]/div/span/div[2]/div/div/table/tbody/tr/td[1]/table/tbody/tr[1]/td/div/table/tbody/tr/td[3]/div/button/span").click()
            time.sleep(1.5)
            initialWidth = int(initialWidth)
            initialWidth += 10
            initialWidth = str(initialWidth)

    def addingPile(self):
        for curtain in ["Pilesiz Düz Dikim", "Seyrek Pile (1'e 2)", "Orta Pile - (1'e 2.5)", "Sık Pile - (1'e 3)"]:
            self.driver.find_element_by_id("optionalAttributeValueSelectorTable:1:optionalValue").send_keys(curtain)
            self.driver.find_element_by_xpath('/html/body/div[3]/form/div[2]/div/div/div[2]/div/div/div[3]/div/div[8]/div[2]/div/span/div[2]/div/div/table/tbody/tr/td[2]/table/tbody/tr[1]/td/div/table/tbody/tr/td[3]/div/button/span').click()
            time.sleep(0.85)