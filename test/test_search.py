from ..aims.cart import Cart, DigitalVideoDisc, search_by_title

def main():
    my_cart = Cart()

    dvd1 = DigitalVideoDisc(title="The Lion King", category="Animation", cost=19.99)
    dvd2 = DigitalVideoDisc(title="Aladdin", category="Animation/Musical", cost=24.99)
    dvd3 = DigitalVideoDisc(title="Avatar", category="Sci-Fi", cost=19.99)
    dvd4 = DigitalVideoDisc(title="The Avengers", category="Action/Sci-Fi", cost=22.50)

    print("--- ĐANG THÊM CÁC ĐĨA VÀO GIỎ HÀNG ---")
    my_cart.add_dvd(dvd1)
    my_cart.add_dvd(dvd2)
    my_cart.add_dvd(dvd3)
    my_cart.add_dvd(dvd4)
    print("\n" + "="*45)
    print("KIỂM THỬ: search_by_title (Từ khóa: 'The')")
    print("="*45)
    title_results = search_by_title(my_cart.items, "The")
    
    if title_results:
        for item in title_results:
            print(item)
    else:
        print("Không tìm thấy đĩa nào phù hợp.")

if __name__ == "__main__":
    main()