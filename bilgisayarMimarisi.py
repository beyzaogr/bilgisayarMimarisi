class ALU:
    @staticmethod
    def add_bit(a, b):
        carry_out = a & b  # Taşıma biti
        result = a ^ b  # Toplama biti
        return result, carry_out

    @staticmethod
    def subtract_bit(a, b):
        borrow_in = ~a & b  # Ödünç biti
        result = a ^ b  # Fark biti
        return result, borrow_in

    @staticmethod
    def logic_and(a, b):
        return a & b

    @staticmethod
    def logic_or(a, b):
        return a | b

class CPU:
    def __init__(self):
        self.register = 0  # 1 bitlik register

    def execute_instruction(self, opcode, operand1, operand2):
        if opcode == 0:  # Toplama işlemi
            result, carry = ALU.add_bit(operand1, operand2)
            print(f"Toplama işlemi: {operand1} + {operand2} = {result}, Carry: {carry}")
        elif opcode == 1:  # Çıkarma işlemi
            result, borrow = ALU.subtract_bit(operand1, operand2)
            print(f"Çıkarma işlemi: {operand1} - {operand2} = {result}, Borrow: {borrow}")
        elif opcode == 2:  # Mantıksal AND işlemi
            result = ALU.logic_and(operand1, operand2)
            print(f"Mantıksal AND işlemi: {operand1} AND {operand2} = {result}")
        elif opcode == 3:  # Mantıksal OR işlemi
            result = ALU.logic_or(operand1, operand2)
            print(f"Mantıksal OR işlemi: {operand1} OR {operand2} = {result}")
        else:
            print("Geçersiz opcode")

    def user_interface(self):
        while True:
            print("\n1. Toplama\n2. Çıkarma\n3. Mantıksal AND\n4. Mantıksal OR\n5. Çıkış")
            choice = input("Seçenek girin: ")

            if choice == '5':
                print("Çıkış yapılıyor...")
                break

            num1 = int(input("Birinci sayı (0 veya 1): "))
            num2 = int(input("İkinci sayı (0 veya 1): "))

            # Opcode oluşturma
            opcode = int(choice) - 1  # Kullanıcı girişi ile opcode oluşturuluyor

            # İşlemi gerçekleştir
            self.execute_instruction(opcode, num1, num2)

# Örnek kullanım
cpu = CPU()
cpu.user_interface()
