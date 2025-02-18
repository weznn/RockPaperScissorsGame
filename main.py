import random


def get_winner(player, computer):
    if player == computer:
        return "Berabere!"
    elif (player == "taş" and computer == "makas") or \
            (player == "kağıt" and computer == "taş") or \
            (player == "makas" and computer == "kağıt"):
        return "Kazandın! 🎉"
    else:
        return "Kaybettin! 😢"


def main():
    secenekler = ["taş", "kağıt", "makas"]

    while True:
        oyuncu_secimi = input("Taş, kağıt, makas? (Çıkmak için q): ").lower()
        if oyuncu_secimi == "q":
            print("Oyun bitti. Çıkılıyor...")
            break
        if oyuncu_secimi not in secenekler:
            print("Geçersiz seçim, lütfen tekrar dene.")
            continue

        bilgisayar_secimi = random.choice(secenekler)
        print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

        sonuc = get_winner(oyuncu_secimi, bilgisayar_secimi)
        print(sonuc + "\n")


if __name__ == "__main__":
    main()
