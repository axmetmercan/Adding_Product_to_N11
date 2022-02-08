from N11 import N11
import  time

class Editing(N11):
    def __init__(self):
        super().__init__("UserName","Password")


# Finds The Product and Goes in its Details ###
    def goProducts(self):
        self.driver.get("https://so.n11.com/selleroffice/product/products")
        time.sleep(3)
        self.driver.find_element_by_css_selector("#idDataTable_paginator_bottom > span.ui-paginator-pages > span:nth-child(4)").click()
        time.sleep(4)
        self.driver.find_element_by_css_selector("#idDataTable\:31\:j_id_7x").click()
        time.sleep(45)

# Old values and variables will be deleted#
    def deletingOldInformations(self):
        self.driver.find_element_by_css_selector("#tabView\:optionalAttributeValueSelectorTable\:0\:j_id_ix > span.ui-button-text").click()
        time.sleep(10)
        self.driver.find_element_by_css_selector("#tabView\:customTextOptionsTable\:0\:j_id_hz").click()
        time.sleep(5)

    def createNewVariants(self):


        self.driver.find_element_by_css_selector("#tabView\:addOtherOption > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default").click()
        time.sleep(3)

        self.driver.find_element_by_id("tabView:customOptionalValue").send_keys("Kumaş Seçiniz")
        self.driver.find_element_by_css_selector("#tabView\:j_id_hh > span").click()
        time.sleep(4)
        self.driver.find_element_by_id("tabView:customOptionalValue").send_keys("En Seçiniz")
        self.driver.find_element_by_css_selector("#tabView\:j_id_hh > span").click()
        time.sleep(4)
        self.driver.find_element_by_id("tabView:customOptionalValue").send_keys("Pile Seçiniz")
        self.driver.find_element_by_css_selector("#tabView\:j_id_hh > span").click()
        time.sleep(4)
        self.driver.find_element_by_css_selector("#tabView\:j_id_hl > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default").click()
        time.sleep(4)
        self.driver.find_element_by_id("tabView:customTextOption").send_keys("Boy Ölçünüz")
        self.driver.find_element_by_css_selector("#tabView\:customerOption > span").click()
        time.sleep(4)

        for fabric in ["Yüksek Gramajlı(Tavsiye Edilen)","Standart Gramaj"]:

            self.driver.find_element_by_id("tabView:optionalAttributeValueSelectorTable:0:optionalValue").send_keys(fabric)
            self.driver.find_element_by_css_selector("#tabView\:optionalAttributeValueSelectorTable\:0\:j_id_iq > span").click()
            time.sleep(4)

        widthStarter = 80
        widthFinal =  600

        self.driver.find_element_by_id("tabView:optionalAttributeValueSelectorTable:1:optionalValue").send_keys("Numune Talep Et")
        self.driver.find_element_by_css_selector("#tabView\:optionalAttributeValueSelectorTable\:1\:j_id_iq > span").click()
        time.sleep(2)


        while widthStarter<=widthFinal:
            self.driver.find_element_by_id("tabView:optionalAttributeValueSelectorTable:1:optionalValue").send_keys(widthStarter)
            self.driver.find_element_by_css_selector("#tabView\:optionalAttributeValueSelectorTable\:1\:j_id_iq > span").click()
            time.sleep(4)
            widthStarter += 10

        for pile in ["Pilesiz", "Seyrek Pile", "Orta Pile", "Sık Pile"]:
            self.driver.find_element_by_id("tabView:optionalAttributeValueSelectorTable:2:optionalValue").send_keys(pile)
            self.driver.find_element_by_css_selector("#tabView\:optionalAttributeValueSelectorTable\:2\:j_id_iq > span").click()
            time.sleep(3)

        self.driver.find_element_by_css_selector("#tabView\:j_id_j0 > span").click()
        time.sleep(45)
        self.driver.find_element_by_css_selector("#tabView\:j_id_j1\:createOptionalValuesIdButton > span.ui-button-text").click()
        time.sleep(10)






        for numune in ["2","3","4","217","218","219","220"]:
            self.driver.find_element_by_css_selector("#tabView\:optionalValuetable_data > tr:nth-child({}) > td.ui-selection-column > div > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default".format(numune)).click()

        ### Deletes thoses##

        self.driver.find_element_by_css_selector("#tabView\:j_id_k7 > span.ui-button-text").click()
        time.sleep(45)


        #################################################################################CALCULATER OF THE PRİCES#################################################################################
        ##########################################################################################################################################################################################
        ##########################################################################################################################################################################################


    def calculteTulPrice(self):
        initialwidth = int(80)
        lastwidth = int(600)
        quantitySku = (((lastwidth - initialwidth)/10)+1)*4
        initialSku = "1"
        lastSku = int(quantitySku)

        while int(initialSku) <= lastSku:
            for pile in [1, 2, 2.5, 3]:
                self.driver.find_element_by_id("tabView:optionalValuetable:{}:skuCurrencyAmount".format(initialSku)).clear()

                if pile != 3:
                    price = (((initialwidth/100)*pile)+20/100)*int(60)
                    price = int(price)
                    price = str(price)
                    self.driver.find_element_by_id("tabView:optionalValuetable:{}:skuCurrencyAmount".format(initialSku)).send_keys(price)

                    initialSku = int(initialSku)
                    initialSku += 1
                    initialSku = str(initialSku)

                elif pile == 3:
                    price = (initialwidth/100)*pile*int(60)
                    price = int(price)
                    price = str(price)



                    self.driver.find_element_by_id("tabView:optionalValuetable:{}:skuCurrencyAmount".format(str(initialSku))).send_keys(price)

                    initialSku = int(initialSku)
                    initialSku += 1
                    initialSku = str(initialSku)

            initialwidth += 10



    def calculteTulPrice1(self):
        initialwidth = int(80)
        lastwidth = int(600)

        quantitySku = (((lastwidth - initialwidth)/10)+1)*4
        initialSku = "213"
        lastSku = 212+212

        while int(initialSku) <= lastSku:
            for pile in [1, 2, 2.5, 3]:
                self.driver.find_element_by_id("tabView:optionalValuetable:{}:skuCurrencyAmount".format(initialSku)).clear()

                if pile != 3:
                    price = (((initialwidth/100)*pile)+20/100)*int(50)
                    price = int(price)
                    price = str(price)
                    self.driver.find_element_by_id("tabView:optionalValuetable:{}:skuCurrencyAmount".format(initialSku)).send_keys(price)

                    initialSku = int(initialSku)
                    initialSku += 1
                    initialSku = str(initialSku)

                elif pile == 3:
                    price = (initialwidth/100)*pile*int(50)
                    price = int(price)
                    price = str(price)



                    self.driver.find_element_by_id("tabView:optionalValuetable:{}:skuCurrencyAmount".format(str(initialSku))).send_keys(price)

                    initialSku = int(initialSku)
                    initialSku += 1
                    initialSku = str(initialSku)

            initialwidth += 10


    def save(self):
        self.driver.find_element_by_id("j_id119_j_id_1v7").click()








"""
        fabric = 0
        totalVariants = ((self.lastWidth- self.initialWidth)/10)
        piles = 3


        while fabric <=1 :

            fabric -= 1
            while totalVariants >= 0 :


                totalVariants -=1
                while piles >= 0 :


                    pile -= 1 

"""
######### Test.py will be here #######

deneme = Editing()
deneme.goProducts()
deneme.deletingOldInformations()
deneme.createNewVariants()
deneme.calculteTulPrice()
deneme.calculteTulPrice1()
time.sleep(2)
#deneme.save()
