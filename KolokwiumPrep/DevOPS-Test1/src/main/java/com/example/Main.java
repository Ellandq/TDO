package com.example;

public class Main {
    public static void main(String[] args) {

        var message = System.getenv().getOrDefault("MESSAGE", "Brak Komunikatu");

        try{
            while (true) {
                System.out.println("Komunikat: " + message);
                Thread.sleep(5000);
            }
        } catch (InterruptedException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}