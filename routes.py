from flask import Blueprint, jsonify, render_template, request
from database import db
from models import LostItem


routes = Blueprint('routes', __name__)

# @routes.route('/add_lost_item', methods=['POST'])
# def add_lost_item():
#     # Add a new lost item to the database
#     new_item = LostItem(name="Lost Wallet", description="Black leather wallet")
#     db.session.add(new_item)
#     db.session.commit()
#     return jsonify({"message": "Lost item added!"})

# @routes.route('/view_lost_items', methods=['GET'])
# def view_lost_items():
#     # Fetch all lost items from the database
#     items = LostItem.query.all()
#     return jsonify([item.to_dict() for item in items])

# Home page
@routes.route('/')
def home():
    return render_template('main.html')

# Add a lost item
@routes.route('/add_lost_item', methods=['POST'])
def add_lost_item():
    data = request.json  # Expecting JSON input from frontend
    new_item = LostItem(name=data['name'], description=data['description'])
    db.session.add(new_item)
    db.session.commit()
    # new_item = LostItem(name="name", description="description")
    # db.session.add(new_item)
    # db.session.commit()
    return jsonify({"message": "Lost item added!"})



# View all lost items
# @routes.route('/view_lost_items', methods=['GET'])
# def view_lost_items():
#     items = LostItem.query.all()
#     return jsonify([item.to_dict() for item in items])
@routes.route('/view_lost_items', methods=['GET'])
def view_lost_items():
    search_query = request.args.get('search', '')
    if search_query:
        items = LostItem.query.filter(LostItem.name.ilike(f'%{search_query}%')).all()
    else:
        items = LostItem.query.all()
    return jsonify([item.to_dict() for item in items])

#Search for a lost item by name
# @routes.route('/search_lost_items', methods=['GET'])
# def search_lost_items():
#     search_query = request.args.get('query', '')  # Get search parameter
#     items = LostItem.query.filter(LostItem.name.ilike(f"%{search_query}%")).all()
#     return render_template('search.html', items=items, message="Items Found" if items else "No items found")

# Update a lost item
@routes.route('/update_lost_item/<int:item_id>', methods=['PUT'])
def update_lost_item(item_id):
    item = LostItem.query.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    data = request.json
    item.name = data.get('name', item.name)
    item.description = data.get('description', item.description)

    db.session.commit()
    return jsonify({"message": "Lost item updated!"})

# Delete a lost item
@routes.route('/delete_lost_item/<int:item_id>', methods=['DELETE'])
def delete_lost_item(item_id):
    item = LostItem.query.get(item_id)
    if not item:
        return jsonify({"error": "Item not found"}), 404

    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Lost item deleted!"})


@routes.route('/search')
def search_page():
    return render_template('search.html')  # Serve the search page

@routes.route('/search_lost_items', methods=['GET'])
def search_lost_items():
    query = request.args.get('query', '').strip()
    if not query:
        return jsonify({"message": "Please enter a search term."})

    # Search for items that match the query
    items = LostItem.query.filter(LostItem.name.ilike(f"%{query}%")).all()
    return jsonify([item.to_dict() for item in items])
