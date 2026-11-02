from ..aims.cart import Cart, DigitalVideoDisc


def main():
  my_cart = Cart()

  print("=== BẮT ĐẦU THÊM 20 ĐĨA DVD VÀO GIỎ HÀNG ===")
  for i in range(1, 21):
    dvd = DigitalVideoDisc(
        title=f"Movie {i}",
        category="Science Fiction",
        director=f"Director {i}",
        length=120,
        cost=19.99,
    )

    print(f"Thêm đĩa {i:2d}: ", end="")
    my_cart.add_dvd(dvd)

  print("\n--- KẾT QUẢ SAU KHI THÊM 20 ĐĨA ---")
  print(f"Tổng số đĩa trong giỏ: {len(my_cart.items)}")
  print(f"Tổng giá tiền: {my_cart.total_cost():.2f} $")

  print("\n=== THỬ THÊM ĐĨA THỨ 21 (VƯỢT QUÁ GIỚI HẠN) ===")
  extra_dvd = DigitalVideoDisc(title="Movie 21", cost=15.0)
  my_cart.add_dvd(extra_dvd)


if __name__ == "__main__":
  main()