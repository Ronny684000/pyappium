import pytest

from screens.screen import MainMenuScreen, ItemScreen


@pytest.mark.target
@pytest.mark.parametrize("city", ["London"])
def test_sc(city):
    MainMenuScreen().\
        click_city_label().\
        hide_popup().\
        find_and_select_city(city).\
        verify_selected_region(city)
    actual_price = MainMenuScreen().\
        get_discount_price()
    original_price = MainMenuScreen().\
        get_pure_price()
    discount = MainMenuScreen().\
        get_discount()
    brand = MainMenuScreen().\
        get_brand()
    MainMenuScreen().\
        click_first_discount_item().\
        verify_correct_item_is_loaded(brand).\
        verify_item_discount(discount).\
        verify_item_old_price(original_price).\
        verify_item_actual_price(actual_price)
    seller_name = ItemScreen().\
        get_item_seller_name()
    seller_city = ItemScreen().\
        get_item_seller_city()
    ItemScreen().\
        click_seller_avatar().\
        verify_seller_city(seller_city).\
        verify_seller_name(seller_name)

