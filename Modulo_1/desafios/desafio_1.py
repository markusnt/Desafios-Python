def create_contact(contacts, contact_name, contact_phone, contact_email):
    contact = {
        "name": contact_name,
        "phone": contact_phone,
        "email": contact_email,
        "favorite": False
    }
    contacts.append(contact)
    print(f"Contato de {contact_name} salvo com sucesso!")

def list_contacts(contacts):
    print("\nMeus contatos:")
    for index, contact in enumerate(contacts, start=1):
        status = "♡" if contact["favorite"] else " "
        print(f"{index}. [{status}] {contact['name']}")
    return

def handle_contact(contacts, index_contact, new_contact_name):
    index_contact_ajust = int(index_contact) - 1
    if 0 <= index_contact_ajust < len(contacts):
        contacts[index_contact_ajust]["name"] = new_contact_name
        print(f"Contato {index_contact} atualizado para {new_contact_name}")
    else:
        print("Índice de contato inválido.")

def favorite_contact(contacts, index_contact):
    index_contact_ajust = int(index_contact) - 1
    if 0 <= index_contact_ajust < len(contacts):
        contacts[index_contact_ajust]["favorite"] = True
        print("Contato favoritado com sucesso!")
    else:
        print("Índice de contato inválido.")

def delete_contact(contacts, index_contact):
    index_contact_ajust = int(index_contact) - 1
    if 0 <= index_contact_ajust < len(contacts):
        deleted = contacts.pop(index_contact_ajust)
        print(f"Contato {deleted['name']} removido com sucesso.")
    else:
        print("Índice de contato inválido.")

def list_favorites(contacts):
    print("\nContatos Favoritos:")
    for index, contact in enumerate(contacts, start=1):
        if contact["favorite"]:
            print(f"{index}. ♡ {contact['name']}")

# --------------------
# Menu principal
# --------------------
contacts = []

while True:
    print("\nMenu do Gerenciador de Contatos:")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Editar contato")
    print("4. Favoritar contato")
    print("5. Ver favoritos")
    print("6. Apagar contato")
    print("0. Sair")

    option = input("Digite a sua escolha: ")

    match option:
        case "1":
            contact_name = input("Nome: ")
            contact_phone = input("Telefone: ")
            contact_email = input("Email: ")
            create_contact(contacts, contact_name, contact_phone, contact_email)

        case "2":
            list_contacts(contacts)

        case "3":
            list_contacts(contacts)
            index_contact = input("Número do contato a atualizar: ")
            new_contact_name = input("Novo nome: ")
            handle_contact(contacts, index_contact, new_contact_name)

        case "4":
            list_contacts(contacts)
            index_contact = input("Número do contato a favoritar: ")
            favorite_contact(contacts, index_contact)

        case "5":
            list_favorites(contacts)

        case "6":
            list_contacts(contacts)
            index_contact = input("Número do contato a deletar: ")
            delete_contact(contacts, index_contact)

        case "0":
            print("Programa finalizado.")
            break

        case _:
            print("Opção inválida. Tente novamente.")
