from Contact import Contact;

class Schedule:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self):
        contact = Contact(
            input('Nome: '),
            input('Email: '),
            int(input('Telefone: ')),
            input('Favorito? (s/n): ').lower() == 's'
        )
        self.contacts.append(contact)
    
    def view_contacts(self):
        for contact in self.contacts:
            print(contact)
    
    def find_contact_by_name(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def remove_contact(self, name):
        contacts_to_keep = list(filter(lambda contact: contact.name != name, self.contacts))
        
        if len(contacts_to_keep) < len(self.contacts):
            self.contacts = list(contacts_to_keep)
            print(f"Contato '{self.name}' removido com sucesso.")
        else:
            print(f"Contato '{self.name}' não encontrado.")
    
    def see_favorites(self):
        count = 0
        for contact in self.contacts:
            if contact.favorite:
                print(contact)
                count += 1
        if count == 0:
            print("Nenhum contato favorito encontrado.")
    
    def edit_contact(self):
        name = input('Digite o nome do contato que deseja editar: ')
        contact = self.find_contact_by_name(name)

        if contact:
            contact.email = input(f'Novo Email ({contact.email}): ') or contact.email
            contact.phone = int(input(f'Novo Telefone ({contact.phone}): ')) or int(contact.phone)
            contact.favorite = input(f'Favorito? (s/n) ({contact.favorite}): ').lower() == 's' or contact.favorite

            print(f"Contato '{name}' editado com sucesso.")
        else:
            print(f"Contato '{name}' não encontrado.")

    def edit_favorite_contact(self):
        name = input('Nome: ')
        favorite = input('Favorite: ').lower() == 's'
        contact = self.find_contact_by_name(name)
        if contact:
            contact.favorite = favorite
            print(f"Contato '{self.name}' editado com sucesso.")
        else:
            print(f"Contato '{self.name}' não encontrado.")
