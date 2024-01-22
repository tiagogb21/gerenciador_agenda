from Schedule import Schedule

class Start:
    def __init__(self):
        self.schedule = Schedule()

    def show_menu(self):
        print('1 - Cadastrar contato')
        print('2 - Listar contatos')
        print('3 - Remover contato')
        print('4 - Editar contato')
        print('5 - Ver contatos favoritos')
        print('6 - Marcar/Desmarcar contato como favorito')
        print('7 - Sair')

    def run(self):
        while True:
            self.show_menu()

            option = int(input('Escolha uma opção: '))

            if option == 1:
                self.schedule.add_contact()
            elif option == 2:
                self.schedule.view_contacts()
            elif option == 3:
                name = input('Digite o nome do contato que deseja remover: ')
                contact_to_remove = self.schedule.find_contact_by_name(name)
                if contact_to_remove:
                    self.schedule.remove_contact(contact_to_remove)
                else:
                    print('Contato não encontrado')
            elif option == 4:
                self.schedule.edit_contact()
            elif option == 5:
                self.schedule.see_favorites()
            elif option == 6:
                self.schedule.edit_favorite_contact()
            elif option == 7:
                print('Saindo...')
                break
            else:
                print('Opção inválida. Tente novamente.')

start_service = Start()

start_service.run()