from flask import Blueprint, jsonify, request
from app.models import Resource
from app import db

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/resources', methods=['GET', 'POST'])
def resources():
    if request.method == 'GET':
        resources = Resource.query.all()
        resource_list = [{'id': res.id, 'title': res.title, 'content': res.content, 'author': res.author} for res in resources]
        return jsonify({'resources': resource_list})

    elif request.method == 'POST':
        data = request.get_json()
        new_resource = Resource(title=data['title'], content=data['content'], author='Anonymous')
        db.session.add(new_resource)
        db.session.commit()
        return jsonify({'id': new_resource.id, 'title': new_resource.title, 'content': new_resource.content, 'author': new_resource.author}), 201

@api_bp.route('/resources/<int:resource_id>', methods=['GET', 'PUT', 'DELETE'])
def resource_detail(resource_id):
    resource = Resource.query.get_or_404(resource_id)

    if request.method == 'GET':
        return jsonify({'id': resource.id, 'title': resource.title, 'content': resource.content, 'author': resource.author})

    elif request.method == 'PUT':
        data = request.get_json()
        resource.title = data['title']
        resource.content = data['content']
        db.session.commit()
        return jsonify({'message': 'Resource updated successfully'})

    elif request.method == 'DELETE':
        db.session.delete(resource)
        db.session.commit()
        return jsonify({'message': 'Resource deleted successfully'})

# Add more routes if needed
