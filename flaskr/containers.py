from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.db import get_db

bp = Blueprint('containers', __name__)


@bp.route('/')
def index():
    db = get_db()
    serialised_recipes = []
    recipes = db.execute('SELECT * FROM recipes').fetchall()
    for recipe in recipes:
        serialised_recipe = {
            'name': recipe['name'],
            'description': recipe['description'],
            'ingredients': db.execute(
                'SELECT ingredients.*, units.name AS unit_name, ri.amount FROM ingredients \
                INNER JOIN units ON ingredients.unit_id=units.id \
                INNER JOIN recipes__ingredients ri ON ri.ingredient_id=ingredients.id \
                INNER JOIN recipes r ON ri.recipe_id=r.id \
                WHERE r.id=?', (recipe['id'], )).fetchall(),
            'recipe': recipe['recipe'],
            'id': recipe['id']
        }
        serialised_recipes.append(serialised_recipe)
    return render_template('containers.html', recipes=serialised_recipes)


@bp.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    db = get_db()
    db.execute('DELETE FROM recipes WHERE id = ?', (id,))
    db.execute('DELETE FROM recipes__ingredients WHERE recipe_id = ?', (id,))
    db.commit()
    return redirect(url_for('containers.index'))


@bp.route('/<int:id>/edit', methods=('POST',))
def edit(id):
    title = request.form['title-input']
    description = request.form['description-input']
    recipe = request.form['recipe-input']
    db = get_db()
    db.execute('UPDATE recipes SET name = ?, description = ?, recipe = ? WHERE id = ?', (title, description, recipe, id,))
    db.commit()
    return redirect(url_for('containers.index'))


@bp.route('/add', methods=('POST',))
def add():
    title = request.form['title-input']
    description = request.form['description-input']
    recipe = request.form['recipe-input']
    db = get_db()
    db.execute('INSERT INTO recipes (name, description, recipe) VALUES (?, ?, ?)', (title, description, recipe))
    db.commit()
    return redirect(url_for('containers.index'))
