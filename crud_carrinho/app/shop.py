from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from app.auth import login_required
from app.db import get_db

bp = Blueprint('shop', __name__)

@bp.route('/')
def index():
    db = get_db()
    products = db.execute(
        'SELECT id, name, description, price FROM product'
    ).fetchall()
    return render_template('shop/index.html', products=products)

# Nova rota para o Carrinho (RF12)
@bp.route('/cart')
@login_required
def cart():
    db = get_db()
    # Busca os itens que o usuário logado adicionou (RF18)
    cart_items = db.execute(
        'SELECT p.name, p.price, c.quantity, c.id, (p.price * c.quantity) as subtotal'
        ' FROM cart_item c JOIN product p ON c.product_id = p.id'
        ' WHERE c.user_id = ?',
        (g.user['id'],)
    ).fetchall()

    # Cálculo automático do valor total (RF14)
    total = sum(item['subtotal'] for item in cart_items)

    return render_template('shop/cart.html', items=cart_items, total=total)