from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from app.auth import login_required
from app.db import get_db

bp = Blueprint('shop', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    db = get_db()
    
    if request.method == 'POST':
        if g.user is None:
            return redirect(url_for('auth.login'))
            
        product_id = request.form['product_id']
        quantity = int(request.form.get('quantity', 1))
        user_id = g.user['id']
        
        if quantity <= 0:
            flash('A quantidade deve ser pelo menos 1.')
        else:
            item_existente = db.execute(
                'SELECT id, quantity FROM cart_item WHERE user_id = ? AND product_id = ?',
                (user_id, product_id)
            ).fetchone()
            
            if item_existente:
                db.execute(
                    'UPDATE cart_item SET quantity = quantity + ? WHERE id = ?',
                    (quantity, item_existente['id'])
                )
            else:
                db.execute(
                    'INSERT INTO cart_item (user_id, product_id, quantity) VALUES (?, ?, ?)',
                    (user_id, product_id, quantity)
                )
            
            db.commit()
            flash('Produto adicionado ao carrinho!')
            return redirect(url_for('index'))

    products = db.execute(
        'SELECT id, name, description, price FROM product'
    ).fetchall()
    return render_template('shop/index.html', products=products)

@bp.route('/cart')
@login_required
def cart():
    db = get_db()
    cart_items = db.execute(
        'SELECT p.name, p.price, c.quantity, c.id, (p.price * c.quantity) as subtotal'
        ' FROM cart_item c JOIN product p ON c.product_id = p.id'
        ' WHERE c.user_id = ?',
        (g.user['id'],)
    ).fetchall()

    total = sum(item['subtotal'] for item in cart_items)

    return render_template('shop/cart.html', items=cart_items, total=total)

@bp.route('/<int:id>/update', methods=('POST',))
@login_required
def update_quantity(id):
    quantity = int(request.form.get('quantity', 1))
    if quantity > 0:
        db = get_db()
        db.execute(
            'UPDATE cart_item SET quantity = ? WHERE id = ? AND user_id = ?',
            (quantity, id, g.user['id'])
        )
        db.commit()
    else:
        flash("Quantidade inválida.")
    return redirect(url_for('shop.cart'))

@bp.route('/<int:id>/remove', methods=('POST',))
@login_required
def remove(id):
    db = get_db()
    db.execute('DELETE FROM cart_item WHERE id = ? AND user_id = ?', (id, g.user['id']))
    db.commit()
    return redirect(url_for('shop.cart'))

@bp.route('/clear', methods=('POST',))
@login_required
def clear():
    db = get_db()
    db.execute('DELETE FROM cart_item WHERE user_id = ?', (g.user['id'],))
    db.commit()
    return redirect(url_for('shop.cart'))

@bp.route('/<int:id>/details')
def details(id):
    db = get_db()
    product = db.execute(
        'SELECT id, name, description, price FROM product WHERE id = ?',
        (id,)
    ).fetchone()
    return render_template('shop/details.html', product=product)