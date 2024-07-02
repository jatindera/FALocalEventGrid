import logging
import azure.functions as func
from datetime import datetime

app = func.FunctionApp()

@app.function_name(name="displayLogs")
@app.event_grid_trigger(arg_name="azeventgrid")
def FALocalEventGridTrigger(azeventgrid: func.EventGridEvent):
    logging.info('Python EventGrid trigger processed an event')
    logging.info('Function triggered to process a message: %s', azeventgrid.get_json())
    logging.info('  Subject=%s', azeventgrid.subject)
    logging.info('  Event Type=%s', azeventgrid.event_type)
    logging.info('  Event Time=%s', azeventgrid.event_time)
    logging.info('  Data=%s', azeventgrid.get_json())


