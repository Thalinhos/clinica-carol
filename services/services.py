from utils.utils import getBrHour
from utils.utils import db

def create_produto_entrada(name: str, quantity: int, employee_entry: str):
    db.connect()
    try:
        db.produtoentrada.create({
            "name": name,
            "quantity": quantity,
            "entryDate": getBrHour(),
            "employeeEntry": employee_entry
        })
        produtoTotal = db.produtostotal.find_unique(where={"name": name})
        if (produtoTotal is None):
            db.produtostotal.create({
                "name": name,
                "amount": quantity
            })
        else:
            updated_amount = produtoTotal.amount + quantity
            db.produtostotal.update(
            where={"name": produtoTotal.name},
            data={"amount": updated_amount}
        )            
    except Exception as e:
        print(f"Erro ao criar produto de entrada: {e}")
    finally:
        db.disconnect()

def create_produto_saida(name: str, quantity: int, employee_entry: str, motivo: str):
    db.connect()
    try:
        db.produtosaida.create({
            "name": name,
            "quantity": quantity,
            "leftDate": getBrHour(),
            "employeeLeft": employee_entry,
            "motivo": motivo
        })
        produtoTotal = db.produtostotal.find_unique(where={"name": name})
        if (produtoTotal):
            updated_amount = produtoTotal.amount - quantity
            db.produtostotal.update(
            where={"name": produtoTotal.name},
            data={"amount": updated_amount}
            )
        else:
            return None            
        
    except Exception as e:
        print(f"Erro ao retirar, produto insuficiente ou inexistente {e}")
    finally:
        db.disconnect()

