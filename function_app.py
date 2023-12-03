import azure.functions as func
import datetime
import json
import logging
from FuncTest2.main import bp2
from FuncTest1.main import bp1

app = func.FunctionApp()

app.register_functions(bp1)
app.register_functions(bp2)
