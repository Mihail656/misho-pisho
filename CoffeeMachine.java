import java.util.Scanner;

public class CoffeeMachine {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("=== Кафе машина ===");
        System.out.println("1. Еспресо - 1.00 лв.");
        System.out.println("2. Лате - 1.50 лв.");
        System.out.println("3. Капучино - 1.20 лв.");
        System.out.print("Изберете номер напитка: ");
        int choice = sc.nextInt();

        double price = 0;

        if (choice == 1) {
            price = 1.00;
            System.out.println("Избрано: Еспресо");
        } else if (choice == 2) {
            price = 1.50;
            System.out.println("Избрано: Лате");
        } else if (choice == 3) {
            price = 1.20;
            System.out.println("Избрано: Капучино");
        } else {
            System.out.println("Грешка в системата!");
            return;
        }

        System.out.print("Въведете пари: ");
        double money = sc.nextDouble();

        if (money >= price) {
            System.out.println("Приготвяне...");
            System.out.println("Получавате вашето кафе!");
            System.out.println("Ресто: " + (money - price) + " лв.");
        } else {
            System.out.println("Недостатъчно пари! Трябват още: " + (price - money) + " лв.");
        }
    }
}
