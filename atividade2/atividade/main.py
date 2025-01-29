from professor import Professor

def main():
    professor1 = Professor("Ana Costa", "123456", 20)
    professor2 = Professor("Carlos Silva", "789012", 30)

    print("Professor 1:") 
    print("Nome:", professor1.get_nome())
    print("SIAPE:", professor1.get_siape())
    print("Carga horária semanal:", professor1.get_carga_horaria())

    print("nProfessor 2:")
    print("Nome:", professor2.get_nome())
    print("SIAPE:", professor2.get_siape())
    print("Carga horária semanal:", professor2.get_carga_horaria())

    professor1.set_nome("Ana Paula Costa")
    professor2.set_carga_horaria(25)

    print("Após modificações:")
    print("Professor 1 nome:", professor1.get_nome())
    print("Professor 2 carga horária:", professor2.get_carga_horaria())

    professor1.maisHoras(5)
    professor2.menosHoras(10)

    print("nApós ajustes de carga horária:")
    print("Professor 1 carga horária:", professor1.get_carga_horaria())
    print("Professor 2 carga horária:", professor2.get_carga_horaria())

    professor1.menosHoras(30)
    professor2.maisHoras(-5)

if __name__ == "__main__":
    main()
