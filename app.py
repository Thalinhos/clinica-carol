from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, session, url_for
from utils.utils import db, sqlite3RawQueryWithNoParams, sqlite3RawQueryWithParams, sqlite3RawQueryWithParams2One
from services.services import create_produto_entrada, create_produto_saida

app = Flask(__name__)

app.secret_key = 'BAD_SECRET_KEY_BY_EXAMPLE'

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/logoff")
def logoff():
    session.clear()
    return redirect(url_for('login'))

@app.route("/handleLogin", methods=['GET', 'POST'])
def handleLogin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        userToBeFound = sqlite3RawQueryWithParams2One("SELECT * FROM users WHERE name = ? AND password = ?", (username, password))
        print(userToBeFound)
        if userToBeFound is None:
            return "User not found"

        session['logged_in'] = True
        session['username'] = username
        return redirect(url_for('afterLogin'))

@app.route("/afterLogin")
def afterLogin():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template("main_page.html")

@app.route('/show_all_products', methods=['GET', 'POST'])
def show_all_products():
    if 'username' not in session:
        return redirect(url_for('login'))

    msgSuccess = session.get('201')
    session.pop('201', None)

    allProducts = sqlite3RawQueryWithNoParams("select * from ProdutosTotal;")
    
    return render_template('show_all_products.html', allProducts=allProducts, msgSuccess=msgSuccess)


@app.route("/add_product", methods=['GET', 'POST'])
def add_product():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']

        return render_template('add_product.html', name=name, amount=amount)

@app.route("/add_product_soma", methods=['GET', 'POST'])
def add_product_soma():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        create_produto_entrada(name, abs(int(amount)), session['username'])
        session['201'] = 'Item inserido com sucesso.'
        return redirect(url_for('show_all_products'))

@app.route('/sub_product', methods=['GET', 'POST'])
def sub_product():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        
        return render_template('sub_product.html', name=name, amount=amount)
    
@app.route("/sub_product_sub", methods=['GET', 'POST'])
def sub_product_sub():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        motivo = request.form['motivo']

        produto = sqlite3RawQueryWithParams("SELECT * FROM ProdutosTotal where name = ?", (name, ))
        if produto[2] <= 0:
            return "Não é possível diminuir o valor de zero."

        if motivo == '' or len(motivo) < 8:
            return "Necessário preencher a descrição/motivo com no mínimo 8 charactéres."
        

        create_produto_saida(name, abs(int(amount)), session['username'], motivo)
        session['201'] = 'Item excluído com sucesso.'
        return redirect(url_for('show_all_products'))
    
@app.route("/add_new_product", methods=['GET','POST'])
def add_new_product():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('add_new_product.html')

@app.route('/sub_product_without_parameters', methods=['GET', 'POST'])
def sub_product_without_parameters():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        try:
            produto = sqlite3RawQueryWithParams("SELECT * FROM ProdutosTotal where name = ?", (request.form['name'],))
            if(int(request.form['amount']) > produto[2]):
                flash("Não é possível retirar quantidade maior que a disponível", 'error')
                return redirect(url_for('sub_product_without_parameters'))

            create_produto_saida(request.form['name'], abs(int(request.form['amount'])), session['username'], request.form['motivo'])
            flash("Valores atualizados", 'success')
            return redirect(url_for('sub_product_without_parameters'))

        except ValueError as e:
            flash("Valores precisam ser preenchidos", 'error')
            return redirect(url_for('sub_product_without_parameters'))
        except Exception as e:      
            flash("Algo deu errado, contate o adminsitrador", 'error')
            return redirect(url_for('sub_product_without_parameters'))
        

    
    produtos = sqlite3RawQueryWithNoParams("SELECT * FROM ProdutosTotal where amount > 0;")
    return render_template('sub_product_without_parameters.html', produtos=produtos)

