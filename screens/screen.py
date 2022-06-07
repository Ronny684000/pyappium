from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

from elements.button import Button
from elements.input_field import InputField
from elements.label import Label


class MainMenuScreen:
    __first_discount_item_locator = "//android.widget.RelativeLayout[./android.widget.RelativeLayout" \
                                    "[./android.widget.RelativeLayout[./android.widget.TextView[2]]]][1]"
    __city_label = Label("tvToolbarCity", AppiumBy.ID, "City label")
    __first_discount_item = Label(__first_discount_item_locator, AppiumBy.XPATH, "First item with discount")
    __first_discount_item_discount = Label(__first_discount_item_locator + "//child::android.widget.TextView[contains(@resource-id, 'tvDiscount')]",
                                           AppiumBy.XPATH, "First item discount")
    __first_discount_item_old_price = Label(__first_discount_item_locator + "//child::android.widget.TextView[contains(@resource-id, 'tvSumm')]",
                                            AppiumBy.XPATH, "First item old price")
    __first_discount_item_actual_price = Label(__first_discount_item_locator + "//child::android.widget.TextView[contains(@resource-id, 'tvPrice')]",
                                               AppiumBy.XPATH, "First item actual price")
    __first_discount_item_brand = Label(__first_discount_item_locator + "//child::android.widget.TextView[contains(@resource-id, 'tvBrand')]",
                                        AppiumBy.XPATH, "First item seller")

    def click_city_label(self):
        self.__city_label.click()
        return CityChoiceScreen()

    def click_first_discount_item(self):
        self.__first_discount_item.click()
        return ItemScreen()

    def get_pure_price(self):
        return self.__first_discount_item_old_price.get_text().split(' ')[0]

    def get_discount_price(self):
        return self.__first_discount_item_actual_price.get_text().split(' ')[0]

    def get_discount(self):
        return self.__first_discount_item_discount.get_text().replace('-', '').replace('%', '')

    def get_brand(self):
        return self.__first_discount_item_brand.get_text()

    def get_city(self):
        return self.__city_label.get_text()

    def verify_selected_region(self, region):
        assert self.__city_label.get_text().strip() == region.strip(), self.__city_label.get_text() + " " + region
        return self


class CityChoiceScreen:
    __popup_ok_button = Button("android:id/button2", AppiumBy.ID, "Popup ok button")
    __search_field = InputField("etSearchTest", AppiumBy.ID, "Search input field")
    __search_button = Button("imageView7", AppiumBy.ID, "Search button")
    __found_city = None

    def hide_popup(self):
        self.__popup_ok_button.click()
        return self

    def __type_in_search_field(self, text):
        self.__search_field.send_text(text)

    def __click_search_button(self):
        self.__search_button.click()

    def __click_city_option(self):
        self.__found_city = Button("tvCityItemName", By.ID, "City option")
        self.__found_city.click()

    def find_and_select_city(self, text):
        self.__type_in_search_field(text)
        self.__click_search_button()
        self.__click_city_option()
        return MainMenuScreen()


class ItemScreen:
    __item_old_price = Label("tvItemOriginalPrice", AppiumBy.ID, "Item original price")
    __item_actual_price = Label("tvItemPrice", AppiumBy.ID, "Item actual price")
    __item_discount = Label("tvItemDiscount", AppiumBy.ID, "Item discount")
    __item_brand = Label("tvItemBrand", AppiumBy.ID, "Item brand")
    __item_seller_name = Label("tvItemSellerName", AppiumBy.ID, "Item seller name")
    __item_seller_city = Label("tvItemSellerCity", AppiumBy.ID, "Item seller city")
    __item_seller_avatar = Button("ivSellerAvatar", AppiumBy.ID, "Seller avatar")

    def verify_item_discount(self, discount):
        assert self.__item_discount.get_text().replace('-', '').replace('%', '') == discount, "Discount is not correct"
        return self

    def verify_item_old_price(self, price):
        assert self.__item_old_price.get_text().split(' ')[0] == price, "Old price is not correct"
        return self

    def verify_item_actual_price(self, price):
        assert self.__item_actual_price.get_text().split(' ')[0] == price, "Actual price is not correct"
        return self

    def verify_correct_item_is_loaded(self, brand):
        assert self.__item_brand.get_text() == brand, "Actual price is not correct"
        return self

    def get_item_seller_name(self):
        return self.__item_seller_name.get_text()

    def get_item_seller_city(self):
        return self.__item_seller_city.get_text()

    def click_seller_avatar(self):
        self.__item_seller_avatar.click()
        return SellerScreen()


class SellerScreen:
    __seller_city = Label("//android.widget.TextView[contains(@text, "
                          "'City')]/parent::android.widget.RelativeLayout/child::android.widget.TextView[2]",
                          AppiumBy.XPATH, "Seller city")
    __seller_name = Label("//android.view.ViewGroup/android.widget.TextView", AppiumBy.XPATH, "Seller name")

    def verify_seller_name(self, name):
        assert self.__seller_name.get_text() == name, "Seller name is not correct"
        return self

    def verify_seller_city(self, city):
        assert self.__seller_city.get_text() == city, "Seller city is not correct"
        return self

