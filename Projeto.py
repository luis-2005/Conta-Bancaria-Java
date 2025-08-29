import java.util.Scanner;

public class ContaBancaria {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Dados da conta
        String nomeCliente;
        double saldo = 0.0;

        System.out.println("===== Bem-vindo ao Banco Console =====");
        System.out.print("Digite seu nome: ");
        nomeCliente = scanner.nextLine();

        System.out.println("\nOlá, " + nomeCliente + "! Sua conta foi criada com sucesso.");
        System.out.println("Seu saldo atual é: R$ " + saldo);

        boolean continuar = true;

        while (continuar) {
            System.out.println("\nEscolha uma opção:");
            System.out.println("1 - Consultar saldo");
            System.out.println("2 - Depositar");
            System.out.println("3 - Sacar");
            System.out.println("4 - Sair");

            System.out.print("Opção: ");
            int opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    System.out.println("\nSeu saldo atual é: R$ " + saldo);
                    break;

                case 2:
                    System.out.print("\nDigite o valor a depositar: R$ ");
                    double deposito = scanner.nextDouble();
                    if (deposito > 0) {
                        saldo += deposito;
                        System.out.println("Depósito realizado com sucesso! Novo saldo: R$ " + saldo);
                    } else {
                        System.out.println("Valor inválido! O depósito precisa ser maior que zero.");
                    }
                    break;

                case 3:
                    System.out.print("\nDigite o valor a sacar: R$ ");
                    double saque = scanner.nextDouble();
                    if (saque > 0) {
                        if (saque <= saldo) {
                            saldo -= saque;
                            System.out.println("Saque realizado com sucesso! Novo saldo: R$ " + saldo);
                        } else {
                            System.out.println("Saldo insuficiente para saque.");
                        }
                    } else {
                        System.out.println("Valor inválido! O saque precisa ser maior que zero.");
                    }
                    break;

                case 4:
                    System.out.println("\nObrigado por usar o Banco Console, " + nomeCliente + "! Até logo.");
                    continuar = false;
                    break;

                default:
                    System.out.println("Opção inválida! Tente novamente.");
            }
        }

        scanner.close();
    }
}