@app.route('/add_new_product_add', methods=['GET','POST'])
def add_new_product_add():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']

        create_produto_entrada(name.lower(), abs(int(amount)), session['username'])
        session['201'] = 'Item novo criado com sucesso.'
        return redirect(url_for('show_all_products'))

@app.route("/transaction_register_entry", methods=['GET', 'POST'])
def transaction_register_entry():
    if 'username' not in session:
        return redirect(url_for('login'))

    produtos = sqlite3RawQueryWithNoParams("SELECT * FROM ProdutoEntrada LIMIT 100;")
    produtos = [{
        'id': produto[0],
        'name': produto[1],
        'quantity': produto[2],
        'employeeEntry': produto[4],
        'entryDate': datetime.strptime(produto[3], '%d/%m/%Y %H:%M:%S') if produto[3] else None   
    } for produto in produtos]
    
    produtos_ordenados = sorted(produtos, key=lambda x: x['entryDate'], reverse=True)
    return render_template('transaction_register_entry.html', produtos_ordenados=produtos_ordenados)
    

@app.route("/transaction_register_extract", methods=['GET', 'POST'])
def transaction_register_extract():
    if 'username' not in session:
        return redirect(url_for('login'))

    produtos = sqlite3RawQueryWithNoParams("SELECT * FROM ProdutoSaida;")
    produtos = [{
        'id': produto[0],
        'name': produto[1],
        'quantity': produto[2],
        'employeeLeft': produto[4],
        'motivo': produto[5],
        'leftDate': datetime.strptime(produto[3], '%d/%m/%Y %H:%M:%S') if produto[3] else None
    } for produto in produtos]
    
    produtos_ordenados = sorted(produtos, key=lambda x: x['leftDate'], reverse=True)
    return render_template('transaction_register_extract.html', produtos_ordenados=produtos_ordenados)

@app.route('/searchSQLEntry', methods=['GET','POST'])
def searchSQLEntry():
    searchValue = request.form['search']

    produtos = sqlite3RawQueryWithNoParams("SELECT * FROM ProdutoEntrada;")
    produtos = [{
        'id': produto[0],
        'name': produto[1],
        'quantity': produto[2],
        'employeeEntry': produto[4],
        'entryDate': datetime.strptime(produto[3], '%d/%m/%Y %H:%M:%S') if produto[3] else None   
    } for produto in produtos]
    
    produtosOrdenados = sorted(produtos, key=lambda x: x['entryDate'], reverse=True)
    produtos_ordenados = []
    for produto in produtosOrdenados:
        if searchValue.lower() in produto['name'].lower() or searchValue.lower() in produto['employeeEntry'] or searchValue.lower() in str(produto['entryDate']):
            produtos_ordenados.append(produto)

    return render_template('components/searchSQLEntry.html', produtos_ordenados=produtos_ordenados)

@app.route('/sqlSearchLeft', methods=['GET','POST'])
def sqlSearchLeft():
    searchValue = request.form['search']

    produtos = sqlite3RawQueryWithNoParams("SELECT * FROM ProdutoSaida;")
    produtos = [{
        'id': produto[0],
        'name': produto[1],
        'quantity': produto[2],
        'employeeLeft': produto[4],
        'motivo': produto[5],
        'leftDate': datetime.strptime(produto[3], '%d/%m/%Y %H:%M:%S') if produto[3] else None
    } for produto in produtos]

    produtosOrdenados = sorted(produtos, key=lambda x: x['leftDate'], reverse=True)
    produtos_ordenados = []
    for produto in produtosOrdenados:
        if searchValue.lower() in produto['name'].lower() or searchValue.lower() in produto['employeeLeft'] or searchValue.lower() in str(produto['leftDate']) or searchValue.lower() in produto['motivo']:
            produtos_ordenados.append(produto)
    
    
    return render_template('components/sqlSearchLeft.html', produtos_ordenados=produtos_ordenados)






if __name__ == "__main__":
    app.run(debug=True)

    



#http://localhost:8080
#waitress-serve --port=8080 app:app