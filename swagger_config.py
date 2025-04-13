from flasgger import Swagger

def init_swagger(app):
    swagger = Swagger(app, template={
        "swagger": "2.0",
        "info": {
            "title": "API de Itens",
            "description": "Documentação da API de Itens usando Swagger",
            "version": "1.0.0"
        },
        "basePath": "/",
        "schemes": [
            "http",
            "https"
        ]
    })
    return swagger
