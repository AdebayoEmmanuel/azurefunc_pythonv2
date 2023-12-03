import logging 
import azure.functions as func 
import logging

bp2 = func.Blueprint() 

@bp2.route(route="HttpExample2", auth_level=func.AuthLevel.ANONYMOUS)
def HttpExample2(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('I am the second function.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    
